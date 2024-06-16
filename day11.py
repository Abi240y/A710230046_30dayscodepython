#program buku telpon
kontak = {}
for i in range(1, 6):
    nama = input('masukkan nama teman {}: '.format(i))
    no_hp = input('masukkan nomor HP teman {}: '.format(i))
    kontak[nama] = no_hp

kata = 'phone book'

print()
print(kata.center(50))
print()
for no, nama in enumerate(kontak, start=1):
    print('{}. [{}] = [{}]'. format(no, nama, kontak[nama]))

