import json
import os

# gather all files - json in particular
files = []
for file in os.listdir('json_raw'):
    if file.endswith('.json'):
        files.append(file)

# sieve all files
for file in files:
    data = {}
    data['messages'] = []

    f = open('json_raw/' + file)
    a = json.load(f)
    f.close()

    # extract all messages
    msgs = []
    for msg in a['messages']:
        msgs.append(msg)

    # extract all embeds
    # embeds = []
    for msg in msgs:
        if msg['embeds']:
            msg['embeds'][0].pop('url', None)
            msg['embeds'][0].pop('timestamp', None)
            msg['embeds'][0].pop('color', None)
            thumb = msg['embeds'][0].get('thumbnail')
            if thumb:
                msg['embeds'][0].get('thumbnail').pop('width', None)
                msg['embeds'][0].get('thumbnail').pop('height', None)
            msg['embeds'][0].pop('footer', None)
            # embeds.append(msg['embeds'])
            data['messages'].append(msg['embeds'])

    json_data = json.dumps(data, indent=2)
    json_file = open('json_embeds/' + file, 'w')
    json_file.write(json_data)
    json_file.close()
