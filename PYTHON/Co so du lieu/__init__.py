import hashlib
import os

# File lưu trữ thông tin tài khoản
ACCOUNTS_FILE = "accounts.txt"

# Hàm mã hóa mật khẩu bằng SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hàm kiểm tra file lưu trữ
def check_accounts_file():
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "w") as file:
            file.write("")

# Hàm đăng ký tài khoản mới
def register_account():
    username = input("Nhập tên người dùng: ").strip()
    password = input("Nhập mật khẩu: ").strip()

    # Kiểm tra nếu tên người dùng đã tồn tại
    with open(ACCOUNTS_FILE, "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(":")
            if stored_username == username:
                print("Tên người dùng đã tồn tại. Vui lòng chọn tên khác!")
                return

    # Lưu tài khoản vào file
    hashed_password = hash_password(password)
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    print("Đăng ký thành công!")

# Hàm đăng nhập
def login():
    username = input("Nhập tên người dùng: ").strip()
    password = input("Nhập mật khẩu: ").strip()
    hashed_password = hash_password(password)

    # Kiểm tra thông tin đăng nhập
    with open(ACCOUNTS_FILE, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if stored_username == username and stored_password == hashed_password:
                print("Đăng nhập thành công!")
                return
    print("Tên người dùng hoặc mật khẩu không chính xác!")

# Hàm chính
def main():
    check_accounts_file()
    while True:
        print("\n=== Quản Lý Tài Khoản ===")
        print("1. Đăng ký tài khoản mới")
        print("2. Đăng nhập")
        print("3. Thoát")
        choice = input("Chọn một tùy chọn: ").strip()

        if choice == "1":
            register_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại!")

if __name__ == "__main__":
    main()

