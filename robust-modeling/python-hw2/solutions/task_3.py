from typing import Tuple


def counter(cls, *args) -> Tuple[list, list, list, list]:
    tmp = cls(*args)
    methods_list = [attr for attr in dir(cls) if
                    callable(getattr(cls, attr)) and attr.startswith('_') is False]
    attrs_list = [attr for attr in dir(cls) if
                  not callable(getattr(cls, attr)) and attr.startswith('_') is False]
    new_methods = list(set(attr for attr in dir(tmp) if
                           callable(getattr(tmp, attr)) and attr.startswith('_') is False).difference(
        set(methods_list)))
    new_attrs = list({attr for attr in dir(tmp) if
                      not callable(getattr(tmp, attr)) and attr.startswith('_') is False}.difference(set(attrs_list)))
    return sorted(methods_list), sorted(attrs_list), sorted(new_methods), sorted(new_attrs)
