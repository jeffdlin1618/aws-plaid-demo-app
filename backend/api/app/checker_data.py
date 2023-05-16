import json


CHECKER_DATA = {
    "CitiBank": [
        {
            "account_type": {
                "names": ["business checking account in-branch"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-12"
                },
                "constraint_or": [{
                    "amount_within_days": 30,
                    "amount_greater": 5000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 30,
                    "amount_greater": 15000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 30,
                    "amount_greater": 25000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 30,
                    "amount_greater": 50000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 30,
                    "amount_greater": 100000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 30,
                    "amount_greater": 200000,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": 60,
                    "for_date": None,
                    "minimum_balance": "same",
                },
                "bonuses": [{
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 200
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 500
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 700
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 1000
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 1500
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 2000
                }],
                "info": {
                    "amount_credit": "within 90 days from the end of the month"
                }
            }
            ]
        },
        {
            "account_type": {
                "names": ["Priority Account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-23"
                },
                "constraint_or": [{
                    "amount_within_days": 20,
                    "amount_greater": 10000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 20,
                    "amount_greater": 30000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 20,
                    "amount_greater": 75000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 20,
                    "amount_greater": 200000,
                    "amount_less": None,
                    "amount_equals": None
                }, {
                    "amount_within_days": 20,
                    "amount_greater": 300000,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": 60,
                    "after_days": 21,
                    "for_date": None,
                    "minimum_balance": "same",
                },
                "bonuses": [{
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 200
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 500
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 1000
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 1500
                }, {
                    "credit_after_days": "info",
                    "credit_after_date": "info",
                    "amount": 2000
                }],
                "info": {
                    "amount_credit": "within 30 calendar days after completing the requirements"
                }
            }
            ]
        }
    ],
    "U.S. Bank": [
        {
            "account_type": {
                "name": ["Business Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-04-23"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": 3000,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "minimum_balance": "same",
                },
                "bonuses": [{
                    "credit_after_days": 45,
                    "credit_after_date": None,
                    "amount": 500
                }]
            }]
        },
        {
            "account_type": {
                "name": ["Standard Savings Account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-02"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_within_date": "2023-05-31",
                    "amount_greater": 15000,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": None,
                    "after_days": None,
                    "for_date": "2023-08-31",
                    "minimum_balance": 25000,
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 200
                }]
            }]
        }, {
            "account_type": {
                "name": ["Smartly checking account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-02"
                },
                "constraint_or": [{
                    "amount_within_days": 90,
                    "amount_within_date": None,
                    "amount_greater": 5000,
                    "no_of_recurring_deposits": 2,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": None,
                    "after_days": None,
                    "for_date": None,
                    "minimum_balance": None,
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": None,
                    "amount": 200
                }]
            }]
        },
    ],
    "Chase": [
        {
            "account_type": {
                "name": ["Chase Private Client Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-19"
                },
                "constraint_or": [
                {
                    "amount_within_days": 45,
                    "amount_greater": 150000,
                    "amount_less": None,
                    "amount_equals": None
                },
                {
                    "amount_within_days": 45,
                    "amount_greater": 250000,
                    "amount_less": None,
                    "amount_equals": None
                },
                {
                    "amount_within_days": 45,
                    "amount_greater": 500000,
                    "amount_less": None,
                    "amount_equals": None
                },
                ],
                "maintain": {
                    "for_days": 90,
                    "after_days": None,
                    "for_date": None,
                    "minimum_balance": "same",
                },
                "bonuses": [
                {
                    "credit_after_days": 45,
                    "credit_after_date": None,
                    "amount": 1000
                },
                {
                    "credit_after_days": 45,
                    "credit_after_date": None,
                    "amount": 2000
                },
                {
                    "credit_after_days": 45,
                    "credit_after_date": None,
                    "amount": 3000
                },
                ]
            }]
        },
        {
            "account_type": {
                "name": ["Chase Business Complete Banking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-08-03"
                },
                "constraint_or": [
                {
                    "amount_within_days": None,
                    "amount_greater": 2000,
                    "amount_less": None,
                    "amount_equals": None
                },
                {
                    "amount_within_days": None,
                    "amount_greater": 15000,
                    "amount_less": None,
                    "amount_equals": None
                },
                ],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": "2023-08-3",
                    "minimum_balance": 2000,
                },
                "bonuses": [
                {
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 300
                },
                {
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 500
                },
                ]
            }]
        },
        {
            "account_type": {
                "name": ["Chase total checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-19"
                },
                "bonuses": [{
                    "credit_after_days": 90,
                    "credit_after_date": None,
                    "amount": 200
                }]
            }]
        },

        {
            "account_type": {
                "name": ["Chase College Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-19"
                },
               "constraint_or": [
                {
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "minimum_balance": "same",
                    "transactions": 10,
                },
                "bonuses": [{
                    "credit_after_days": 15,
                    "credit_after_date": None,
                    "amount": 100
                }]
            }]
        },
        {
            "account_type": {
                "name": ["Chase Secure Banking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-19"
                },
                "bonuses": [{
                    "credit_after_days": 15,
                    "credit_after_date": None,
                    "amount": 100
                }]
            }]
        }
    ],
    "Bank of America": [
        {
            "account_type": {
                "name": ["Advantage Banking Account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-07-19"
                },
                "maintain": {
                    "for_days": 90,
                    "after_days": None,
                    "for_date": None
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": None,
                    "amount": 100
                },]
            }]
        },
        {
            "account_type": {
                "name": ["Bank of America Business Advantage Checking Bonus Offer"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 5000,
                },],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": "2023-08-3",
                    "minimum_balance": 5000,
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 300
                }]
            }],
            "info": {
                "amount_credit": "bonus will be deposited within 60 days from the end of your qualifications"
            }
        }
    ],
    "SoFi": [
        {
            "account_type": {
                "name": ["SoFi Checking and Savings"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-12-31"
                },
                "constraint_or": [{
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 1000,
                },
                {
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 5000,
                },
                ],
                "maintain": {
                    "for_days": 90,
                    "after_days": None,
                    "for_date": None
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 50
                },
                {
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 250
                },
                ],
                "info": {
                    "amount_credit": "Complete at least 1 direct deposit during the promotion period."
                }
            }]
        },
        {
            "account_type": {
                "name": ["SoFi Checking and Savings - 75"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 14,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 10,
                },],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": "2023-08-3",
                    "minimum_balance": 5000,
                },
                "bonuses": [{
                    "credit_after_days": 14,
                    "credit_after_date": None,
                    "amount": 75
                }]
            }],
            "info": {
                "amount_credit": "Share your SoFi Checking and Savings referral link with friends who are new to SoFi."
            }
        }
    ],

    "M1 FINANCE": [
        {
            "account_type": {
                "name": ["M1 Spend"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-12-31"
                },
                "constraint_or": [{
                    "amount_within_days": 14,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 2500,
                },
                {
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 5000,
                },
                ],
                "maintain": {
                    "for_days": 30,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 100
                }
                ],
            }]
        }
    ],
    "Axos Bank": [
        {
            "account_type": {
                "name": ["Rewards Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 90,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 1500
                },
                ],
                "bonuses": [{
                    "credit_after_days": 10,
                    "credit_after_date": None,
                    "amount": 100
                }
                ],
            }],
            "info": {
                "amount_credit": "Open a new Rewards Checking account with promo code RC100 and fund it within 60 days of account opening."
            }
        },
        {
            "account_type": {
                "name": ["Business Interest Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": None
                },],
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 5,
                    "credit_after_date": None,
                    "amount": 200
                }],
            }],
        },
        {
            "account_type": {
                "name": ["Basic Business Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 5,
                    "credit_after_date": None,
                    "amount": 200
                }],
            }],
            "info": {
                "amount_credit": "Open a new Basic Business checking account from Axos Bank with promo code NEWBIZ200 (or NEWAXOSBIZ for older companies)."
            }
        },
         {
            "account_type": {
                "name": ["Business Premium Savings"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 5,
                    "credit_after_date": None,
                    "amount": 200
                }],
            }],
            "info": {
                "amount_credit": "Open a new Business Premium Savings account from Axos Bank with promo code NEWBIZ200 for businesses incorporated after 06/01/2020 (or NEWAXOSBIZ for older companies)."
            }
        },
        {
            "account_type": {
                "name": ["Business Savings"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 5,
                    "credit_after_date": None,
                    "amount": 200
                }],
            }],
            "info": {
                "amount_credit": "Open a new Business Savings account using the link below. If you incorporated after June 1, 2020, use promo code NEWBIZ200 for the $200 bonus, otherwise use promo code NEWAXOSBIZ for a $100 bonus."
            }
        },
        {
            "account_type": {
                "name": ["Business Money Market"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 60,
                    "after_days": None,
                    "for_date": None,
                    "balance_above": 2500
                },
                "bonuses": [{
                    "credit_after_days": 5,
                    "credit_after_date": None,
                    "amount": 200
                }],
            }],
            "info": {
                "amount_credit": "Open a new Business Money Market Account using promocode NEWBIZ200 ($200) or NEWAXOSBIZ ($100)."
            }
        }
     ],
    "Discover": [
        {
            "account_type": {
                "name": ["Online savings account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-15"
                },
                "constraint_or": [{
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 15000,
                },
                {
                    "amount_within_days": 30,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "deposit": 25000,
                },
                ],
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 150
                },
                {
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 200
                }
                ],
            }],
        },
         {
            "account_type": {
                "name": ["Cashback debit"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-15"
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": None,
                    "amount": 360
                },],
            }],
            "info": {
                "amount_credit": "Use your debit card to earn cashback up to $30 can be earned per month "
            }
        }
    ],
    "Alliant": [
    {
        "account_type": {
            "names": ["High-Rate Savings"]
        },
        "conditions": [{
            "start": {
                "date": None,
            },
            "expiry": {
                "date": "2023-05-27"
            },
            "constraint_or": [{
                "amount_within_days": 30,
                "amount_greater": 1000,
                "amount_less": None,
                "amount_equals": 1000
            },],
            "maintain": {
                "for_days": 90,
                "for_date": None,
                "minimum_balance": "same",
            },
            "bonuses": [{
                "credit_after_days": 30,
                "credit_after_date": "info",
                "amount": 100
            }],
        }]},
    {
        "account_type": {
            "names": ["Ultimate Opportunity Savings Account"]
        },
        "conditions": [{
            "start": {
                "date": None,
            },
            "expiry": {
                "date": "2023-12-31"
            },
            "maintain": {
                "for_days": 360,
                "for_date": None,
                "minimum_balance": 100,
            },
            "bonuses": [{
                "credit_after_days": "info",
                "credit_after_date": "info",
                "amount": 100
            }],
        }]
    },
    ],
    "PNC Bank": [
        {
            "account_type": {
                "names": ["Virtual Wallet® with Performance Select"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": 5000,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": "same",
                    "deposit": 5000
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": "info",
                    "amount": 400
                }],
            }]
        },
        {
            "account_type": {
                "names": ["Virtual Wallet® with Performance Spend"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": "same",
                    "deposit": 2000
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": "info",
                    "amount": 200
                }],
            }]
        },
        {
            "account_type": {
                "names": ["Virtual Wallet [Out of Footprint]"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": "same",
                    "deposit": 2000
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": "info",
                    "amount": 200
                }],
                "info": {
                    "amount_credit": "Reside in a state that doesn't have a PNC branch."
                }
            }]
        },
        {
            "account_type": {
                "names": ["Virtual Wallet®"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": None,
                    "within_days": 30,
                    "for_date": None,
                    "minimum_balance": "same",
                    "deposit": 500
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": "info",
                    "amount": 50
                }],
                "info": {
                    "amount_credit": "Open a Virtual Wallet® account"
                }
            }]
        },
        {
            "account_type": {
                "names": ["Enterprise Checking Account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 90,
                    "within_days": None,
                    "for_date": None,
                    "minimum_balance": 30000,
                    "deposit": None,
                },
                "bonuses": [{
                    "credit_after_days": 90,
                    "credit_after_date": "info",
                    "amount": 500
                }],
                "info": {
                    "amount_credit": "Open a new Treasury Enterprise Plan or Analysis Business Checking account."
                }
            }]
        },
        {
            "account_type": {
                "names": ["Business Checking Account"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "maintain": {
                    "for_days": 90,
                    "within_days": None,
                    "for_date": None,
                    "minimum_balance": 5000,
                    "deposit": None,
                },
                "Cycles": {
                    "statement_cycles": 90, # 3 statement cycles
                    "transactions": 20,
                },
                "bonuses": [{
                    "credit_after_days": 90,
                    "credit_after_date": "info",
                    "amount": 200
                }],
                "info": {
                    "amount_credit": "Open a new Business Checking or Business Checking Plus account."
                }
            }]
        },
    ],
    "Upgrade": [
        {
            "account_type": {
                "names": ["Rewards Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-30"
                },
                "constraint_or": [{
                    "amount_within_days": 60,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "purchases": 3
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": "same",
                    "deposit": 5000
                },
                "bonuses": [{
                    "credit_after_days": 60,
                    "credit_after_date": "info",
                    "amount": 200
                }],
            }]
        }
    ],
     "Wells Fargo Bank": [
        {
            "account_type": {
                "names": ["Premier Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-13"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "purchases": None,
                }],
                "maintain": {
                    "for_days": 90,
                    "within_days": 45,
                    "for_date": None,
                    "minimum_balance": 250000,
                    "deposit": 250000
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": "info",
                    "amount": 2500
                }],
            }]
        },
        {
            "account_type": {
                "names": ["Personal Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-22"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "purchases": None,
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 90,
                    "for_date": None,
                    "minimum_balance": None,
                    "deposit": 25,
                    "direct_deposits": 1000,
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": "info",
                    "amount": 325
                }],
            }]
        },
        {
            "account_type": {
                "names": ["Way2Save® Savings"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-23"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": None,
                    "purchases": None,
                }],
                "maintain": {
                    "for_days": 90,
                    "within_days": 30,
                    "for_date": None,
                    "minimum_balance": None,
                    "deposit": 25000,
                    "direct_deposits": None,
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": "info",
                    "amount": 525
                }],
            }]
        }
    ],
    "Wings Financial Credit Union": [
        {
            "account_type": {
                "names": ["Personal Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-31"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": 25,
                    "purchases": 5,
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": None,
                    "deposit": None,
                    "direct_deposits": 600
                },
                "bonuses": [{
                    "credit_after_days": 30,
                    "credit_after_date": "info",
                    "amount": 300
                }],
            }]
        },
    ],
    "Thrivent Federal Credit Union": [
        {
            "account_type": {
                "names": ["Rewards Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-06-09"
                },
                "constraint_or": [{
                    "amount_within_days": None,
                    "amount_greater": None,
                    "amount_less": None,
                    "amount_equals": 25,
                    "purchases": None,
                    "purchases_amount": 500,
                }],
                "maintain": {
                    "for_days": None,
                    "within_days": 90,
                    "for_date": None,
                    "minimum_balance": None,
                    "deposit": None,
                    "direct_deposits": 2500
                },
                "bonuses": [{
                    "credit_after_days": 90,
                    "credit_after_date": "info",
                    "amount": 200
                }],
            }]
        },
    ],
    "Andrews Federal Credit Union": [
        {
            "account_type": {
                "names": ["Payback Checking"]
            },
            "conditions": [{
                "start": {
                    "date": None,
                },
                "expiry": {
                    "date": "2023-05-31"
                },
                "maintain": {
                    "for_days": None,
                    "within_days": 60,
                    "for_date": None,
                    "minimum_balance": None,
                    "deposit": None,
                    "direct_deposits": 500
                },
                "bonuses": [{
                    "credit_after_days": 90,
                    "credit_after_date": "info",
                    "amount": 125
                }],
            }]
        },
    ],
}

with open('CHECKER_DATA.json', 'w') as file:
    json.dump(CHECKER_DATA, file)