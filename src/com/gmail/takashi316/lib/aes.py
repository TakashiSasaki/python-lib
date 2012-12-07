# -*- coding: utf8 -*- 
from __future__ import unicode_literals, print_function
from random import randint
import uuid
import base64
from base64 import b64decode

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
                ba[x] = randint(0, 255)
            self._key = ba
            return
        key = base64.b64decode(key_base64)
        assert len(key) == 16
        self._key = bytearray(key)

    def getKey(self):
        assert isinstance(self._key, str) or isinstance(self._key, bytearray)
        return base64.b64encode(self._key)
    
    def decryptIntListToStr(self, encrypted_int_list):
        assert isinstance(encrypted_int_list, list) or isinstance(encrypted_int_list, bytearray)
        assert self._iv is not None
        assert self._key is not None
        encrypted_string = bytearray(encrypted_int_list)
        decr = self._moo.decrypt(encrypted_string, len(encrypted_string), 2, self._key,
                                 self._moo.aes.keySize["SIZE_128"], self._iv)
        assert isinstance(decr, str)
        split_decrypted_string = decr.split(b"\0")
        assert isinstance(split_decrypted_string, list)
        truncated_decrypted_string = split_decrypted_string[0]
        assert isinstance(truncated_decrypted_string, str)
        return truncated_decrypted_string
        
    def encryptStrToIntList(self, clear_str):
        assert isinstance(clear_str, str)
        assert self._iv is not None
        assert self._key is not None
        mode, orig_len, ciph = self._moo.encrypt(clear_str, self._moo.modeOfOperation["CBC"],
                                                 self._key, self._moo.aes.keySize["SIZE_128"], self._iv)
        assert mode == 2
        assert orig_len == len(clear_str)
        assert isinstance(ciph, list)
        return ciph
    
    def decryptIntListToUnicode(self, encrypted_int_list):
        assert isinstance(encrypted_int_list, list) or isinstance(encrypted_int_list, bytearray)
        decrypted_bytearray = self.decryptIntListToStr(encrypted_int_list)
        assert isinstance(decrypted_bytearray, str)
        split_decrypted_bytearray = decrypted_bytearray.split("\0")
        assert isinstance(split_decrypted_bytearray, list)
        truncated_decrypted_bytearray = split_decrypted_bytearray[0]
        assert isinstance(truncated_decrypted_bytearray, unicode)
        #x = truncated_decrypted_bytearray.decode("utf8")
        #assert isinstance(x, unicode)
        return truncated_decrypted_bytearray
    
    def encryptUnicodeToIntList(self, clear_unicode):
        assert isinstance(clear_unicode, unicode)
        clear_utf8_str = clear_unicode.encode("utf8")
        assert isinstance(clear_utf8_str, str)
        encrypted_int_list = self.encryptStrToIntList(clear_utf8_str)
        return encrypted_int_list
    
    def encryptUnicodeToBase64(self, clear_unicode):
        encrypted_bytearray = bytearray(self.encryptUnicodeToIntList(clear_unicode))
        encrypted_base64 = base64.b64encode(encrypted_bytearray)
        return encrypted_base64
        
    def decryptBase64ToUnicode(self, encrypted_base64):
        encrypted_str = b64decode(encrypted_base64)
        isinstance(encrypted_str, str)
        encrypted_bytearray = bytearray(encrypted_str)
        decrypted_unicode = self.decryptIntListToUnicode(encrypted_bytearray)
        return decrypted_unicode

def _printhex(l):
    from array import array
    aa = array(b'B', l)
    for a in aa:
        print (l.__class__, hex(a)),
    print
    
from unittest import TestCase, main

class _Test(TestCase):
    clearText = "This is a test!"
    
    def setUp(self):
        TestCase.setUp(self)
    
    def tearDown(self):
        TestCase.tearDown(self)
        
    def testSlowAes(self):
        import slowaes
        moo = slowaes.AESModeOfOperation()
        cypherkey = [143, 194, 34, 208, 145, 203, 230, 143, 177, 246, 97, 206, 145, 92, 255, 84]
        iv = [103, 35, 148, 239, 76, 213, 47, 118, 255, 222, 123, 176, 106, 134, 98, 92]
        mode, orig_len, ciph = moo.encrypt(self.clearText, moo.modeOfOperation["CBC"],
                cypherkey, moo.aes.keySize["SIZE_128"], iv)
        self.assertEqual(mode, 2)
        self.assertEqual(orig_len, 15)
        self.assertEqual(len(self.clearText), 15)
        self.assertListEqual(ciph, [159, 182, 104, 205, 136, 106, 78, 200, 24, 108, 64, 74, 16, 10, 199, 145])
        #print ('m=%s, ol=%s (%s), ciph=%s' % (mode, orig_len, len(cleartext), ciph))
        decr = moo.decrypt(ciph, orig_len, mode, cypherkey, moo.aes.keySize["SIZE_128"], iv)
        #print (decr)
        self.assertEqual(self.clearText, decr)
        
    def testHmac(self):
        _SALT = b"diopioahpqu788guahoivanio"
        import hmac
        h = hmac.new(_SALT)
        h.update(hex(uuid._windll_getnode()))
        hex_digest = h.hexdigest()
        self.assertEqual(len(hex_digest), 32)
        self.assertIsInstance(hex_digest, str)
        assert isinstance(hex_digest, str)
        from re import match
        m = match("^[0-9a-f]+$", hex_digest)
        self.assertIsNotNone(m)
        m = match("^[xyz]+$", hex_digest)
        self.assertIsNone(m)

class TestAes(TestCase):
    __slots__ = ["aes"]
    unicodeText = u"abcあいうえお"
    stringText = b"本日は晴天なり"

    def setUp(self):
        TestCase.setUp(self)
        self.aes = Aes()
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def testKey(self):
        self.assertRaises(AttributeError, self.aes.getKey)
        self.aes.setKey()
        key = self.aes.getKey()
        self.assertRegexpMatches(key, "^[0-9a-zA-Z+/]+=*$")
        self.aes.setKey(self.aes.getKey())
        self.assertEqual(key, self.aes.getKey())

    def testIv(self):
        self.assertRaises(AttributeError, self.aes.getIv)
        self.aes.setIv()
        iv = self.aes.getIv()
        self.assertRegexpMatches(iv, "^[0-9a-zA-Z+/]+=*$")
        self.aes.setIv(self.aes.getIv())
        self.assertEqual(iv, self.aes.getIv())
    
    def testUnicode(self):
        self.aes.setKey()
        self.aes.setIv()
        encrypted_int_list = self.aes.encryptUnicodeToIntList(self.unicodeText)
        decrypted_unicode = self.aes.decryptIntListToUnicode(encrypted_int_list)
        self.assertIsInstance(decrypted_unicode, unicode)
        self.assertEqual(self.unicodeText, decrypted_unicode)
        
    def testString(self):
        self.aes.setKey()
        self.aes.setIv()
        encrypted_int_list = self.aes.encryptStrToIntList(self.stringText)
        decrypted_str = self.aes.decryptIntListToStr(encrypted_int_list)
        self.assertEqual(self.stringText, decrypted_str)
    
    def testBase64(self):
        self.aes.setKey()
        self.aes.setIv()
        encrypted_base64 = self.aes.encryptUnicodeToBase64(self.unicodeText)
        assert isinstance(encrypted_base64, str)
        decrypted_unicode = self.aes.decryptBase64ToUnicode(encrypted_base64)
        assert isinstance(decrypted_unicode, unicode)
        self.assertEqual(self.unicodeText, decrypted_unicode)

if __name__ == "__main__":
    main()    
