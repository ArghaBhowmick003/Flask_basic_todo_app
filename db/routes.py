from flask import render_template, request, redirect, url_for

from models import Todo


def register_routes(app, db):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            name = request.form.get('name')
            work = request.form.get('work')
            todo = Todo(name=name, work=work)

            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))

        todoList = Todo.query.all()
        return render_template('index.html', todoList=todoList)

    @app.route('/delete/<int:pid>', methods=['GET'])
    def delete(pid):
        print(Todo.query.filter(Todo.pid == pid).delete())

        db.session.commit()

        return redirect(url_for('index'))

    @app.route('/details/<pid>')
    def details(pid):
        todo = Todo.query.filter(Todo.pid == pid).first()
        return render_template('details.html', todo=todo)
