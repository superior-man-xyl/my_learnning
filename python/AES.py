from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

# 如果text不足十六位的倍数用空格补充
def add_to_16(text):
  if len(text.encode('utf8')) % 16:
    add = 16 - (len(text.encode('utf8')) % 16)
  else:
    add = 0
  text = text + '\0' * add
  return text

# 加密
def encrypt(text,keys):
  key = keys.encode('utf8')
#   16位密钥
  mode = AES.MODE_CBC
  iv = b'qqqqqqqqqqqqqqqq'
  text = add_to_16(text)
  cryptos = AES.new(key, mode, iv)
  cipher_text = cryptos.encrypt(text.encode('utf-8'))
  # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
  return b2a_hex(cipher_text)

# 解密后去掉空格
def decrypt(text,keys):
  key = keys.encode('utf8')
  mode = AES.MODE_CBC
  iv = b'qqqqqqqqqqqqqqqq'
  cryptos = AES.new(key, mode, iv)
  plain_text = cryptos.decrypt(a2b_hex(text))
  return bytes.decode(plain_text).rstrip('\0')

if __name__ == '__main__':
  print('请输入明文：')
  h=input()
  print('请输入16位密钥：')
  keys=input()
  a = encrypt(h,keys)
  b = decrypt(a,keys)
  print('加密', a)
  print('解密', b)