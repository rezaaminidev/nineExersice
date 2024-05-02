class ReversePhonebook:
    def __init__(self, contacts):
        self.contacts = contacts
        self.reverse_contacts = {v: k for k, v in contacts.items()}

    def get_name(self, number):
        if number in self.reverse_contacts:
            return self.reverse_contacts[number]
        else:
            return "مخاطبی با این شماره تلفن یافت نشد."

    def get_number(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "مخاطبی با این نام یافت نشد."


def main():
    contacts = {
        "آرمان": "09123456789",
        "سارا": "09129876543",
        "علی": "09127654321",
        "نازنین": "09121112233"
    }

    reverse_phonebook = ReversePhonebook(contacts)

    while True:
        print("\n1. دریافت نام براساس شماره تلفن")
        print("2. دریافت شماره تلفن براساس نام")
        print("3. خروج")
        choice = input("لطفاً عدد مربوطه را وارد کنید: ")

        if choice == '1':
            number = input("شماره تلفن را وارد کنید: ")
            name = reverse_phonebook.get_name(number)
            print(f"نام مخاطب: {name}")
        elif choice == '2':
            name = input("نام مخاطب را وارد کنید: ")
            number = reverse_phonebook.get_number(name)
            print(f"شماره تلفن: {number}")
        elif choice == '3':
            print("با تشکر از استفاده شما. خداحافظ!")
            break
        else:
            print("ورودی نامعتبر. لطفاً عدد صحیح بین ۱ تا ۳ را وارد کنید.")


if __name__ == "__main__":
    main()
