LETTERS_ONLY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
'P': 'abbbb','Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa', 'V': 'babab',
'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

test_message = 'I feel at home in this chaos'
from frankenstein import frankenstein

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

# def remove_non_letters(text):
#     """remove non-letters from text so indexes match biliteral"""
#     just_letters = []
#     for character in text:
#         if character in LETTERS_ONLY:
#             just_letters.append(character)
#     return just_letters


def biliteral_to_decoy(decoy_text, cipher_text):
    """from a/b binary to letters cases in decoy text"""
    decoy_text, cipher_text = map_spaces(decoy_text, cipher_text)

    for index in range(len(cipher_text)):
        if cipher_text[index] == 'a':
            decoy_text[index] =decoy_text[index].lower()
        elif cipher_text[index] == 'b':
            decoy_text[index]=decoy_text[index].upper()
    decoy_text = ''.join(decoy_text)
    return decoy_text

print(plaintext_to_biliteral(test_message))
print(biliteral_to_decoy(frankenstein, 'abaaaaababaabaaaabaaababbaaaaabaabbaabbbabbbaabbaaaabaaabaaaabbabbaabbaabbbabaaabaabaaaabaaabbbaaaaaabbbabaaba'))
print(decoy_to_biliteral('yOu will ReJoiCe to hEar tHaT No disaSteR Has ACCoMPAniED the cOmmeNcemeNT oF An eNTerPRIsE whiCh yOu havE regARDed with SUCh EviL forebodings I arrived here yesterday and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling? This breeze, which has travelled from the regions towards which I am advancing, gives me a foretaste of those icy climes. Inspirited by this wind of promise, my daydreams become more fervent and vivid. I try in vain to be persuaded that the pole is the seat of frost and desolation; it ever presents itself to my imagination as the region of beauty and delight. There, Margaret, the sun is for ever visible, its broad disk just skirting the horizon and diffusing a perpetual splendour. There—for with your leave, my sister, I will put some trust in preceding navigators—there snow and frost are banished; and, sailing over a calm sea, we may be wafted to a land surpassing in wonders and in beauty every region hitherto discovered on the habitable globe. Its productions and features may be without example, as the phenomena of the heavenly bodies undoubtedly are in those undiscovered solitudes. What may not be expected in a country of eternal light? I may there discover the wondrous power which attracts the needle and may regulate a thousand celestial observations that require only this voyage to render their seeming eccentricities consistent for ever. I shall satiate my ardent curiosity with the sight of a part of the world never before visited, and may tread a land never before imprinted by the foot of man. These are my enticements, and they are sufficient to conquer all fear of danger or death and to induce me to commence this laborious voyage with the joy a child feels when he embarks in a little boat, with his holiday mates, on an expedition of discovery up his native river. But supposing all these conjectures to be false, you cannot contest the inestimable benefit which I shall confer on all mankind, to the last generation, by discovering a passage near the pole to those countries, to reach which at present so many months are requisite; or by ascertaining the secret of the magnet, which, if at all possible, can only be effected by an undertaking such as mine.'))
print(biliteral_to_plaintext('abaaaaababaabaaaabaaababbaaaaabaabbaabbbabbbaabbaaaabaaabaaaabbabbaabbaabbbabaaabaabaaaabaaabbbaaaaaabbbabaabaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaaaaaaaaaabaaaaaaaaaaaaaaaaaabaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))


