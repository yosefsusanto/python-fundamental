# Sekuensial
"""
print('ibu berkata,"Pergi ke toko"')
print('Budi menjawab, "Baik,apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu, dan jika ada telur beli 6" ')
print('Maka budi pergi ke toko')
print('dan mulai berbelanja')
"""

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587

print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print('Budi mengecek harganya, dan ternyata uangnya cukup')
    if jumlah_telur == 0:
        print('Budi membeli 1 botol susu')
else :
    print('Budi tidak jadi membeli botol susu')

print('Budi pulang ke rumah')
print('Menyerahkan hasilnya kepada ibu')
