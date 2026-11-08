# Legacy Bank mainframe - receives DES-ECB encrypted messages
# Mohammad Hazem - 202200696

import socket
from des import ecb_decrypt, ecb_encrypt

KEY = b"56374804"
HOST = "127.0.0.1"
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
print("Mainframe listening on", HOST, PORT)
print("Key:", KEY.decode())

while True:
    conn, addr = server.accept()
    ciphertext = conn.recv(4096)
    print("\nConnection from", addr[0], addr[1])
    print("Ciphertext received:", ciphertext.hex().upper())
    for i in range(0, len(ciphertext), 8):
        print("  block", i // 8 + 1, ":", ciphertext[i:i + 8].hex().upper())

    plaintext = ecb_decrypt(ciphertext, KEY)
    print("Decrypted message  :", plaintext.decode())

    conn.sendall(ecb_encrypt(b"ACK " + plaintext, KEY))
    conn.close()
