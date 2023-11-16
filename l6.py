def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Inner function untuk menghitung nilai C
    def hitung_C(x, y):
        return y - M * x

    # Menggunakan closure untuk mendapatkan nilai C
    C = hitung_C(*p1)

    return f"y = {M:.2f}x + {C:.2f}"

# Menampilkan persamaan garis yang melalui titik (6,-2) dan bergradien -2
print("Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
print(line_equation_of(point(0, 8), 4))
