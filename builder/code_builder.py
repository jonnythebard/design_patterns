class CodeBuilder:
    INDENT_SIZE = 4
    BASE = 'class {root_name}:\n{indent}def __init__(self):'

    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = [self.BASE.format(root_name=self.root_name, indent=' ' * self.INDENT_SIZE)]

    def add_field(self, attr, value):
        self.fields.append(
            f'self.{attr} = {value}'
        )
        return self

    def __str__(self):
        return ('\n' + ' ' * self.INDENT_SIZE * 2).join(self.fields)

"""
class Person:
    def __init__(self):
        self.name = ''
        self.age = 0
"""

if __name__ == '__main__':
    code = CodeBuilder('Person').add_field('name', "''") \
                                .add_field('age', '0')
    print(code)
