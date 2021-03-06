from snowv import *
from Cyphers.AES import AES_3GPP as AES
from Cyphers.SNOW3G import SNOW3G
from Cyphers.ZUC import ZUC
from Cyphers.SNOWV import SNOWV

"""
Alguns testes do cifradores do 5G
Testar com o pytest: pytest tests/test_cyphers.py
"""

def test_aes_EEA2_set_1():
    aes3gpp = AES()
    key     = b'\xd3\xc5\xd5\x922\x7f\xb1\x1c@5\xc6h\n\xf8\xc6\xd1'
    count   = 0x398a59b4 
    bearer  = 0x15
    direct  = 1
    data    = b'\x98\x1b\xa6\x82L\x1b\xfb\x1a\xb4\x85G )\xb7\x1d\x80\x8c\xe3>,\xc3\xc0\xb5\xfc\x1f=\xe8\xa6\xdcf\xb1\xf0'
    bitlen  = 253
    output  = b'\xe9\xfe\xd8\xa6=\x15S\x04\xd7\x1d\xf2\x0b\xf3\xe8"\x14\xb2\x0e\xd7\xda\xd2\xf23\xdc<"\xd7\xbd\xee\xed\x8ex'
    assert aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def test_snow3g_EEA1_set_1():
    snow    = SNOW3G()
    key     = b'\xef\xa8\xb2"\x9er\x0c*|6\xeaU\xe9`V\x95'
    count   = 3800813435
    bearer  = 24
    direct  = 0
    data    = b"\x10\x11\x121\xe0`%:C\xfd?W\xe3v\x07\xab('\xb5\x99\xb6\xb1\xbb\xda7\xa8\xab\xccZ\x8cU\r\x1b\xfb/IF$\xfbP6\x7f\xa3l\xe3\xbch\xf1\x1c\xf9;\x15\x107k\x02\x13\x0f\x81*\x9f\xa1i\xd8"
    bitlen  = 510
    output  = b'\xe0\xda\x15\xca\x8e%T\xf5\xe5l\x94h\xdcl|\x12\x9cV\x8a\xa5\x03#\x17\xe0N\x07)dl\xab\xef\xa6\x89\x86LA\x0f$\xf9\x19\xe6\x1e=\xfd\xfa\xd7~V\r\xb0\xa9\xcd6\xc3J\xe4\x18\x14\x90\xb2\x9f_\xa2\xfc'
    assert snow.EEA1(key, count, bearer, direct, data, bitlen) == output

def test_zuc_EEA3_set_1():
    zuc     = ZUC()
    key     = b'\xd4U*\x8f\xd6\xe6\x1c\xc8\x1a \t\x14\x1a)\xc1\x0b'
    count   = 0x76452ec1
    bearer  = 2
    direct  = 1
    data    = b'8\xf0\x7fK\xe2\xd8\xffX\x05\xf5\x13")\xbd\xe9;\xbb\xdc\xaf8+\xf1\xee\x97/\xbf\x99w\xba\xda\x89E\x84z*l\x9a\xd3JfuT\xe0M\x1f\x7f\xa2\xc32A\xbd\x8f\x01\xba"\r<\xa4\xecA\xe0tY_T\xae+EO\xd9qC C`\x19e\xcc\xa8\\$\x17\xedl\xbe\xc3\xba\xda\x84\xfc\x8aW\x9a\xeax7\xb0\'\x11w$*d\xdc\n\x9d\xe7\x1a\x8e\xde\xe8l\xa3\xd4}\x03=k\xf59\x80N\xca\x86\xc5\x84\xa9\x05-\xe4j\xd3\xfc\xedeT;\xd9\x02\x077+\'\xaf\xb7\x924\xf5\xffC\xea\x87\x08 \xe2\xc2\xb7\x8a\x8a\xaea\xcc\xe5*\x05\x15\xe3H\xd1\x96fJ4V\xb1\x82\xa0|@nJ y\x12q\xcf\xed\xa1e\xd55\xec^\xa2\xd4\xdf@\x00\x00\x00'
    bitlen  = 1570
    output  = b'\x83\x83\xb0"\x9f\xcc\x0b\x9d"\x95\xecA\xc9w\xe9\xc2\xbbr\xe2 7\x81A\xf9\xc81\x8f:\'\r\xfb\xcd\xeed\x11\xc2\xb3\x04O\x17m\xc6\xe0\x0f\x89`\xf9z\xfa\xcd\x13\x1a\xd6\xa3\xb4\x9b\x16\xb7\xba\xbc\xf2\xa5\t\xeb\xb1ju\xdc\xab\x14\xff\']\xbe\xee\xa1\xa2\xb1U\xf9\xd5,&E-\x01\x87\xc3\x10\xa4\xeeU\xbe\xaax\xab@$a[\xa9\xf5\xd5\xad\xc7r\x8fsV\x06q\xf0\x13\xe5\xe5P\x08]2\x91\xdf}_\xec\xed\xde\xd5Yd\x1bl/XR3\xbcq\xe9`+\xd20XU\xbb\xd2_\xfa\x7f\x17\xec\xbc\x04-\xaa\xe3\x8c\x1fW\xad\x8e\x8e\xbd74oq\xbe\xfd\xbbt2\xe0\xe0\xbb,\xfc\t\xbc\xd9ep\xcb\x0c\x0c9\xdf^))N\x82p:c\x7f\x80'
    assert zuc.EEA3(key, count, bearer, direct, data, bitlen) == output

def test_snowv_GCM_set_1():
    snowv = SNOWV()
    key = bytes.fromhex('505152535455565758595a5b5c5d5e5f0a1a2a3a4a5a6a7a8a9aaabacadaeafa')
    iv = bytes.fromhex('0123456789abcdeffedcba9876543210')
    aad = bytes.fromhex('30313233343536373839616263646566')
    plaintxt = b''
    ciphertxt = b''
    mac = bytes.fromhex('250ec8d77a022c087adf08b65adcbb1a')

    enc, mac1 = snowv.gcm_encrypt(key, iv, plaintxt, aad)
    assert enc == ciphertxt and mac1 == mac
