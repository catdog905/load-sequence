class PureAction:

    def __init__(self, func, **kwargs):
        self.func = func
        self.kwargs = kwargs

    def call(self):
        return self.func(**self.kwargs)
        