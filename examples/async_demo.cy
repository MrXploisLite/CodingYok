# Demo Async/Await functionality in CodingYok v5.0

async fungsi main():
    tulis("🚀 Mulai program async...")
    tulis("⏰ Tidur async selama 1 detik...")
    menunggu async_tidur(1)
    tulis("✅ Async operation selesai!")
    hasil = menunggu async_hitung(5)
    tulis(f"Hasil async_hitung: {hasil}")

async fungsi async_hitung(nilai):
    menunggu async_tidur(0.5)
    kembalikan nilai * 2