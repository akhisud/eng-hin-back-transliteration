import random
import string
for word_error in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]:
	filename = 'Bollywood_oversampled.txt'
	f = open(filename,'r',encoding='utf-8')

	chars = 0
	words = 0


	for line in f:
		chars = chars + len(line.split('\t')[0])
		words = words + 1
	av_chars = chars*1.00/words

	char_error = word_error/av_chars
	pi = char_error/3
	pd = char_error/3
	pm = char_error/3

	# print("word error,av chars,char error,pi,pd,pm:",word_error,av_chars,char_error,pi,pd,pm)
	# input("pause")

	f_new = open('Noisy_bollywood.txt','w',encoding='utf-8')


	f.seek(0,0)
	w_wrong=0 
	for line in f:
		word = (line.split('\t')[0])
		orig_word = word 
		hin = (line.split('\t')[1])
		for pos in range(len(word)):
			# print(pos)
			if random.random()<pm:
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
			if random.random()<pi:
				rand_char = random.choice(string.ascii_lowercase)
				# print(word[word.index(char)]," ")
				# print(word)
				word= word[:pos+1] + rand_char + word[pos + 1:]

				# new = word+'\t'+hin
				# f_new.write(new)
		# print("insert:",word)
		for pos in range(len(word)):
			if random.random()<pd:
				if pos == 0:
					word= word[pos + 1:]
				else:
					word= word[:pos] + word[pos + 1:]
		# print("delete:",word)
		if word!= orig_word:
			w_wrong = w_wrong + 1
		new = word+'\t'+hin
		f_new.write(new)
	w_err = w_wrong*1.0/words
	print("Word error set, obtained:",word_error,w_err)



