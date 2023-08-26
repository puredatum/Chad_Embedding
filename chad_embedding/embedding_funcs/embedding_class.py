from sentence_transformers import SentenceTransformer


class EmbeddingClass:
    def __init__(self, db_instance):
        self._model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embedding_result = None
        self.text_in = None
        self.save_embedding_option = True
        self._embdedding_db = db_instance

    # Returns an embedding for a string
    def return_embedding(self, sentence):
        return self._model.encode(sentence)

    # Makes an embedding for a string and stores it in the json database
    def make_embedding(self, sentence):
        self.text_in = sentence
        self.embedding_result = self._model.encode(self.text_in)

        if self.save_embedding_option:
            self.save_embedding()

    # Save an embedding and string to a database
    def save_embedding(self):
        self._embdedding_db.insert_row(self.text_in, self.embedding_result.tolist())

    # Return the entire database
    def get_saved_embeddings(self):
        return self._embdedding_db.get_saved_rows()
