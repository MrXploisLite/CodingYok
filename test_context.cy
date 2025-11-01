# Test context manager

tulis("Testing context manager")

kelas MyContext:
    fungsi __enter__(diri):
        tulis("Entering")
        kembalikan diri
    
    fungsi __exit__(diri, a, b, c):
        tulis("Exiting")
        kembalikan salah

tulis("Before with")
dengan MyContext() sebagai ctx:
    tulis("Inside with")
tulis("After with")
