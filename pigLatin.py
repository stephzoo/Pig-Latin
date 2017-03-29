## Pig latin script
import re

# Translate a single word to Pig Latin
def translate_word(word):
	# Vowel database
	vowels = ['a', 'e', 'i', 'o', 'u']

	# Uppercase word flag
	uppercase = word[0].isupper()
	word = word.lower()

	# Translation of word to pig latin
	if word[0] in vowels:
		word = word + 'way'
	else:
		word = word_w_prefix(word, vowels) + 'ay'

	# Uppercase first letter if uppercase
	if uppercase:
		word = word[0].upper() + word[1:]
	return word

# Translate multiple word phrase and catch punctuation
def translate_sentence(phrase):
	# Punctuation database
    punctuation = ['.', ',', '!', '?', ';', ':']
    final_phrase = ""

    # Translate sentence, word by word, with regard to punctuation
    for word in phrase:
    	if word in punctuation:
    		final_phrase = final_phrase[:-1] + word + " "
    	else:
    		word = translate_word(word)
    		final_phrase = final_phrase + word + " "
    return final_phrase

# Know word starts with consonant, return prefix
def word_w_prefix(word, vowels):

	for i, c in enumerate(word):
		# Base case
		if word[i] in vowels:
			return word
		# Special case for "qu"
		elif word[i] == 'q':
			if word[i+1] == 'u':
				return word[i+2:] + word[i:i+2]
		# If word has consonants, append to consanant to end and use recursion
		else:
			word = word[i+1:] + c
			return word_w_prefix(word, vowels)

# Main method
def main():
	# Prompt for input
    phrase = str(raw_input("Input Sentence: \n"))
    p = re.compile(r'\w+|[^\w\s]')
    sentence = p.findall(phrase)

    print translate_sentence(sentence)


