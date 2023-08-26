from .embedding_funcs import EmbeddingClass
from .vector_funcs import VectorFunctions
from .database_funcs import JsonDatabase


class ChadEmbeddingFunc:
	def __init__(self):
		self.vec_db = JsonDatabase()
		self.embd_class = EmbeddingClass(self.vec_db)
		self.vec_system = VectorFunctions(self.embd_class)

	# Interface function to add an string and convert it into an embedding
	def add_entry(self, string_in):
		self.embd_class.make_embedding(string_in)

	# Interface function to return a list of the best matches with cosine similarity
	def best_match(self, text_check, top_scores_return):
		return self.vec_system.find_best_match(text_check, self.embd_class.get_saved_embeddings(), top_scores_return)