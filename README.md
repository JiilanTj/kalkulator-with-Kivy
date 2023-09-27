# Kalkulator Sederhana dengan Kivy

Aplikasi ini adalah kalkulator sederhana yang dibangun dengan menggunakan framework Kivy. Ini memungkinkan pengguna untuk melakukan operasi perhitungan sederhana seperti penjumlahan, pengurangan, perkalian, dan pembagian. Berikut adalah penjelasan singkat tentang bagaimana kode ini bekerja:

1. `CalculatorApp`: Ini adalah kelas utama yang mewarisi dari `App` yang disediakan oleh Kivy. Kelas ini mendefinisikan antarmuka pengguna dan perilaku kalkulator.

2. `build()`: Metode ini digunakan untuk membuat antarmuka pengguna kalkulator. Ini menginisialisasi tampilan kalkulator yang terdiri dari tombol-tombol angka, tombol operasi, tombol "C" (untuk menghapus), dan tombol "=" (untuk menghitung hasil).

3. `on_button_press(self, instance)`: Metode ini dipanggil ketika salah satu tombol di tekan. Ini mengambil teks tombol yang ditekan dan menambahkannya ke tampilan kalkulator.

4. `on_clear(self, instance)`: Metode ini dipanggil ketika tombol "C" ditekan. Ini menghapus semua teks dari tampilan kalkulator.

5. `on_solution(self, instance)`: Metode ini dipanggil ketika tombol "=" ditekan. Ini mencoba menghitung hasil ekspresi matematika yang ada di tampilan kalkulator menggunakan fungsi `eval()` dan menampilkan hasilnya. Jika terjadi kesalahan selama perhitungan, akan ditampilkan pesan "Error".

## Menjalankan Kode

Anda dapat menjalankan kode ini dengan menggunakan interpreter Python yang sudah memiliki library Kivy terinstal. Pastikan Anda sudah menginstal Kivy sebelum menjalankan kode ini. Jika belum, Anda dapat menginstalnya dengan perintah berikut:

```bash
pip install kivy
```

1. Salin kode di atas dan simpan dalam sebuah file dengan ekstensi `.py`.

2. Jalankan file tersebut dengan perintah berikut melalui terminal:

   ```bash
   python nama_file.py
   ```

   Gantilah `nama_file.py` dengan nama file tempat Anda menyimpan kode ini.

## Hasil

Setelah kode dijalankan, jendela aplikasi kalkulator akan muncul. Anda dapat mengklik tombol angka, tombol operasi matematika, tombol "C" untuk menghapus, dan tombol "=" untuk menghitung hasil perhitungan. Hasil perhitungan akan ditampilkan di bagian atas tampilan kalkulator.

Selamat mencoba menggunakan kalkulator sederhana ini!
