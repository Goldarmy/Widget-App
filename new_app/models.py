from new_app import db
import json


class Widget(db.Model):
    __tablename__ = 'Widget'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT, nullable=False)
    cost = db.Column(db.INTEGER, nullable=False)

    def __repr__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "cost": self.cost
        })
