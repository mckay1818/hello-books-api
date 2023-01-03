from app import db

#create class method to create Book instance with from_dict
@classmethod
def create_from_dict(cls, dict_data):
    pass

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        dict = {}
        dict["id"] = self.id
        dict["title"] = self.title
        dict["description"] = self.description

        return dict