bridge_sum_DNF ={}
bridge_sum_CNF = {}

bridge_sum_DNF[0]=[ [ -2, -8, -7, -6, -5, -4, -3, -1 ],  ]
bridge_sum_DNF[1]=[ [ 1, -2, -8, -7, -6, -5, -4, -3 ],  [ 3, -2, -8, -7, -6, -5, -4, -1 ],  [ 5, -2, -8, -7, -6, -4, -3, -1 ],  [ 7, -2, -8, -6, -5, -4, -3, -1 ],  ]
bridge_sum_DNF[2]=[ [ 2, -8, -7, -6, -5, -4, -3, -1 ],  [ 4, -2, -8, -7, -6, -5, -3, -1 ],  [ 6, -2, -8, -7, -5, -4, -3, -1 ],  [ 8, -2, -7, -6, -5, -4, -3, -1 ],  [ 1, 3, -2, -8, -7, -6, -5, -4 ],  [ 1, 5, -2, -8, -7, -6, -4, -3 ],  [ 1, 7, -2, -8, -6, -5, -4, -3 ],  [ 3, 5, -2, -8, -7, -6, -4, -1 ],  [ 3, 7, -2, -8, -6, -5, -4, -1 ],  [ 5, 7, -2, -8, -6, -4, -3, -1 ],  ]
bridge_sum_DNF[3]=[ [ 1, 2, -8, -7, -6, -5, -4, -3 ],  [ 1, 4, -2, -8, -7, -6, -5, -3 ],  [ 1, 6, -2, -8, -7, -5, -4, -3 ],  [ 1, 8, -2, -7, -6, -5, -4, -3 ],  [ 2, 5, -8, -7, -6, -4, -3, -1 ],  [ 2, 7, -8, -6, -5, -4, -3, -1 ],  [ 3, 4, -2, -8, -7, -6, -5, -1 ],  [ 3, 6, -2, -8, -7, -5, -4, -1 ],  [ 3, 8, -2, -7, -6, -5, -4, -1 ],  [ 4, 7, -2, -8, -6, -5, -3, -1 ],  [ 5, 6, -2, -8, -7, -4, -3, -1 ],  [ 5, 8, -2, -7, -6, -4, -3, -1 ],  [ 7, 8, -2, -6, -5, -4, -3, -1 ],  [ 1, 3, 5, -2, -8, -7, -6, -4 ],  [ 1, 3, 7, -2, -8, -6, -5, -4 ],  [ 1, 5, 7, -2, -8, -6, -4, -3 ],  [ 3, 5, 7, -2, -8, -6, -4, -1 ],  ]
bridge_sum_DNF[4]=[ [ 2, 4, -8, -7, -6, -5, -3, -1 ],  [ 2, 6, -8, -7, -5, -4, -3, -1 ],  [ 2, 8, -7, -6, -5, -4, -3, -1 ],  [ 4, 6, -2, -8, -7, -5, -3, -1 ],  [ 4, 8, -2, -7, -6, -5, -3, -1 ],  [ 6, 8, -2, -7, -5, -4, -3, -1 ],  [ 1, 2, 5, -8, -7, -6, -4, -3 ],  [ 1, 2, 7, -8, -6, -5, -4, -3 ],  [ 1, 3, 6, -2, -8, -7, -5, -4 ],  [ 1, 3, 8, -2, -7, -6, -5, -4 ],  [ 1, 4, 7, -2, -8, -6, -5, -3 ],  [ 1, 5, 6, -2, -8, -7, -4, -3 ],  [ 1, 5, 8, -2, -7, -6, -4, -3 ],  [ 1, 7, 8, -2, -6, -5, -4, -3 ],  [ 2, 5, 7, -8, -6, -4, -3, -1 ],  [ 3, 4, 7, -2, -8, -6, -5, -1 ],  [ 3, 5, 6, -2, -8, -7, -4, -1 ],  [ 3, 5, 8, -2, -7, -6, -4, -1 ],  [ 3, 7, 8, -2, -6, -5, -4, -1 ],  [ 1, 3, 5, 7, -2, -8, -6, -4 ],  ]
bridge_sum_DNF[5]=[ [ 1, 2, 6, -8, -7, -5, -4, -3 ],  [ 1, 2, 8, -7, -6, -5, -4, -3 ],  [ 1, 4, 6, -2, -8, -7, -5, -3 ],  [ 1, 4, 8, -2, -7, -6, -5, -3 ],  [ 1, 6, 8, -2, -7, -5, -4, -3 ],  [ 2, 4, 7, -8, -6, -5, -3, -1 ],  [ 2, 5, 6, -8, -7, -4, -3, -1 ],  [ 2, 5, 8, -7, -6, -4, -3, -1 ],  [ 2, 7, 8, -6, -5, -4, -3, -1 ],  [ 3, 4, 6, -2, -8, -7, -5, -1 ],  [ 3, 4, 8, -2, -7, -6, -5, -1 ],  [ 3, 6, 8, -2, -7, -5, -4, -1 ],  [ 4, 7, 8, -2, -6, -5, -3, -1 ],  [ 1, 2, 5, 7, -8, -6, -4, -3 ],  [ 1, 3, 5, 6, -2, -8, -7, -4 ],  [ 1, 3, 5, 8, -2, -7, -6, -4 ],  [ 1, 3, 7, 8, -2, -6, -5, -4 ],  ]
bridge_sum_DNF[6]=[ [ 2, 4, 6, -8, -7, -5, -3, -1 ],  [ 2, 4, 8, -7, -6, -5, -3, -1 ],  [ 2, 6, 8, -7, -5, -4, -3, -1 ],  [ 4, 6, 8, -2, -7, -5, -3, -1 ],  [ 1, 2, 5, 6, -8, -7, -4, -3 ],  [ 1, 2, 5, 8, -7, -6, -4, -3 ],  [ 1, 2, 7, 8, -6, -5, -4, -3 ],  [ 1, 3, 6, 8, -2, -7, -5, -4 ],  [ 1, 4, 7, 8, -2, -6, -5, -3 ],  [ 3, 4, 7, 8, -2, -6, -5, -1 ],  ]
bridge_sum_DNF[7]=[ [ 1, 2, 6, 8, -7, -5, -4, -3 ],  [ 1, 4, 6, 8, -2, -7, -5, -3 ],  [ 2, 4, 7, 8, -6, -5, -3, -1 ],  [ 3, 4, 6, 8, -2, -7, -5, -1 ],  ]
bridge_sum_DNF[8]=[ [ 2, 4, 6, 8, -7, -5, -3, -1 ],  ]


bridge_sum_CNF[0]=[ [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[1]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[2]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[3]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[4]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[5]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[6]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[7]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -2, -4, -6, -8, 7, 5, 3, 1 ],  ]
bridge_sum_CNF[8]=[ [ 2, 8, 7, 6, 5, 4, 3, 1 ],  [ -1, 2, 8, 7, 6, 5, 4, 3 ],  [ -3, 2, 8, 7, 6, 5, 4, 1 ],  [ -5, 2, 8, 7, 6, 4, 3, 1 ],  [ -7, 2, 8, 6, 5, 4, 3, 1 ],  [ -2, 8, 7, 6, 5, 4, 3, 1 ],  [ -4, 2, 8, 7, 6, 5, 3, 1 ],  [ -6, 2, 8, 7, 5, 4, 3, 1 ],  [ -8, 2, 7, 6, 5, 4, 3, 1 ],  [ -1, -3, 2, 8, 7, 6, 5, 4 ],  [ -1, -5, 2, 8, 7, 6, 4, 3 ],  [ -1, -7, 2, 8, 6, 5, 4, 3 ],  [ -3, -5, 2, 8, 7, 6, 4, 1 ],  [ -3, -7, 2, 8, 6, 5, 4, 1 ],  [ -5, -7, 2, 8, 6, 4, 3, 1 ],  [ -1, -2, 8, 7, 6, 5, 4, 3 ],  [ -1, -4, 2, 8, 7, 6, 5, 3 ],  [ -1, -6, 2, 8, 7, 5, 4, 3 ],  [ -1, -8, 2, 7, 6, 5, 4, 3 ],  [ -2, -5, 8, 7, 6, 4, 3, 1 ],  [ -2, -7, 8, 6, 5, 4, 3, 1 ],  [ -3, -4, 2, 8, 7, 6, 5, 1 ],  [ -3, -6, 2, 8, 7, 5, 4, 1 ],  [ -3, -8, 2, 7, 6, 5, 4, 1 ],  [ -4, -7, 2, 8, 6, 5, 3, 1 ],  [ -5, -6, 2, 8, 7, 4, 3, 1 ],  [ -5, -8, 2, 7, 6, 4, 3, 1 ],  [ -7, -8, 2, 6, 5, 4, 3, 1 ],  [ -1, -3, -5, 2, 8, 7, 6, 4 ],  [ -1, -3, -7, 2, 8, 6, 5, 4 ],  [ -1, -5, -7, 2, 8, 6, 4, 3 ],  [ -3, -5, -7, 2, 8, 6, 4, 1 ],  [ -2, -4, 8, 7, 6, 5, 3, 1 ],  [ -2, -6, 8, 7, 5, 4, 3, 1 ],  [ -2, -8, 7, 6, 5, 4, 3, 1 ],  [ -4, -6, 2, 8, 7, 5, 3, 1 ],  [ -4, -8, 2, 7, 6, 5, 3, 1 ],  [ -6, -8, 2, 7, 5, 4, 3, 1 ],  [ -1, -2, -5, 8, 7, 6, 4, 3 ],  [ -1, -2, -7, 8, 6, 5, 4, 3 ],  [ -1, -3, -6, 2, 8, 7, 5, 4 ],  [ -1, -3, -8, 2, 7, 6, 5, 4 ],  [ -1, -4, -7, 2, 8, 6, 5, 3 ],  [ -1, -5, -6, 2, 8, 7, 4, 3 ],  [ -1, -5, -8, 2, 7, 6, 4, 3 ],  [ -1, -7, -8, 2, 6, 5, 4, 3 ],  [ -2, -5, -7, 8, 6, 4, 3, 1 ],  [ -3, -4, -7, 2, 8, 6, 5, 1 ],  [ -3, -5, -6, 2, 8, 7, 4, 1 ],  [ -3, -5, -8, 2, 7, 6, 4, 1 ],  [ -3, -7, -8, 2, 6, 5, 4, 1 ],  [ -1, -3, -5, -7, 2, 8, 6, 4 ],  [ -1, -2, -6, 8, 7, 5, 4, 3 ],  [ -1, -2, -8, 7, 6, 5, 4, 3 ],  [ -1, -4, -6, 2, 8, 7, 5, 3 ],  [ -1, -4, -8, 2, 7, 6, 5, 3 ],  [ -1, -6, -8, 2, 7, 5, 4, 3 ],  [ -2, -4, -7, 8, 6, 5, 3, 1 ],  [ -2, -5, -6, 8, 7, 4, 3, 1 ],  [ -2, -5, -8, 7, 6, 4, 3, 1 ],  [ -2, -7, -8, 6, 5, 4, 3, 1 ],  [ -3, -4, -6, 2, 8, 7, 5, 1 ],  [ -3, -4, -8, 2, 7, 6, 5, 1 ],  [ -3, -6, -8, 2, 7, 5, 4, 1 ],  [ -4, -7, -8, 2, 6, 5, 3, 1 ],  [ -1, -2, -5, -7, 8, 6, 4, 3 ],  [ -1, -3, -5, -6, 2, 8, 7, 4 ],  [ -1, -3, -5, -8, 2, 7, 6, 4 ],  [ -1, -3, -7, -8, 2, 6, 5, 4 ],  [ -2, -4, -6, 8, 7, 5, 3, 1 ],  [ -2, -4, -8, 7, 6, 5, 3, 1 ],  [ -2, -6, -8, 7, 5, 4, 3, 1 ],  [ -4, -6, -8, 2, 7, 5, 3, 1 ],  [ -1, -2, -5, -6, 8, 7, 4, 3 ],  [ -1, -2, -5, -8, 7, 6, 4, 3 ],  [ -1, -2, -7, -8, 6, 5, 4, 3 ],  [ -1, -3, -6, -8, 2, 7, 5, 4 ],  [ -1, -4, -7, -8, 2, 6, 5, 3 ],  [ -3, -4, -7, -8, 2, 6, 5, 1 ],  [ -1, -2, -6, -8, 7, 5, 4, 3 ],  [ -1, -4, -6, -8, 2, 7, 5, 3 ],  [ -2, -4, -7, -8, 6, 5, 3, 1 ],  [ -3, -4, -6, -8, 2, 7, 5, 1 ],  ]
