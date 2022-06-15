import json


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        for todo in self.todos:
            if todo['done'] == False:
                todo['done'] = "NIE"
            if todo['done'] == True:
                todo['done'] = "TAK"

        self.todos = sorted(self.todos, key=lambda k:k['done'])

        return self.todos

    def get(self, id):
        return self.todos[id]


    def create(self, data):
        self.todos.append(data)
        self.save_all()

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    def delete(self, id):
        todo = self.get(id)
        if todo:
            self.todos.remove(todo)
            self.save_all()
            return True
        return False

    def update(self, id, data):
        todo = self.get(id)
        if todo:
            index = self.todos.index(todo)
            self.todos[index] = data
            self.save_all()
            return True
        return False


todos = Todos()

