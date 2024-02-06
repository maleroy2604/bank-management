import os.path
import pickle


class FileManager:

    @staticmethod
    def create_file(file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass

    @staticmethod
    def save_to_file(entity, filename):
        entities = FileManager.load_from_file(filename) or []
        entities.append(entity)
        with open(filename, 'wb') as file:
            pickle.dump(entities, file)

    @staticmethod
    def load_from_file(filename):
        if os.path.getsize(filename) == 0:
            return None
        with open(filename, 'rb') as file:
            entities = pickle.load(file)
        return entities
