import pytest
from src.trie import Trie


def test_complete_case_insensitive():
    t = Trie()
    t.insert('Apple', 5)
    t.insert('application', 3)
    # mixed-case prefix should work
    res = t.complete('App', 5)
    assert res[:2] == ['apple', 'application']


def test_complete_invalid_k_values():
    t = Trie()
    words = [('a', 1), ('aa', 2), ('aaa', 3)]
    for w, f in words:
        t.insert(w, f)
    # string integer should be accepted
    assert t.complete('a', '2') == ['aaa', 'aa'][:2]
    # zero or negative k -> empty
    assert t.complete('a', 0) == []
    assert t.complete('a', -1) == []
    # non-numeric k -> empty
    assert t.complete('a', 'notint') == []


def test_insert_invalid_freq_raises():
    t = Trie()
    with pytest.raises(ValueError):
        t.insert('word', 'notafloat')


def test_non_string_inputs_raise():
    t = Trie()
    # insert with non-string should raise (attribute error when lower() called)
    with pytest.raises(Exception):
        t.insert(123, 1.0)
    with pytest.raises(Exception):
        t.contains(123)
    with pytest.raises(Exception):
        t.remove(123)


def test_complete_with_none_prefix():
    t = Trie()
    t.insert('cat', 2)
    t.insert('dog', 1)
    # None prefix should behave like empty prefix -> return top k
    out = t.complete(None, 2)
    assert set(out) == {'cat', 'dog'}


def test_long_word_insert_remove_contains():
    t = Trie()
    long_word = 'x' * 2000
    t.insert(long_word, 1.0)
    assert t.contains(long_word) is True
    assert t.remove(long_word) is True
    assert t.contains(long_word) is False
