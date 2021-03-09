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
    
myRoom_url = f"{WEBEX_BASE_URL}/v1/rooms"
payload = {
    'title': 'Mari test room'
}
roomlist_url = f"{config['WEBEX_BASE_URL']}/v1/rooms"
    
if counter == '0':
    myRoom = requests.post(myRoom_url, headers=headers, data=payload)
    myRoomId = myRoom.json()['id']

print(myRoomId)