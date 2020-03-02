import hashlib
import sys

try:
    password = sys.argv[1]
except Exception as err:
    print(f'Digite o password para transformar em sha1')
    exit()


def encode(pwd):
    return hashlib.sha1(pwd.encode('utf-8')).hexdigest()


print(encode(password))