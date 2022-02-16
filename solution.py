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

    def first_letter_index(word: str, from_end: bool = False) -> Optional[int]:
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

    def first_letter(word: str) -> Optional[str]:
        index = first_letter_index(word)
        if index is None: return None

        return list(word)[index]

    def contains_alpha(word: str) -> bool:
        return first_letter_index(word) is not None

    def is_vowel(letter: str) -> bool:
        return letter.lower() in vowels

    def is_consonant(letter: str) -> bool:
        return letter.isalpha() and not is_vowel(letter)

    def begins_with_vowel(word: str) -> bool:
        letter = first_letter(word)
        if letter is None: return False

        return is_vowel(letter)

    def begins_with_consonant(word: str) -> bool:
        return contains_alpha(word) and not begins_with_vowel(word)

    def begins_with_consonant_cluster(word: str) -> bool:
        letters = list(word)
        index = first_letter_index(word)

        return (is_consonant(letters[index])
         and is_consonant(letters[index + 1])
         and letters[index + 1].lower() != 'y')

    def move_first_letter_to_end(word: str) -> str:
        first_index = first_letter_index(word)

        # If there are no letters, simply return the word
        if first_index is None: return word

        characters = list(word)
        first_letter = characters.pop(first_index)

        last_index = first_letter_index(word="".join(characters), from_end=True)

        characters.insert(last_index, first_letter)

        return "".join(characters)

    # Remove all apostrophes because Pig Latin does not use
    # contractions and then create a list of every word
    words = text.replace("'", '').split(' ')
    translated_words = []

    for word in words:
        translated_word = word
        if begins_with_consonant(word):
            translated_word = move_first_letter_to_end(word)

            if begins_with_consonant_cluster(word):
                translated_word = move_first_letter_to_end(translated_word)

            # Add the suffix to the end of the word
            index = first_letter_index(word=word, from_end=True)
            characters = list(translated_word)
            characters.insert(index, CONSONANT_SUFFIX)

            translated_word = "".join(characters)
        elif begins_with_vowel(word):
            # Add the suffix to the end of the word
            index = first_letter_index(word=word, from_end=True)
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
