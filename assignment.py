#(32°F − 32) × 5/9 = 0°C

#(0°C × 9/5) + 32 = 32°F

while True:
    menu = input("1) Fahrenheit to Celsius  2) Celsius to Fahrenheit  3) Quit program : ")
    if menu == '1':
        fahrenheit = float(input("Input Fahrenheit : "))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
        break
    elif menu =='2':
        Celsius = float(input("Input Fahrenheit : "))
        print(f'Celsius : {Celsius}C, Fahrenheit : {((Celsius * 9.0/5.0) + 32.0):.4f}F')
        break
    elif menu == '3':
        print("Terminate program")
        break
    else:
        print("choose number 1 or 2 or 3!")
