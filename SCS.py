def hitung_S(CN):

    return (25400 / CN) - 254

def hitung_Q(P, S):
    if P <= 0.2 * S:
        Q = 0
    else:
        Q = ((P - 0.2 * S) ** 2) / (P + 0.8 * S)
    return Q

S = hitung_S(float(input("Masukkan nilai Curve Number (CN): ")))
Q = hitung_Q(float(input("Masukkan curah hujan (mm): ")),S)
print("Nilai Q = ", Q, " mm")

# ===== Interpretasi Nilai S =====
if S < 50:
    print("Kapasitas tampungan tanah sangat kecil — tanah cenderung kedap air.")
elif S < 150:
    print("Kapasitas tampungan tanah sedang — sebagian air terserap, sebagian menjadi limpasan.")
else:
    print("Kapasitas tampungan tanah besar — tanah mampu menahan banyak air.")

# ===== Interpretasi Nilai Q =====
if Q == 0:
    print("Tidak ada limpasan — air hujan sepenuhnya terserap.")
elif Q < 10:
    print("Limpasan ringan — kondisi tanah baik.")
elif Q < 50:
    print("Limpasan sedang — potensi genangan lokal.")
else:
    print("Limpasan tinggi — risiko banjir meningkat.")