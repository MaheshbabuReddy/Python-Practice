def translate_to_ancient_language(sentence):
    def reverse_consonants(word):
        vowels = "aeiou"
        consonants = ""
        for letter in word:
            if letter not in vowels:
                consonants += letter
        reversed_consonants = consonants[::-1]
        ancient_word = ""
        i = 0
        for letter in word:
            if letter in vowels:
                ancient_word += letter
            else:
                ancient_word += reversed_consonants[i]
                i += 1
        return ancient_word

    translated_sentence = []
    words = sentence.split()
    for word in words:
        translated_word = reverse_consonants(word)
        translated_sentence.append(translated_word)

    return " ".join(translated_sentence)

# Input sentence in English
english_sentence = "The Earth is in Galaxy"

# Translate to the ancient language
ancient_translation = translate_to_ancient_language(english_sentence)

# Output the translation
print("English: " , english_sentence)
print("Ancient Language: " , ancient_translation)
