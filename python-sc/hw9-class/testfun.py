class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, errs=[]):
        check = 0
        for s in suite:
            try:
                self.fun(*s)
            except Exception as ex:
                check2 = 0
                for allowed_ex in errs:
                    if isinstance(ex, allowed_ex):
                        check2 = 1
                if check2 == 1:
                    check = max(1, check)
                else:
                    check = 2
        if check == 2:
            return 1
        if check == 1:
            return -1
        return 0
