
class CallingLogger(object):
    def __init__(self, method):
        self.called = False
        self.method = method

    def __call__(self):
       self.method()
       self.called = True
