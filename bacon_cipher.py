# take a sample text ('Frankenstein'?), change the fonts by one pixel for A, B, and space
# so Frankenstein'll be 5 times longer than the code: slice message x 5
# like PROT.py from Rosalind
# message to all caps
# encrypt: strip spaces first?
# message -> binary -> change fonts
from frankenstein import text

cipher = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
'P': 'abbba','Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba', 'U': 'baabb', 'V': 'babab',
'W': 'babaa', 'X': 'babab', 'Y': 'babba', 'Z': 'babbb'}

message = 'I feel at home in this chaos'
def encrypt_message(message):
    """plaintext to ciphertext"""
    message = message.strip()
    cipher_text = ''
    for letter in message:
        if letter.upper() in cipher:
            cipher_text += cipher[letter.upper()]
    return cipher_text


def decrypt_message(cipher_text):
    """ ciphertext to plaintext """
    cipher_text = cipher_text.strip()
    decryption = ''
    counter = 0
    index1 = 0
    index2 = 5
    while counter < len(cipher_text):
        binary_block = (cipher_text[index1:index2])
        for k, v in cipher.items():
            if binary_block in v:
                decryption += k
        counter += 5
        index1 += 5
        index2 += 5

    return decryption

coded = encrypt_message(message)
shortened = text[:len(message)*5]
print(len(shortened))
print(len(message)*5)

