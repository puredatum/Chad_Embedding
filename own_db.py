import json
from chad_embedding import ChadEmbeddingFunc


# Setup the embedding class
chad_emb = ChadEmbeddingFunc()


# Load your own database and run the embedding to add it
db_name = "scraped_database.json"

add_data = False
if add_data:
	with open(db_name, 'r') as file:
		data = json.load(file)

	for item in data:
		chad_emb.add_entry(f"'{item['quote']}' - {item['author']}")


# Run a search for cosine similarity
text_check = "What do we do with our time?"
top_scores_return = 5
best_match, index_sorted = chad_emb.best_match(text_check, top_scores_return)

for match in best_match:
	print(f"{match[0]} - {round(match[1], 3)}")