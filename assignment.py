# day3 First Assignment

while True:
    menu = input("1) Fahrenheit to Celsius\t2) Celsius to Fahrenheit\t\
    3) Check Prime Number\t4) Specify the Prime Number's range(2 inputs)\t5) Quit program : ")

    #Fahrenheit to Celsius
    if menu == '1':
        fahrenheit = float(input("Input Fahrenheit : "))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')

    # Celsius to Fahrenheit
    elif menu =='2':
        Celsius = float(input("Input Fahrenheit : "))
        print(f'CelsiusQD : {Celsius}C, Fahrenheit : {((Celsius * 9.0/5.0) + 32.0):.4f}F')

    # Check Prime Number
    elif menu == '3':
        number = int(input("Input number : "))
        isPrime = True
        if number < 2:
            print(f"{number} is not prime number")
        else:
            i = 2
            while i < number:
                if number % i == 0:
                    isPrime = False
                    break
                i += 1
        if isPrime:
            print(f"{number} is prime number")
        else:
            print(f"{number} is not prime number")
        print()

    # Specify range
    elif menu == '4':
        prime_list = []
        numbers = input("Input First number and Second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        for number in range(n1, n2 + 1):
            isPrime = True
            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        isPrime = False
                        break
                if isPrime:
                    prime_list.append(str(number)) # number(int)를 string으로 변환하여 리스트에 추가
        prime_str = ", ".join(prime_list) # join으로 list를 string으로 변환
        print(f'{n1}와 {n2} 사이의 소수는 {prime_str} 입니다.')
        print()

    # Quit program
    elif menu == '5':
        print("Terminate program")
        break
    else:
        print("choose number 1 or 2 or 3!")