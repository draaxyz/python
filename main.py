#komentar

from tokenize import String


print("Hello world")

bendaBerat = "laptop"
print("saya mempunyai benda bennama"+bendaBerat)

#type data di python: 1.string 2.int 3.float 4.boolean

#string

String = "ini tipe data string"
print(String)

#int
int = 10
print("ini tipe data int",+int)

#tipe data float
float = 10,5

#boolean
#terdiri dari false dan true

print("tipe data boolean =",+ 10 > 9)

a = 444
b = 555

print("termasuk tipe data boolean apa?", + a == b)

#operator aritmatika
# (+) (-) (*) (/) (**) (%)

#penjumalahan
print("hasil dari penjumlahan ini adalah =" ,+ a+b)

#pengurangan
print("hasil dari pengurangan ini adalah =" ,+ a-b)

#perkalian
print("hasil dari perkalian ini adalah =" ,+ a*b)

#pembagian
print("hasil dari pembagian ini adalah =" ,+ a/b)

#kuadrat
print("hasil dari kuadrat ini adalah =" ,+ a**b)

#modulus
a = 8
b = 5
print("hasil dari modulus ini adalah =" ,+ a%b)

jarak = 30
waktu_telat = 10
waktu_rill = 60
kecepatan = jarak / waktu_rill * waktu_telat
print("Kecepatan : ", kecepatan , "Km/s")


