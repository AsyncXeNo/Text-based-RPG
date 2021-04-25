import string
import random

generated = []

def code_generator(length):
	gen = ''.join(random.choices(string.ascii_uppercase, k=length))
	while gen in generated:
		gen = ''.join(random.choices(string.ascii_uppercase, k=length))
	generated.append(gen)
	return gen
