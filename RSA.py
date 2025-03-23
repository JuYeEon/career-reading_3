#RSA 1024비트 개인키와 공개키 생성 -> 단문 메시지를 공개키로 암호화 -> 암호화한 메시지 개인키로 복호화화

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_enc(msg):
    private_key = RSA.generate(1024)
    public_key = private_key.public_key()
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    print(encdata)

    cipher = PKCS1_OAEP.new(private_key)
    decdata = cipher.decrypt(encdata)
    print(decdata)

def main():
    msg = 'I love python'
    rsa_enc(msg.encode('utf-8'))

main()
