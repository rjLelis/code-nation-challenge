import requests
import utils

# First part

key = 'c287d8c593d3a2279ea43de3734aeecb343824d9'

urls = {
    'generate_file': f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={key}',
    'submit_file': f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={key}'
}

r = requests.get(urls['generate_file'])

utils.write_json_content('answer.json', r.json())

# Second part


json_content = utils.read_json_content('answer.json')

json_dict = utils.to_dict(json_content)

encrypted_text = json_dict['cifrado']
key = json_dict['numero_casas']

decrypted_text = utils.decrypt(encrypted_text, key)
sha1_text = utils.get_sha1(decrypted_text)

json_dict['decifrado'] = decrypted_text
json_dict['resumo_criptografico'] = sha1_text

utils.write_json_content('answer.json', json_dict)

# Third Part


files = {'answer': open('answer.json', 'rb')}

r = requests.post(urls['submit_file'], files=files)

print(r.text)