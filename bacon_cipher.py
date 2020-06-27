#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


LETTERS_ONLY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
          'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab',
          'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa', 'V': 'babab',
          'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

def read_and_split(file):
    with open(file) as file_object:
        content = file_object.read().split()
    return content

def plaintext_to_biliteral(message):
    """plaintext to ciphertext"""
    message = message.strip()
    cipher_text = ''
    for letter in message:
        if letter.upper() in cipher:
            cipher_text += cipher[letter.upper()]
    return cipher_text


def decoy_to_biliteral(decoy_text):
    """remove spaces from decoy, convert it to bacon bilteral"""
    bilteral_string = ''
    decoy_text = list(decoy_text)
    for letter in decoy_text:
        if letter.isupper():
            bilteral_string += 'b'
        elif letter.islower():
            bilteral_string += 'a'
    return bilteral_string


def biliteral_to_plaintext(cipher_text):
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


def map_spaces(decoy_text, cipher_text):
    """so indexes of characters in bileteral and decoy match"""
    decoy_text = list(decoy_text)
    cipher_text = list(cipher_text)
    for index in range(len(decoy_text)):
        if decoy_text[index].upper() not in LETTERS_ONLY:
            cipher_text.insert(index, " ")
    return decoy_text, cipher_text


def biliteral_to_decoy(decoy_text, cipher_text):
    """from a/b binary to letters cases in decoy text"""
    decoy_text, cipher_text = map_spaces(decoy_text, cipher_text)

    for index in range(len(cipher_text)):
        if cipher_text[index] == 'a':
            decoy_text[index] = decoy_text[index].lower()
        elif cipher_text[index] == 'b':
            decoy_text[index] = decoy_text[index].upper()
    decoy_text = ''.join(decoy_text)
    return decoy_text
