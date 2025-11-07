def hitung_reynolds(v, D):
    rho = 1000                # kg/m3
    viskositas = 0.001005     # Pa.s
    Re = (rho * v * D) / viskositas
    return Re

# Program utama
print("=== Perhitungan Bilangan Reynolds (Re) ===")

v = float(input("Masukkan kecepatan aliran (m/s): "))
D = float(input("Masukkan diameter pipa (m): "))

Re = hitung_reynolds(v, D)
print("Bilangan Reynolds (Re) = ", Re)

# Klasifikasi aliran
if Re < 2000:
    print("Karakteristik aliran: LAMINAR (aliran halus, kecepatan rendah)")
elif 2000 <= Re <= 4000:
    print("Karakteristik aliran: TRANSISI (mulai tidak stabil, waspada perubahan tekanan)")
else:
    print("Karakteristik aliran: TURBULEN (aliran bergejolak, efisiensi energi rendah)")
