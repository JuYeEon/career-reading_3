def makeCodebook():
    decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', 'g':'m', '*':'n', '%':'o', '=':'p',\
               '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '} #복호화 할 때 사용할 딕셔너리
    
    encbook = {} #암호화 할 때 사용할 딕셔너리
    #encbook에 decbook의 key를 value로 value를 key로 바꿔 저장하는 반복문
    for k in decbook: 
        val = decbook[k]
        encbook[val] = k

    return encbook, decbook

#암호화
def encrypt(msg, encbook): #plaintext를 msg로 받음
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c]) 

    return msg

#복호화
def decrypt(msg, decbook): #plaintext를 msg로 받음
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])

    return msg

if __name__ == '__main__':
    plaintext = 'python password and code'

    encbook, decbook = makeCodebook()
    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print(deciphertext)
