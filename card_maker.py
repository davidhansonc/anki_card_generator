import genanki

# Function to read the lexicon and extract words and definitions
def read_lexicon(lexicon_path):
    # Implement the logic to read and parse the lexicon
    # This is a placeholder for your lexicon reading logic
    pass

# Function to add cards to an existing Anki deck
def add_cards_to_existing_deck(lexicon_path, existing_deck_id):
    # Create a new deck instance with the existing deck's ID
    my_deck = genanki.Deck(
        existing_deck_id,
        'Existing Deck Title'  # You can keep the same title or change it
    )

    # Assume the model is the same as the existing deck's model
    my_model = genanki.Model(
        1607392319,  # Use the existing model ID
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',  # The front of the card
                'afmt': '{{Answer}}',    # The back of the card
            },
        ])

    for greek_word, definition in read_lexicon(lexicon_path):
        my_note = genanki.Note(
            model=my_model,
            fields=[greek_word, definition]
        )
        my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file('output.apkg')

# Replace 'path_to_lexicon' with the actual path to the Scott-Liddle lexicon file
# Replace 'Greek Words' with your desired deck title
# Provide a unique deck_id for each deck you create
create_anki_deck('path_to_lexicon', 'Greek Words', 123456789)