import json
from chad_embedding import ChadEmbeddingFunc


chad_emb = ChadEmbeddingFunc()

add_data = False

with open("scraped_database.json", 'r') as file:
	data = json.load(file)

if add_data:
	for item in data:
		chad_emb.add_entry(f"'{item['quote']}' - {item['author']}")


text_check = "Working hard at a life project."
top_scores_return = 5
best_match, index_sorted = chad_emb.best_match(text_check, top_scores_return)

for match in best_match:
	print(match)