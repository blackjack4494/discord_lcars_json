import json

f = open('sample.json')
a = json.load(f)
f.close()

data = {}
data['messages'] = []

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
json_file = open('sample_embed.json', 'w')
json.dump(data, json_file, indent=2)
json_file.close()
