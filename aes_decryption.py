from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

def aes_decrypt(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)

    iv = encrypted_data[:AES.block_size]
    encrypted_text = encrypted_data[AES.block_size:]

    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)

    decrypted = unpad(cipher.decrypt(encrypted_text), AES.block_size)

    return decrypted.decode('utf-8')


# 加密秘钥
key = '0e03759119cf0310c14f9f06a2699413'

#解密
decrypted = aes_decrypt("填写加密字符", key)
print(f"Decrypted: {decrypted}")


#生成随机字符
def Random_String():
    key = os.urandom(16)
    print("密钥（16字节）:", key.hex())

