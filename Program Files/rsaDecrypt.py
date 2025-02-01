from rsaHelpers import fast_mod_exp
from typing import Tuple

# Type defs
Key = Tuple[int, int]

def rsa_decrypt(c: int, priv_key: Key) -> int:
    '''
    Description: Decrypts the ciphertext using the private key
    Args: c (encrypted cipher)
    Returns: m (decrypted message, an integer)
    '''
    # Formula is m = (c ** d) mod n
    return fast_mod_exp(c, priv_key[1], priv_key[0])
