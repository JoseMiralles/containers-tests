from app.models.users_model import User

def start_seed(db):
    new_user = User(
        name="Jose Miralles"
    )
    db.session.add(new_user)
    db.session.commit()
