# -*- coding: utf8 -*-
from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.file.ApplicationDirectory import ApplicationDirectory
from com.gmail.takashi316.lib.file.RotatingFile import RotatingFile
import json
from com.gmail.takashi316.lib.aes import Aes

class ApplicationSettings(object):
    
    __slots__ = ["settings", "settingsRotatingFile"]
    
    def __init__(self, application_module):
        application_directory = ApplicationDirectory(application_module)
        application_directory_path = application_directory.getApplicationDirectoryPath()
        self.settingsRotatingFile = RotatingFile(application_directory_path, "settings")
        self.settings = {}
        #self.load()

    def save(self):
        self.settingsRotatingFile.rotate()
        settings_file = self.settingsRotatingFile.openLast()
        json.dump(self.settings, settings_file)
        settings_file.close()

    def load(self):
        settings_file = self.settingsRotatingFile.openLast()
        try:
            self.settings = json.load(settings_file, "utf8")
        except ValueError:
            self.settings = {}

    def clear(self):
        self.settings = {}
        self.save()
    
    def setSetting(self, key, value):
        assert isinstance(key, unicode)
        self.settings[key] = value
    
    def get(self, key, default = None):
        assert isinstance(key, unicode)
        return self.settings.get(key, default)
    
    def has_key(self, key):
        return key in self.settings.keys()
    
    def clearSettings(self):
        self.settings = {}
    
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
        self.assert_(self.applicationSettings.has_key("testkey"))
        self.applicationSettings.setSetting("testkey2", "testvalue2")
        self.assertEqual(self.applicationSettings.get("testkey"), "testvalue")
        self.assertEqual(self.applicationSettings.get("testkey2"), "testvalue2")
        self.applicationSettings.save()
        self.applicationSettings.clearSettings()
        self.applicationSettings.load()
        self.assertEqual(self.applicationSettings.get("testkey"), "testvalue")
        self.assertEqual(self.applicationSettings.get("testkey2"), "testvalue2")
        
if __name__ == "__main__":
    main()
    
