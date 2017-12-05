from keras.models import Model
from keras.utils import plot_model
from keras.layers import (Input, Embedding, LSTM, Concatenate, Dense, RepeatVector, )
from keras.layers.merge import concatenate,add
from data import Dataset
from keras.callbacks import EarlyStopping, ModelCheckpoint, Callback
import copy


# h_max = 10
# e_max = 12
# hindi_ind_to_char = [0]*26
# emb_dim = 128
# enc_dim = 64
# dec_dim = 128

class keras_model:
	def __init__(self,dataset):
		self.dataset= dataset
		self.h_max = dataset.h_max
		self.e_max = dataset.e_max
		self.hindi_ind_to_char = dataset.hindi_ind_to_char
		self.model = None
		

	def config(self):

		emb_dim = 128
		enc_dim = 64
		dec_dim = 128

		hin_inp = Input(shape=(self.h_max,),dtype='float32')
		print hin_inp
		hin_emb = Embedding(len(self.hindi_ind_to_char),emb_dim)(hin_inp)
		print hin_emb
		enc_forward = LSTM(enc_dim, return_sequences=False)(hin_emb)
		print enc_forward
		enc_backward = LSTM(enc_dim, return_sequences=False)(hin_emb)
		print enc_backward
		encoder = concatenate([enc_forward,enc_backward])
		print encoder
		decoder_inp = concatenate([hin_emb,RepeatVector(self.h_max)(encoder)])
		decoder = LSTM(dec_dim, return_sequences=True)(decoder_inp)
		dense = Dense(self.e_max,activation='softmax')(encoder)
		self.model = Model(input= hin_inp, output= dense)
		plot_model(self.model,'model.png',show_shapes='True')
		

	def compile(self):
		self.model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
		
	def train_model(self):
		train_x =self.dataset.train_x_np
		train_y = self.dataset.train_y_np
		dev_x = self.dataset.dev_x_np
		dev_y = self.dataset.dev_y_np

		hist = self.model.fit(train_x,train_y,validation_data=(dev_x,dev_y),verbose=2, epochs=10, batch_size=1, callbacks=[EarlyStopping(patience=10), ModelCheckpoint('saved_model.hdf5', save_best_only=True, verbose=1)])
		return hist
	def get_model(self):
		return self.model

dataset = Dataset('../Datasets/Bollywood_sample.txt',0.8,0.1,0.1)
# dataset = Dataset('../Datasets/Bollywood_dataset.txt',0.8,0.1,0.1)
test_x,test_y= dataset.get_test_data()
ker_mod = keras_model(dataset)
ker_mod.config()
ker_mod.compile()
hist = ker_mod.train_model()
print hist
model = ker_mod.get_model()
evl=model.evaluate(test_x, test_y, batch_size=1, verbose=2)
print(model.metrics_names[0],":",evl[0])
print(model.metrics_names[1],":",evl[1])








