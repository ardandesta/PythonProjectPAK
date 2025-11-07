def laju_panas_hilang(ma, T_awal, T_akhir, t):
    """
    Menghitung laju panas hilang (kJ/s)
    Rumus: q = (ma * Cp * (T_awal - T_akhir)) / t
    """
    Cp = 4.186  # kJ/kg°C
    q = (ma * Cp * (T_awal - T_akhir)) / t
    return q

# Input dari user
ma = float(input("Masukkan massa air (kg): "))
T_awal = float(input("Masukkan suhu awal (°C): "))
T_akhir = float(input("Masukkan suhu akhir (°C): "))
t = float(input("Masukkan waktu pengukuran (detik): "))

# Hitung laju panas hilang
hasil = laju_panas_hilang(ma, T_awal, T_akhir, t)
print("Laju panas hilang: ", hasil, " kJ/s")

# Evaluasi efisiensi sistem pendinginan
if hasil < 0:
    print("Data tidak valid — periksa input suhu atau waktu.")
elif hasil < 0.200:
    print("Sistem pendinginan sangat efisien.")
elif hasil < 0.500:
    print("Sistem pendinginan cukup efisien.")
else:
    print("Kehilangan panas tinggi — isolasi perlu diperbaiki.")
