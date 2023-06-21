#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests  # Impor modul requests untuk melakukan permintaan HTTP
import csv  # Impor modul csv untuk memanipulasi file CSV

key = input('masukkan keyword :')  # Meminta input kata kunci dari pengguna
#bisa masukkan key nya sandal

write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))  # Membuka file CSV baru dengan nama file sesuai dengan kata kunci yang dimasukkan
header = ['Nama', 'Harga', 'Alamat']  # Menentukan header file CSV
write.writerow(header)  # Menulis header ke dalam file CSV

url = 'https://api.bukalapak.com/multistrategy-products'  # URL API untuk mengambil data produk
count = 0  # Inisialisasi variabel untuk menghitung jumlah produk

for page in range(1, 3):  # Melakukan pengulangan untuk mengambil beberapa halaman data
    parameter = {
        'keywords': 'sepeda',
        'limit': 50,
        'offset': 50,
        'facet': True,
        'page': 2,
        'shouldUseSeoMultistrategy': False,
        'isLoggedIn': False,
        'show_search_contexts': True,
        'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg3MzE5MjIzLCJuYmYiOjE2ODczMDU2MDMsImlhdCI6MTY4NzMwNTYwMywianRpIjoibHdtTi1ZMktPUzVFSWdEb1hPWkYxQSIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.z79oMtPyds1hFTrwtvlb293DEl8JzCJwK-iux0l7pbdmosAFji9bRZO3EF-FHLJzZytmL3LPd0PnV2ZLRdu7Xy_qW24GFpCBZMyd0qPYQPms3-rlD0PR7mkLf_3rCID5IPWLWTuBn_mEZ-iZi1VHJwVtn2ITOnGe-GA-qH8Nli-YyvZZxJMPTG3bGiHYK7zhqaEeRu-VGVTzKJ0Q2y73QHenucbO_3TQmBFmpo6yRkpiDA95WpqSxKpv1XuZ32AAcZ0FMeokDWu8mq_9TLRTERgVi_Spf8hhDJG6aH18eD8opwT3QG0yeIduCHqA_8MmRHRn8OKk8xEg0dZjioCQJw'
        # Access token untuk otentikasi
    }  # Menentukan parameter untuk permintaan API

    r = requests.get(url, params=parameter).json()  # Mengirim permintaan GET ke API dan mengambil respons dalam format JSON

    products = r['data']  # Mengambil data produk dari respons

    for p in products:  # Melakukan pengulangan untuk setiap produk
        nama = p['name']  # Mengambil nama produk
        harga = p['price']  # Mengambil harga produk
        alamat = p['store']['address']['city']  # Mengambil alamat toko

        count += 1  # Menambah jumlah produk

        print('No:', count, 'nama:', nama, 'harga:', harga, 'alamat', alamat)  # Menampilkan informasi produk di layar

        write = csv.writer(open('Hasil/{}.csv'.format(key), 'a', newline=''))  # Membuka file CSV dalam mode append
        data = [nama, harga, alamat]  # Membuat data produk
        write.writerow(data)  # Menulis data produk ke dalam file CSV


# In[2]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv'.format(key), 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Mengabaikan header
    for row in reader:
        data.append(row)

# Mengambil kolom harga
harga = [float(row[1]) for row in data]

# Mengatur posisi x pada sumbu x
posisi_x = range(1, len(harga) + 1)

# Membuat line chart
plt.plot(posisi_x, harga)
plt.xlabel('Nomor Produk')
plt.ylabel('Harga')
plt.title('Line Chart Harga Produk')
plt.show()


# In[3]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv'.format(key), 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Mengabaikan baris header
    for row in reader:
        data.append(row)

# Mengambil data alamat dan harga
alamat = [row[2] for row in data]
harga = [float(row[1]) for row in data]

# Membuat bar chart
plt.bar(alamat, harga)
plt.xlabel('Alamat')
plt.ylabel('Harga')
plt.title('Bar Chart Alamat vs Harga')

plt.xticks(rotation=90)  # Memutar label alamat agar tidak tumpang tindih
plt.tight_layout()  # Menyesuaikan layout

plt.show()  # Menampilkan grafik


# In[4]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Mengabaikan header
    for row in reader:
        data.append(row)

# Mengumpulkan data alamat dan harga
alamat = []
harga = []
for row in data:
    alamat.append(row[2])  # Kolom alamat
    harga.append(float(row[1]))  # Kolom harga (dikonversi ke float)

# Membuat histogram
plt.figure(figsize=(10, 6))
plt.hist(harga, bins=10, edgecolor='black')  # Ubah nilai bins sesuai kebutuhan
plt.xlabel('Harga')
plt.ylabel('Jumlah Produk')
plt.title('Histogram Harga Produk')
plt.grid(True)

plt.show()


# In[5]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Membuat dictionary untuk menghitung jumlah harga berdasarkan alamat
harga_per_alamat = {}
for row in data:
    alamat = row[2]
    harga = int(row[1])
    if alamat in harga_per_alamat:
        harga_per_alamat[alamat] += harga
    else:
        harga_per_alamat[alamat] = harga

# Mengambil data alamat dan harga
alamat = list(harga_per_alamat.keys())
harga = list(harga_per_alamat.values())

# Membuat pie chart
plt.pie(harga, labels=alamat, autopct='%1.1f%%')
plt.title('Persentase Harga berdasarkan Alamat')

# Agar pie chart menjadi lingkaran
plt.axis('equal')  

# mencetak pie chart
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv('Hasil/{}.csv'.format(key))

# Mendapatkan kolom 'Alamat' dan 'Harga'
alamat = data['Harga']
harga = data['Alamat']

# Membuat scatter plot
plt.scatter(harga, alamat)
plt.title('Scatter Alamat dan Harga')

# Memberikan label sumbu x dan y
plt.xlabel('Harga')
plt.ylabel('Alamat')

# Menampilkan scatter plot
plt.show()


# In[7]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Mengabaikan baris header
    for row in reader:
        data.append(row)

# Mengambil data alamat dan harga
alamat = [row[2] for row in data]
harga = [float(row[1]) for row in data]

# Membuat bar chart
plt.bar(alamat, harga)
plt.xlabel('Alamat')
plt.ylabel('Harga')
plt.title('Bar Chart Alamat vs Harga')

plt.xticks(rotation=90)  # Memutar label alamat agar tidak tumpang tindih
plt.tight_layout()  # Menyesuaikan layout

plt.savefig('Hasil/bar chart.jpg')  # Menyimpan diagram ke dalam file JPG

plt.show()  # Menampilkan grafik


# In[8]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('Hasil/sepeda.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Membuat dictionary untuk menghitung jumlah harga berdasarkan alamat
harga_per_alamat = {}
for row in data:
    alamat = row[2]
    harga = int(row[1])
    if alamat in harga_per_alamat:
        harga_per_alamat[alamat] += harga
    else:
        harga_per_alamat[alamat] = harga

# Mengambil data alamat dan harga
alamat = list(harga_per_alamat.keys())
harga = list(harga_per_alamat.values())

# Membuat pie chart
plt.pie(harga, labels=alamat, autopct='%1.1f%%')
plt.title('Persentase Harga berdasarkan Alamat')
plt.axis('equal')  # Agar pie chart menjadi lingkaran

# Menyimpan diagram sebagai file JPG
plt.savefig('Hasil/pie chart.jpg', format='jpg')

# Menampilkan diagram
plt.show()


# In[ ]:




