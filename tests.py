import pytest
import myfile as myfile

def testAdd():
    assert myfile.add(1,2) is 3

def testSubtract():
    assert myfile.subtract(2,1) is 1