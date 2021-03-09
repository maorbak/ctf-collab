import requests

from env import config

# https://webexapis.com/v1/meetings

headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

meetings_url = f"{config['WEBEX_BASE_URL']}/v1/meetings?max=100"
meetings = requests.get(meetings_url, headers=headers)

counter = 0

for item in meetings.json()['items']:
    print(item['title'])
    counter = counter + 1

print(counter)
# print(meetings.json()['items'])


# Find number of messages in a space
messages_url = f"{config['WEBEX_BASE_URL']}/v1/messages/direct?personEmail=sifang@cisco.com"
messages = requests.get(messages_url, headers=headers)


counterM = 0

for item in messages.json()['items']:
    counterM = counterM + 1

print(counterM)

# Find number of messages in a space

messages2_url = f"{config['WEBEX_BASE_URL']}/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYjI1ZTJlNDYtZGQ5Ny0zNzMyLTgyODItYWQ3NzVlY2RlNTc0&max=10000"
messages2 = requests.get(messages2_url, headers=headers)


counterN = 0

for item in messages2.json()['items']:
    counterN = counterN + 1

print(counterN)


