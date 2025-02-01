from rsaHelpers import fast_mod_exp
from typing import Tuple

# Type defs
Key = Tuple[int, int]

def rsa_encrypt(m: int, pub_key: Key) -> int:
    '''
    Description: Encrypts the message with the given public key
    Args: m (positive integer input)
    Returns: c (encrypted cipher)
    '''
    # Formula is c = (m ** e) mod n
    return fast_mod_exp(m, pub_key[1], pub_key[0])