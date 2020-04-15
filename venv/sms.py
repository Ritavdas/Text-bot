from twilio.rest import Client

account_sid = 'AC33b1631b7fb1bff8912dca2a15909cae'
auth_token = '1dc3ab6e934b45c2112ae3ed8ce106f4'  # your auth token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="HELLO KAUSIK DAS . YOU SEND SOMEONE DOWN TO GET FRUITS OR MEDICINES AGAIN . IT WILL BOT BE GOOD",
    from_='+18507357744',
    to="+919650098075"
)

print(message.sid)
