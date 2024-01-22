import sqlite3

class AnkiDeckManager:
    def __init__(self, collection_path):
        self.collection_path = collection_path

    def get_deck_id(self, deck_name):
        # Connect to the Anki database
        conn = sqlite3.connect(self.collection_path)
        cursor = conn.cursor()

        # Query the decks table for the deck ID
        cursor.execute("SELECT id FROM decks WHERE name = ?", (deck_name,))
        deck_id = cursor.fetchone()

        # Close the connection
        conn.close()

        if deck_id:
            return deck_id[0]
        else:
            return None

# Usage
collection_path = '/path/to/collection.anki2'  # Replace with your Anki collection path
deck_name = 'Name of the existing deck'  # Replace with the name of your deck

anki_manager = AnkiDeckManager(collection_path)
deck_id = anki_manager.get_deck_id(deck_name)

if deck_id:
    print(f"The deck ID for '{deck_name}' is {deck_id}")
else:
    print(f"No deck found with the name '{deck_name}'")