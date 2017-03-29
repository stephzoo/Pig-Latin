## Pig latin script
import re

# Translate a single word to Pig Latin
def translate(word):
	# Look out for special cases with starting letters
	vowels = ['a', 'e', 'i', 'o', 'u']
	cons_clust_duo = ['bl', 'br',  'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 
						'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 
						'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
	cons_clust_trio = ['sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']

	# Uppercase word flag
	uppercase = word[0].isupper()
	word = word.lower()

	# Translation of word to pig latin
	if word[0] in vowels:
		word = word + 'way'
	elif triple_prefix(word) in cons_clust_trio:
		word = word[3:] + triple_prefix(word) + "ay"
	elif duo_prefix(word) in cons_clust_duo:
		word = word[2:] + duo_prefix(word) + "ay"
	else:
		word = word[1:] + word[0] + "ay"

	# Uppercase first letter if uppercase
	if uppercase:
		word = word[0].upper() + word[1:]
	return word

# Get double consanant cluster
def duo_prefix(word):
	if len(word) < 2:
		return False
	else:
		return word[0:2]

# Get triple consanant cluster
def triple_prefix(word):
	if len(word) < 3:
		return False
	else:
		return word[0:3]

# Main method
def main():
    phrase = str(raw_input("Input Sentence: \n"))
    p = re.compile(r'\w+|[^\w\s]')
    sentence = p.findall(phrase)

    # Check for punctuation
    punctuation = ['.', ',', '!', '?', ';', ':']

    # Translate each word in sentence, put back together
    new_sentence = ""
    for word in sentence:
    	if word in punctuation:
    		new_sentence = new_sentence[:-1] + word + " "
    	else:
    		word = translate(word)
    		new_sentence = new_sentence + word + " "
    print new_sentence

main()

