
# This module defines a parser which can parse a string into a Command object.
# A command object consists of a verb instance and a object instance.
# For now the objects are always the direct object of the verb.
# The objects and verbs can have modifiers applied a.k.a adjectives/adverbs


"""
Brainstorm:

Export Vocab to another file

Pronouns: 
subject pronouns not needed since subject is always player
object pronouns: me, you, him, her, it, them
possessive pronouns: not really needed
indefinite pronouns: all, both, each, either
relative pronouns: that, which

Adjectives:
How to implement positive/comparative/superlative adjectives? 

possessive adjectives: my, your, his, her, its, their
^ should be easy to identify, they should appear before the noun they refer to.
^^ But they're not really needed that much to be honest.

Indirect Objects:
Unsure how I'll implement this one

Adverbs:
> I don't think they're really needed.

"""
# I may move some of the strings around, e.g. moving the 'extra' ones to 'command'
WORD_TYPES = {
    'verb' : ['go', 'use', 'look', 'get', 'inspect', 'grab', 'check', 'talk', 'take', 'pick', 'listen', 'pet', 'eat', 'shower'],
    'direction' : ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right'],
    'noun': ['door', 'key', 'man', 'woman', 'bed', 'window', 'desk', 'dressers', 'hallway', 'kitchen', 'bedroom', 'cat', 'banana', 'shower', 'fridge'],
    'pronoun': ['me', 'you', 'him', 'her', 'it', 'them'],
    'adjective': ['red', 'blue', 'green', 'black', 'white', 'big', 'small', 'sturdy'],
    'adverb': [],
    'preposition': ['on', 'under', 'from', 'to', 'behind', 'into', 'in', 'inside'],
    'article': ['a', 'an', 'the'],
    'command': ['status', 'stats', 'location', 'help', 'exit', 'inventory', 'bag', 'map', 'name', 'quests'],
    'extra': ['save', 'load', 'reset']
}

# This creates a dictionary of (word, type)
#VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}
VOCABULARY = {}
for word_type in WORD_TYPES:
	for word in WORD_TYPES[word_type]:
		try:
			VOCABULARY[word].append(word_type)
		except:
			VOCABULARY[word] = [word_type]

class Command(object):
	"""This class is what is returned by Parser.parse()
	and for the moment consists of a verb and a direct object if it exists.
	"""
	def __init__(self, verb):
		self.verb = verb
		self.object = None
		self.raw = None # raw sentence given to yield the command

class Verb(object):
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.modifiers = []

class Object(object):
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.adjectival_modifiers = []
		self.prepositional_modifiers = []

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
				word_type = VOCABULARY[word][0]
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
		if tokens == []:
			return command
		if tokens[0][0] == 'verb':
			command = Command(Verb(tokens[0][1], 'normal'))
			for token in tokens[0:]:
				
				if token[0] == 'noun':
					object = Object(token[1], 'direct')
					command.object = object

					# Check for Adjectives
					index = tokens.index(token) - 1
					while True:
						if tokens[index][0] == 'adjective':
							object.adjectival_modifiers.append(tokens[index][1])
						if tokens[index][0] == 'preposition':
							object.type = 'prepositional_phrase'
							if tokens[index][1] == 'inside':
								# inside and in will be treated the same, as 'in'
								object.prepositional_modifiers.append('in')
							else:
								object.prepositional_modifiers.append(tokens[index][1])

						elif tokens[index][0] == 'verb':
							break
						index = index - 1

				elif token[0] == 'error':
					command.object = Object(token[1], 'error')

		elif tokens[0][0] == 'command' or tokens[0][0] == 'extra':
			command = Command(Verb(tokens[0][1], 'command'))

		return command

	def tokenise(self, sentence):
		"""Returns a list of clean tokens"""
		output = self.preprocess(sentence)
		output = self.scan(output)
		output = self.clean(output)
		return output

	def parse(self, sentence):
		"""Takes a sentence and returns a Command object"""
		cmd = self.classify(self.tokenise(sentence))
		cmd.raw = sentence
		return cmd
		return self.classify(self.tokenise(sentence))


if __name__ == '__main__':
    for key,value in VOCABULARY.items():
    	print key + ": ", value