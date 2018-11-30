from model import db, Pin

def seed_test_data():
    data = [
        Pin("http://imsca.red", "Ashley's homepage"),
        Pin("hackbrightacademy.com", "cool bootcamp"),
        Pin("fellowship.hackbrightacademy.com/materials/challenges",
            "code challenges"
            )
    ]

    db.session.add_all(data)
    db.session.commit()

    for p in data:
        print("Added {} to the database".format(p.__repr__()))

if __name__ == "__main__":
    from server import app
    from util.connect import connect_to_db

    connect_to_db(app, db)

