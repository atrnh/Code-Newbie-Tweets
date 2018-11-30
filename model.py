from flask_sqlalchemy import SQLAlchemy

from util.connect import connect_to_db
from mixin.model_mixins import ApiModel


db = SQLAlchemy()


class Pin(ApiModel, db.Model):
    """A pinned link."""

    __tablename__ = "tweets"

    pin_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True,
                       nullable=False,
                       )
    url = db.Column(db.String(125))
    desc = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return "<Pin pin_id={} url={}>".format(self.pin_id, self.url)

    def __init__(self, url, desc=None):
        self.url = url
        self.desc = desc


if __name__ == "__main__":
    from server import app

    connect_to_db(app, db)
    print("Connected to database")
