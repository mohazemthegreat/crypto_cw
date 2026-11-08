# Checks my hand calculation of DES round 1 (Appendix A)
# Mohammad Hazem - 202200696

from des import (IP, E, P, PC1, PC2, to_bits, to_hex, permute, shift_left,
                 xor, s_box, f, encrypt_block, decrypt_block)

PLAINTEXT = b"mohazem8"
KEY = b"56374804"

# values from my worksheet (pages 1-6)
hand = {
    "M":            "0110110101101111011010000110000101111010011001010110110100111000",
    "K":            "0011010100110110001100110011011100110100001110000011000000110100",
    "C0":           "0000000000000000111111111111",
    "D0":           "0000111010011011001000001111",
    "C1":           "0000000000000001111111111110",
    "D1":           "0001110100110110010000011110",
    "K1":           "010100000010110010101100010001010010001011110101",
    "IP(M)":        "0111111110010000011000110110101100000000111111111101011100010010",
    "L0":           "01111111100100000110001101101011",
    "R0":           "00000000111111111101011100010010",
    "E(R0)":        "000000000001011111111111111010101110100010100100",
    "E(R0) xor K1": "010100000011101101010011101011111100101001010001",
    "S-box output": "01101101100001111110101100011100",
    "f":            "10011011011011001111001110110000",
    "R1":           "11100100111111001001000011011011",
    "L1":           "00000000111111111101011100010010",
}

# the same steps done by the program
prog = {}
prog["M"] = to_bits(PLAINTEXT)
prog["K"] = to_bits(KEY)
cd = permute(prog["K"], PC1)
prog["C0"], prog["D0"] = cd[:28], cd[28:]
prog["C1"] = shift_left(prog["C0"], 1)
prog["D1"] = shift_left(prog["D0"], 1)
prog["K1"] = permute(prog["C1"] + prog["D1"], PC2)
prog["IP(M)"] = permute(prog["M"], IP)
prog["L0"], prog["R0"] = prog["IP(M)"][:32], prog["IP(M)"][32:]
prog["E(R0)"] = permute(prog["R0"], E)
prog["E(R0) xor K1"] = xor(prog["E(R0)"], prog["K1"])
prog["S-box output"] = s_box(prog["E(R0) xor K1"])
prog["f"] = permute(prog["S-box output"], P)
prog["R1"] = xor(prog["L0"], prog["f"])
prog["L1"] = prog["R0"]

print("DES round 1 - hand calculation vs program")
print("plaintext:", PLAINTEXT.decode(), "  key:", KEY.decode())
print()
print("stage           hand              program           result")
matches = 0
for name in hand:
    ok = hand[name] == prog[name]
    matches += ok
    print(name.ljust(15), to_hex(hand[name]).ljust(17), to_hex(prog[name]).ljust(17),
          "MATCH" if ok else "WRONG")

print()
print(matches, "of", len(hand), "stages match")
print("Output after round 1: L1R1 =", to_hex(prog["L1"]), to_hex(prog["R1"]))
print("check f(R0, K1) directly :", to_hex(f(prog["R0"], prog["K1"])))

print()
print("Full DES (16 rounds)")
c = encrypt_block(PLAINTEXT, KEY)
print("encrypt mohazem8 ->", c.hex().upper())
print("decrypt back      ->", decrypt_block(c, KEY).decode())

# known test vector from the DES literature
test = encrypt_block(bytes.fromhex("0123456789ABCDEF"), bytes.fromhex("133457799BBCDFF1"))
print("test vector        ->", test.hex().upper(), "(expected 85E813540F0AB405)")
