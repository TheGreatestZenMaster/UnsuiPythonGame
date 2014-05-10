# Vocabulary
WORD_TYPES = {
	'noun': ['desk', 'dressers', 'bed', 'window', 'fridge', 'hammer', 'nail'],
	'relative_pronoun': ['that', 'which'],
	'adjective': ['red', 'big', 'small'],
	'preposition': ['into', 'in', 'inside', 'on', 'above' 'under', 'below', 'behind', 'with'],
	'verb': ['go', 'look', 'use', 'grab', 'take', 'talk', 'hit', 'is'],
	'determiner': ['the', 'a', 'an'],
	'conjuction': ['and']
}
WORD_TAGS = {
	'noun':'N',
	'relative_pronoun':'RLP',
	'adjective':'ADJ',
	'preposition':'P',
	'verb':'V',
	'determiner':'DET',
	'conjuction':'CNJ'
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

class Parser(object):
	"""
	Parses natural language input and returns sentence objects that refer to the game world
	
	NB:
		1) Input should be provided in the imperative mood
		2) Subject is always assumed to be the player
		3) First word should be a verb
	"""

	def tokenise(self, sentence):
		"""Tokenises sentence returning a list of the words and their types"""
		sentence = sentence.lower()
		tokens = []
		for word in sentence.split():
			try:
				word_type = WORD_TAGS[VOCABULARY[word]]
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

	def parse(self, tokenlist):
		pass
		#level 1: Parse Determiners
		for token in tokenlist:
			if token[0][0] == 'verb':
				pass
			else:

if __name__ == '__main__':
	parser = Parser()
	test_string = 'hit the nail with the hammer which is red'
	print parser.tokenise(test_string)
	# Break it down into chunks
	# [verb][direct object][adverbial phrase]
	#						^- [preposition][relative clause]