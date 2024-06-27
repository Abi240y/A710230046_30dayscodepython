def hitung_vokal(string):
    vokal = "aiueoAIUEO"
    jumlah_vokal = 0
    
    for char in string:
        if char in vokal:
            jumlah_vokal += 1
    
    return jumlah_vokal

def main():
    input_string = input("Masukkan sebuah kata: ")
    jumlah_vokal = hitung_vokal(input_string)
    print(f"Jumlah huruf vokal dalam kata '{input_string}' adalah: {jumlah_vokal}")

if __name__ == "__main__":
    main()
