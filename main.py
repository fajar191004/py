print("DATA MASYARAKAT PUJI DADI")
while True:
    nama = input("masukan nama anda: ")
    tbt = input("masukan tanggal lahir anda: ")
    tbt1 = input("masukan bulan lahir anda: ")
    tbt2 = input("masukan tahun lahir anda: ")
    kelamin = input("masukan jenis kelamin anda: ")
    jk = input("masukan jumlah keluarga anda: ")
    supir = input("apakah data sudah benar (y/n) :")
    if supir == "n":
        print("HARAP ISI DENGAN BENAR !!!")
        continue

    else:
        supir != "n" 
        print(f"\nnama anda: {nama}")
        print(f"tanggal-bulan-lahir anda: {tbt}-{tbt1}-{tbt2}")
        print(f"jenis kelamin: {kelamin}")
        print(f"jumlah keluarga anda: {jk}")
        break
print("\nTerimah kasih telah mencoba...")