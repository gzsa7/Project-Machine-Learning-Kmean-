# Project-Machine-Learning-Kmean-
PENGGUNAAN ALGORITMA K-MEANS DALAM PENGELOMPOKAN INDEKS STANDAR POLUSI UDARA (ISPU) DI PROVINSI DKI JAKARTA, INDONESIA

## 1️⃣ Import Library
Pertama, saya mengimpor beberapa library utama seperti Pandas dan NumPy untuk pengolahan data, Matplotlib dan Seaborn untuk visualisasi, serta StandardScaler dan KMeans dari Scikit-learn untuk proses machine learning.
> Library ini digunakan untuk membentuk satu pipeline machine learning dari awal sampai interpretasi hasil.”*

## 2️⃣ Load dan Persiapan Data
Selanjutnya, data ISPU saya baca dari file CSV. Setelah itu, nama kolom saya seragamkan menjadi huruf kecil dan menghilangkan spasi untuk menghindari kesalahan pemanggilan kolom.
> Tahap ini penting agar proses selanjutnya berjalan konsisten.

## 3️⃣ Pemilihan Fitur dan Imputasi
Kemudian, saya memilih enam fitur polutan utama yaitu PM2.5, PM10, SO2, CO, O3, dan NO2. Kolom kategori ISPU tidak saya sertakan karena K-Means merupakan unsupervised learning.
> Untuk mengatasi missing value, saya menggunakan imputasi median karena median lebih tahan terhadap outlier dibandingkan mean.

## 4️⃣ Standardisasi Data
Setelah data bersih, saya melakukan standardisasi menggunakan StandardScaler. Standardisasi ini mengubah data ke dalam bentuk Z-score.
> Langkah ini sangat penting karena K-Means menggunakan jarak Euclidean, sehingga fitur dengan skala besar tidak boleh mendominasi.

## 5️⃣ Penerapan Algoritma K-Means
Setelah data distandarisasi, saya menerapkan algoritma K-Means dengan jumlah cluster sebanyak tiga.
> Parameter random_state digunakan agar hasil konsisten, dan n_init diset untuk memastikan hasil clustering optimal.
> Hasil dari tahap ini adalah label cluster untuk setiap data.

## 6️⃣ Penggabungan Hasil Cluster
Label cluster yang dihasilkan kemudian saya gabungkan kembali ke data utama. Hal ini memungkinkan saya untuk mengaitkan cluster dengan informasi lain seperti stasiun dan kategori ISPU.

## 7️⃣ Standardisasi CO untuk Visualisasi
Pada tahap visualisasi, saya melakukan standardisasi ulang khusus untuk polutan CO. Tujuannya adalah agar distribusi CO antar cluster bisa dibandingkan secara adil.
> Scaler ini terpisah dari scaler training agar tidak memengaruhi model K-Means.

## 8️⃣ Visualisasi Distribusi CO per Cluster
Saya menggunakan stripplot untuk menampilkan distribusi nilai CO pada setiap cluster, dengan warna yang membedakan stasiun pengukuran.
> Visualisasi ini membantu memahami karakteristik masing-masing cluster secara visual.

## 9️⃣ Distribusi Cluster terhadap ISPU
Selanjutnya, saya menggunakan crosstab untuk melihat hubungan antara cluster hasil K-Means dengan kategori ISPU.
> Analisis ini berfungsi sebagai validasi tidak langsung terhadap hasil clustering.

## 🔟 Statistik Polutan per Cluster
Saya juga menghitung rata-rata nilai polutan asli pada setiap cluster. Statistik ini memudahkan interpretasi secara praktis dan mudah dipahami.

## 1️⃣1️⃣ Distribusi ISPU dalam Persentase
Selain frekuensi, saya menghitung persentase kategori ISPU pada tiap cluster agar perbandingan antar cluster lebih jelas.

## 1️⃣2️⃣ Interpretasi Berbasis Z-Score
Untuk interpretasi yang lebih valid, saya kembali ke ruang data standar, yaitu Z-score, karena K-Means dilatih pada data yang sudah distandarisasi.
> Dari rata-rata Z-score per cluster, saya menentukan polutan yang paling dominan secara relatif terhadap keseluruhan dataset.

## 1️⃣3️⃣ Tabel Interpretasi Akhir
> Tahap terakhir adalah menyusun tabel interpretasi yang berisi cluster, polutan dominan, dan kategori ISPU yang paling sering muncul.”*
> Tabel ini bertujuan untuk menjembatani hasil machine learning dengan pemahaman manusia.
