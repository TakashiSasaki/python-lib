# -*- coding: utf8 -*- 
from __future__ import unicode_literals, print_function
from random import randint
import uuid
import base64

def _assertUnsignedChars(iterable):
    for x in xrange(len(iterable)):
        i = iterable[x]
        if isinstance(i, int):
            o = i
        elif isinstance(i, str):
            o = ord(i)
        assert isinstance(o, int)
        if not (0 <= o and o <= 255):
            raise ValueError("the value of item in position %s is %s and can not be represented as integer between 0 and 255." % (x, o))

class Aes(object):
    
    __slot__ = ["iv", "_key", "_moo"]
    
    
    def __init__(self):
        import slowaes
        self._moo = slowaes.AESModeOfOperation()
    
    def setIv(self, iv_base64=None):
        if iv_base64 is None:
            ba = bytearray(16)
            for x in xrange(16):
                ba[x] = randint(0, 255)
            self._iv = ba
            return
        iv = base64.b64decode(iv_base64)
        assert len(iv) == 16
        self._iv = bytearray(iv)

    def getIv(self):
        assert isinstance(self._iv, str) or isinstance(self._iv, bytearray)
        return base64.b64encode(self._iv)
    
    def setKey(self, key_base64=None):
        if key_base64 is None:
            ba = bytearray(16)
            for x in range(16):
                ba[x]=randint(0, 255)
            self._key = ba
            return
        key = base64.b64decode(key_base64)
        assert len(key) == 16
        self._key = bytearray(key)

    def getKey(self):
        assert isinstance(self._key, str) or isinstance(self._key, bytearray)
        return base64.b64encode(self._key)
    
    def decrypt(self, encrypted_text):
        _assertUnsignedChars(encrypted_text)
        assert self._iv is not None
        assert self._key is not None
        decr = self._moo.decrypt(encrypted_text, len(encrypted_text), 2, self._key,
                                 self._moo.aes.keySize["SIZE_128"], self._iv)
        return decr
        
    def encrypt(self, clear_text):
        _assertUnsignedChars(clear_text)
        assert self._iv is not None
        assert self._key is not None
        mode, orig_len, ciph = self._moo.encrypt(clear_text, self._moo.modeOfOperation["CBC"],
                                                 self._key, self._moo.aes.keySize["SIZE_128"], self._iv)
        assert mode == 2
        assert orig_len == len(clear_text)
        return ciph

def _printhex(l):
    from array import array
    aa = array(b'B', l)
    for a in aa:
        print (l.__class__, hex(a)),
    print

SALT = b"diopioahpqu788guahoivanio"
if __name__ == "__main__":
    import hmac
    h = hmac.new(SALT)
    h.update(hex(uuid._windll_getnode()))
    print (h.hexdigest())
    #for x in CLIENT_ID_FOR_INSTALLED_APPLICATIONS["installed"].iteritems():
    #    print(x)
    
    print("sample code to use slowaes")
    import slowaes
    moo = slowaes.AESModeOfOperation()
    cleartext = "This is a test!"
    cypherkey = [143, 194, 34, 208, 145, 203, 230, 143, 177, 246, 97, 206, 145, 92, 255, 84]
    iv = [103, 35, 148, 239, 76, 213, 47, 118, 255, 222, 123, 176, 106, 134, 98, 92]
    mode, orig_len, ciph = moo.encrypt(cleartext, moo.modeOfOperation["CBC"],
            cypherkey, moo.aes.keySize["SIZE_128"], iv)
    print ('m=%s, ol=%s (%s), ciph=%s' % (mode, orig_len, len(cleartext), ciph))
    decr = moo.decrypt(ciph, orig_len, mode, cypherkey,
            moo.aes.keySize["SIZE_128"], iv)
    print (decr)

    print("sample code to use Aes class")
    aes = Aes()
    aes.setKey()
    print ("key\t: %s" % aes.getKey(), aes._key.__class__)
    aes.setKey(aes.getKey())
    print ("key\t: %s" % aes.getKey(), aes._key.__class__)
    aes.setIv()
    print ("iv\t: %s" % aes.getIv(), aes._iv.__class__)
    aes.setIv(aes.getIv())
    print ("iv\t: %s" % aes.getIv(), aes._iv.__class__)
    original_text = u"abcあいうえお"
    encrypted_text = aes.encrypt(original_text.encode("utf8"))
    clear_text = aes.decrypt(encrypted_text)
    print (clear_text.decode("utf8"))
