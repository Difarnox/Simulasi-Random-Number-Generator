import matplotlib.pyplot as plt

# Fungsi LCG untuk menghasilkan angka acak
def lcg(seed, a, c, m, n):
    results = []
    Z = seed
    for i in range(1, n + 1):
        Z_prev = Z
        Z = (a * Z + c) % m
        U = Z / m
        rumus = f"({a} * {Z_prev} + {c}) mod {m}"
        results.append([i, Z_prev, rumus, Z, round(U, 3)])
    return results

# Parameter LCG
seed = 42  # Nilai awal
a = 1664525  # Multiplikator
c = 1013904223  # Increment
m = 37  # Modulus
n = 1000  # Jumlah simulasi

# Hasil simulasi
results = lcg(seed, a, c, m, n)

# Tampilkan tabel hasil (hanya 20 iterasi pertama untuk kejelasan)
print(f"{'i':<3} | {'Zi-1 (Bilangan Sebelumnya)':<28} | {'Rumus Zi = (a.Zi-1 + c) mod m':<45} | {'Zi (Bilangan Acak)':<20} | {'Ui = Zi/m (Bilangan Acak Seragam)':<30}")
print("-" * 130)
for row in results[:20]:
    print(f"{row[0]:<3} | {row[1]:<28} | {row[2]:<45} | {row[3]:<20} | {row[4]:<30}")

# Visualisasi distribusi hasil roulette
roulette_results = [row[3] for row in results]
plt.hist(roulette_results, bins=range(37), edgecolor='black', density=True)
plt.title("Distribusi Angka Roulette")
plt.xlabel("Angka Roulette")
plt.ylabel("Frekuensi Relatif")
plt.grid(True)
plt.show()