import hashlib
import sys

try:
    arg = sys.argv[1]
except Exception as err:
    print('Digite algo para transformar em sha1')
    exit()


def encode(arg):
    return hashlib.sha1(arg.encode('utf-8')).hexdigest()


print(encode(arg))
