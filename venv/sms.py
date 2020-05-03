from twilio.rest import Client

account_sid = ''
auth_token = ''  # your auth token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="*enters gibberish*",
    from_='************', #enter twilio number here
    to="***********" # enter number where you want to send text
)

print(message.sid)
