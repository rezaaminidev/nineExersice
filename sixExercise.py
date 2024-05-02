def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"محتوای فایل {source_file} با موفقیت در فایل {destination_file} کپی شد.")
    except FileNotFoundError:
        print("فایل مورد نظر یافت نشد.")
    except Exception as e:
        print(f"خطا در اجرای برنامه: {e}")


def main():
    source_file = input("لطفاً نام فایل مبدأ را وارد کنید: ")
    destination_file = input("لطفاً نام فایل مقصد را وارد کنید: ")

    copy_file(source_file, destination_file)


if __name__ == "__main__":
    main()
