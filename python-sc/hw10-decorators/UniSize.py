def sizer(cls):
    class Sz:
        def __get__(self, obj, cls):
            sz = 0
            try:
                sz = len(obj)
            except Exception as ex:
                try:
                    sz = abs(obj)
                except Exception as ex:
                    return 0
                else:
                    return sz
            else:
                return sz

    def wr(*args, **kwargs):
        cls.size = Sz()
        return cls(*args, **kwargs)
    return wr
