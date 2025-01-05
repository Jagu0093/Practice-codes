# import unittest

# # # # from collections import Counter

# # # # def majority_vote(lst):
# # # #     n = len(lst)
# # # #     element_counts = Counter(lst)
    
# # # #     for element, count in element_counts.items():
# # # #         if count >= n / 2:
# # # #             return element
    
# # # #     return None  # Return None if no majority vote

# # # # # Example usage
# # # # print(majority_vote([1,1,2, 3,3,3]))  # Output: 2
# # # # print(majority_vote([1, 2, 3, 4, 5,5]))  # Output: None

# # # # print(majority_vote(["A", "A", "A", "B", "C", "A"]))

# # # # def censor_string(txt, lst, char):
# # # #     """
# # # #     Censors words in a string based on a list of words.

# # # #     Args:
# # # #         txt: The input string.
# # # #         lst: A list of words to censor.
# # # #         char: The character to replace censored words with.

# # # #     Returns:
# # # #         The censored string.
# # # #     """

# # # #     words = txt.split()  # Split the string into words
# # # #     censored_words = []

# # # #     for word in words:
# # # #         cleaned_word = word.strip('.,!?"\'()[]{}') # Remove punctuation for better matching
# # # #         if cleaned_word.lower() in [w.lower() for w in lst]: # Case-insensitive comparison
# # # #             censored_words.append(char * len(word)) # Replace with char * word length
# # # #         else:
# # # #             censored_words.append(word)

# # # #     return " ".join(censored_words)

# # # def censor_string(txt, lst, char):
# # #     """
# # #     Censors words in a string based on a list of words.

# # #     Args:
# # #         txt: The input string.
# # #         lst: A list of words to censor.
# # #         char: The character to replace censored words with.

# # #     Returns:
# # #         The censored string.
# # #     """

# # #     words = txt.split()  # Split the string into words
# # #     censored_words = []

# # #     for word in words:
# # #         cleaned_word = word.strip('.,!?"\'()[]{}') # Remove punctuation for better matching
# # #         if cleaned_word.lower() in [w.lower() for w in lst]: # Case-insensitive comparison
# # #             censored_words.append(char * len(word)) # Replace with char * word length
# # #         else:
# # #             censored_words.append(word)

# # #     return " ".join(censored_words)

# # # # Example usage:
# # # text = "The quick brown fox jumps over the lazy dog. The dog barks loudly."
# # # censored_words = ["Fox", "dog"]
# # # replacement_char = "*"

# # # censored_text = censor_string(text, censored_words, replacement_char)
# # # print(censored_text)
# # # # Output: The quick brown *** jumps over the lazy ***. The *** barks loudly.

# # # text2 = "He is a big fool and a big idiot."
# # # censored_words2 = ["fool", "idiot", "big"]
# # # replacement_char2 = "#"
# # # censored_text2 = censor_string(text2, censored_words2, replacement_char2)
# # # print(censored_text2)
# # # # Output: He is a ### #### and a ### #####.

# # # text3 = "This is a test. test Test TEST"
# # # censored_words3 = ["test"]
# # # replacement_char3 = "@"
# # # censored_text3 = censor_string(text3, censored_words3, replacement_char3)
# # # print(censored_text3)
# # # # Output: This is a @@@@. @@@@ @@@@ @@@@

# # # text4 = "Hello, world! This is a test."
# # # censored_words4 = ["world", "test"]
# # # replacement_char4 = "$"
# # # censored_text4 = censor_string(text4, censored_words4, replacement_char4)
# # # print(censored_text4)
# # # # Output: Hello, $$$$$! This is a $$$$.


# # def encrypt(word):
# #     r_string = word[::-1]
# #     e_string = []
# #     print(r_string)
# #     for char in r_string:
# #         if char == 'a' or char == 'A':  # Corrected condition
# #             e_string.append(0)
# #         elif char == 'e':
# #             e_string.append(1)
# #         elif char == 'i':
# #             e_string.append(2)
# #         elif char == 'o':
# #             e_string.append(2)
# #         elif char == 'u':
# #             e_string.append(2)
# #         else:
# #             e_string.append(char)
# #     return "".join(map(str,e_string)) + "aca" #Added return statement and converted list to string

# def encode_morse(message):
#     char_to_dots = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#         '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#         '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#         ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#         '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }
#     new_list = []
#     for msg in message:
#         new_list.append(char_to_dots[msg])
#     return " ".join(new_list)

# class TestEncodeMorse(unittest.TestCase):
#     def test_encode_morse(self):
#         self.assertEqual(
#             encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."),
#             ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-"
#         )

# if __name__ == '__main__':
#     unittest.main()

def uncensor(txt, vowels):
	words = txt.split(" ")
	new_word = []
	vowel_index = 0
	for word in words:
		if '*' in word:
			#n = word.count('*')
			for i in word:
				if i == '*':
					new_word.append(vowels[vowel_index])
					vowel_index += 1
				else:
					new_word.append(i)
	return " ".join(new_word)				
print(uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo'))
print(uncensor('abcd', ''))