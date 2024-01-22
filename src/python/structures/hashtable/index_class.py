class Index:
    def __init__(self):
        self.value = []
    
    def add_value(self, value):
        self.value.append(value)
        return value

    def __len__(self):
        i = 0
        for item in self.value:
            i += 1

        return i

    def __repr__(self):
        return str(self.value)