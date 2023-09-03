print("\n======UNDIAN BERHADIAH======\n")
print("ketentuan :\t 10.000 3 x percobaan\t 50.000 17 x percobaan\t 100.000 35 x percobaan\n")
print("DATA DIRI JANGAN SAMPAI SALAH !!!")
name = str(input("\nMASUKAN NAMA ANDA = "))
usia = str(input("MASUKAN USIA ANDA = "))
depo = float(input("MAU DEPO BERAPA ? = Rp"))
print(f"\nNAMA ANDA ={name} ")
print(f"USIA ANDA ={usia} ")
print(f"DEPO ANDA =Rp{depo}00\n")
while True:
    user = input("masukkan angka jitu anda : ")
    angka_jitu = "34" 
    
    if user == angka_jitu:
        print("selamat tebakan angka jitu anda benar")
        break
    else: 
        user != angka_jitu
        print("ayo coba lagi")
        continue