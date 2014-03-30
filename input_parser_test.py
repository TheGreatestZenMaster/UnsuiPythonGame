import unittest

from nose.tools import *
from input_parser import Command, Verb, Object, Parser

parser = Parser()

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
        
def parser_tokenise_test():

    # Basic tokenising 
    assert_equal(parser.tokenise('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
    assert_equal(parser.tokenise('pet cat on bed'), [('verb', 'pet'), ('noun', 'cat'), ('preposition', 'on'), ('noun', 'bed')])

    # Article stripping
    assert_equal(parser.tokenise('go to the hallway'), [('verb', 'go'), ('preposition', 'to'), ('stop', 'the'), ('noun', 'hallway')])
    assert_equal(parser.tokenise('eat a banana'), [('verb', 'eat'), ('noun', 'banana')])

    # Test Caps and Errors
    assert_equal(parser.tokenise('MAP'), [('command', 'map')])
    assert_equal(parser.tokenise('tHis IS CrAZy'), [('error', 'this'), ('error', 'is'), ('error', 'crazy')])