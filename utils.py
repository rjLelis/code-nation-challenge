from hashlib import sha1
import json

def decrypt(message, key):

    ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z')


    translated = ''

    for letter in message.lower():

        if letter in ALPHABET:
            index = ALPHABET.index(letter)
            index -= key
            if index < 0:
                index += len(ALPHABET)

            translated += ALPHABET[index]

        else:
            translated += letter        

    return translated


def get_sha1(message):
    return sha1(message.encode('utf-8')).hexdigest()


def write_json_content(file, content):
    with open(file, 'w') as file:
        json_file = json.dumps(content, indent=2)
        file.write(json_file)


def read_json_content(file):
    with open(file, 'r') as json_file:
        json_content = json_file.read()
    return json_content


def to_dict(content):
    return json.loads(content)


def to_json(content, indent=0):
    return json.dumps(content, indent=indent)