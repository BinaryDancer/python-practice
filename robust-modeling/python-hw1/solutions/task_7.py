def is_valid_regex(regex: str) -> bool:
    import re
    try:
        re.compile(regex)
    except Exception:
        return False
    return True


# should be true
assert is_valid_regex(r".*\+") == True
assert is_valid_regex(r".*+") == False
