#아핀 암호 

ENC = 0
DEC = 1

def makeDisk(k1, k2):
    enc_disk = {} #{평문문자:암호문문자}
    dec_disk = {} #{암호문문자:평문문자}

    for i in range(26):
        enc_i = (k1 * i + k2) % 26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i+65)

    return enc_disk, dec_disk

def caesar(msg, key1, key2, mode):
    ret = ''

    msg = msg.upper() #모든 문자를 대문자로 변경
    enc_disk, dec_disk = makeDisk(key1, key2)

    if enc_disk is None:
        return ret
    #암호화
    if mode is ENC:
        disk = enc_disk
    #복호화
    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c
    
    return ret

def main():
    k1, k2 = map(int, input().split())
    plaintext = 'abcdefghijklmnopqrstuvwxyz'

    print('Original: \t%s' %plaintext.upper())

    ciphertext = caesar(plaintext, k1, k2, ENC)
    print('Caesar Cipher: \t%s' %ciphertext)

    deciphertext = caesar(ciphertext, k1, k2, DEC)
    print('Deciphered: \t%s' %deciphertext)

if __name__ == '__main__':
    main()
