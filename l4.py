import math

def create_transform_function(tx=None, ty=None, sx=None, sy=None, sudut=None):
    # Inner function untuk translasi
    def translasi(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y

    # Inner function untuk dilatasi
    def dilatasi(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y

    # Inner function untuk rotasi
    def rotasi(x, y):
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y

    # Closure yang memilih inner function berdasarkan transformasi yang diberikan
    def transformasi(x, y):
        if tx is not None and ty is not None:
            return translasi(x, y)
        elif sx is not None and sy is not None:
            return dilatasi(x, y)
        elif sudut is not None:
            return rotasi(x, y)
        else:
            # Jika tidak ada transformasi yang dipilih, kembalikan titik awal
            return x, y

    return transformasi

# Contoh kasus
titik_awal = (3, 5)

# Translasi dengan tx = 2 dan ty = -1
transformasi_translasi = create_transform_function(tx=2, ty=-1)
titik_translasi = transformasi_translasi(*titik_awal)
print("Setelah translasi:", titik_translasi)

# Dilatasi dengan sx = 2 dan sy = -1
transformasi_dilatasi = create_transform_function(sx=2, sy=-1)
titik_dilatasi = transformasi_dilatasi(*titik_awal)
print("Setelah dilatasi:", titik_dilatasi)

# Rotasi dengan sudut = 30 derajat
transformasi_rotasi = create_transform_function(sudut=30)
titik_rotasi = transformasi_rotasi(*titik_awal)
print("Setelah rotasi:", titik_rotasi)
