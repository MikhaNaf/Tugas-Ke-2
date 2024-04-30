#Menentukan Bilangan Ganjil
#Part B
def cetak_kuadrat_ganjil(n):
    for i in range(n):
        if i % 2 != 0: 
            print(i*i)

n = int(input("Masukkan nilai n: "))
cetak_kuadrat_ganjil(n)
