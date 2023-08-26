from chad_embedding import ChadEmbeddingFunc


chad_emb = ChadEmbeddingFunc()

make_entries = False
if make_entries:
	chad_emb.add_entry('Bitcoin is is a useful way to make digital gold')
	chad_emb.add_entry('What is bitcoin?')
	chad_emb.add_entry('Bitcoin is bad')
	chad_emb.add_entry('What is cryptocurrency?')
	chad_emb.add_entry('What is a cat?')
	chad_emb.add_entry('What is money?')
	chad_emb.add_entry('What is ethereum?')
	chad_emb.add_entry('What is gold as a currency?')
	chad_emb.add_entry('The dog is brown')
	chad_emb.add_entry('Bitcoin is an interesting form of currency')


text_check = "Bitcoin is a cool concept"
top_scores_return = 3
best_match = chad_emb.best_match(text_check, top_scores_return)

print(text_check)
print(best_match)