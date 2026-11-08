# Legacy Bank mobile app - sends a DES-ECB encrypted message
# Mohammad Hazem - 202200696
# usage: python client.py            (sends mohazem8)
#        python client.py some text  (sends some text)

import socket
import sys
from des import ecb_encrypt, ecb_decrypt

KEY = b"56374804"
HOST = "127.0.0.1"
PORT = 5050

if len(sys.argv) > 1:
    message = " ".join(sys.argv[1:])
else:
    message = "mohazem8"

ciphertext = ecb_encrypt(message.encode(), KEY)
print("Key       :", KEY.decode())
print("Plaintext :", message)
print("Ciphertext:", ciphertext.hex().upper())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(ciphertext)
reply = client.recv(4096)
client.close()

print("Server reply (decrypted):", ecb_decrypt(reply, KEY).decode())
