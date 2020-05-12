import re

r = r"[^a-z]*([y]o|[h']?ello|ok|hi|hey|(good[ ])?(morn[gin']{0,3}|"\
    r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(r, flags=re.IGNORECASE)
re_greeting.match('Hello Rosa')
#<_sre.SRE_Match object; span=(0, 10), match='Hello Rosa'>
re_greeting.match('Hello Rosa').groups()
('Hello', None, None, 'Rosa')
re_greeting.match("Good morning Rosa")
#<_sre.SRE_Match object; span=(0, 17), match="Good morning Rosa">
re_greeting.match("Good Manning Rosa")#.groups()
# ('Good Manning', 'Good', 'Manning', 'Rosa')
re_greeting.match('Good evening Rosa Parks').groups()
('Good evening', 'Good ', 'evening', 'Rosa')
re_greeting.match("Good Morn'n Rosa")
#<_sre.SRE_Match object; span=(0, 16), match="Good Morn'n Rosa">
re_greeting.match("yo Rosa")
#<_sre.SRE_Match object; span=(0, 7), match='yo Rosa'>

# print(re_greeting.match)
# print(re_greeting.groups)
# print(re_greeting)


my_names = set(['rosa', 'rose', 'chatty', 'chatbot', 'bot',
    'chatterbot'])
curt_names = set(['hal', 'you', 'u'])
rude_names = set(['69', 'bitch', '420', 'fag'])
greeter_name = ''
match = re_greeting.match(input('You: '))

if match:
    at_name = match.groups()[-1]
    if at_name in curt_names:
        print("Rosa: Good one.")
    elif at_name.lower() in my_names:
        print("Rosa: Hi {}, How are you?".format(greeter_name))
    elif at_name in rude_names:
        print("Rosa: Fuck you.")
