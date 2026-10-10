# ==========================================
# KASUS 2: STREAMING DATA SENSOR IoT
# ==========================================

def sensor_suhu():
    """Menghasilkan data suhu satu per satu."""
    data_suhu = [
        18.5, 19.8, 21.0, 23.5, 27.0,
        29.5, 31.2, 33.0, 25.5, 17.8
    ]

    for suhu in data_suhu:
        yield suhu


def kategori_suhu(suhu):
    """Menentukan kategori berdasarkan suhu."""
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    else:
        return "Panas"


def main():
    print("=" * 48)
    print("       MONITORING SUHU SENSOR IoT")
    print("=" * 48)

    # Mengambil data secara bertahap menggunakan generator
    pembacaan = sensor_suhu()

    for nomor in range(1, 11):
        suhu = next(pembacaan)
        status = kategori_suhu(suhu)

        print(
            f"Pembacaan {nomor:02d} | "
            f"Suhu: {suhu:5.1f}°C | "
            f"Status: {status}"
        )

    print("=" * 48)
    print("Selesai: 10 pembacaan sensor diproses.")


if __name__ == "__main__":
    main()