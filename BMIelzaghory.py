import pyfiglet
from colorama import Fore

txt = pyfiglet.figlet_format("BMIelzaghory")
print(txt) 

print()
print(Fore.RED + 'Pemilik : ElZaghory')
print('Github : https://github.com/Elzaghory')
print("Program ini untuk mengira BMI secara individu\n")
nama = input("Masukkan Nama Anda : ")
berat = float(input("Masukkan berat(kg) anda : "))
tinggi = float(input("Masukkan tinggi(cm) anda : "))

bmi = berat / (tinggi ** 2 ) *10000

if bmi < 18.5:
    print(f"{nama} kurang berat badan {bmi} BMI")
elif bmi >= 18.5 and bmi < 22.9:
    print(f"{nama} berat badan normal {bmi} BMI")
elif bmi >= 23 and bmi < 30:
    print(f"{nama} berat badan berlebihan {bmi} BMI")    
elif bmi >= 30:
    print(f"{nama} berat badan obesiti {bmi} BMI")    
