class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, info):
        self.contacts[name] = info
        print(f"{name} با اطلاعات زیر به دفترچه تلفن اضافه شد:")
        print(info)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} با موفقیت از دفترچه تلفن حذف شد.")
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"اطلاعات مخاطب {name}:")
            print(self.contacts[name])
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def get_contacts(self):
        print("مخاطبین:")
        for name, info in self.contacts.items():
            print(f"{name}: {info}")


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
            address = input("آدرس مخاطب را وارد کنید: ")
            phone = input("شماره تلفن مخاطب را وارد کنید: ")
            email = input("آدرس ایمیل مخاطب را وارد کنید: ")
            age = input("سن مخاطب را وارد کنید: ")
            mobile = input("شماره موبایل مخاطب را وارد کنید: ")
            info = [address, phone, email, age, mobile]
            phonebook.add_contact(name, info)
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
