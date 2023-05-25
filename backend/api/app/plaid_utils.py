from plaid.model.products import Products
from plaid.model.country_code import CountryCode
from plaid.model.payment_initiation_payment_get_request import PaymentInitiationPaymentGetRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.identity_get_request import IdentityGetRequest
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.item_get_request import ItemGetRequest
from plaid.model.institutions_get_by_id_request import InstitutionsGetByIdRequest
from plaid.model.transfer_authorization_create_request import TransferAuthorizationCreateRequest
from plaid.model.transfer_create_request import TransferCreateRequest
from plaid.model.transfer_network import TransferNetwork
from plaid.model.transfer_type import TransferType
from plaid.model.transfer_user_in_request import TransferUserInRequest
from plaid.model.ach_class import ACHClass
from plaid.model.transfer_create_idempotency_key import TransferCreateIdempotencyKey
from plaid.model.transfer_user_address_in_request import TransferUserAddressInRequest
from plaid.api import plaid_api
from flask import Flask
from flask import request
from flask import jsonify
import plaid
import os
import json
import time
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')

PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')

PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions').split(',')


PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US').split(',')


def empty_to_none(field):
    value = os.getenv(field)
    if value is None or len(value) == 0:
        return None
    return value


host = plaid.Environment.Sandbox

if PLAID_ENV == 'sandbox':
    host = plaid.Environment.Sandbox

if PLAID_ENV == 'development':
    host = plaid.Environment.Development

if PLAID_ENV == 'production':
    host = plaid.Environment.Production


PLAID_REDIRECT_URI = empty_to_none('PLAID_REDIRECT_URI')

configuration = plaid.Configuration(
    host=host,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
        'plaidVersion': '2020-09-14'
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

products = []
for product in PLAID_PRODUCTS:
    products.append(Products(product))


access_token = None

payment_id = None

transfer_id = None

item_id = None


@app.route('/api/info', methods=['POST'])
def info():
    global access_token
    global item_id
    return jsonify({
        'item_id': item_id,
        'access_token': access_token,
        'products': PLAID_PRODUCTS
    })


@app.route('/api/create_link_token', methods=['POST'])
def create_link_token():
    try:
        request = LinkTokenCreateRequest(
            products=products,
            client_name="Plaid Quickstart",
            country_codes=list(
                map(lambda x: CountryCode(x), PLAID_COUNTRY_CODES)),
            language='en',
            user=LinkTokenCreateRequestUser(
                client_user_id=str(time.time())
            )
        )
        if PLAID_REDIRECT_URI != None:
            request['redirect_uri'] = PLAID_REDIRECT_URI
    # create link token
        response = client.link_token_create(request)
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        return json.loads(e.body)


@app.route('/api/set_access_token', methods=['POST'])
def get_access_token():
    global access_token
    global item_id
    global transfer_id
    public_token = request.form['public_token']
    try:
        exchange_request = ItemPublicTokenExchangeRequest(
            public_token=public_token)
        exchange_response = client.item_public_token_exchange(exchange_request)
        access_token = exchange_response['access_token']
        item_id = exchange_response['item_id']
        if 'transfer' in PLAID_PRODUCTS:
            transfer_id = authorize_and_create_transfer(access_token)
        return jsonify(exchange_response.to_dict())
    except plaid.ApiException as e:
        return json.loads(e.body)


@app.route('/api/auth', methods=['GET'])
def get_auth():
    try:
        request = AuthGetRequest(
            access_token=access_token
        )
        response = client.auth_get(request)
        pretty_print_response(response.to_dict())
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    # Set cursor to empty to receive all historical updates
    cursor = ''

    # New transaction updates since "cursor"
    added = []
    modified = []
    removed = []  # Removed transaction ids
    has_more = True
    try:
        # Iterate through each page of new transaction updates for item
        while has_more:
            request = TransactionsSyncRequest(
                access_token=access_token,
                cursor=cursor,
            )
            response = client.transactions_sync(request).to_dict()
            # Add this page of results
            added.extend(response['added'])
            modified.extend(response['modified'])
            removed.extend(response['removed'])
            has_more = response['has_more']
            # Update cursor to the next cursor
            cursor = response['next_cursor']
            pretty_print_response(response)

        # Return the 8 most recent transactions
        latest_transactions = sorted(added, key=lambda t: t['date'])[-8:]
        return jsonify({
            'latest_transactions': latest_transactions})

    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/identity', methods=['GET'])
def get_identity():
    try:
        request = IdentityGetRequest(
            access_token=access_token
        )
        response = client.identity_get(request)
        pretty_print_response(response.to_dict())
        return jsonify(
            {'error': None, 'identity': response.to_dict()['accounts']})
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/balance', methods=['GET'])
def get_balance():
    try:
        request = AccountsBalanceGetRequest(
            access_token=access_token
        )
        response = client.accounts_balance_get(request)
        pretty_print_response(response.to_dict())
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    try:
        request = AccountsGetRequest(
            access_token=access_token
        )
        response = client.accounts_get(request)
        pretty_print_response(response.to_dict())
        return jsonify(response.to_dict())
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/payment', methods=['GET'])
def payment():
    global payment_id
    try:
        request = PaymentInitiationPaymentGetRequest(payment_id=payment_id)
        response = client.payment_initiation_payment_get(request)
        pretty_print_response(response.to_dict())
        return jsonify({'error': None, 'payment': response.to_dict()})
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


@app.route('/api/item', methods=['GET'])
def item():
    try:
        request = ItemGetRequest(access_token=access_token)
        response = client.item_get(request)
        request = InstitutionsGetByIdRequest(
            institution_id=response['item']['institution_id'],
            country_codes=list(
                map(lambda x: CountryCode(x), PLAID_COUNTRY_CODES))
        )
        institution_response = client.institutions_get_by_id(request)
        pretty_print_response(response.to_dict())
        pretty_print_response(institution_response.to_dict())
        return jsonify({'error': None, 'item': response.to_dict()[
            'item'], 'institution': institution_response.to_dict()['institution']})
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


def pretty_print_response(response):
    print(json.dumps(response, indent=2, sort_keys=True, default=str))


def format_error(e):
    response = json.loads(e.body)
    return {'error': {'status_code': e.status, 'display_message':
                      response['error_message'], 'error_code': response['error_code'], 'error_type': response['error_type']}}

# This is a helper function to authorize and create a Transfer after successful
# exchange of a public_token for an access_token. The transfer_id is then used
# to obtain the data about that particular Transfer.


def authorize_and_create_transfer(access_token):
    try:
        # We call /accounts/get to obtain first account_id - in production,
        # account_id's should be persisted in a data store and retrieved
        # from there.
        request = AccountsGetRequest(access_token=access_token)
        response = client.accounts_get(request)
        account_id = response['accounts'][0]['account_id']

        request = TransferAuthorizationCreateRequest(
            access_token=access_token,
            account_id=account_id,
            type=TransferType('credit'),
            network=TransferNetwork('ach'),
            amount='1.34',
            ach_class=ACHClass('ppd'),
            user=TransferUserInRequest(
                legal_name='FirstName LastName',
                email_address='foobar@email.com',
                address=TransferUserAddressInRequest(
                    street='123 Main St.',
                    city='San Francisco',
                    region='CA',
                    postal_code='94053',
                    country='US'
                ),
            ),
        )
        response = client.transfer_authorization_create(request)
        pretty_print_response(response)
        authorization_id = response['authorization']['id']

        request = TransferCreateRequest(
            idempotency_key=TransferCreateIdempotencyKey(
                '1223abc456xyz7890001'),
            access_token=access_token,
            account_id=account_id,
            authorization_id=authorization_id,
            type=TransferType('credit'),
            network=TransferNetwork('ach'),
            amount='1.34',
            description='Payment',
            ach_class=ACHClass('ppd'),
            user=TransferUserInRequest(
                legal_name='FirstName LastName',
                email_address='foobar@email.com',
                address=TransferUserAddressInRequest(
                    street='123 Main St.',
                    city='San Francisco',
                    region='CA',
                    postal_code='94053',
                    country='US'
                ),
            ),
        )
        response = client.transfer_create(request)
        pretty_print_response(response)
        return response['transfer']['id']
    except plaid.ApiException as e:
        error_response = format_error(e)
        return jsonify(error_response)


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 8000))
