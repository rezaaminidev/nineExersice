class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, info):
        if name in self.contacts:
            self.contacts[name].extend(info)
        else:
            self.contacts[name] = info
        print(f"اطلاعات به مخاطب {name} اضافه شد.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"مخاطب {name} با موفقیت حذف شد.")
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"اطلاعات مخاطب {name}:")
            print(self.contacts[name])
        else:
            print(f"مخاطبی با نام {name} یافت نشد.")

    def get_contacts_by_info(self, info):
        matching_contacts = [name for name, contact_info in self.contacts.items() if info in contact_info]
        if matching_contacts:
            print(f"مخاطبین مرتبط با {info}:")
            for name in matching_contacts:
                print(name)
        else:
            print(f"هیچ مخاطبی با اطلاعات {info} یافت نشد.")


def main():
    phonebook = Phonebook()
    while True:
        print("\n1. افزودن مخاطب")
        print("2. حذف مخاطب")
        print("3. جستجوی مخاطب بر اساس نام")
        print("4. جستجوی مخاطب بر اساس اطلاعات")
        print("5. نمایش همه مخاطبین")
        print("6. خروج")
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
            info = input("اطلاعات مورد نظر را وارد کنید: ")
            phonebook.get_contacts_by_info(info)
        elif choice == '5':
            phonebook.get_contacts()
        elif choice == '6':
            print("با تشکر از استفاده شما. خداحافظ!")
            break
        else:
            print("ورودی نامعتبر. لطفاً عدد صحیح بین ۱ تا ۶ را وارد کنید.")


if __name__ == "__main__":
    main()
