## Pig latin script
import re

# Translate a single word to Pig Latin
def translate(word):
	# Look out for special cases with starting letters
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	cons_clust_duo = ['bl', 'br',  'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 
						'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 
						'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
	cons_clust_trio = ['sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']

	# Actual translation of word to pig latin
	# If upper, then switch capitalized letter
	if word[0].isupper():
		if word[0] in vowels:
			word = word + 'way'
		elif triple_prefix(word) in cons_clust_trio:
			word = word[3].upper() + word[4:] + triple_prefix(word).lower() + "ay"

		elif duo_prefix(word) in cons_clust_duo:
			word = word[2].upper() + word[3:] + duo_prefix(word).lower() + "ay"
		else:
			word = word[1].upper() + word[2:] + word[0].lower() + "ay"
	else:
		if word[0] in vowels:
			word = word + 'way'
		elif triple_prefix(word) in cons_clust_trio:
			word = word[3:] + triple_prefix(word) + "ay"

		elif duo_prefix(word) in cons_clust_duo:
			word = word[2:] + duo_prefix(word) + "ay"
		else:
			word = word[1:] + word[0] + "ay"
	return word
	
def duo_prefix(word):
	if len(word) < 2:
		return "no"
	else:
		prefix = word[0] + word[1]
		return prefix.lower()

def triple_prefix(word):
	if len(word) < 3:
		return "no"
	else:
		prefix = word[0] + word[1] + word[2]
		return prefix.lower()

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

