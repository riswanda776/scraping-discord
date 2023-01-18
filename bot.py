import requests

CHANNELID = '1063089224800280656'
HEADERS = {'authorization': 'ODM3MzI1NjA2MjE0OTU5MTQ1.G1vhJo.8DrfPYSifQYu0USn_DaSCA92XhFToAfsn_xGac'}
LIMIT=100
all_messages = []

r = requests.get(f'https://discord.com/api/v9/channels/{CHANNELID}/messages?limit={LIMIT}',headers=HEADERS)
all_messages.extend(r.json())

print(f'len(r.json()) is {len(r.json())}','\n')

while len(r.json()) == LIMIT:
    last_message_id = r.json()[-1].get('id')
    r = requests.get(f'https://discord.com/api/v9/channels/{CHANNELID}/messages?limit={LIMIT}&before={last_message_id}',headers=HEADERS)
    all_messages.extend(r.json())
    print(f'len(r.json()) is {len(r.json())} and last_message_id is {last_message_id} and len(all_messages) is {len(all_messages)}')