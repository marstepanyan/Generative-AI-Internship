class TaskToDo:
    last_id = 0

    def __init__(self, title, description):
        TaskToDo.last_id += 1
        self.id = TaskToDo.last_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
