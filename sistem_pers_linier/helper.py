def showEqualities(n, mtrx):
    print("\nDaftar persamaan:")
    for baris in mtrx:
        if abs(baris[0]) != 1:
            print(f'{baris[0]:.0f}', end="")
        if baris[0] == -1:
            print("-", end="")
        print("x1", end="")
        for i in range(1, n):
            if baris[i] == 0:
                continue
            if baris[i] < 0:
                print(" - ", end="")
            else:
                print(" + ", end="")
            if abs(baris[i]) != 1:
                print(f'{abs(baris[i]):.0f}', end="")
            print(f'x{i + 1}', end="")
        print(" = ", end="")
        print(baris[n])

def showMatriceMultiplication(n, a, b, c, mnn, mn1):
    print(f'\n\n\t{a}.{b} = {c}\n')
    for i in range(n):
        print("    [\t", end='')
        for j in range(n):
            print(f'{mnn[i][j]:.3f}\t', end='')
        print("]", end='')

        print(f' [ {b}{i+1} ]  =  [ {mn1[i][0]:.3f} ]')

def showAAsLUProduct(n, a, l, u):
    print("\n\n\tA = L.U\n")
    for i in range(n):
        print("[  ", end='')
        for j in range(n):
            print(f'  {a[i][j]}\t', end='')
        print("]", end='')

        if i == int(n/2):
            print("   =\t", end='')
        else:
            print('\t', end='')

        print("[    ", end='')
        for j in range(n):
            print(f'{l[i][j]:.3f}\t', end='')
        print("]", end='')

        print(" [   ", end='')
        for j in range(n):
            print(f'{u[i][j]:.3f}\t', end='')
        print("]")