
#!/usr/bin/env python3

# ----------------------------------------------------------------------
# test_MultiSet.py
# Dave Reed
# 11/30/2018

# ----------------------------------------------------------------------

import sys
import unittest

sys.path.insert(0, '..')
from MultiSet import *

# ----------------------------------------------------------------------

class TestMultiSet(unittest.TestCase):

    # ------------------------------------------------------------------

    def testEmpty(self):
        s = MultiSet()
        self.assertEqual(len(s), 0, "empty MultiSet does not have length 0")

    # ------------------------------------------------------------------

    def testOneCopy(self):
        s = MultiSet()
        for i in range(1, 11):
            s.insert(i)
        for i in range(1, 11):
            self.assertEqual(s.count(i), 1, f"count of {i} not 1")
        self.assertEqual(len(s), 10, "length with 1-10 is not 10")

    # ------------------------------------------------------------------

    def testZeroCount(self):
        s = MultiSet()
        s.insert(2)
        self.assertEqual(len(s), 1, "length with item 2 is not 1")
        self.assertEqual(s.count(1), 0, "count of 1 is not 0")

    # ------------------------------------------------------------------

    def testMultiCount(self):
        s = MultiSet()
        for i in range(11):
            s.insert(i)
        for i in range(1, 11, 2):
            s.insert(i)
        for i in range(1, 11, 2):
            self.assertEqual(s.count(i), 2, "count of odds is not 2")
        for i in range(0, 11, 2):
            self.assertEqual(s.count(i), 1, "count of evens is not 1")
        self.assertEqual(len(s), 16, "length is not 16")

    # ------------------------------------------------------------------

    def testRemove(self):
        s = MultiSet()
        for i in range(11):
            s.insert(i)
        for i in range(1, 11, 2):
            s.insert(i)
        for i in range(1, 11):
            s.remove(i)
        self.assertEqual(len(s), 6, "length is not 6")
        self.assertEqual(s.count(0), 1, "count of 0 is not 1")
        for i in range(1, 11, 2):
            self.assertEqual(s.count(i), 1, f"count of {i} is not 1")
        for i in range(2, 11, 2):
            self.assertEqual(s.count(i), 0, f"count of {i} is not 0")

    # ------------------------------------------------------------------

    def testRemoveAll(self):
        s = MultiSet()
        for i in range(11):
            s.insert(i)
        for i in range(1, 11, 2):
            s.insert(i)
        for i in range(1, 6):
            s.removeAll(i)
        for i in range(1, 6):
            self.assertEqual(s.count(i), 0, f"count of {i} is not 0 after removeAll of 1-5")
        self.assertEqual(s.count(0), 1, f"count of 0 is not 1 after removeAll for 1-5")
        for i in range(6, 11, 2):
            self.assertEqual(s.count(i), 1, f"count of {i} is not 1")
        for i in range(7, 11, 2):
            self.assertEqual(s.count(i), 2, f"count of {i} is not 2")

    # ------------------------------------------------------------------

    def testRemoveItemNotInSet(self):
        s = MultiSet()
        s.insert(1)
        s.insert(2)
        # this may crash if remove not implemented correctly
        s.remove(3)
        self.assertEqual(s.count(2), 1)
        self.assertEqual(len(s), 2)

    # ------------------------------------------------------------------


# ----------------------------------------------------------------------

def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        # raised by sys.exit(True) when tests failed
        if inst.args[0] is True:
            raise

# ----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
