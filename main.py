import random

def generate_random_list(n):
    if n < 0:
        raise ValueError("Кількість елементів не може бути від’ємною")
    return [random.randint(0, 100) for _ in range(n)]

if __name__ == "__main__":
    try:
        n = int(input("Введи кількість елементів у списку: "))
        result = generate_random_list(n)
        print("Згенерований список:", result)
    except ValueError:
        print("Введи ціле додатнє число!")
45