import math

def hitung_arus(P, V, efisiensi):
    I = P / (V * efisiensi)
    return I

def hitung_L(N, A, l):
    mu = 4 * math.pi * 10**-7
    L = (mu * N**2 * A) / l
    return L

def hitung_efisiensi(Pout, Pin):
    eta = (Pout / Pin) * 100
    return eta

def hitung_Pout(Q, h):
    rho = 1000
    g = 9.81
    Pout = (rho * g * Q * h) / 1000
    return Pout
print(" SOAL RESPONSIPRAKTIKUM PYTHON - SISTEM LISTRIK & POMPA AIR ")
print("Pilih perhitungan yang ingin dilakukan:")
print("1. Arus motor pompa")
print("2. Induktansi kumparan starter")
print("3. Efisiensi pompa")
print("4. Daya mekanik keluaran\n")

pilihan = int(input("Masukkan pilihan (1-4): "))
print()

if pilihan == 1:
    print("=== Hitung Arus Motor ===")
    P = float(input("Masukkan daya motor (W): "))
    V = float(input("Masukkan tegangan (V): "))
    ef = float(input("Masukkan efisiensi motor (0–1): "))
    I = hitung_arus(P, V, ef)
    print(f"Arus motor = {I:.3f} A")

    if I < 2:
        print("Motor hemat energi.")
    elif I < 5:
        print("Motor bekerja normal.")
    else:
        print("Motor kelebihan beban.")

elif pilihan == 2:
    print("=== Hitung Induktansi Kumparan ===")
    N = float(input("Masukkan jumlah lilitan (N): "))
    A = float(input("Masukkan luas penampang (m²): "))
    l = float(input("Masukkan panjang kumparan (m): "))
    L = hitung_L(N, A, l)
    print(f"Induktansi = {L:.6f} H")

    if L < 0.1:
        print("Induktansi kecil — respon cepat.")
    elif L < 1:
        print("Induktansi sedang.")
    else:
        print("Induktansi besar — respon lambat.")

elif pilihan == 3:
    print("=== Hitung Efisiensi Pompa ===")
    Pout = float(input("Masukkan daya keluaran (W): "))
    Pin = float(input("Masukkan daya masuk (W): "))
    eta = hitung_efisiensi(Pout, Pin)
    print(f"Efisiensi = {eta:.2f}%")

    if eta < 60:
        print("Efisiensi rendah.")
    elif eta < 85:
        print("Efisiensi sedang.")
    else:
        print("Efisiensi tinggi.")

elif pilihan == 4:
    print("=== Hitung Daya Mekanik Keluaran ===")
    Q = float(input("Masukkan debit air (m³/s): "))
    h = float(input("Masukkan tinggi tekan (m): "))
    Pout = hitung_Pout(Q, h)
    print(f"Daya mekanik = {Pout:.2f} W")

    if Pout < 100:
        print("Pompa ringan — irigasi kecil.")
    elif Pout < 1000:
        print("Pompa sedang — irigasi menengah.")
    else:
        print("Pompa industri — kapasitas besar.")

else:
    print("Pilihan tidak valid. Silakan ulangi.")
