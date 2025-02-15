"""Tests for the functions in process_childes.py.

Your task is to implement some test cases to increase our confidence in the correctness 
of the functions in process_childes.py.
"""
import os
import unittest

import process_childes as pc


class TestPrepareChildes(unittest.TestCase):
    """Tests for the functions in process_childes.py."""

    def test_process_unidentifiable(self):
        """Test the process_unidentifiable function."""
        self.assertEqual(pc.process_unidentifiable('xxx'), '<unk>')
        self.assertEqual(pc.process_unidentifiable('*CHI xxx yyy'), '*CHI <unk> <unk>')
        # TODO: write your test cases here
        test_cases = {
            "*CHI xxx .": "*CHI <unk> .", # testing if it works with fullstops
            "xxxyyy":"xxxyyy", # testing if it prevents matching with substrings which are reserved strings
            "www.":"<unk>.", # testing if match includes fullstops when not separated by space
        }
        for x in test_cases:
            self.assertEqual(pc.process_unidentifiable(x),test_cases[x])

    def test_process_incomplete(self):
        """Test the process_incomplete function."""
        self.assertEqual(pc.process_incomplete('I been sit(ting) all day'), 'I been sitting all day')
        # TODO: write your test cases here
        test_cases = {
            "I (have) been sitting all day":"I have been sitting all day", # testing stand-alone words
            "I been si(tt)i(n)g all day":"I been sitting all day", # testing words with multiple brackets
        }
        for x in test_cases:
            self.assertEqual(pc.process_incomplete(x),test_cases[x])

    def test_process_omit(self):
        """Test the process_omit function."""
        # TODO: write your test cases here
        # Assumption - removal of these symbols require that the associated space be consumed, which is unique to this function
        test_cases = {
            "I want &=to start.":"I want start.", # post-2024 symbol form
            "I want &=0to build":"I want build", # pre-2024 symbol form
            "I want &=0to":"I want", # removal of space at end
            "&=I want.":"want." # removal of space at start
        }
        for x in test_cases:
            self.assertEqual(pc.process_omit(x),test_cases[x])

    def test_process_paralinguistic(self):
        """Test the process_paralinguistic function."""
        # TODO: write your test cases here
        test_cases = {
            "I want it? [=! whining]":"I want it? ", # testing for punctuation
            "I want <it!> [=!whining]":"I want it! ", # testing for absence of space, presence of <>
            "&=whining .":".", # events without vocalization
            "I <want> [!] it.":"I want  it.", # in-sentence symbol, stressing
            "I want [# 1] <it> [!!]":"I want  it ", # multiple symbols, contrastive stressing
            "I want <all of them> [# 2.2] right now.":"I want all of them  right now." # floating point time
        }
        for x in test_cases:
            self.assertEqual(pc.process_paralinguistic(x),test_cases[x])

    def test_complex(self):
        """Test some complex cases."""
        process_pipeline = lambda x: pc.process_unidentifiable(
            pc.process_omit(
                pc.process_incomplete(
                    pc.process_paralinguistic(x)
                )
            )
        )
        self.assertEqual(process_pipeline('xxx sit(ting) &=jumps www'), '<unk> sitting <unk>')
        # TODO: write your test cases here
        test_cases = {
            "I be xxx <all of that> [!]":"I be <unk> all of that ", # checking order of pipeline
            "   .":"   .", # preservation of number of spaces
            "what is a <solution to www conjecture> [!!]":"what is a solution to <unk> conjecture " # checking order of pipeline
        }
        for x in test_cases:
            self.assertEqual(process_pipeline(x),test_cases[x])