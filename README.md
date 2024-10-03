# Bike Sharing Dashboard

Ini adalah proyek **dashboard analisis penggunaan sepeda** menggunakan **Streamlit**. Aplikasi ini memberikan berbagai visualisasi yang membantu memahami pola penggunaan sepeda berdasarkan cuaca, musim, dan tipe pengguna (casual vs registered).

## Fitur Dashboard
- **Visualisasi Pengaruh Cuaca**: Menampilkan rata-rata penggunaan sepeda berdasarkan kondisi cuaca (cerah, mendung, hujan).
- **Visualisasi Pola Musiman**: Menampilkan pola musiman penggunaan sepeda.
- **Visualisasi Pengguna Casual vs Registered**: Membandingkan rata-rata penggunaan sepeda oleh pengguna kasual dan pengguna terdaftar.

## Persyaratan Sistem
- **Python 3.7+**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**

## Pengaturan Proyek dengan PyCharm
1. **Clone Repository**: Clone repository ini ke direktori lokal Anda.
    ```bash
    https://github.com/aldirohmatakbar/dashboardproject.git
    cd dashboardProject
    ```

2. **Buka Proyek di PyCharm**:
    - Buka PyCharm dan pilih `Open` lalu arahkan ke folder proyek yang baru saja di-clone.

3. **Membuat Environment Virtual (Opsional tapi Disarankan)**:
    - Disarankan untuk menggunakan environment virtual untuk mengelola dependensi.
    - Anda dapat membuat virtual environment langsung dari PyCharm:
        - Buka **File > Settings** di PyCharm.
        - Arahkan ke **Project: [Your Project Name] > Python Interpreter**.
        - Klik ikon roda gigi dan pilih **Add** > **Virtualenv Environment**.
        - Pilih **New environment** dan tentukan direktori untuk environment baru Anda, lalu klik **OK**.

4. **Menginstal Dependensi**:
    - Install semua library yang diperlukan dari **requirements.txt** atau manual.
    
    **Cara 1**: Menggunakan `requirements.txt` (Jika tersedia)
    ```bash
    pip install -r requirements.txt
    ```

    **Cara 2**: Install secara manual di terminal PyCharm:
    ```bash
    pip install streamlit pandas matplotlib seaborn
    ```

5. **Menjalankan Aplikasi Streamlit**:
    - Setelah semua dependensi terinstall, jalankan aplikasi **Streamlit** dengan perintah berikut di terminal PyCharm:
    ```bash
    streamlit run app.py
    ```

