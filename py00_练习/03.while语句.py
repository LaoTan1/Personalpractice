# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
_author_ = '谭华锦'

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program.'

messag = ' '

while messag != 'quit':
    messag = input(prompt)

    if messag != 'quit':
        print(prompt)

while True:
    city = input('prompt')

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + '!')
