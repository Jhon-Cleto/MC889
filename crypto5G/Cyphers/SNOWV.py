from snowv import *
from .utils import *

class SNOWV(object):

    key_size = 32
    iv_size = 16
    
    def _initializer(self, key, iv):
        try:
            return snowv_initializer(key, iv, 0)
        except ValueError as e:
            raise(CMException(e))

    def _keystream(self):
        try:
            return snowv_keystream()
        except ValueError as err:
            raise(CMException(err))

    def test_case(self, key, iv):
        z0 = self._initializer(key, iv)
        z = b''
        for i in range(8):
            z += self._keystream()
        
        return z0, z

    def encrypt(self, key, iv, plaintxt):
        if type(plaintxt) != bytes:
            plaintxt = bytes(plaintxt.encode('ascii'))
        try:
            return snowv_encrypt(key, iv, plaintxt)
        except ValueError as e:
            raise CMException(e)        

    def decrypt(self, key, iv, ciphertxt):
        if type(ciphertxt) != bytes:
            ciphertxt = bytes(ciphertxt.encode('ascii'))
        try:
            return snowv_decrypt(key, iv, ciphertxt)
        except ValueError as e:
            raise CMException(e)    

    def gcm_encrypt(self, key, iv, plaintxt, aad):
        if type(plaintxt) != bytes:
            plaintxt = bytes(plaintxt.encode('ascii'))
        
        if type(aad) != bytes:
            aad = bytes(aad.encode('ascii'))

        try:
            return snowv_gcm_encrypt(key, iv, plaintxt, aad)
        except ValueError as e:
            raise CMException(e)

    def gcm_decrypt(self, key, iv, ciphertxt, aad, mac):
        if type(ciphertxt) != bytes:
            ciphertxt = bytes(ciphertxt.encode('ascii'))
        
        if type(aad) != bytes:
            aad = bytes(aad.encode('ascii'))
        
        try:
            return snowv_gcm_decrypt(key, iv, ciphertxt, aad, mac)
        except ValueError as e:
            raise CMException(e)