import pytest
from binary_search import *

def test_binary_search_pos1():
    test_case1 = BinarySearch()
    assert test_case1.binary_search(nums=[1,2,3,4,5,6,7,8,9,10], target=4) == 3

def test_binary_search_pos2():
    test_case2 = BinarySearch()
    assert test_case2.binary_search(nums=[1,2,3,4,5,6,7,8,9,10], target=10) == 9

def test_binary_search_neg():
    test_case3 = BinarySearch()
    assert test_case3.binary_search(nums=[1,2,3,4,5,6,7,8,9,10], target=13) == -1

def test_binar_search_rec():
    test_case_rec1 = BinarySearch()
    assert test_case_rec1.binary_search_recursive(nums=[1,2,3,4,5,6,7,8,9,10], target=4) == 3

def test_binar_search_rec_neg():
    test_case_rec_neg = BinarySearch()
    assert test_case_rec_neg.binary_search_recursive(nums=[1,2,3,4,5,6,7,8,9,10], target=13) == -1

def test_search():
    test_search = BinarySearch()
    assert test_search.search(nums=[1,2,3,4,5,6,7,8,9,10], target=7) == 6

def test_search_rec():
    test_search_rec = BinarySearch()
    assert test_search_rec.search(nums=[1,2,3,4,5,6,7,8,9,10], target=7, recursive=True) == 6