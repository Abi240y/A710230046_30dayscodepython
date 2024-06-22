def next_day(day):
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    index = days_of_week.index(day)
    return days_of_week[(index + 1) % 7]

today = input("Masukkan hari ini (dalam Bahasa Indonesia): ")
print("Hari berikutnya adalah:", next_day(today))
