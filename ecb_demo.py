# ECB demo: two identical blocks and one different block
# Mohammad Hazem - 202200696

from des import encrypt_block

KEY = b"56374804"
blocks = [b"mohazem8", b"mohazem8", b"hazem696"]

print("Key:", KEY.decode())
print()
print("block  plaintext   ciphertext")
cipher = []
for i, block in enumerate(blocks):
    c = encrypt_block(block, KEY).hex().upper()
    cipher.append(c)
    print(" ", i + 1, "  ", block.decode(), "  ", c)

print()
print("C1 == C2 :", cipher[0] == cipher[1])
print("C1 == C3 :", cipher[0] == cipher[2])
print()
print("Same plaintext block gives the same ciphertext block in ECB,")
print("so an attacker can see that blocks 1 and 2 are the same message.")
