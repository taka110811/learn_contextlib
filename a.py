import contextlib

@contextlib.contextmanager
def tag(name):
    print("<{}>".format(name))
    yield
    print("</{}>".format(name))

@tag('h2')
def say_hello():
    print('hello')

say_hello()