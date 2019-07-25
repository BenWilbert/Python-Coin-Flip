import random
num = input("How many times would you like to flip:")
choices = ['heads','tails']
tails_count = 0
heads_count = 0
choice = random.choice(choices)
while int(num) > 0:
	choice = random.choice(choices)
	num = (int(num) -1)
	choice = random.choice(choices)
	if choice == 'tails':
		tails_count = (tails_count +1)
	else:
		heads_count = (heads_count +1)

print("The amount of times heads was flipped is:", heads_count)
print("The amount of times tails was flipped is:", tails_count)
