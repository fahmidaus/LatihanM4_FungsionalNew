def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # Mendapatkan koordinat x dan y dari kedua titik
    x1, y1 = p1
    x2, y2 = p2

    # Menghitung gradien (m) menggunakan rumus (y2 - y1) / (x2 - x1)
    M = (y2 - y1) / (x2 - x1)

    # Menghitung konstanta (c) menggunakan rumus y - mx
    C = y1 - M * x1

    return f"y = {M:.2f}x + {C:.2f}"
print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1,0),point(8,4)))