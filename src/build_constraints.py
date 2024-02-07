import os
from pysat.formula import CNF, IDPool
from assets.bridge_sum import bridge_sum_CNF_opt as bridge_sum
import math


def build_constraints(field, from_gui, num):
    class Node:
        def __init__(self,
                     bridge_no,
                     horizontal_bridge1=None,
                     horizontal_bridge2=None,
                     vertical_bridge1=None,
                     vertical_bridge2=None):
            self.val = bridge_no
            self.h1 = horizontal_bridge1
            self.h2 = horizontal_bridge2
            self.v1 = vertical_bridge1
            self.v2 = vertical_bridge2

    # formula f, nodes array n, variable pool vpool
    f = CNF()
    n = [[Node(0) for _ in range(len(field[0]))] for _ in range(len(field))]
    vpool = IDPool()
    def v(i): return vpool.id('{0}'.format(i))

    def initialize_nodes():
        for i in range(0, len(field)):
            for j in range(0, len(field[0])):
                n[i][j] = Node(field[i][j], v(f'h_{i}_{j}'), v(
                    f'dh_{i}_{j}'), v(f'v_{i}_{j}'), v(f'dv_{i}_{j}'))

                # frame variables are necessary to build degree constraint but should themselves be set to false to help with connectivity constraint later
                if i == 0 or i == (len(field) - 1) or j == 0 or (j == len(field[0])-1):
                    f.extend([[-n[i][j].h1], [-n[i][j].h2],
                             [-n[i][j].v1], [-n[i][j].v2]])
        return n

    n = initialize_nodes()

    def build_constraints():
        for i in range(1, len(field)-1):
            for j in range(1, len(field[0])-1):
                if n[i][j].val == 0:

                    # no cross: only one type of bridge on none island nodes
                    f.extend([[-n[i][j].h1, -n[i][j].v1], [-n[i][j].h2, -n[i][j].v2],
                              [-n[i][j].h1, -n[i][j].v2], [-n[i][j].h2, -n[i][j].v1],
                              [-n[i][j].h1, -n[i][j].h2], [-n[i][j].v1, -n[i][j].v2],
                              ])

                    # continuity: bridges extend from an island node to an island node
                    f.extend([[-n[i][j].v1, n[i - 1][j].v1],
                             [-n[i][j].v2, n[i - 1][j].v2]])
                    f.extend([[-n[i][j].v1, n[i + 1][j].v1],
                             [-n[i][j].v2, n[i + 1][j].v2]])
                    f.extend([[-n[i][j].h1, n[i][j - 1].h1],
                             [-n[i][j].h2, n[i][j - 1].h2]])
                    f.extend([[-n[i][j].h1, n[i][j + 1].h1],
                             [-n[i][j].h2, n[i][j + 1].h2]])
                else:
                    # start_and_end: bridges need to start from and end at islands
                    f.extend([[n[i][j].h1], [n[i][j].v1],
                             [n[i][j].h2], [n[i][j].v2]])

                    # degree: bridges built by an island must be equal to its node val
                    degree_clauses = bridge_sum[n[i][j].val]

                    # clauses for the degree constraint carry index integers, we need to map them to their corresponding value
                    mapping = {}

                    mapping[1] = n[i-1][j].v1
                    mapping[2] = n[i-1][j].v2
                    mapping[3] = n[i+1][j].v1
                    mapping[4] = n[i+1][j].v2
                    mapping[5] = n[i][j-1].h1
                    mapping[6] = n[i][j-1].h2
                    mapping[7] = n[i][j+1].h1
                    mapping[8] = n[i][j+1].h2

                    resolved_degree_clauses = [[int(math.copysign(1, literal))*mapping[abs(literal)] for literal in clause] for clause in degree_clauses]

                    f.extend(resolved_degree_clauses)

    build_constraints()

    def write_dimacs(cnf, filename):
        with open(filename, 'w') as f:
            f.write('p cnf {} {}\n'.format(len(cnf), 4*len(field)*len(field[0])))
            for clause in cnf:
                clause_str = ' '.join(str(lit) for lit in clause)
                f.write(clause_str + ' 0\n')

    output_folder = os.path.join(os.getcwd(), 'DIMACS')
    write_dimacs(f.clauses, f"{output_folder}/{'man_input' if from_gui else 'test'}{num}.cnf")

    return n, vpool, f
