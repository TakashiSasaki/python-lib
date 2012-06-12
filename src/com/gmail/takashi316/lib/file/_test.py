from unittest import TestCase, main
from com.gmail.takashi316.lib.file import HomeDirectory
from com.gmail.takashi316.lib.string import isUnicode

class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
    def tearDown(self):
        TestCase.tearDown(self)
    def test(self):
        home_directory = HomeDirectory()
        assert isUnicode(home_directory())
        assert isUnicode(home_directory.get())

if __name__ == "__main__":
    main()
