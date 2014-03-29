
# This module defines a parser which can parse a string into a Command object.
# A command object consists of a verb instance and a object instance.
# For now the objects are always the direct object of the verb.
# The objects can have modifiers applied a.k.a adjectives


# I may move some of the strings around, e.g. moving the 'extra' ones to 'command'
WORD_TYPES = {
    'verb' : ['go', 'use', 'look', 'get', 'check', 'talk', 'take', 'pick', 'listen', 'pet'],
    'direction' : ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right'],
    'noun': ['door', 'key', 'man', 'woman', 'bed', 'window', 'desk', 'hallway', 'kitchen', 'bedroom'],
    'adjective': ['red'],
    'preposition': ['on', 'under', 'from', 'to', 'behind'],
    'stop': ['the', 'in', 'of'],
    'article': ['a', 'an', 'the'],
    'command': ['status', 'help', 'exit'],
    'extra': ['exit', 'save', 'load', 'reset']
}

# This creates a dictionary of (word, type)
VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

class Command(object):
	"""This class is what is returned by Parser.parse()
	and for the moment consists of a verb and a direct object if it exists.
	"""
	def __init__(self, verb):
		self.verb = verb
		self.object = None

class Verb(object):
	def __init__(self, name):
		self.name = name

class Object(object):
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.modifiers = []

class Parser(object):
	"""
	The main method which is needed is the Parser.parse() method.
	"""
	def preprocess(self, sentence):
		"""Returns sentence in lowercase."""
		return sentence.lower()

	def scan(self, sentence):
		"""Tokenises sentence returning a list of the words and their types"""
		tokens = []
		for word in sentence.split():
			try:
				word_type = VOCABULARY[word]
			except KeyError:
				try:
					value = int(word)
				except ValueError:
					tokens.append( ('error', word))
				else:
					tokens.append( ('int', value))
			else:
				tokens.append( (word_type, word))
		return tokens
		
	def clean(self, tokens):
		"""Removes articles from the token list"""
		clean_tokens = tokens
		for token in clean_tokens:
			if token == ('article', 'an') or token == ('article', 'a'):
				clean_tokens.remove(token)
		return clean_tokens

	def classify(self, tokens):
		"""Creates the Command object and applies modifiers to objects."""
		command = False
		if tokens[0][0] == 'verb':
			command = Command(Verb(tokens[0][1]))
			for token in tokens[0:]:
				
				if token[0] == 'noun':
					object = Object(token[1], 'direct')
					command.object = object

					# Check for Adjective:
					index = tokens.index(token) - 1
					while True:
						if tokens[index][0] == 'adjective':
							object.modifiers.append(tokens[index][1])
						elif tokens[index][0] == 'verb':
							break
						index = index - 1
				elif token[0] == 'error':
					command.object = Object(token[1], 'error')
		elif tokens[0][0] == 'command':
			command = Command(Verb(tokens[0][1]))
		return command

	def tokenise(self, sentence):
		"""Returns a list of clean tokens"""
		output = self.preprocess(sentence)
		output = self.scan(output)
		output = self.clean(output)
		return output

	def parse(self, sentence):
		"""Takes a sentence and returns a Command object"""
		return self.classify(self.tokenise(sentence))