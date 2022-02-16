import unittest
from translate import translate

class TestTranslateWord(unittest.TestCase):
    """
    Tests the translator against single words -- the simplest test case
    """
    # Rule 1 - Words that begin with a consonant

    # Place first letter at end of the word and add the suffix -ay.
    # Preserve the letter casing of the word so that it matches
    # the original word. For mixed case, convert to lowercase and
    # handle according to lowercase rule.

    # Examples:
    # Title case: Hello -> Ellohay, Denver -> Enverday
    # Lowercase: cat -> atcay, banana -> ananabay, my -> ymay
    # Uppercase: STOP -> TOPSAY, NO -> ONAY
    # Mixed case: hEaRt -> earthay, sOrRy -> orrysay

    def test_consonant_rule_titlecase(self):
        translation = translate("Hello")
        self.assertEqual(translation, 'Ellohay')

    def test_consonant_rule_lowercase(self):
        translation = translate("sorry")
        self.assertEqual(translation, 'orrysay')

    def test_consonant_rule_uppercase(self):
        translation = translate("GASP")
        self.assertEqual(translation, 'ASPGAY')

    def test_consonant_rule_mixedcase(self):
        translation = translate("PiZza")
        self.assertEqual(translation, 'izzapay')

    # Rule 2 - Words that begin with a consonant cluster
    #
    # A consonant cluster is a word that begins with a pair (2) consonants
    # Should follow the consonant rule, except the first two letters should
    # placed at the end instead of only the first letter.
    #
    # Examples:
    # Plant -> Antplay, What -> Atwhay
    # clean -> eanclay, special -> ecialspay

    def test_consonant_cluster(self):
        translation = translate('Grenade')
        self.assertEqual(translation, 'Enadegray')

    # Rule 3 - Words that begin with a vowel
    #
    # Words that begin with a vowel should simply have the
    # suffix -yay added to the end.
    #
    # Examples:
    # Am -> Amyay, I -> Iyay, our -> ouryay
    # is -> isyay, apple -> appleyay, outstanding -> outstandingyay

    def test_vowel_rule(self):
        translation = translate('ostritch')
        self.assertEqual(translation, 'ostritchyay')

    def test_single_vowel(self):
        translation = translate('I')
        self.assertEqual(translation, 'Iyay')

    # Rule 4 - Words that begin with a consonant and
    # have 'y' as the second letter, should not be treated
    # as a consonant cluster, but should use the normal consonant rule
    #
    # Examples:
    # Typed -> Ypedtay, byword -> ywordbay, cyanide -> yanidecay
    # Cycle -> Yclecay, cylinder, ylindercay

    def test_special_y_rule(self):
        translation = translate('dyslexic')
        self.assertEqual(translation, 'yslexicday')

    # Rule 5 - No apostrophes
    # Pig Latin does not have words with contractions, therefore
    # all apostrophes should be eliminated when translating
    #
    # Examples:
    # Don't -> Ontday, can't -> antcay, wasn't -> asntway
    # Shouldn't -> Ouldntshay

    def test_no_apostrophe_rule(self):
        translation = translate('shouldn\'t')
        self.assertEqual(translation, 'ouldntshay')


    # Rule 6 - Words that have punctuation should keep the punctuation
    # in the proper place after translating.
    # Characters that are not alphabetical should not be changed.
    #
    # Examples:
    # Wow! -> Owway!
    # "So," -> "Osay,"
    # Who? -> Owhay?
    # -- -> --
    # 5 -> 5
    # & -> &

    def test_period_at_end_of_word(self):
        translation = translate('Alright.')
        self.assertEqual(translation, 'Alrightyay.')

    def test_questionmark_at_end_of_word(self):
        translation = translate('What?')
        self.assertEqual(translation, 'Atwhay?')


    def test_multiple_questionmarks_at_end_of_word(self):
        translation = translate('How????')
        self.assertEqual(translation, 'Owhay????')

    def test_exclamation_at_end_of_word(self):
        translation = translate('Wonderful!')
        self.assertEqual(translation, 'Onderfulway!')

    def test_double_quoted_word_with_comma(self):
        translation = translate('"Well,"')
        self.assertEqual(translation, '"Ellway,"')

    def test_number_characters(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for number in numbers:
            translation = translate(number)
            self.assertEqual(translation, number)

    def test_non_alpha_characters(self):
        characters = ['-', '=', '_', '+', '/', '\\', '[', ']', '{', '}', '@',
        '#', '$', '%', '^', '*', '(', ')', '<', '>', '.', ',', ';', ':', '|',
        '~', '`', '¡', '™', '£', '¢', '¢', '∞', '§', '¶', '•', '≠', '∑', '®',
        '†', '¥', '¨', '“', '‘', '∂', '©', '˙', '∆', '˚', '¬', '…', '≈', '√',
        '∫','≤', '≥', '÷', '¿']

        for char in characters:
            translation = translate(char)
            self.assertEqual(translation, char)

if __name__ == '__main__':
    unittest.main()
