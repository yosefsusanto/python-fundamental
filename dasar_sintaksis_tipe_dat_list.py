daftar_buku = ['Seven Habits','How to Influence People','First Things First','4DX',"You are d'Best"]
print("Tampilkan variable daftar_buku")
print(daftar_buku)

print('\nProses semua dengan for in')
for book in daftar_buku:
    print(book)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Vol 2',-313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('Kembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits','How to Influence People','First Things First','4DX',"You are d'Best"]
print('Tambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits','How to Influence People','First Things First','4DX',"You are d'Best"]
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku = ['Seven Habits','How to Influence People','First Things First','4DX']
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

