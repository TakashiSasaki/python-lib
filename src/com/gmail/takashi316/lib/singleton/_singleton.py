from __future__ import unicode_literals, print_function
from com.gmail.takashi316.lib.singleton import *
from com.gmail.takashi316.lib.debug import * 

from unittest import TestCase, main
class _(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testSoftSingleton(self):
        
        class A(object):
            __metaclass__ = SoftSingleton
            _count = 0
            def __init__(self, x):
                self._count += 1
                debug("A.__init__ was called")
                self._x = x
                debug("self._x = %s" % self._x)
        
        self.assertEqual(A._count, 0)
        a1 = A(123) # this line invokes A.__init__
        self.assertEqual(a1._count, 1)
        a2 = A(456) # this line does not invoke A.__init__
        self.assertEqual(a1._count, 1)
        self.assertIs(a1, a2)

    def testHardSingleton(self):
        
        class B(object):
            __metaclass__ = HardSingleton
            def __init__(self, x):
                debug("B.__init__ was called")
                self._x = x
                debug("self._x = %s" % self._x)
        
        b1 = B(123)
        def b2():
            b2 = B(456) 
        self.assertRaises(AssertionError, b2)

if __name__ == "__main__":
    main()
    