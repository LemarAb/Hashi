import os


def print_to_txt(n, model, num, gui):

    output_folder = os.path.join(os.getcwd(), 'Solution')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    s = 'man_input' if gui else 'test'

    output_path = os.path.join(output_folder, f'{s}{num}.txt')
    with open(output_path, 'w') as file:
        if model is None:
            file.write("No model!")
            print("No model!")
            return
        j = 0
        def I(i): return (i // 4) // len(n[0])

        for i in range(0, len(model), 4):
            if n[I(i)][j].val != 0:
                file.write(f'{n[I(i)][j].val} ')
                print(f'{n[I(i)][j].val} ', end=' ')
            else:
                if I(i) == 0 or (I(i) == len(n) - 1) or j == 0 or (j == len(n[0]) - 1):
                    file.write('~ ')
                    print('~ ', end=' ')
                else:
                    chunk = model[i:i + 4]

                    to_write = '0 '
                    for c in chunk:
                        if c > 0:
                            # print corresponding bridge symbol from {v1, v2, h1, h2}
                            to_write = chr(104 + ((c - i) // 3) *
                                        14) + f"{((c + 1) % 2) + 1}"
                    file.write(to_write)
                    print(to_write, end=' ')

            j += 1
            if (((i // 4) + 1) % len(n[0])) == 0:
                file.write('\n')
                print('\n')
                j = 0
            else:
                file.write('  ')
                print('  ', end=' ')
