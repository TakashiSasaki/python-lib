# -*- coding: utf8 -*-
from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.file.ApplicationDirectory import ApplicationDirectory
from com.gmail.takashi316.lib.file.RotatingFile import RotatingFile
import json
from com.gmail.takashi316.lib.aes import Aes

class ApplicationSettings(object):
    
    __slots__ = ["settings", "credentials", "settingsRotatingFile", "credentialsRotatingFile"]
    
    def __init__(self, application_module):
        application_directory = ApplicationDirectory(application_module)
        application_directory_path = application_directory.getApplicationDirectoryPath()
        self.settingsRotatingFile = RotatingFile(application_directory_path, "settings")
        self.credentialsRotatingFile = RotatingFile(application_directory_path, "credentials")
        self.settings = {}
        self.credentials = {}
        #self.load()

    def save(self):
        self.saveSettings()
        self.saveCredentials()
            
    def saveSettings(self):
        self.settingsRotatingFile.rotate()
        settings_file = self.settingsRotatingFile.openLast()
        json.dump(self.settings, settings_file)
        settings_file.close()

    def saveCredentials(self):
        self.credentialsRotatingFile.rotate()
        credentials_json = json.dumps(self.credentials)
        assert isinstance(credentials_json, str)
        aes = Aes()
        aes.setIv()
        aes.setKeyByMacAddress()
        encrypted_credentials = aes.encryptStrToBase64(credentials_json)
        
        d = aes.decryptBase64ToUnicode(encrypted_credentials)
        assert credentials_json == d

        encrypted_json_object = {"iv": aes.getIv(), "encrypted_credentials": encrypted_credentials}
        encrypted_json_str = json.dumps(encrypted_json_object)
        assert isinstance(encrypted_json_str, str)
        assert len(encrypted_json_str) > 0
        credentials_file = self.credentialsRotatingFile.openLast()
        credentials_file.write(encrypted_json_str)
        credentials_file.close()
        
    def load(self):
        self.loadSettings()
        self.loadCredentials()
            
    def loadSettings(self):
        settings_file = self.settingsRotatingFile.openLast()
        try:
            self.settings = json.load(settings_file, "utf8")
        except ValueError:
            self.settings = {}

    def loadCredentials(self):
        credentials_file = self.credentialsRotatingFile.openLast()
        try:
            encrypted_json = json.load(credentials_file, "utf8")
        except ValueError:
            self.credentials = {}
            return
        aes = Aes()
        aes.setIv(encrypted_json["iv"])
        aes.setKeyByMacAddress()
        credentials_json = aes.decryptBase64ToUnicode(encrypted_json["encrypted_credentials"])
        self.credentials = json.loads(credentials_json)
    
    def setSetting(self, key, value):
        assert isinstance(key, unicode)
        self.settings[key] = value
    
    def getSetting(self, key):
        assert isinstance(key, unicode)
        return self.settings[key]
    
    def clearSettings(self):
        self.settings = {}
    
    def setCredential(self, key, value):
        assert isinstance(key, unicode)
        self.credentials[key] = value
    
    def getCredential(self, key):
        assert isinstance(key, unicode)
        return self.credentials[key]    
    
    def clearCredentials(self):
        self.credentials = {}

from unittest import TestCase, main

class _Test(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        from com.gmail.takashi316.lib.file import hello 
        self.applicationSettings = ApplicationSettings(hello)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def testFilePats(self):
        #print (self.applicationSettings.credentialsRotatingFile)
        self.assertRegexpMatches(self.applicationSettings.credentialsRotatingFile.__str__(),
                                 "C:\\\\Users\\\\[^\\\\]+\\\\AppData\\\\Roaming\\\\com\\.gmail\\.takashi316\\.lib\\.file\\.hello\\\\credentials[0-9]+\\.txt")
        #print (self.applicationSettings.settingsRotatingFile)
        self.assertRegexpMatches(self.applicationSettings.settingsRotatingFile.__str__(),
                                 "C:\\\\Users\\\\[^\\\\]+\\\\AppData\\\\Roaming\\\\com\\.gmail\\.takashi316\\.lib\\.file\\.hello\\\\settings[0-9]+\\.txt")

    def testJson(self):
        bb_json = json.dumps({b"バイトストリング": b"バイトストリング"})
        self.assertIsInstance(bb_json, str)
        bu_json = json.dumps({b"バイトストリング": u"ユニコード"})
        self.assertIsInstance(bu_json, str)
        ub_json = json.dumps({u"ユニコード": b"バイトストリング"})
        self.assertIsInstance(ub_json, str)
        uu_json = json.dumps({u"バイトストリング": u"ユニコード"})
        self.assertIsInstance(uu_json, str)

    def testSettings(self):
        self.applicationSettings.setSetting("testkey", "testvalue")
        self.applicationSettings.setSetting("testkey2", "testvalue2")
        self.assertEqual(self.applicationSettings.getSetting("testkey"), "testvalue")
        self.assertEqual(self.applicationSettings.getSetting("testkey2"), "testvalue2")
        self.applicationSettings.saveSettings()
        self.applicationSettings.clearSettings()
        self.applicationSettings.loadSettings()
        self.assertEqual(self.applicationSettings.getSetting("testkey"), "testvalue")
        self.assertEqual(self.applicationSettings.getSetting("testkey2"), "testvalue2")

    def testCredentials(self):
        self.applicationSettings.setCredential("testkey3", "testvalue3")
        self.assertEqual(self.applicationSettings.getCredential("testkey3"), "testvalue3")
        self.applicationSettings.saveCredentials()
        file = self.applicationSettings.credentialsRotatingFile.openLast()
        #for x in file:
        #    print(x)
        self.applicationSettings.clearCredentials()
        self.applicationSettings.loadCredentials()
        self.assertEqual(self.applicationSettings.getCredential("testkey3"), "testvalue3")
        
if __name__ == "__main__":
    main()
    
