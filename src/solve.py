from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


def solve(vpool, f):
    with Solver(bootstrap_with=f) as s:
        s.solve()
        print("\nModel:\n")
        model = s.get_model()

    if model is None:
        return
    res = list(map(lambda x: vpool.obj(x) if x > 0 else '~' + vpool.obj(-x), model))
    print(res)
    print()

    return model
