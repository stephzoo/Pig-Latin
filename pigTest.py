import unittest
import pigLatin

class TestPigLatinMethods(unittest.TestCase):

    global vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Test for translate_word, individual words translated with regard to capitalization
    def test_translate_word(self):
        self.assertEqual(pigLatin.translate_word('hello'), 'ellohay')
        self.assertEqual(pigLatin.translate_word('eat'), 'eatway')
        self.assertEqual(pigLatin.translate_word('Hello'), 'Ellohay')
        self.assertEqual(pigLatin.translate_word('Apples'), 'Applesway')
        self.assertEqual(pigLatin.translate_word('school'), 'oolschay')
        self.assertEqual(pigLatin.translate_word('quick'), 'ickquay')
        self.assertEqual(pigLatin.translate_word('Schnitzel'), 'Itzelschnay')

    # Test for translate_sentence, sentence gets parsedin as list of words, with punctuation as separate elements of list
    def test_translate_sentence(self):
        self.assertEqual(pigLatin.translate_sentence(['eat', 'world']), 'eatway orldway ')
        self.assertEqual(pigLatin.translate_sentence(['eat', '.', '.', '.', 'world', '?', '!']), 'eatway... orldway?! ')
        self.assertEqual(pigLatin.translate_sentence(['Can', 'I', 'break', 'this', '?']), 'Ancay Iway eakbray isthay? ')
        self.assertEqual(pigLatin.translate_sentence(['I', 'scream', 'for', 'ice', 'cream', '!']), 'Iway eamscray orfay iceway eamcray! ')
        self.assertEqual(pigLatin.translate_sentence(['Quail', 'is', 'scrumptious', '.']), 'Ailquay isway umptiousscray. ')

    # Test for word_w_prefix, returns word without "ay" appended to end
    def test_word_w_prefix(self):
        self.assertEqual(pigLatin.word_w_prefix('happy', vowels), 'appyh')
        self.assertEqual(pigLatin.word_w_prefix('glad', vowels), 'adgl')
        self.assertEqual(pigLatin.word_w_prefix('splendid', vowels), 'endidspl')
        self.assertEqual(pigLatin.word_w_prefix('schnitzel', vowels), 'itzelschn')
        self.assertEqual(pigLatin.word_w_prefix('pterodactyl', vowels), 'erodactylpt')

    def test_main(self):
        pigLatin.main()

if __name__ == '__main__':
    unittest.main()
