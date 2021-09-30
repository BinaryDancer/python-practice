from solutions.task_4 import C


def test_C():
    M, N = C(), C(1, 2, 3, 4)
    assert str(M) == "C"
    assert str(N) == "C"

    M[13] = N.abc = 37
    assert M[13] == 13
    assert N.abc == "abc"

    assert list(C("QWERQWERQWER")) == []
    del M["QQ"], N[6:10], M[...], N._

    assert M.adhd == "adhd"
    assert N[-2] == -2

    Nm = map(C, range(10))
    assert "".join((f"{n}" for n in Nm)) == "CCCCCCCCCC"

    Nm = map(C, range(10))
    assert list(map(list, (map(str, N) for N in Nm))) == [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    N = C(int)
    assert type(N) == C
    assert str(C()[C()[C()[C()]]]) == "C"
