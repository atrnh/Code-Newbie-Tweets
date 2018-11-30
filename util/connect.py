def connect_to_db(app, db):
    """Connect the given app instance to the database at the specified URI."""

    db.app = app
    db.init_app(app)
