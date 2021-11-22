class Lock:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Lock, cls).__new__(cls)

            cls.sem = {}
        return cls._instance

    @staticmethod
    def locked(cls):
        cls.lock = Semaphore()
        cls._resource = None

        def new_del(self):
            del self.lock
            try:
                super(type(self), self).__del__
            except AttributeError:
                pass
            else:
                super(type(self), self).__del__()
        cls.__del__ = new_del
        return cls


class Semaphore:
    def __init__(self):
        self.resources = Lock()

    def __get__(self, instance, owner):
        locking_owner = self.resources.sem.get(instance._resource)
        if not locking_owner:
            self.resources.sem[instance._resource] = id(instance)
            return instance._resource
        elif locking_owner == id(instance):
            return instance._resource
        else:
            return None

    def __set__(self, instance, value):
        if self.resources.sem.get(instance._resource) == id(instance):
            self.resources.sem[instance._resource] = None
        instance._resource = value

    def __delete__(self, instance):
        if self.resources.sem.get(instance._resource) == id(instance):
            self.resources.sem[instance._resource] = None
        instance._lock = None
