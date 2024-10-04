def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        user_input = int(input("Nhập một số nguyên: "))
        if is_prime(user_input):
            print(f"{user_input} là số nguyên tố.")
        else:
            print(f"{user_input} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
