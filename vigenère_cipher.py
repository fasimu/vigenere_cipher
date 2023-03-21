"""
The Vigenère cipher is a method of encrypting alphabetic text
by using a series of interwoven Caesar ciphers,
based on the letters of a keyword.
"""

# decode Vigenère Cipher
def vigenere_decode(encrypt_text,keyword):
    encrypt_text = encrypt_text.upper()
    keyword = keyword.upper()
    
    # generate key from given keyword
    key = list(keyword)
    if len(encrypt_text) == len(keyword):
        return(keyword)
    else:
        for i in range(len(encrypt_text) -
                       len(keyword)):
            key.append(keyword[i % len(keyword)])

    # dechiper the encrypted text
    lst_final = []
    code = list(encrypt_text)
    for i, char in enumerate(code):
        if char.isalpha():
            lst_final.append(chr(((ord(encrypt_text[i]) - ord(key[i % len(key)])) % 26) + ord('A')))
        else:
            lst_final.append(char)
    return (''.join(lst_final))


# encode Vigenère Cipher
def vigenere_encode(encrypt_text,keyword):
    encrypt_text = encrypt_text.upper()
    keyword = keyword.upper()
    
    # generate key from given keyword
    key = list(keyword)
    if len(encrypt_text) == len(keyword):
        return(keyword)
    else:
        for i in range(len(encrypt_text) -
                       len(keyword)):
            key.append(keyword[i % len(keyword)])

    lst_final = []
    code = list(encrypt_text)
    for i,char in enumerate(code):
        if char.isalpha():
            lst_final.append(chr(((ord(encrypt_text[i]) + ord(key[i % len(key)])) % 26) + ord('A')))
        else:
            lst_final.append(char)
    return ''.join(lst_final)


print(vigenere_encode('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS'))
print(vigenere_decode('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS'))
print(vigenere_encode('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR'))
print(vigenere_decode('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR'))

"""
vigenere_encode('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS')
'PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!'

vigenere_decode('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS')
'NOBODY EXPECTS THE SPANISH INQUISITION!'

vigenere_encode('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR')
'OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!'

vigenere_decode('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR')
'OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!' 
"""