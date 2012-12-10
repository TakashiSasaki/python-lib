# -*- coding: utf8 -*-
from __future__ import unicode_literals, print_function
import os.path
import re
from time import sleep

def getYYYYMMDDhhmmss(dt=None):
    import datetime
    if dt == None:
        dt = datetime.datetime.now()
    assert isinstance(dt, datetime.datetime)
    return "%04d%02d%02d%02d%02d%02d" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

def removeFileIfExists(p):
    assert isinstance(p, unicode)
    if os.path.exists(p) and os.path.isfile(p):
        os.remove(p)
    
def isIncludedIn(a,b):
    assert isinstance(a, list) and isinstance(b, list)
    for x in a:
        if x not in b: return False
    return True
    
class RotatingFile(object):
    __slots__ = ["directory", "stem", "ext", "regexString", "regularExpression", "sequences", "maxNumberOfFilesToKeep"]

    def __init__(self, directory="." + os.sep, stem="saved-at-", ext="txt", max_number_of_files_to_keep=10):
        if directory[-1] != os.sep:
            raise RuntimeError("directory should be end with %s" % os.sep)
        self.directory = directory
        self.stem = stem
        self.ext = ext
        assert(max_number_of_files_to_keep >= 2)
        self.maxNumberOfFilesToKeep = max_number_of_files_to_keep
        self.regexString = "^" + self.stem + "([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])[.]" + self.ext + "$"
        self.regularExpression = re.compile(self.regexString)
        self.scanDirectory()
        if len(self.sequences) == 0:
            self.rotate()
    
    def scanDirectory(self):
        self.sequences = []
        for x in os.listdir(self.directory):
            m = self.regularExpression.search(x)
            if m is None: continue
            self.sequences.append(int(m.group(1)))
        self.sequences.sort()
        
    def _toBeRemoved(self):
        exceeding = len(self.sequences) - self.maxNumberOfFilesToKeep
        exceeding = max(0, exceeding)
        if exceeding <= 0: return []
        to_be_removed = self.sequences[0:exceeding]
        return to_be_removed
        
    def _toBeKept(self):
        exceeding = len(self.sequences) - self.maxNumberOfFilesToKeep
        exceeding = max(0, exceeding)
        if exceeding <= 0: return self.sequences
        to_be_kept = self.sequences[exceeding:]
        return to_be_kept

    def rotate(self):
        self.scanDirectory()
        
        s = getYYYYMMDDhhmmss()
        assert isinstance(s, unicode)
        YYYYMMDDhhmmss = long(s)
        assert isinstance(YYYYMMDDhhmmss, long)
        if YYYYMMDDhhmmss not in self.sequences:
            self.sequences.append(YYYYMMDDhhmmss)
        
        to_be_removed = self._toBeRemoved()
        assert isinstance(to_be_removed, list)
        to_be_kept = self._toBeKept()
        assert isinstance(to_be_kept, list)
        assert(to_be_kept.__len__() + to_be_removed.__len__() == len(self))
        
        for x in to_be_removed:
            assert isinstance(x, long)
            p = self.getFilePath(x)
            removeFileIfExists(p)
        
        assert isIncludedIn(to_be_kept, self.sequences)
        self.sequences = to_be_kept
        assert len(self.sequences) >= 1        
    
    def touch(self, seconds = 0):
        last = self.sequences[-1]
        last_file_path = self.getFilePath(last)
        if os.path.exists(last_file_path): return
        file = open(last_file_path, "a+")
        file.write("")
        file.close()
        if seconds >0:sleep(seconds)
        stat = os.stat(last_file_path)
        assert stat.st_size == 0
    
    def openLast(self):
        last = self.sequences[-1]
        last_file_path = self.getFilePath(last)
        return open(last_file_path, "a+")
        
    def removeAllFiles(self):
        for x in self.sequences:
            p = self.getFilePath(x)
            if os.path.exists(p) and os.path.isfile(p):
                removeFileIfExists(p)
        self.scanDirectory()
    
    def getFilePath(self, sequence):
        assert isinstance(sequence, long)
        return self.directory + self.stem + "%014d." % sequence + self.ext

    def getCurrentFilePath(self):
        last = self.sequences[-1]
        return self.getFilePath(last)
    
    def save(self, s):
        f = open(self.getCurrentFilePath(), "a+")
    
    def __str__(self):
        s = self.getCurrentFilePath()
        assert isinstance(s, unicode)
        return s
    
    def __unicode__(self):
        unicode(self.__str__())
        
    def __len__(self):
        return len(self.sequences)

from unittest import TestCase, main

class TestRotatingFile(TestCase):
    __slots__ = ["rotatingFile"]
    
    def setUp(self):
        TestCase.setUp(self)
        self.rotatingFile = RotatingFile(".\\", "test", "txt", 3)
    
    def tearDown(self):
        TestCase.tearDown(self)
        self.rotatingFile.removeAllFiles()
        self.rotatingFile.scanDirectory()
        self.assertEqual(len(self.rotatingFile), 0) 
        
    def test(self):
        p = self.rotatingFile.getCurrentFilePath()
        d, f = os.path.split(p)
        self.assertRegexpMatches(f, self.rotatingFile.stem + 
                                 "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][.]" 
                                 + self.rotatingFile.ext)

    def test2(self):
        self.assertGreater(len(self.rotatingFile), 0)
    
    def test3(self):
        self.rotatingFile.touch(1)
        before = len(self.rotatingFile.sequences)
        self.rotatingFile.rotate()
        self.rotatingFile.touch()
        after = len(self.rotatingFile.sequences)
        self.assertEqual(before + 1, after)
    
    def test4(self):
        self.rotatingFile.removeAllFiles()
        
    def test0(self):
        x = getYYYYMMDDhhmmss()
        self.assertRegexpMatches(x, "20[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]")
    
    def testSave(self):
        self.rotatingFile.save("abc")
        
    def testRemove(self):
        self.rotatingFile.removeAllFiles()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 0)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 0)

        self.rotatingFile.rotate()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 1)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 1)
        self.rotatingFile.touch(1)
        
        self.rotatingFile.rotate()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 2)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 2)
        self.rotatingFile.touch(1)

        self.rotatingFile.rotate()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 3)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 3)
        self.rotatingFile.touch(1)

        self.rotatingFile.rotate()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 3)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 3)
        self.rotatingFile.touch(1)
        
        self.rotatingFile.rotate()
        self.assertEqual(self.rotatingFile._toBeKept().__len__(), 3)
        self.assertEqual(self.rotatingFile._toBeRemoved().__len__(), 0)
        self.assertEqual(len(self.rotatingFile), 3)
        self.rotatingFile.touch(1)
    
if __name__ == "__main__":
    main()
