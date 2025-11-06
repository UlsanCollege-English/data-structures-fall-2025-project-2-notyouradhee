# tests/student/test_extreme_edge_cases.py
"""Additional edge case tests beyond the basic test suite."""

import pytest
from src.trie import Trie
from pathlib import Path

# Extreme edge cases that test boundary conditions
def test_zero_and_negative_k():
    t = Trie()
    t.insert('word', 1.0)
    assert t.complete('w', 0) == []  # k=0 should return empty
    assert t.complete('w', -1) == []  # negative k should return empty

def test_identical_words_different_cases():
    t = Trie()
    t.insert('WORD', 1.0)  # should be normalized to 'word'
    t.insert('word', 2.0)  # should update frequency
    t.insert('WoRd', 3.0)  # should update frequency
    assert t.complete('w', 1) == ['word']  # only one entry with latest freq
    words, _, _ = t.stats()
    assert words == 1  # should count as single word

def test_extremely_long_word():
    t = Trie()
    long_word = 'a' * 1000  # 1000 character word
    t.insert(long_word, 1.0)
    assert t.contains(long_word)
    assert t.complete('a' * 500, 1) == [long_word]

def test_special_characters():
    t = Trie()
    # Test words with spaces, numbers, symbols
    test_words = ['hello world', 'test123', 'special!@#']
    for w in test_words:
        t.insert(w, 1.0)
    # Should find all despite special chars
    assert len(t.complete('', 10)) == len(test_words)

def test_exact_frequency_ordering():
    t = Trie()
    # Insert in non-sorted order
    words = [('c', 1.0), ('b', 1.0), ('a', 1.0)]
    for w, f in words:
        t.insert(w, f)
    # Should be lexicographically ordered for same frequency
    assert t.complete('', 3) == ['a', 'b', 'c']
    
    # Update frequencies
    t.insert('b', 2.0)  # now highest
    t.insert('a', 1.5)  # middle
    # Should be ordered by frequency first
    assert t.complete('', 3) == ['b', 'a', 'c']

def test_node_cleanup_after_remove():
    t = Trie()
    # Create a chain: root -> h -> e -> l -> l -> o
    t.insert('hello', 1.0)
    initial_nodes = t.stats()[2]  # get initial node count
    
    t.remove('hello')
    final_nodes = t.stats()[2]  # get final node count
    
    # All nodes should be cleaned up since no other words share the path
    assert final_nodes < initial_nodes
    assert not t.contains('hello')
    assert t.complete('he', 1) == []

def test_prefix_is_word():
    t = Trie()
    # 'help' is both a complete word and a prefix of 'helper'
    t.insert('help', 1.0)
    t.insert('helper', 2.0)
    # Both should be found when completing 'help'
    results = t.complete('help', 2)
    assert len(results) == 2
    assert 'helper' in results
    assert 'help' in results

def test_remove_shared_prefix():
    t = Trie()
    # Words sharing prefixes
    t.insert('test', 1.0)
    t.insert('testing', 2.0)
    t.remove('test')
    # 'test' should be gone but 'testing' remains
    assert not t.contains('test')
    assert t.contains('testing')
    assert t.complete('test', 1) == ['testing']

def test_stats_verification():
    t = Trie()
    # Empty trie
    words, height, nodes = t.stats()
    assert words == 0
    assert height == 0
    assert nodes == 1  # just root

    # Single character word
    t.insert('a', 1.0)
    words, height, nodes = t.stats()
    assert words == 1
    assert height == 1
    assert nodes == 2  # root + 'a'

def test_empty_string_operations():
    t = Trie()
    # Empty string operations
    t.insert('', 1.0)  # should handle gracefully
    assert not t.contains('')  # shouldn't store empty string
    assert not t.remove('')  # should return False for empty string