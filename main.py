def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Zero Division!")
    return a / b


def main():
    a = add_numbers(1, 2)
    b = multiply_numbers(3, 4)
    print(divide_numbers(b, a))


if __name__ == "__main__":
    main()
