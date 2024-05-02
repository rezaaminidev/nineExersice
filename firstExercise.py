class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"{name} با شماره تلفن {number} به دفترچه تلفن اضافه شد.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} با موفقیت از دفترچه تلفن حذف شد.")
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"شماره تلفن {name}: {self.contacts[name]}")
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def get_contacts(self):
        print("مخاطبین:")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")


def main():
    phonebook = Phonebook()
    while True:
        print("\n1. افزودن مخاطب")
        print("2. حذف مخاطب")
        print("3. جستجوی مخاطب")
        print("4. نمایش همه مخاطبین")
        print("5. خروج")
        choice = input("لطفاً عدد مربوطه را وارد کنید: ")

        if choice == '1':
            name = input("نام مخاطب را وارد کنید: ")
            number = input("شماره تلفن مخاطب را وارد کنید: ")
            phonebook.add_contact(name, number)
        elif choice == '2':
            name = input("نام مخاطب را وارد کنید: ")
            phonebook.delete_contact(name)
        elif choice == '3':
            name = input("نام مخاطب را وارد کنید: ")
            phonebook.search_contact(name)
        elif choice == '4':
            phonebook.get_contacts()
        elif choice == '5':
            print("با تشکر از استفاده شما. خداحافظ!")
            break
        else:
            print("ورودی نامعتبر. لطفاً عدد صحیح بین ۱ تا ۵ را وارد کنید.")


if __name__ == "__main__":
    main()
