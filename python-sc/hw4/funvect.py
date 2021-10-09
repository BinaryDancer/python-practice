from sys import stdin


def superposition(funmod, funseq):
    return [lambda x, f1=f: funmod(f1(x)) for f in funseq]


for line in stdin:
    exec(line)
