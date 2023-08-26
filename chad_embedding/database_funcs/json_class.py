import json
import os


class JsonDatabase:
    def __init__(self):
        self._database_name = "my_database"
        self.create_database()

    # Create the database if needed
    def create_database(self):
        if not os.path.exists(f'{self._database_name}.json'):
            print("Making database file")
            data = []
            with open(f'{self._database_name}.json', 'w') as file:
                json.dump(data, file)

    # Insert text and an embedding
    def insert_row(self, text_in, embedding):
        if os.path.exists(f'{self._database_name}.json'):
            try:
                with open(f'{self._database_name}.json', 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                data = []
        
        data.append({"text_in": text_in, "embedding": embedding})

        with open(f'{self._database_name}.json', 'w') as file:
            json.dump(data, file)
        print("Row inserted into databse.")

    # Return all the rows of the database
    def get_saved_rows(self):
        if os.path.exists(f'{self._database_name}.json'):
            with open(f'{self._database_name}.json', 'r') as file:
                data = json.load(file)

        return data