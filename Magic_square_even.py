def generate_even_magic_square(n):
    if n < 4 or n % 2 != 0:
        print("Enter an even number >= 4.")
        return

    square = [[0] * n for _ in range(n)]

    if n % 4 == 0:
        # Doubly even magic square (n divisible by 4)
        num = 1
        for i in range(n):
            for j in range(n):
                if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                    square[i][j] = n * n + 1 - num
                else:
                    square[i][j] = num
                num += 1

    else:
        # Singly even magic square (n = 4k + 2)
        half = n // 2
        sub_size = half * half
        sub = [[0] * half for _ in range(half)]

        # Generate sub-square using Siamese method
        i, j = 0, half // 2
        for num in range(1, sub_size + 1):
            sub[i][j] = num
            ni, nj = (i - 1 + half) % half, (j + 1) % half
            if sub[ni][nj] != 0:
                i = (i + 1) % half
            else:
                i, j = ni, nj

        # Combine four sub-squares into main square
        for r in range(half):
            for c in range(half):
                val = sub[r][c]
                square[r][c] = val
                square[r + half][c + half] = val + sub_size
                square[r][c + half] = val + 2 * sub_size
                square[r + half][c] = val + 3 * sub_size

        # Swap columns to fix magic square properties
        k = (half - 1) // 2
        for r in range(half):
            for c in range(k):
                square[r][c], square[r + half][c] = square[r + half][c], square[r][c]
        for r in range(half):
            for c in range(n - k + 1, n):
                square[r][c], square[r + half][c] = square[r + half][c], square[r][c]

    print(f"Magic square of size {n}:")
    for row in square:
        print("\t".join(str(val) for val in row))


if __name__ == "__main__":
    n = int(input("Enter an even number for Magic Square: "))
    generate_even_magic_square(n)