import random
import string

filename = './Datasets/sample.txt'
f = open(filename,'r',encoding='utf-8')
f_new = open('./Datasets/noisy_sample.txt','w',encoding='utf-8')
# print(string.ascii_lowercase[:26])
for line in f:
	word = (line.split('\t')[0])
	hin = (line.split('\t')[1])
	for pos in range(len(word)):
		# print(pos)
		if random.random()<0.2:
			rand_char = random.choice(string.ascii_lowercase)
			# print(word[word.index(char)]," ")
			# print(word)
			word= word[:pos] + rand_char + word[pos + 1:]
			# new = word+'\t'+hin
			# f_new.write(new)
			# print(word[word.index(char)]," ")
			# print(word)
	# print("mutate:",word)
	for pos in range(len(word)):	
		if random.random()<0.2:
			rand_char = random.choice(string.ascii_lowercase)
			# print(word[word.index(char)]," ")
			# print(word)
			word= word[:pos+1] + rand_char + word[pos + 1:]

			# new = word+'\t'+hin
			# f_new.write(new)
	# print("insert:",word)
	for pos in range(len(word)):
		if random.random()<0.2:
			if pos == 0:
				word= word[pos + 1:]
			else:
				word= word[:pos] + word[pos + 1:]
	# print("delete:",word)
	new = word+'\t'+hin
	f_new.write(new)
	# input("next")

