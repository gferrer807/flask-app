from pymongo import MongoClient

# Connect to your MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
db = client['manga_db']
manga_collection = db['manga']

def insert_manga(manga):
    # Validate the manga document using the `validate_manga` function
    if validate_manga(manga):
        manga_collection.insert_one(manga)
    else:
        raise ValueError("Invalid manga document")

def validate_manga(manga):
    # Define the required fields and their types
    required_fields = {
        'title': str,
        'description': str,
        'status': str,
        'genres': list,
        'authors': list,
        'artists': list,
        'imageUrl': str,
        'chapters': list
    }

    # Check if all required fields are present and their types match
    for field, field_type in required_fields.items():
        if field not in manga or not isinstance(manga[field], field_type):
            return False

    # Validate chapters
    for chapter in manga['chapters']:
        if not validate_chapter(chapter):
            return False

    return True

def validate_chapter(chapter):
    required_fields = {
        'number': int,
        'title': str,
        'date': str,
        'images': list
    }

    for field, field_type in required_fields.items():
        if field not in chapter or not isinstance(chapter[field], field_type):
            return False

    return True

# Example usage
manga_example = {
    'title': 'Manga 1',
    'description': 'A sample manga',
    'status': 'Ongoing',
    'genres': ['Action', 'Adventure'],
    'authors': ['Author 1'],
    'artists': ['Artist 1'],
    'imageUrl': 'https://path/to/manga1/image.jpg',
    'chapters': [
        {
            'number': 1,
            'title': 'Chapter 1',
            'date': '2022-01-01',
            'images': ['https://path/to/chapter1/image1.jpg', 'https://path/to/chapter1/image2.jpg']
        }
    ]
}

# Insert the example manga into the collection
insert_manga(manga_example)