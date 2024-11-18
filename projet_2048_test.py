import pytest
from  projet_2048 import *

def test_construction_sep():
    assert construction_sep(1)=="------"
    assert construction_sep(10)==("------"*10)

