print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
print("1 perkalian")
print("2.pembagian")
l = 1
e = input("Masukkan model matematika yang diinginkan 1/2 :")
o = int(input("Menampilkan table matematika dari angka:"))
if(e=="1"):    
    while l <= 10:
        print(o,'x',l,'=',o*l)
        l = l+1
        if l == 11:
            break
elif(e=="2"):
    while l<= 10:
        print(o,':',l,'=',o/l)
        l=l+1
        if l==11:
            break
else:
    print("pilihan tidak tersedia, jangan ngasal!")