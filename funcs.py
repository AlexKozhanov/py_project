def summ_two_namber(a,b):
    return print(f"Сумма переменных равна {a+b}")

def subtraction_two_namber(a,b):
    return print(f"Разность переменных равна {a - b}")

def main():
    print("Введите переменную a")
    A = int(input())
    print("Введите переменную b")
    B = int(input())
    summ_two_namber(A,B)
    subtraction_two_namber(A,B)

if __name__ == '__main__':
    main()
