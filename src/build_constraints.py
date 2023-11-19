import sympy
from pysat.formula import CNF, IDPool
from assets import *
import math


def build_constraints(field):
    # Create a class named Node representing each x and y value on the field.
    class Node:
        def __init__(self,
                     bridge_no,  # Number of bridges on a given node [ bridge_no element of (0,8)].
                     # hb(X) and vb(Y) refer to the horizontal and vertical bridges. Set to true by default.
                     # The rules of Hashi explain that an island can have at most 2 bridges running in each direction.
                     horizontal_bridge1=sympy.true,
                     horizontal_bridge2=sympy.true,
                     vertical_bridge1=sympy.true,
                     vertical_bridge2=sympy.true):
            self.val = bridge_no
            self.h1 = horizontal_bridge1
            self.h2 = horizontal_bridge2
            self.v1 = vertical_bridge1
            self.v2 = vertical_bridge2

    f = CNF()
    n = [[Node(0) for x in range(len(field[0]))] for y in range(len(field))]
    # variable pool for formula
    vpool = IDPool()
    v = lambda i: vpool.id('{0}'.format(i)) 

    def initialize_nodes():
        for i in range(0, len(field)):
            for j in range(0, len(field[0])):
                    n[i][j] = Node(field[i][j] if field[i][j]!='.' else 0, v(f'h_{i}_{j}'), v(f'dh_{i}_{j}'), v(f'v_{i}_{j}'), v(f'dv_{i}_{j}'))
        return n

    n = initialize_nodes()

    # TODO: Check later whether we need this or not
    # a = [[Node(0, Atom(n[x][y].h1), Atom(n[x][y].h2), Atom(n[x][y].v1), Atom(n[x][y].v2)) for y in range(len(field[0]))]
    #      for x in range(len(field))]
    
    def build_constraints():
        for i in range(0, len(field)):
            for j in range(0, len(field[0])):
                if n[i][j].val == 0:
                    # no cross: only one type of bridge on none island nodes
                    f.extend([[-n[i][j].h1, -n[i][j].v1], [-n[i][j].h2, -n[i][j].v2],
                              [-n[i][j].h1, -n[i][j].v2], [-n[i][j].h2, -n[i][j].v1],
                              [-n[i][j].h1, -n[i][j].h2], [-n[i][j].v1, -n[i][j].v2]
                             ])
                    # continuity: bridges extend from an island node to an island node  
                    if i >= 1:
                        f.extend([[-n[i][j].v1, n[i - 1][j].v1], [-n[i][j].v2, n[i - 1][j].v2]])
                    if i < len(field) - 1:
                        f.extend([[-n[i][j].v1, n[i + 1][j].v1], [-n[i][j].v2, n[i + 1][j].v2]])
                    if j >= 1:
                        f.extend([[-n[i][j].h1, n[i][j - 1].h1], [-n[i][j].h2, n[i][j - 1].h2]])
                    if j < len(field) - 1:
                        f.extend([[-n[i][j].h1, n[i][j + 1].h1], [-n[i][j].h2, n[i][j + 1].h2]])
                else:
                    print(f"THIS IS I,J {i} {j}")
                    # start_and_end: bridges need to start from and end at islands
                    f.extend([[n[i][j].h1], [n[i][j].v1], [n[i][j].h2], [n[i][j].v2]])
                    
                    # degree: bridges built by an island must be equal to its node val
                    clauses = bridge_sum[n[i][j].val]
                    
                    # Since the clauses carry index integers, we need to map them to their corresponding value
                    map_literal = {
                            1: n[i-1][j].v1,
                            2: n[i-1][j].v2,
                            3: n[i+1][j].v1,
                            4: n[i+1][j].v2,
                            5: n[i][j-1].h1,
                            6: n[i][j-1].h2,
                            7: n[i][j+1].h1,
                            8: n[i][j+1].h2
                    }
                    mapped_clauses = [[int(math.copysign(1, var))*map_literal[abs(var)] for var in clause] for clause in clauses]
                    print(list(map(lambda x: vpool.obj(x) if x > 0 else '~' + vpool.obj(-x), mapped_clauses[0])))
                    f.extend(mapped_clauses)
                    
        

    build_constraints()
    # f.extend([[n[4][1].h1], [n[4][3].h2]])
    return n, vpool, f # TODO: this seems too specific, should we delete it?

    # with Solver(bootstrap_with=f) as s:
    #         s.solve()
    #         print("\nModel:")
    #         for m in s.enum_models():
    #             print(m)
