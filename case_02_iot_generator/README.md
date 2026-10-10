Studi Kasus 2 — Streaming Data Sensor IoT

Deskripsi

Program ini mensimulasikan pembacaan suhu dari sensor IoT secara bertahap. Data suhu diproses satu per satu tanpa menampung seluruh hasil pembacaan ke dalam list baru.

Kategori Suhu

- Dingin: suhu di bawah 20°C.
- Normal: suhu dari 20°C sampai 30°C.
- Panas: suhu di atas 30°C.

Konsep Python yang Digunakan

- Generator Function: menggunakan "yield" untuk menghasilkan data suhu secara bertahap.
- Iterator Pattern: menggunakan "next()" untuk mengambil nilai berikutnya dari generator.
- Efisiensi Memori: data diproses satu per satu tanpa menyimpan seluruh hasil pembacaan dalam list besar.

Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Buka file "main.py" di folder ini.
3. Jalankan program menggunakan tombol Run di VS Code, atau jalankan perintah berikut di terminal:

python main.py

Hasil Program

Program menampilkan 10 pembacaan suhu sensor beserta kategorinya di terminal.

Bukti eksekusi tersedia pada file "output.png" di folder ini.