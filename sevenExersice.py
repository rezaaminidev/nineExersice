def replace_word(file_path, target_word, replacement):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        modified_content = content.replace(target_word, replacement)
        
        with open(file_path, 'w') as file:
            file.write(modified_content)
        
        print(f"کلمه '{target_word}' با موفقیت به '{replacement}' در فایل {file_path} جایگزین شد.")
    except FileNotFoundError:
        print("فایل مورد نظر یافت نشد.")
    except Exception as e:
        print(f"خطا در اجرای برنامه: {e}")


def main():
    file_path = input("لطفاً نام فایل متنی را وارد کنید: ")
    target_word = input("لطفاً کلمه مورد نظر را برای جایگزینی وارد کنید: ")
    replacement = input("لطفاً کلمه جایگزین را وارد کنید: ")

    replace_word(file_path, target_word, replacement)


if __name__ == "__main__":
    main()
