# Test file for v2.0 features
tulis("Testing CodingYok v2.0")
tulis("=" * 30)

# Test list comprehension
angka = [1, 2, 3, 4, 5]
kuadrat = [x * x untuk x dalam angka]
tulis("List comprehension:")
tulis(kuadrat)

# Test dict comprehension
dict_test = {x: x * 2 untuk x dalam rentang(1, 4)}
tulis("Dict comprehension:")
tulis(dict_test)

# Test set
set_test = {1, 2, 2, 3, 3}
tulis("Set (removes duplicates):")
tulis(set_test)

# Test generator
fungsi count_up(n):
    untuk i dalam rentang(n):
        hasilkan i

tulis("Generator test:")
untuk num dalam count_up(5):
    tulis(num)

# Test pattern matching
fungsi test_match(x):
    cocokkan x:
        kasus 1:
            tulis("Satu")
        kasus 2:
            tulis("Dua")
        kasus _:
            tulis("Lainnya")

tulis("Pattern matching test:")
test_match(1)
test_match(2)
test_match(99)

tulis("=" * 30)
tulis("All tests completed!")
