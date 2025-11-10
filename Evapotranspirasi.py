# Fungsi menghitung ET0
def hitung_et0(delta, Rn, G, gamma, T, u2, es, ea):
    ET0 = ((0.408 * delta * (Rn - G)) + (gamma * (900 / (T + 273)) * u2 * (es - ea))) / (delta + gamma * (1 + 0.34 * u2))
    return ET0

# Fungsi menentukan kategori ET0
def kategori_et0(ET0):
    if ET0 < 2:
        return "Kehilangan air rendah — cocok untuk tanaman padi muda."
    elif ET0 < 5:
        return "Kehilangan air sedang — irigasi periodik diperlukan."
    else:
        return "Kehilangan air tinggi — perlu peningkatan frekuensi irigasi."

# Fungsi menampilkan hasil
def tampilkan_hasil(ET0):
    print(f"\nEvapotranspirasi Referensi (ET₀) = {ET0:.3f} mm/hari")
    print("Kategori:", kategori_et0(ET0))

# Input dari pengguna
print("=== Perhitungan Evapotranspirasi (ET₀) Metode Penman–Monteith ===")
delta = float(input("Masukkan nilai Δ (kPa/°C): "))
Rn = float(input("Masukkan radiasi bersih Rn (MJ/m²/hari): "))
G = float(input("Masukkan fluks panas tanah G (MJ/m²/hari), biasanya 0: "))
gamma = float(input("Masukkan konstanta psikometrik γ (kPa/°C): "))
T = float(input("Masukkan suhu udara rata-rata T (°C): "))
u2 = float(input("Masukkan kecepatan angin u₂ (m/s): "))
es = float(input("Masukkan tekanan uap jenuh eₛ (kPa): "))
ea = float(input("Masukkan tekanan uap aktual eₐ (kPa): "))

# Proses perhitungan
ET0 = hitung_et0(delta, Rn, G, gamma, T, u2, es, ea)

# Output hasil
tampilkan_hasil(ET0)
