import json
import os
import sys
sys.path.append('..')

class MetaData:
    def __init__(self):
        self.data = {}
        self.file_path = 'data/meta/meta.json'
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f)

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def remove(self, key):
        if key in self.data:
            del self.data[key]
            self.save()

    def clear(self):
        self.data.clear()
        self.save()