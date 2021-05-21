import matematika.geometri2D

def main():
    sisi = 3

    luas = matematika.geometri2D.l_bujursangkar(sisi)

    print("\nBUJUR SANGKAR")
    print(f"Panjang Sisi\t: {sisi}")
    print(f"Luas\t\t: {luas}\n")

if __name__ == "__main__":
    main()