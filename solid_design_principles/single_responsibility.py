"""
A class should only have one reason to change.
Separation of concerns - different classes handling different, independent tasks/problems
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, idx):
        del self.entries[idx]

    def __str__(self):
        return '\n'.join(self.entries)

    """Not good to give persistence responsibility"""
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('i read a book')
j.add_entry('i ate ramen')
print(j)


PersistenceManager.save_to_file(j, 'journal.txt')
