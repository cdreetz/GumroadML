import tensorflow as tf
import datetime
import sys, os
import numpy as np
sys.path.append(os.pardir)
import core.utils as utils
import core.config as cfg
from model.layers import MaskedEmbeddingsAggregatorLayer, L2NormLayer
from model.candidates import CandidateGeneration
from model.ranking import Ranking
from core.dataset import Dataset
# from core.dataset import Dataset

class DeepRecommendations(object):
	def __init__(self, input_data):
		self.trainset = input_data
		self.candidate_generation = CandidateGeneration().build_nework()
		self.ranking = Ranking().build_nework()
		# self.trainset = Dataset('train')
	
	def fit(self):
		history = self.candidate_generation.fit([tf.keras.preprocessing.sequence.pad_sequences(self.trainset['product_id']),
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['purchase_hist_time'], dtype=float),
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['search_hist'], dtype=float) + 1e-10,
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['example_age'], dtype=float),
			],self.trainset['predict_labels'].values,
			steps_per_epoch=1, epochs=50)

		pred = self.candidate_generation.predict([tf.keras.preprocessing.sequence.pad_sequences(self.trainset['product_id']),
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['purchase_hist_time'], dtype=float),
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['search_hist'], dtype=float) + 1e-10,
			tf.keras.preprocessing.sequence.pad_sequences(self.trainset['example_age'], dtype=float),
			])

		print(pred)
		# candidate generation: 
		# purchases = utils.get_topk(6)
		N = 6
		k = np.sort((-pred).argsort()[:,:N])
		print(k)
		k = k.flatten()
		# k[k>data["purhcases"].max()]=0
		k = np.unique(k)

		print(k)

		Dataset('train').preprocess_ranking(k)