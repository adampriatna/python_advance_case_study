import re
from datetime import datetime
from functools import wraps


# ==========================================
# KASUS 3: KEAMANAN AKUN DAN AUDIT LOGIN
# ==========================================

class User:
    def __init__(self, username, password):
        self._username = None
        self._password = None

        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError(
                "Username minimal 5 karakter dan hanya huruf/angka."
            )
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password minimal 8 karakter.")
        if not re.search(r"\d", value):
            raise ValueError("Password wajib mengandung angka.")
        self._password = value


# Decorator untuk mencatat audit login
def audit_log(func):
    @wraps(func)
    def wrapper(username, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            hasil = func(username, password)
            status = "BERHASIL" if hasil else "DITOLAK"
            alasan = "" if hasil else "Username atau password salah."
        except ValueError as error:
            hasil = False
            status = "DITOLAK"
            alasan = str(error)

        print(f"\nWaktu   : {waktu}")
        print(f"Username: {username}")
        print(f"Status  : {status}")
        if alasan:
            print(f"Alasan  : {alasan}")

        return hasil

    return wrapper


# Data akun yang terdaftar
akun_terdaftar = {
    "adam123": "rahasia123"
}


@audit_log
def login(username, password):
    # Validasi format menggunakan RegEx
    if not re.fullmatch(r"[A-Za-z0-9]{5,}", username):
        raise ValueError(
            "Format username tidak valid."
        )

    if len(password) < 8:
        raise ValueError(
            "Password terlalu pendek (minimal 8 karakter)."
        )

    if not re.search(r"\d", password):
        raise ValueError(
            "Password wajib mengandung minimal satu angka."
        )

    # Memeriksa kecocokan akun
    if akun_terdaftar.get(username) == password:
        return True

    return False


def main():
    print("=" * 50)
    print("       SISTEM KEAMANAN AKUN")
    print("=" * 50)

    print("\nUJI 1: Username tidak valid")
    login("ad!", "rahasia123")

    print("\nUJI 2: Password terlalu pendek")
    login("adam123", "abc12")

    print("\nUJI 3: Password tidak mengandung angka")
    login("adam123", "rahasiaaja")

    print("\nUJI 4: Login berhasil")
    login("adam123", "rahasia123")

    print("\n" + "=" * 50)
    print("Pengujian selesai.")


if __name__ == "__main__":
    main()