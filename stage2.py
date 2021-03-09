import requests

from env import config

# https://webexapis.com/v1/meetings

headers = {
    'Authorization': f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

roomlist_url = f"{config['WEBEX_BASE_URL']}/v1/rooms"
roomlist = requests.get(roomlist_url, headers=headers)


