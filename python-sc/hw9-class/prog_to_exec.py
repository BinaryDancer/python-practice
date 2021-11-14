
class Z:
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['v','m','a','d','g','q'])


class X(Z):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['k','q','d','g'])


class W(X, Z):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['q','m'])


class P:
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['m','k'])


class O:
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['l','a','d','v'])


class M(P, W, X, Z, O):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['k'])


class L(M, W, X, Z):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update([])


class K(L, P):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['v','q','m'])


class J(K, M, P, W, X, Z, O):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['m'])


class I:
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['m','v','d','a','k'])


class H(L, M, W, X, O):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['v','l','k','a'])


class G(H, I, J, K, L, P, W, X, Z, O):
    def __init__(self):
        self.parts = set()
        super().__init__()
        self.parts.update(['g','k','a'])


class PepelaC3(H, I, K, P, X, O):
    def __init__(self):
        self.req_elements = set(['a', 'v', 'q', 'g', 'm', 'l'])
        self.parts = set()
        super().__init__()
        self.parts.update(['m'])
        for el in self.req_elements:
            if el not in self.parts:
                raise "Can't construct"


PepelaC3()

