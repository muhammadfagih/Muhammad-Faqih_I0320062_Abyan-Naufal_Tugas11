import geometri2D

p = 10
l = 8

luas = geometri2D.l_persegipanjang(p,l)
kel = geometri2D.k_persegipanjang(p,l)

print("\nPERSEGI PANJANG")
print(f"Panjang\t\t: {p}")
print(f"Lebar\t\t: {l}")
print(f"Luas\t\t: {luas}")
print(f"Keliling\t: {kel}")

jarijari = 3

luas = geometri2D.l_lingkaran(jarijari)
kel = geometri2D.k_lingkaran(jarijari)

print("\nLINGKARAN")
print(f"Jari-Jari\t: {jarijari}")
print(f"Luas\t\t: {luas}")
print(f"Keliling\t: {kel}\n")