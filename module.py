import random as r
import os

def batch(batch_command):
    os.system(batch_command)

lower_vowels = ["a", "e", "i", "o", "u", "y"]
upper_vowels = ["A", "E", "I", "O", "U", "Y"]
lower_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
upper_consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]

class Word:
    def __init__(self, times):
        self.times = times
		steps = 0
		list = []
		for i in range(self.times):
			if steps % 2 == 0:
				list.append(r.choice(consonants))
			elif steps % 2 != 0:
				list.append(r.choice(vowels))
			steps += 1
		self.result = "".join(list).capitalize()
    def __repr__(self):
		return self.result
	def __len__(self):
		return len(self.result)
	def get(self, mode = "normal"):
		self.mode = mode
		self.result_reversed = self.result[::-1]
		self.result_lower = self.result_reversed.lower()
		self.result_capitalize = self.result_lower.capitalize()
		if self.mode == "normal":
			return self.result
		elif self.mode == "reversed":
			return self.result_capitalize
		elif self.mode == "lenght":
			return len(self.result)
		elif self.mode == "capitalized":
			return self.result.capitalize()
		elif self.mode == "lowered":
			return self.result.lower()
		elif self.mode == "uppered":
			return self.result.upper()
		else:
			return self.result

class String:
    def __init__(self, text):
        self.text = text
    def each_letter(self):
        for letter in self.text:
            print(letter)
    def get(self, times = 1):
        self.times = times
        for x in range(self.times):
            print(self.text)
    def get_lenght(self):
        print(len(self.text))
    def letter(self, l):
        self.l = l
        try:
            print(self.text[l])
        except NameError:
            print("ERROR: Invalid index!")
        except TypeError:
            print("ERROR: Invalid index!")
        except:
            print("ERROR: Invalid index!")
    def reverse(self):
        print(self.text[::-1])
