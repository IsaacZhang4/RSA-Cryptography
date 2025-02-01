from rsaEncrypt import rsa_encrypt
from rsaDecrypt import rsa_decrypt
import random
import rsaHelpers

if __name__ == '__main__':
    # Sample implementation
    n = 512
    p = rsaHelpers.generate_prime(n)
    q = rsaHelpers.generate_prime(n)
    publicKey, privateKey = rsaHelpers.generate_keypair(p, q)
    message = random.getrandbits(n)
    ciphertext = rsa_encrypt(message, publicKey)
    decrypted = rsa_decrypt(ciphertext, privateKey)

    print(f"Original: {message}\n"
          f"Ciphertext: {ciphertext}\n"
          f"Decrypted: {decrypted}")
