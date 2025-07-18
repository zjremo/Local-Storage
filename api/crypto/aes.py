from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


# aes加密
def aes_encrypt(plaindata, hex_key):
    # 声明一个hex_key
    key = bytes.fromhex(hex_key)
    # 初始化一个aes类
    cipher = AES.new(key, AES.MODE_CBC)
    # 填充数据
    padded_data = pad(plaindata.encode("utf-8"), AES.block_size)
    # 执行加密操作
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(bytes(cipher.iv) + encrypted_data)


# aes解密
def aes_decrypt(encrypted_data, hex_key):
    key = bytes.fromhex(hex_key)
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data[AES.block_size :])
    return unpad(decrypted_data, AES.block_size)
