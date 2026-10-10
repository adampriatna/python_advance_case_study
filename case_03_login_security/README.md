Studi Kasus 3 — Sistem Keamanan Akun dan Audit Login

Deskripsi

Program ini menerapkan validasi kredensial pengguna dan pencatatan aktivitas login. Program menguji beberapa kondisi login gagal dan login berhasil menggunakan Python.

Konsep Python yang Digunakan

- Class dan Object: Class "User" digunakan untuk merepresentasikan akun pengguna.
- Property: "@property" dan setter digunakan untuk mengakses serta memvalidasi atribut username dan password.
- Regular Expression (RegEx): Memvalidasi username agar minimal 5 karakter dan hanya terdiri dari huruf atau angka.
- Validasi Password: Password harus memiliki minimal 8 karakter dan mengandung setidaknya satu angka.
- Decorator: "@audit_log" mencatat waktu, username, status login, dan alasan penolakan.
- Exception Handling: Menangani kesalahan validasi menggunakan "ValueError" agar program tetap dapat menjalankan pengujian berikutnya.

Skenario Pengujian

1. Username tidak valid: Login ditolak karena format username tidak sesuai.
2. Password terlalu pendek: Login ditolak karena password kurang dari 8 karakter.
3. Password tanpa angka: Login ditolak karena password tidak mengandung angka.
4. Login berhasil: Login diterima ketika username dan password sesuai dengan akun terdaftar.

Cara Menjalankan

Buka terminal pada folder utama proyek, kemudian jalankan:

"python case_03_login_security/main.py"

Bukti Output

File "output.png" berisi bukti hasil pengujian program, termasuk tiga kondisi login ditolak dan satu kondisi login berhasil.