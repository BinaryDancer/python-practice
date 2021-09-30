class C:
    def __init__(self, *args, **kwargs):
        pass

    def __getitem__(self, key):
        return key

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        pass

    def __delattr__(self, item):
        pass

    def __iter__(self):
        return iter([])

    def __str__(self):
        return "C"
