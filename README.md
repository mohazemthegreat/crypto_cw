# crypto_cw - Milestone 2: DES-ECB Encryption Tunnel

Mohammad Hazem - 202200696  
Lecturer: Dr. Mostafa Shoukry

Legacy Bank scenario: the mobile app (client) sends a message to the mainframe
(server) over TCP, encrypted with DES in ECB mode using a static 64-bit key.

- Key: `56374804`
- Plaintext: `mohazem8`
- Ciphertext: `805F44B134F82434 47935E57DFEB1A48`
- Output after one round of DES: `L1R1 = 00FFD712 E4FC90DB`

## Files

| File | Description |
|------|-------------|
| `des.py` | DES (FIPS 46-3) and ECB mode |
| `server.py` | Mainframe: receives, decrypts and prints the message |
| `client.py` | Mobile app: encrypts and sends the message |
| `ecb_demo.py` | Two identical blocks and one different block under ECB |
| `verify_des.py` | Checks the hand calculation of DES round 1 |
| `outputs/` | Terminal output of each program |

## How to run

Python 3, no extra libraries.

```
python server.py          (terminal 1)
python client.py          (terminal 2)
python ecb_demo.py
python verify_des.py
```
