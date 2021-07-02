# nomor 1
print("===============================================")
print('NOMOR 1')
print("===============================================")

import psycopg2

#establishing the connection
try :
      conn = psycopg2.connect(
         database="latihan", user='postgres', password='easy', 
         host='localhost', port= '5433'
      )
      print('sukses')
except :
   print('gagal')

cursor = conn.cursor()
cursor.execute("SELECT * FROM _offices ORDER BY country, state, city")

rows =cursor.fetchall()
print(rows)
print("===============================================")
print('NOMOR 2')
print("===============================================")


# nomor 2
cursor.execute("SELECT customernumber FROM _customers")
total_compeny = cursor.fetchall()
print(len(total_compeny))
print("===============================================")
print('NOMOR 3')
print("===============================================")


# nomor 3
cursor.execute("SELECT sum (amount) FROM _payments")
price = cursor.fetchall()
print(price)
print("===============================================")
print("NOMOR 4")
print("===============================================")


# nomor 4
cursor.execute("SELECT productline FROM _productlines WHERE productline @@ to_tsquery('Cars') ")
cars = cursor.fetchall()
print(cars)
print("===============================================")
print("NOMOR 5")
print("===============================================")


# nomor 5
cursor.execute("SELECT sum(amount) FROM _payments WHERE paymentdate @@ to_tsquery('2004-10-28')")
tot_okt = cursor.fetchall()
print(tot_okt)
print("===============================================")
print("NOMOR 6")
print("===============================================")


# nomor 6
cursor.execute("SELECT amount FROM _payments WHERE amount > 100000")
pay_greater = cursor.fetchall()
print(pay_greater)
print("===============================================")
print("NOMOR 7")
print("===============================================")


# nomor 7
cursor.execute("SELECT productline FROM _products ")
prod_line = cursor.fetchall()
print(prod_line)
print("===============================================")
print("NOMOR 8")
print("===============================================")


# nomor 8
cursor.execute("SELECT count(distinct productline) FROM _products ")
jenis = cursor.fetchall()
print(jenis)
print("===============================================")
print("NOMOR 9")
print("===============================================")



# nomor 9
cursor.execute("SELECT min(amount) FROM _payments")
minimum = cursor.fetchall()
print(minimum)
print("===============================================")
print("NOMOR 10")
print("===============================================")

# nomor 10
cursor.execute("SELECT (customernumber,checknumber) FROM _payments WHERE amount > 5000")
pay_5000 = cursor.fetchall()
print(pay_5000)
