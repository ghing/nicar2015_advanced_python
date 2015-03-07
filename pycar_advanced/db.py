import dataset

def get_default_db():
    db = dataset.connect('sqlite:///:memory:')
    return db
