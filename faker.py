from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Generate a fake credit card number
credit_card_number = fake.credit_card_number()

print("Fake Credit Card Number:", credit_card_number)
