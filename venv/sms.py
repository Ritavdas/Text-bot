from twilio.rest import Client

account_sid = ''
auth_token = ''  # your auth token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="HELLO. YOU SEND SOMEONE DOWN TO GET FRUITS OR MEDICINES AGAIN . IT WILL BOT BE GOOD",
    from_='************', #enter twilio number here
    to="***********" # enter number where you want to send text
)

print(message.sid)
