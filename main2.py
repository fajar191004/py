print("*** program matematika ***")

while True:
    user1 = input("masukan angka pertama: ")
    if not user1.isdigit():
        print("Angka pertama harus berupa angka!")
        continue

    user2 = input("masukan pilihan bilangan(+,x,-,:): ")
    user3 = input("masukan angka kedua: ")
    if not user3.isdigit():
        print("Angka kedua harus berupa angka!")
        continue

    user1 = int(user1)
    user3 = int(user3)

    if user2 in ["+", "x", "-", ":"]:
        if user2 == "+":
            hasil = user1 + user3
        elif user2 == "x":
            hasil = user1 * user3
        elif user2 == "-":
            hasil = user1 - user3
        else:
            hasil = user1 / user3

        print(f"hasil {user1} {user2} {user3} = {hasil}")
    else:
        print("pilihan bilangan wajib di isi dengan benar !!!")

    user5 = input("mau lanjut (y/n): ")
    if user5.lower() == "n":
        break

print("Terima kasih telah mencoba")
