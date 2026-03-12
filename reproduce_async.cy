async fungsi tes_async():
    tulis("Memulai...")
    menunggu async_tidur(1)
    tulis("Selesai setelah 1 detik")

async fungsi main():
    menunggu tes_async()
