from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Pin(db.Model):
    """A pinned link."""

    __tablename__ = "tweets"

    pin_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True,
                       nullable=False,
                       )
    url = db.Column(db.String(125), nullable=True)
    desc = db.Column(db.Text(), nullable=True)

    def __repr__(self):
        return "<Pin pin_id={}>".format(self.pin_id)


def connect_to_db(app, db_uri):
    """Connect the database to app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app, DB_URI
    connect_to_db(app, DB_URI)
    print("Connected to DB, Woohoo!")
