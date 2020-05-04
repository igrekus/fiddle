ids = ['pig', '', 'sheep']


class Animal:
    def __init__(self, name):
        self.name = name
    @classmethod
    def find(cls, id):
        return animal_db.get(id)
    def __repr__(self):
        return f'<{self.__class__.__name__}> ({self.name=})'


class MissingAnimal:
    name = 'no animal'
    def __repr__(self):
        return f'<{self.__class__.__name__}> ({self.name=})'


animal_db = {
    'pig': Animal('pig'),
    'sheep': Animal('sheep'),
    'dog': Animal('dog')
}


animals = [Animal.find(id) or MissingAnimal() for id in ids]
# animals = filter(bool, animals)   # if None is really nothing, filter it our
for an in animals:
    print(an.name)
