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
    """Test parser tokenising"""
    """
    # Basic tokenising 
    assert_equal(parser.tokenise('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
    assert_equal(parser.tokenise('pet cat on bed'), [('verb', 'pet'), ('noun', 'cat'), ('preposition', 'on'), ('noun', 'bed')])
    assert_equal(parser.tokenise('go south'), [('verb', 'go'), ('direction', 'south')])

    # Article stripping
    assert_equal(parser.tokenise('go to the hallway'), [('verb', 'go'), ('preposition', 'to'), ('article', 'the'), ('noun', 'hallway')])
    assert_equal(parser.tokenise('eat a banana'), [('verb', 'eat'), ('noun', 'banana')])

    # Test Caps and Errors
    assert_equal(parser.tokenise('MAP'), [('command', 'map')])
    assert_equal(parser.tokenise('tHis IS CrAZy'), [('error', 'this'), ('error', 'is'), ('error', 'crazy')])
    """
def parser_classify_test():
    """Test parser sentence classifying"""
    """
    # Basic classifying (verb, verb+object)

    sentence1 = parser.tokenise('look')
    sentence2 = parser.tokenise('go to Kitchen')

    command1 = parser.classify(sentence1)
    command2 = parser.classify(sentence2)

    assert_equal(command1.verb.name, 'look')
    assert_equal(command1.verb.modifiers, [])
    assert_equal(command1.object, None)

    assert_equal(command2.verb.name, 'go')
    assert_equal(command2.verb.modifiers, [])
    assert_equal(command2.object.name, 'kitchen')

    # Single adjectives
    sentence1 = parser.tokenise('pet black cat')
    sentence2 = parser.tokenise('inspect the big window')

    command1 = parser.classify(sentence1)
    command2 = parser.classify(sentence2)

    assert_equal(command1.verb.name, 'pet')
    assert_equal(command1.verb.modifiers, [])
    assert_equal(command1.object.name, 'cat')
    assert_equal(command1.object.type, 'direct')
    assert_equal(command1.object.adjectival_modifiers, ['black'])

    assert_equal(command2.verb.name, 'inspect')
    assert_equal(command2.verb.modifiers, [])
    assert_equal(command2.object.name, 'window')
    assert_equal(command2.object.type, 'direct')
    assert_equal(command2.object.adjectival_modifiers, ['big'])

    # Two adjectives

    sentence1 = parser.tokenise('look under big sturdy desk')

    command1 = parser.classify(sentence1)

    assert_equal(command1.verb.name, 'look')
    assert_equal(command1.verb.modifiers, [])
    assert_equal(command1.object.name, 'desk')
    assert_equal(command1.object.type, 'prepositional_phrase')
    assert_equal(command1.object.prepositional_modifiers, ['under'])
    assert_equal(command1.object.adjectival_modifiers, ['sturdy', 'big'])

    # Prepositional Phrases (TODO)

    sentence1 = parser.tokenise('look inside fridge')
    command1 = parser.classify(sentence1)

    assert_equal(command1.verb.name, 'look')
    assert_equal(command1.verb.modifiers, [])
    assert_equal(command1.object.name, 'fridge')
    assert_equal(command1.object.type, 'prepositional_phrase')
    assert_equal(command1.object.prepositional_modifiers, ['in'])
    assert_equal(command1.object.adjectival_modifiers, [])
    """
