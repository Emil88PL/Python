import pprint

message = 'It was a bright day in April, and the clock were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


### triple '''
