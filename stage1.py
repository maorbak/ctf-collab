import requests

from env import config


# Get room list : https://webexapis.com/v1/rooms
# Get room info : https://webexapis.com/v1/rooms/{roomId}

headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

roomlist_url = f"{config['WEBEX_BASE_URL']}/v1/rooms"
roomlist = requests.get(roomlist_url, headers=headers)

# myRoom = requests.post(myRoom_url, headers=headers, data=payload)

# Make sure no other room exists before creating one
counter = '0'

for item in roomlist.json()['items']:
    if item['title'] == 'Mari test room':
        counter = '1'
    
payload = {
    'title': 'Mari test room'
}
    
if counter == '0':
    myRoom = requests.post(roomlist_url, headers=headers, data=payload)
    myRoomId = myRoom.json()['id']
    
# Create new room
print(myRoomId)

membership_url = f"{config['WEBEX_BASE_URL']}/v1/memberships?roomId={myRoomId}"
membership = requests.get(membership_url, headers=headers)

payloadMember = {
    "personEmail": "mneiding@cisco.com"
}

# addMember = requests.post(membership_url, headers=headers, data=payloadMember)

# print(membership.json())