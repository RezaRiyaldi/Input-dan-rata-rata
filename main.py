jumlah = 0.0
rata = jumlah
n = int(input("Banyaknya data = "))
for i in range(n):
    x = float(input(f"Data ke - {i + 1} = "))
    jumlah += x
    rata = jumlah/n
print(f"Rata - rata = {rata}")
