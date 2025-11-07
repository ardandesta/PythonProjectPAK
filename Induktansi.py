def hitung_induktansi(N, A, l):
    mu = 0.000063  # permeabilitas bahan inti (H/m)
    L = (mu * (N ** 2) * A) / l
    return L

print("=== Perhitungan Induktansi Kumparan (L) ===")

N = int(input("Masukkan jumlah lilitan (N): "))
A = float(input("Masukkan luas penampang inti (m^2): "))
l = float(input("Masukkan panjang inti (m): "))

L = hitung_induktansi(N, A, l)
print("Nilai Induktansi (L) = ", L, " H")  # format desimal

# Klasifikasi hasil
if L <= 0:
    print("Data tidak valid! Periksa kembali input Anda.")
elif L < 0.0001:
    print("Klasifikasi: Induktansi KECIL — efisiensi rendah, sinyal lemah.")
elif 0.0001 <= L <= 0.01:
    print("Klasifikasi: Induktansi SEDANG — cocok untuk sistem kontrol pertanian.")
elif L > 0.01:
    print("Klasifikasi: Induktansi BESAR — digunakan pada elektromagnet daya tinggi.")
else:
    print("Terjadi kesalahan logika dalam perhitungan.")
