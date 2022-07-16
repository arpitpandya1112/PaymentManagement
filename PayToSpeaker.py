n = float(input("Enter the total payment done by the organiser : "))


def calculate_payment(amount):
    return 0.1 * amount


speakerAmount = n - calculate_payment(n)
organisationAmount = calculate_payment(n)

print('Amount paid to speaker', round(speakerAmount, 2))
print('Amount paid to organisation', round(organisationAmount, 2))
