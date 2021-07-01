import random as r
import os

def batch(batch_command):
	os.system(batch_command)

male_samogloski = ["a", "e", "i", "o", "u", "y"]
duze_samogloski = ["A", "E", "I", "O", "U", "Y"]
male_spolgloski = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
duze_spolgloski = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "W", "Z"]

class Phrase:
	def __init__(self, times):
		self.times = times
		steps = 0
		list = []
		for i in range(self.times):
			steps += 1
			if self.times == 1:
				list.append(r.choice(duze_spolgloski))
				break
			if self.times == 2:
				list.append(r.choice(duze_spolgloski))
				list.append(r.choice(male_samogloski))
				break
			if steps == 1:
				list.append(r.choice(duze_spolgloski))
				continue
			elif steps % 2 != 0:
				list.append(r.choice(male_spolgloski))
			elif steps % 2 == 0:
				list.append(r.choice(male_samogloski))
			if steps == times - 1 and steps % 2 != 0:
				list.append(r.choice(male_samogloski))
				break
			elif steps == times - 1 and steps % 2 == 0:
				list.append(r.choice(male_spolgloski))
				break
		self.result = "".join(list)
	def get(self, mode = "normal"):
		self.mode = mode
		self.result_reversed = self.result[::-1]
		self.result_lower = self.result_reversed.lower()
		self.result_capitalize = self.result_lower.capitalize()
		if self.mode == "normal":
			print(self.result)
		if self.mode == "reversed":
			print(self.result_capitalize)

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
			print("BŁĄD: Podano nieprawidłowy indeks!")
		except TypeError:
			print("BŁĄD: Podano nieprawidłowy indeks!")
		except:
			print("BŁĄD: Podano nieprawidłowy indeks!")
	def reverse(self):
		print(self.text[::-1])