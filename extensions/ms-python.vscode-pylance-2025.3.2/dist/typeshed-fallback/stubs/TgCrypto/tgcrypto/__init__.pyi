from typing_extensions import Buffer

def ige256_encrypt(data: Buffer, key: Buffer, iv: Buffer, /) -> bytes: ...
def ige256_decrypt(data: Buffer, key: Buffer, iv: Buffer, /) -> bytes: ...
def ctr256_encrypt(data: Buffer, key: Buffer, iv: Buffer, state: Buffer, /) -> bytes: ...
def ctr256_decrypt(data: Buffer, key: Buffer, iv: Buffer, state: Buffer, /) -> bytes: ...
def cbc256_encrypt(data: Buffer, key: Buffer, iv: Buffer, /) -> bytes: ...
def cbc256_decrypt(data: Buffer, key: Buffer, iv: Buffer, /) -> bytes: ...
