from app import db


class Todo(db.Model):
    __tablename__ = 'todo_list'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    work = db.Column(db.Text)

    def __repr__(self):
        return f'Name of the person is: "{self.name}". And their work is: "{self.work}"'
