import contextlib

class tag(contextlib.ContextDecorator):
    def __init__(self, name) -> None:
        self.name = name
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.end_tag)
        return False
    
with tag('h2'):
    print('hello')