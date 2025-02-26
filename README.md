# Dokumentasi Proyek Brute Force Tester

## 1. Pendahuluan
Tools ini dibuat untuk menguji keamanan endpoint autentikasi dengan mencoba kombinasi username dan password menggunakan metode brute force.

## 2. Struktur Direktori
```
bruteforce-tester/
│── bruteforce_tester/       # Direktori utama aplikasi
│   │── __init__.py          # Menjadikan direktori ini sebagai package
│   │── config.py            # Konfigurasi endpoint, headers, dll.
│   │── wordlist.py          # Modul untuk menangani wordlist username/password
│   │── request_handler.py    # Modul untuk menangani request
│   │── response_analyzer.py  # Modul untuk menganalisis response
│   │── proxy_manager.py      # Modul untuk mengatur proxy
│   │── brute_force.py        # Modul utama brute force
│── logs/                     # Folder untuk menyimpan log hasil testing
│── reports/                  # Folder untuk menyimpan laporan hasil testing
│── tests/                    # Folder untuk unit testing
│   │── test_brute_force.py    # Unit test untuk brute force
│── requirements.txt           # Daftar dependensi
│── run.py                     # Entry point untuk menjalankan aplikasi
│── README.md                  # Dokumentasi proyek
```

## 3. Penjelasan Modul

### 3.1. `config.py`
Berisi konfigurasi dasar aplikasi, termasuk:
- **PROXY_LIST**: Daftar proxy yang dapat digunakan.
- **URL**: Target URL yang akan diuji.
- **HEADERS**: Header HTTP standar.
- **REQUEST_TIMEOUT**: Timeout untuk request.

### 3.2. `wordlist.py`
Mengelola daftar username dan password yang digunakan dalam brute force attack.
- Memuat wordlist dari file atau menggunakan daftar default.
- Mengatasi file yang tidak ditemukan dengan menampilkan peringatan.

### 3.3. `request_handler.py`
Mengirim request HTTP POST ke endpoint login dengan kombinasi username dan password.
- Menggunakan pustaka `requests` untuk komunikasi HTTP.
- Memungkinkan pengiriman header tambahan.

### 3.4. `response_analyzer.py`
Menganalisis response dari server untuk menentukan apakah percobaan login berhasil.
- Mengecek apakah response memiliki status 200 dan mengandung kata kunci tertentu, seperti `dashboard`.

### 3.5. `proxy_manager.py`
Mengatur penggunaan proxy dalam brute force attack.
- Mengambil daftar proxy dan memastikan hanya menggunakan proxy yang valid.
- Melakukan pengecekan terhadap proxy sebelum digunakan.

### 3.6. `brute_force.py`
Modul utama yang menangani eksekusi brute force attack dengan fitur:
- Menggunakan `ThreadPoolExecutor` untuk menjalankan attack secara bersamaan.
- Menggunakan daftar username dan password dari `wordlist.py`.
- Mendukung penggunaan proxy dari `proxy_manager.py`.
- Menyimpan log hasil attack.

### 3.7. `run.py`
Entry point untuk menjalankan aplikasi dengan konfigurasi yang telah ditentukan.
- Menginisialisasi `BruteForceTester` dengan URL target dan opsi penggunaan proxy.

### 3.8. `test_brute_force.py`
Unit test untuk memastikan `response_analyzer.py` bekerja dengan benar.
- Menggunakan `unittest` untuk melakukan pengujian otomatis.

## 4. Cara Penggunaan
### 4.1. Persiapan Lingkungan
Pastikan Python dan pustaka yang dibutuhkan telah diinstal dengan menjalankan:
```sh
pip install -r requirements.txt
```

### 4.2. Menjalankan Brute Force Tester
```sh
python run.py
```

Jika ingin menggunakan proxy, ubah `use_proxy` menjadi `True` di `run.py`:
```python
use_proxy = True
```

## 5. Logging dan Laporan
- Hasil attack disimpan di folder `logs/`.
- Jika ingin melihat laporan hasil testing, bisa diakses di `reports/`.

## 6. Penutup
Proyek ini digunakan untuk tujuan pengujian keamanan dan tidak boleh digunakan untuk aktivitas ilegal. Pastikan Anda memiliki izin sebelum melakukan pengujian keamanan terhadap sistem yang bukan milik Anda.

