from typing import Optional

# Pig Latin Translator
def translate(text: str) -> str:
    """
    Returns the given string translated to Pig Latin.

    Parameters:
    text (str): The string to be translated

    Returns:
    translation (str): The translated text into Pig Latin
    """

    CONSONANT_SUFFIX = 'ay'
    VOWEL_SUFFIX = 'yay'
    vowels = ['a', 'e', 'i', 'o', 'u']

    def firstLetterIndex(word: str, from_end: bool = False) -> Optional[int]:
        """
        Find the index of the first character that is a letter

        If from_end is true, start at the end of the word,
        otherwise, start at the beginning
        """
        characters = list(word)
        if from_end:
            characters = reversed(characters)

        for index, character in enumerate(characters):
            if character.isalpha():
                if from_end:
                    return len(word) - index
                else:
                    return index

        return None

    def firstLetter(word: str) -> Optional[str]:
        index = firstLetterIndex(word)
        if index is None: return None

        return list(word)[index]

    def containsAlpha(word: str) -> bool:
        return firstLetterIndex(word) is not None

    def isVowel(letter: str) -> bool:
        return letter.lower() in vowels

    def isConsonant(letter: str) -> bool:
        return letter.isalpha() and not isVowel(letter)

    def beginsWithVowel(word: str) -> bool:
        letter = firstLetter(word)
        if letter is None: return False

        return isVowel(letter)

    def beginsWithConsonant(word: str) -> bool:
        return containsAlpha(word) and not beginsWithVowel(word)

    def beginsWithConsonantCluster(word: str) -> bool:
        letters = list(word)
        index = firstLetterIndex(word)

        return (isConsonant(letters[index])
         and isConsonant(letters[index + 1])
         and letters[index + 1].lower() != 'y')

    def moveFirstLetterToEnd(word: str) -> str:
        first_index = firstLetterIndex(word)

        # If there are no letters, simply return the word
        if first_index is None: return word

        characters = list(word)
        first_letter = characters.pop(first_index)

        last_index = firstLetterIndex(word="".join(characters), from_end=True)

        characters.insert(last_index, first_letter)

        return "".join(characters)

    # Remove all apostrophes because Pig Latin does not use
    # contractions and then create a list of every word
    words = text.replace("'", '').split(' ')
    translated_words = []

    for word in words:
        translated_word = word
        if beginsWithConsonant(word):
            translated_word = moveFirstLetterToEnd(word)

            if beginsWithConsonantCluster(word):
                translated_word = moveFirstLetterToEnd(translated_word)

            # Add the suffix to the end of the word
            index = firstLetterIndex(word=word, from_end=True)
            characters = list(translated_word)
            characters.insert(index, CONSONANT_SUFFIX)

            translated_word = "".join(characters)
        elif beginsWithVowel(word):
            # Add the suffix to the end of the word
            index = firstLetterIndex(word=word, from_end=True)
            characters = list(word)
            characters.insert(index, VOWEL_SUFFIX)

            translated_word = "".join(characters)

        translation = None
        # transform word case to match original case
        if word.islower():
            translation = translated_word
        elif word.istitle():
            translation = translated_word.title()
        elif word.isupper():
            translation = translated_word.upper()
        else: # mixed case
            translation = translated_word.lower()

        translated_words.append(translation)

    translation = " ".join(translated_words)

    return translation
