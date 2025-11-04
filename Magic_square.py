def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("This method works only for odd n")

    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2  

    for num in range(1, n * n + 1):
        magic_square[i][j] = num

        new_i = (i - 1) % n   
        new_j = (j + 1) % n   

        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n  
        else:
            i, j = new_i, new_j

    return magic_square


n = 3
magic_square = generate_magic_square(n)

print(f"Magic Square of size {n}x{n}:")
for row in magic_square:
    print(row)

magic_constant = n * (n * n + 1) // 2
print("Magic Constant:", magic_constant)