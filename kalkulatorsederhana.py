def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1':
            hasil = angka1 + angka2
            operasi = '+'
        elif pilihan == '2':
            hasil = angka1 - angka2
            operasi = '-'
        elif pilihan == '3':
            hasil = angka1 * angka2
            operasi = '*'
        elif pilihan == '4': 
            if angka2 == 0:
                print("Error! Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = angka1 / angka2
            operasi = '/'

        print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

kalkulator()