# Fungsi 1: Hitung konstanta a
def hitung_a(R, Tc, Pc):
    return (27 * (R**2) * (Tc**2)) / (64 * Pc)

# Fungsi 2: Hitung konstanta b
def hitung_b(R, Tc, Pc):
    return (R * Tc) / (8 * Pc)

# Fungsi 3: Hitung tekanan gas dengan persamaan Van der Waals
def hitung_P(R, T, v, a, b):
    return (R * T) / (v - b) - (a / (v**2))

# Hitung a, b, dan tekanan
a = hitung_a(0.4615, float(input("Masukkan suhu kritis (K): ")), float(input("Masukkan tekanan kritis (kPa): ")))
b = hitung_b(0.4615, float(input("Masukkan suhu kritis (K): ")), float(input("Masukkan tekanan kritis (kPa): ")))
P = hitung_P(0.4615, float(input("Masukkan suhu (K): ")), float(input("Masukkan volume spesifik (m³/kg): ")), a, b)

# Output
print("\nNilai konstanta a = ", a)
print("Nilai konstanta b = ", b)
print("Tekanan gas (Van der Waals) = ", P, " kPa")

# Analisis hasil
if P < 500:
    print("Tekanan rendah — gas mendekati kondisi ideal.")
elif P < 2000:
    print("Tekanan sedang — interaksi antar molekul mulai signifikan.")
else:
    print("Tekanan tinggi — efek Van der Waals dominan.")
