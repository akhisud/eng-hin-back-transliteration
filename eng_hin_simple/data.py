import codecs
import numpy as np

# def all_data(self):
# 	train_x, train_y=format_data(self.train_data)
# 	self.train_size = len(train_x)
# 	self.train_x_np, self.train_y_np = format_data_to_numpy(train_x,train_y)
# 	dev_x, dev_y=format_data(self.dev_data)
# 	self.dev_size = len(dev_x)
# 	self.dev_x_np, self.dev_y_np = format_data_to_numpy(dev_x,dev_y)
# 	test_x, test_y=format_data(self.test_data)
# 	self.test_x_np, self.test_y_np = format_data_to_numpy(test_x,test_y)

class Dataset:

	def __init__(self, filename, train_split, dev_split, test_split):

		def split(filename,train_split,dev_split,test_split):
			f = codecs.open(filename,'r',encoding='utf-8')	
			# = 0.8
			# = 0.1
			# = 0.1
			data = {}
			for line in f:
				hin = (line.split('\t')[1]).strip()
				eng = (line.split('\t')[0])
				if hin not in data.keys():
					data[hin]=[]
				data[hin].append(eng)

			# for i in data:
			# 	print i, data[i], '\n'
				

			total = len(data.keys())
			print total
			train_keys = data.keys()[:int(total*train_split)]
			print len(train_keys)
			dev_keys = data.keys()[int(total*train_split):int(total*train_split)+int(total*dev_split)]
			print len(dev_keys)
			test_keys = data.keys()[int(total*train_split)+int(total*dev_split):]
			print len(test_keys)

			train_data = {}
			for i in train_keys:
				train_data[i] = data[i]
			dev_data = {}
			for i in dev_keys:
				dev_data[i] = data[i]
			test_data = {}
			for i in test_keys:
				test_data[i] = data[i]
			# print train_data, dev_data, test_data
			f.close()
			return data,train_data,dev_data,test_data

		def map_characters(filename):
			f = codecs.open(filename,'r',encoding='utf-8')
			h_chars = set([])
			e_chars = set([])
			for line in f:
				hin = (line.split('\t')[1]).strip()
				eng = (line.split('\t')[0])
				for i in hin:
					h_chars.add(i)
				for i in eng:
					e_chars.add(i)
		 	hindi_ind_to_char = sorted(list(h_chars))
		 	eng_ind_to_char = sorted(list(e_chars))
		 	hindi_ind_to_char.insert(0,'-1')
		 	eng_ind_to_char.insert(0,'-1')
		 	hindi_char_to_ind = {}
		 	for i in hindi_ind_to_char:
		 		hindi_char_to_ind[i]=hindi_ind_to_char.index(i)
		 	eng_char_to_ind = {}
		 	for i in eng_ind_to_char:
		 		eng_char_to_ind[i]=eng_ind_to_char.index(i)
		 	# print self.hindi_ind_to_char, '\n\n', self.eng_ind_to_char, '\n\n', self.hindi_char_to_ind, '\n\n', self.eng_char_to_ind
		 	f.close()
			return hindi_ind_to_char, eng_ind_to_char, hindi_char_to_ind, eng_char_to_ind

		def get_max_lengths(filename):
			f = codecs.open(filename,'r',encoding='utf-8')
			h_max = 0
			e_max = 0
			for line in f:
				hin = (line.split('\t')[1]).strip()
				eng = (line.split('\t')[0])
				h_max = max(h_max,len(hin))
				e_max = max(e_max,len(eng))
			f.close()
			return h_max, e_max

		def encode_hin_one_hot(hin,h_max,hindi_char_to_ind):
			# for i in hindi_char_to_ind:
			# 	print i, hindi_char_to_ind[i]
			hin_encoded = []
			for c in hin:
				# print c
				char_encode = [0]*len(hindi_char_to_ind)
				char_encode[hindi_char_to_ind[c]] = 1
				hin_encoded.append(char_encode)
			if len(hin)<h_max:
				for _ in range(h_max-len(hin)):
					char_encode = [0]*len(hindi_char_to_ind)      
					char_encode[hindi_char_to_ind['-1']] = 1
					hin_encoded.append(char_encode)
			return hin_encoded	

		def encode_eng_one_hot(eng,e_max,eng_char_to_ind):
			
			eng_encoded = []
			for c in eng:
				char_encode = [0]*len(eng_char_to_ind)
				char_encode[eng_char_to_ind[c]] = 1
				eng_encoded.append(char_encode)
			if len(eng)<e_max:
				for _ in range(e_max-len(eng)):
					char_encode = [0]*len(eng_char_to_ind)
					char_encode[eng_char_to_ind['-1']] = 1
					eng_encoded.append(char_encode)
			return eng_encoded

		def encode_hin(hin,h_max,hindi_char_to_ind):
			# for i in hindi_char_to_ind:
			# 	print i, hindi_char_to_ind[i]
			hin_encoded = []
			for c in hin:
				# print c
				char_encode = hindi_char_to_ind[c]
				hin_encoded.append(char_encode)
			if len(hin)<h_max:
				for _ in range(h_max-len(hin)):
					char_encode = hindi_char_to_ind['-1']
					hin_encoded.append(char_encode)
			return hin_encoded	

		def encode_eng(eng,e_max,eng_char_to_ind):
			
			eng_encoded = []
			for c in eng:
				char_encode = eng_char_to_ind[c]
				eng_encoded.append(char_encode)
			if len(eng)<e_max:
				for _ in range(e_max-len(eng)):
					char_encode = eng_char_to_ind['-1']
					eng_encoded.append(char_encode)
			return eng_encoded	

		def format_data(data_subset,h_max,hindi_char_to_ind,e_max,eng_char_to_ind):
			data_subset_x= []
			data_subset_y= []
			for i in data_subset:
				hin_encoded = encode_hin(i,h_max,hindi_char_to_ind)
				for j in data_subset[i]:
					eng_encoded = encode_eng(j,e_max,eng_char_to_ind)
					# print hin_encoded, eng_encoded
					data_subset_x.append(eng_encoded)
					data_subset_y.append(hin_encoded)

			return data_subset_x, data_subset_y

		def format_to_numpy(data_subset_x, data_subset_y):
			# print data_subset_x
			np_x = np.array(data_subset_x,dtype='float32')
			np_y = np.array(data_subset_y,dtype='float32')
			return np_x, np_y


		self.filename = filename
		self.data,self.train_data,self.dev_data,self.test_data = split(filename, train_split, dev_split, test_split) 
		self.hindi_ind_to_char, self.eng_ind_to_char, self.hindi_char_to_ind, self.eng_char_to_ind = map_characters(filename)
		self.h_max, self.e_max = get_max_lengths(filename)
		self.train_data_x, self.train_data_y = format_data(self.train_data,self.h_max, self.hindi_char_to_ind,self.e_max,self.eng_char_to_ind)
		self.dev_data_x, self.dev_data_y = format_data(self.dev_data,self.h_max, self.hindi_char_to_ind,self.e_max,self.eng_char_to_ind)
		self.test_data_x, self.test_data_y = format_data(self.test_data,self.h_max, self.hindi_char_to_ind,self.e_max,self.eng_char_to_ind)
		self.train_x_np, self.train_y_np = format_to_numpy(self.train_data_x, self.train_data_y)
		self.dev_x_np, self.dev_y_np = format_to_numpy(self.dev_data_x, self.dev_data_y)
		self.test_x_np, self.test_y_np = format_to_numpy(self.test_data_x, self.test_data_y)


	def get_test_data(self):
		return self.test_x_np, self.test_y_np

	# def get_train_size(self):
	# 	return self.train_size
		
	# def get_dev_size(self):
	# 	return self.dev_size







