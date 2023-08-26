import numpy as np


class VectorFunctions:
	def __init__(self, embedding_instance):
		self.list_cos_sim = []
		self._embedding_class = embedding_instance
		self._text_in = None
		self._embedding_in = None

	# Magnitude of a vector
	@staticmethod
	def vec_mag(vector_in):
		return np.linalg.norm(vector_in)

	# Dot product of 2 vectors
	@staticmethod
	def vec_dot(v1, v2):	
		return np.dot(v1, v2)

	# Cosine similarity of 2 vectors
	@staticmethod
	def cos_sim(v1, v2):
		numerator = VectorFunctions.vec_dot(v1, v2)
		denominator = VectorFunctions.vec_mag(v1) * VectorFunctions.vec_mag(v2)

		return numerator / denominator

	# Checks a string against a list of strings and vectors and returns the best ones
	def find_best_match(self, text_in, text_list, n_returns):
		self._text_in = text_in
		self._embedding_in = self._embedding_class.return_embedding(self._text_in)

		for item in text_list:
			self.list_cos_sim.append(self.cos_sim(self._embedding_in, item["embedding"]))

		max_index = np.argmax(self.list_cos_sim)
		sorted_index = np.argsort(self.list_cos_sim)[::-1]

		output_list = []
		for index_sorted in sorted_index[:n_returns]:
			output_list.append([text_list[index_sorted]["text_in"], self.list_cos_sim[index_sorted]])

		return output_list
