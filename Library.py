
import os

class Library:
    def __init__(self):
        self.dosya_adı = "books.txt"
        self.dosya_olustur()
        self.kitaplari_listele()

    def dosya_olustur(self):
        if not os.path.exists(self.dosya_adı):
            with open(self.dosya_adı, "w") as dosya:
                pass  

    def kitaplari_listele(self):
        try:
            with open(self.dosya_adı, "r") as dosya:
                for line in dosya:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found.")

    def kitap_ekle(self):
        kitap_adi = input("Enter book title: ")
        yazar_adi = input("Enter author name:")
        yayin_tarihi = input("Enter the publication date: ")
        sayfa_sayisi = input("Enter the number of pages: ")

        with open(self.dosya_adı, "a+") as dosya:
            dosya.write(f"{kitap_adi}, {yazar_adi}, {yayin_tarihi}, {sayfa_sayisi}\n")
        print(f" The book titled '{kitap_adi} - {yazar_adi}' has been added successfully.")        

    def kitap_sil(self):
        silinecek_kitap_adi = input("Enter the title of the book you want to delete: ")

        if os.path.exists(self.dosya_adı):
            with open(self.dosya_adı, "r") as dosya:
                kitaplar = dosya.readlines()

            bulundu = False
            with open(self.dosya_adı, "w") as dosya:
                for kitap in kitaplar:
                    if kitap.split(',')[0].strip() == silinecek_kitap_adi:
                        bulundu = True
                    else:
                        dosya.write(kitap)

            if bulundu:
                print(f"The book '{silinecek_kitap_adi}' was successfully deleted.")
            else:
                print(f"The book titled '{silinecek_kitap_adi}' could not be found.")
        else:
            print(f"The book titled '{silinecek_kitap_adi}' could not be found. Please check the book name and try again.")


    def main(self):
        while True:
            print("***** MENU *****")
            print("1) List Books\n2) Add Book\n3) Remove Book\nQ) Quit")
            secim = input("Please enter an option (1-3): ")

            if secim == "1":
                self.kitaplari_listele()
            elif secim == "2":
                self.kitap_ekle()
            elif secim == "3":
                self.kitap_sil()
            elif secim.upper() == "Q":
                print("The program is closing. Have a nice day!")
                break
            else:
                print(f"Invalid option. Please enter a number between 1-3 (Q).")

if __name__ == "__main__":
    library = Library()
    library.main()


                             

                    

