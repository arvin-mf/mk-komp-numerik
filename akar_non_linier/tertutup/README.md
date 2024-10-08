# Biseksi
## Teori
Metode Biseksi bekerja dengan menetapkan dua titik absis awal, disebut $a$ dan $b$, dengan nilai $f(a)$ dan $f(b)$ yang terpisah oleh sumbu-x. Dengan kata lain, terdapat sebuah titik potong dengan sumbu-x di antara kedua titik tersebut.

Memeriksa apakah $a$ dan $b$ dipisahkan oleh sumbu-x dapat dilakukan dengan mengalikan ordinat keduanya. Jika terpisah oleh sumbu-x maka hasil kalinya pasti bernilai negatif karena salah satu titik berada di bawah sumbu-x (ordinatnya lebih kecil dari 0) dan yang lainnya di atas sumbu-x.

$a$ dan $b$ harus memenuhi: $f(a) \times f(b) < 0$

![Ilustrasi metode biseksi](../../assets/akar_non_linier/biseksi_ilustrasi.png)
(p pada ilustrasi di atas adalah titik tengah a dan b)<br>
*Gambar dari: [Sumber Gambar](https://www.researchgate.net/publication/367361304_Some_naive_and_computationally_polished_techniques_to_approximate_the_roots_of_equations)*

Kemudian kita menandai titik tengah antara dua absis tersebut, lalu menggunakan titik tersebut beserta salah satu titik sebelumnya dengan syarat masih mengapit titik potong yang sedang dicari. Demikian dilakukan terus-menerus hingga semakin mendekati titik potong tersebut.

Titik tengah = $(a + b) \over 2$

## Percobaan
Program akan meminta tiga (3) buah masukan.
- Masukan pertama adalah float untuk batas error yang diinginkan
- Dua masukan berikutnya adalah float sebagai nilai `a` dan `b`

Contoh masukan: `0.001`, `3.0`, dan `4.0`

![Tampilan hasil dari pemanggilan function biseksi](../../assets/akar_non_linier/biseksi.png)

# Regula Falsi
## Teori

Metode Regula Falsi juga diawali dengan memilih dua titik dengan nilai $f(x)$ yang dipisahkan oleh sumbu-x. Perbedaanya dengan Metode Biseksi adalah prinsip penentuan titik $c$ berikutnya.

|  | Biseksi | Regula Falsi | Metode Terbuka |
| --- | :---: | :---: | :---: |
| Nilai acuan yang dibutuhkan [^1] | $a$, $b$ | $a$, $b$ | $x_n$ |
| Titik acuan baru di iterasi berikutnya | titik tengah $a$ dan $b$ | titik potong garis penghubung $f(a)$ dan $f(b)$ dengan sumbu-x | *di chapter lain* |

[^1]: Adapun nilai batas error selalu dibutuhkan dalam semua metode untuk menjadi terminus dari iterasi metode

Pada Metode Regula Falsi, titik berikutnya diambil dari perpotongan garis hubung antara $f(a)$ dan $f(b)$ dengan sumbu-x.

![Ilustrasi metode regula falsi](../../assets/akar_non_linier/regula_falsi_ilustrasi.png)
( $g(x)$ pada ilustrasi di atas adalah garis penghubung antara $f(a)$ dan $f(b)$ )<br>
*Gambar dari: [Sumber Gambar](https://www.researchgate.net/publication/343057501_Advanced_Engineering_Mathematics_-_Numerical_Methods)*

$g(x)$ atau garis penghubung antara $f(a)$ dan $f(b)$ dapat dicari persamaannya dengan cara seperti berikut.
> misalkan nilai $a$ pertama adalah $a_0$ dan nilai $b$ pertama adalah $b_0$

$g_1(x)$ pada gambar ilustrasi adalah garis penghubung antara titik A dan titik B. Titik A adalah $(a_0, f(a_0))$ dan titik B adalah $(b_0, f(b_0))$.
<br>
$x^*$ merupakan titik potong $g_1(x)$ dengan sumbu-x.

Segitiga $[(x^*,0), (b_0, 0), (b_0, f(b_0))]$ dengan segitiga $[(a_0,f(a_0)), (b_0, f(a_0)), (b_0, f(b_0))]$ adalah pasangan segitiga sebangun. Dari kesebangunan ini, kita dapatkan bahwa perbandingan tinggi dan alas pada kedua segitiga tersebut adalah sama.

$$\frac{f(b_0) - 0}{b_0 - x^p} = \frac{f(b_0) - f(a_0)}{b_0 - a_0}$$

Yang kita perlu cari adalah $x^p$ (untuk menjadi titik acuan di iterasi berikutnya).

$$
\begin{aligned}
\qquad \qquad \frac{f(b_0)}{b_0 - x^p} &= \frac{f(b_0) - f(a_0)}{b_0 - a_0}\\
\quad f(b_0)(b_0 - a_0) &= (b_0 - x^p)(f(b_0) - f(a_0))\\
\quad f(b_0)(b_0 - a_0) &= b_0(f(b_0) - f(a_0)) - x^p(f(b_0) - f(a_0))\\
x^p(f(b_0) - f(a_0)) &= b_0(f(b_0) - f(a_0)) - f(b_0)(b_0 - a_0)\\
x^p(f(b_0) - f(a_0)) &= \cancel{b_0f(b_0)} - b_0f(a_0) - \cancel{b_0f(b_0)} + a_0f(b_0)\\
\end{aligned}
$$

$$x^p = \frac{a_0f(b_0) - b_0f(a_0)}{f(b_0) - f(a_0)} \text{ atau } x^p = \frac{b_0f(a_0) - a_0f(b_0)}{f(a_0) - f(b_0)}$$

## Percobaan

Program akan meminta tiga (3) buah masukan.
- Masukan pertama adalah float untuk batas error yang diinginkan
- Dua masukan berikutnya adalah float sebagai nilai `a` dan `b`

Contoh masukan: `0.001`, `3.0`, dan `4.0`

![Tampilan hasil dari pemanggilan function biseksi](../../assets/akar_non_linier/regula_falsi.png)

#
**Catatan Tambahan**<br>
Gunakan angka dengan nilai $f(x)$ tidak terlalu besar (mencapai ribuan). Program hanya menerapkan *tab* sederhana, tidak menyesuaikan panjang kata sebelumnya.

# Referensi
Dey, Shubhajit. (2023). Some naive and computationally polished techniques to approximate the roots of equations. [Link](https://www.researchgate.net/publication/367361304_Some_naive_and_computationally_polished_techniques_to_approximate_the_roots_of_equations)

Wafi, Moh. (2019). Advanced Engineering Mathematics - Numerical Methods. [Link](https://www.researchgate.net/publication/343057501_Advanced_Engineering_Mathematics_-_Numerical_Methods)