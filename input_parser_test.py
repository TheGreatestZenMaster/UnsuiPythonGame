import unittest

from input_parser import Command, Verb, Object, Parser

class basic_class_tests(unittest.TestCase):

    def tokenize_test(self):
        # TODO: use test sentences and ensure that the right token list comes out
        TEST_SENTENCES = [
            "go Bedroom",
            "go",
            'Go',
            'GO',
            "go to Bedroom"
            ]
        TEST_RESULTS   = [
            [('verb','go'),('noun','bedroom')],
            [('verb','go')],
            [('verb','go')],
            [('verb','go')],
            [('verb','go'),('preposition','to'),('noun','bedroom')]
            ]
        
        parser = Parser()
        
        for i in range(len(TEST_SENTENCES)):
            res = parser.tokenise(TEST_SENTENCES[i])
            print res, '=?=', TEST_RESULTS[i]
            self.assertTrue(res == TEST_RESULTS[i])
        