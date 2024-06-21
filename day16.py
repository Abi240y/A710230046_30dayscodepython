# Program konversi suhu dari Celsius ke Fahrenheit dan sebaliknya
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Konversi Suhu:")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == '1':
    suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))
    print(suhu_celsius, "Celsius = ", celsius_to_fahrenheit(suhu_celsius), "Fahrenheit")
elif pilihan == '2':
    suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
    print(suhu_fahrenheit, "Fahrenheit = ", fahrenheit_to_celsius(suhu_fahrenheit), "Celsius")
else:
    print("Pilihan tidak valid.")
