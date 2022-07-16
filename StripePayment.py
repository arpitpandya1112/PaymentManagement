import stripe

stripe.api_key = 'sk_test_51LMIx6DRUlp1uIJcx3ilhxMW7NP6ChX5B6LorJStuKOAGnP4S8nhqoKcOtU3UguX7lfcjciYMkEkKc0p4VKaVbVR00V0a75nTW'


def commission_count(amount):
    return 0.1 * amount


# Stripe is taking amount in the smallest unit so for GBP its penny
stripeCharge = 0.30
buyerPayment = 50
commissionAmount = commission_count(buyerPayment)

totalPayableByUser = int((buyerPayment + stripeCharge) * 100)
totalPayableToSeller = int((buyerPayment - commissionAmount) * 100)
totalPayableToUs = commissionAmount * 100

# Create a PaymentIntent:
payment_intent = stripe.PaymentIntent.create(
    amount=totalPayableByUser,
    currency='gbp',
    payment_method_types=['card'],
    transfer_group='{ORDER10}',
)

# Create a Transfer to a connected account (later):
transfer2 = stripe.Transfer.create(
    amount=totalPayableToUs,
    currency="gbp",
    destination="acct_1032D82eZvKYlo2C",
    transfer_group="{ORDER10}",
)

# Create a second Transfer to another connected account (later):
transfer = stripe.Transfer.create(
    amount=totalPayableToSeller,
    currency='gbp',
    destination='acct_1LMIx6DRUlp1uIJc',
    transfer_group='{ORDER10}',
)
