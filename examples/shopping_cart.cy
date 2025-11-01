# Shopping Cart Application - Demonstrates Module System

# Import modules
dari matematika impor tambah, kali
dari utilitas impor huruf_besar

# Define shopping cart class
kelas ShoppingCart:
    fungsi __init__(diri):
        diri.items = []
    
    fungsi tambah_item(diri, nama, harga, jumlah):
        item = {
            "nama": nama,
            "harga": harga,
            "jumlah": jumlah
        }
        diri.items.append(item)
        tulis(f"✓ {huruf_besar(nama)} ditambahkan ke keranjang")
    
    fungsi hitung_total(diri):
        total = 0
        untuk item dalam diri.items:
            subtotal = kali(item["harga"], item["jumlah"])
            total = tambah(total, subtotal)
        kembalikan total
    
    fungsi tampilkan_ringkasan(diri):
        tulis("\n=== RINGKASAN BELANJA ===")
        tulis(f"{'Item':<20} {'Harga':<10} {'Qty':<5} {'Subtotal':<10}")
        tulis("-" * 50)
        
        untuk item dalam diri.items:
            subtotal = kali(item["harga"], item["jumlah"])
            tulis(f"{item['nama']:<20} Rp{item['harga']:<10,} {item['jumlah']:<5} Rp{subtotal:,}")
        
        tulis("-" * 50)
        total = diri.hitung_total()
        tulis(f"{'TOTAL':<36} Rp{total:,}")
        tulis("=" * 50)

# Main program
tulis("🛒 APLIKASI SHOPPING CART")
tulis("Menggunakan Module System CodingYok v2.0")
tulis()

# Create cart
cart = ShoppingCart()

# Add items
cart.tambah_item("Laptop Gaming", 15000000, 1)
cart.tambah_item("Mouse Wireless", 250000, 2)
cart.tambah_item("Keyboard Mechanical", 850000, 1)
cart.tambah_item("Monitor 24 inch", 2500000, 2)

# Show summary
cart.tampilkan_ringkasan()

tulis("\n✨ Terima kasih telah berbelanja!")
