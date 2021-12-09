from __future__ import print_function
from telesign.messaging import MessagingClient

customer_id = "<Customer_id>"
api_key = "api_key"
messaging = MessagingClient(customer_id, api_key)
message = input("Enter your message: ")
message_type = "ARN"

with open("numbers.txt", "r") as f:
    for i in f.readlines():
        phone_number = i
        print("Sending message to ", i)
        response = messaging.message(phone_number, message, message_type)
        print("Message sent !")
