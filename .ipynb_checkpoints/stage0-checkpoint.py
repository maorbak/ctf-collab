import requests

from env import config


# Get room list : https://webexapis.com/v1/rooms
# Get room info : https://webexapis.com/v1/rooms/{roomId}

headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

roomlist_url = f"{config['WEBEX_BASE_URL']}/v1/rooms"
roomlist = requests.get(roomlist_url, headers=headers)

# print(roomlist.json())

for item in roomlist.json()['items']:
    if item['title'] == "Yogalicious":
        room_id = item['id']

print(room_id)