def hitung_porositas(BV, BJ):
    N = (1 - (BV / BJ)) * 100
    return N

# Program utama
print("=== Perhitungan Porositas Tanah (N) ===")

BV = float(input("Masukkan Berat Volume Tanah (g/cm3): "))
BJ = float(input("Masukkan Berat Jenis Tanah (g/cm3): "))

N = hitung_porositas(BV, BJ)
print("Porositas Tanah = ", N)

# Klasifikasi tanah berdasarkan porositas
if N < 30:
    print("Klasifikasi: Tanah PADAT (drainase buruk, aerasi rendah)")
elif 30 <= N <= 50:
    print("Klasifikasi: Tanah NORMAL (ideal untuk pertanian)")
else:
    print("Klasifikasi: Tanah LONGGAR (mudah kering, daya simpan air rendah)")
