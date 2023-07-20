from abc import ABC, abstractmethod
import os


class DataStorageSystem(ABC):
    @abstractmethod
    def save(self, file_name, data):
        pass

    @abstractmethod
    def load(self, file_name):
        pass

    @abstractmethod
    def delete(self, file_name):
        pass


class FileBasedStorage(DataStorageSystem):
    def save(self, file_name, data):
        with open(file_name, "w+") as file:
            file.write(str(data))
        return f"Data was saved to {file_name} file."

    def load(self, file_name):
        try:
            with open(file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"{file_name} not found."

    def delete(self, file_name):
        try:
            os.remove(file_name)
            return f"{file_name} was deleted."
        except FileNotFoundError:
            return f"{file_name} not found."


file_storage = FileBasedStorage()

print(file_storage.save("first_file.txt", "Hello, here is some data."))
print(file_storage.save("second_file.txt", "Hey, here is another data."))

print(file_storage.load("first_file.txt"))
print(file_storage.load("second_file.txt"))

print(file_storage.delete("first_file.txt"))
print(file_storage.delete("second_file.txt"))

print()


class DatabaseStorage(DataStorageSystem):
    def __init__(self):
        self.database = {}

    def save(self, key, data):
        self.database[key] = str(data)
        return "Data was saved to database."

    def load(self, key):
        return self.database.get(key, f"{key} not found.")

    def delete(self, key):
        if key in self.database:
            del self.database[key]
        return f"{key} was deleted from database."


db_storage = DatabaseStorage()

print(db_storage.save("user1", {"name": "James", "age": 30}))
print(db_storage.save("user2", {"name": "Alice", "age": 25}))

print(db_storage.load("user1"))
print(db_storage.load("user2"))
print(db_storage.load("user3"))

print(db_storage.delete("user1"))
print(db_storage.load("user1"))
