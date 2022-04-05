import requests
import time
import urllib.parse
from base64 import b64encode
import hmac
import hashlib
import binascii

grant_type = 'client_credentials'
oauth_consumer_key = 'BgaP9o8n-3tUI_d9FT3Vdw'
access_key_secret = 'gR4_5N0QG39hgeuJ9mN1ca2caPoElMiTE7WA0A2D25BoDRoH6rFwIurCOHCsB7TjjIPLY_ocVaH17Pbxg0zXdQ'
oauth_nonce = str(int(time.time() * 1000))
oauth_timestamp = str(int(time.time()))
oauth_signature_method = 'HMAC-SHA256'
oauth_version = '1.0'
url = 'https://account.api.here.com/oauth2/token'


# HMAC-SHA256 hashing algorithm to generate the OAuth signature
def create_signature(secret_key, signature_base_string):
    encoded_string = signature_base_string.encode()
    encoded_key = secret_key.encode()
    temp = hmac.new(encoded_key, encoded_string, hashlib.sha256).hexdigest()
    byte_array = b64encode(binascii.unhexlify(temp))
    return byte_array.decode()


# concatenate the six oauth parameters, plus the request parameters from above, sorted alphabetically by the key and
# separated by "&"
def create_parameter_string(grant_type, oauth_consumer_key, oauth_nonce, oauth_signature_method, oauth_timestamp,
                            oauth_version):
    parameter_str = ''
    parameter_str = parameter_str + 'grant_type=' + grant_type
    parameter_str = parameter_str + '&oauth_consumer_key=' + oauth_consumer_key
    parameter_str = parameter_str + '&oauth_nonce=' + oauth_nonce
    parameter_str = parameter_str + '&oauth_signature_method=' + oauth_signature_method
    parameter_str = parameter_str + '&oauth_timestamp=' + oauth_timestamp
    parameter_str = parameter_str + '&oauth_version=' + oauth_version
    return parameter_str


parameter_string = create_parameter_string(grant_type, oauth_consumer_key, oauth_nonce, oauth_signature_method,
                                           oauth_timestamp, oauth_version)
encoded_parameter_string = urllib.parse.quote(parameter_string, safe='')
encoded_base_string = 'POST' + '&' + urllib.parse.quote(url, safe='')
encoded_base_string = encoded_base_string + '&' + encoded_parameter_string

# create the signing key
signing_key = access_key_secret + '&'

oauth_signature = create_signature(signing_key, encoded_base_string)
encoded_oauth_signature = urllib.parse.quote(oauth_signature, safe='')

# ---------------------Requesting Token---------------------
body = {'grant_type': '{}'.format(grant_type)}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'OAuth oauth_consumer_key="{oauth_consumer_key}",oauth_nonce="{oauth_nonce}",oauth_signature="{encoded_oauth_signature}",oauth_signature_method="HMAC-SHA256",oauth_timestamp="{oauth_timestamp}",oauth_version="1.0"'
}

response = requests.post(url, data=body, headers=headers)

print(response.text)
