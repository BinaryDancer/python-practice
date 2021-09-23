def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


assert is_leap(1990) is False  # return true if is_leap is False (correct answer)
assert is_leap(1800) is False
assert is_leap(2200) is False
assert is_leap(2100) is False
assert is_leap(2300) is False
assert is_leap(2500) is False
assert is_leap(2400) is True
assert is_leap(2000) is True
assert is_leap(2012) is True
