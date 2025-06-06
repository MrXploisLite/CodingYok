# Contoh aplikasi web sederhana dengan CodingYok
# File: web_app.cy

tulis("=== APLIKASI WEB CODINGYOK ===\n")

# Data storage sederhana (dalam memori)
data_mahasiswa = []
counter_id = 1

# Fungsi helper untuk generate ID
fungsi generate_id():
    global counter_id
    id_baru = counter_id
    counter_id += 1
    kembalikan id_baru

# Fungsi untuk mencari mahasiswa berdasarkan ID
fungsi cari_mahasiswa(id_mahasiswa):
    untuk mhs dalam data_mahasiswa:
        jika mhs['id'] == id_mahasiswa:
            kembalikan mhs
    kembalikan kosong

# Buat server web
server = buat_server_web('localhost', 8080)

# Route untuk halaman utama
@server.route('/')
fungsi halaman_utama(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistem Mahasiswa CodingYok</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .form-group { margin: 10px 0; }
            label { display: block; margin-bottom: 5px; }
            input, select { padding: 8px; width: 200px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            button:hover { background: #0056b3; }
            .mahasiswa-item { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .error { color: red; }
            .success { color: green; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Sistem Mahasiswa CodingYok</h1>
            
            <h2>Tambah Mahasiswa Baru</h2>
            <form id="formMahasiswa">
                <div class="form-group">
                    <label>Nama:</label>
                    <input type="text" id="nama" required>
                </div>
                <div class="form-group">
                    <label>NIM:</label>
                    <input type="text" id="nim" required>
                </div>
                <div class="form-group">
                    <label>Jurusan:</label>
                    <select id="jurusan">
                        <option value="Teknik Informatika">Teknik Informatika</option>
                        <option value="Sistem Informasi">Sistem Informasi</option>
                        <option value="Teknik Komputer">Teknik Komputer</option>
                        <option value="Manajemen Informatika">Manajemen Informatika</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Semester:</label>
                    <input type="number" id="semester" min="1" max="8" required>
                </div>
                <button type="submit">Tambah Mahasiswa</button>
            </form>
            
            <div id="message"></div>
            
            <h2>Daftar Mahasiswa</h2>
            <div id="daftarMahasiswa">
                <p>Loading...</p>
            </div>
            
            <script>
                // Load mahasiswa saat halaman dimuat
                loadMahasiswa();
                
                // Handle form submission
                document.getElementById('formMahasiswa').addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    const data = {
                        nama: document.getElementById('nama').value,
                        nim: document.getElementById('nim').value,
                        jurusan: document.getElementById('jurusan').value,
                        semester: parseInt(document.getElementById('semester').value)
                    };
                    
                    fetch('/api/mahasiswa', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => response.json())
                    .then(result => {
                        if (result.status === 200) {
                            document.getElementById('message').innerHTML = 
                                '<p class="success">Mahasiswa berhasil ditambahkan!</p>';
                            document.getElementById('formMahasiswa').reset();
                            loadMahasiswa();
                        } else {
                            document.getElementById('message').innerHTML = 
                                '<p class="error">Error: ' + result.message + '</p>';
                        }
                    });
                });
                
                function loadMahasiswa() {
                    fetch('/api/mahasiswa')
                    .then(response => response.json())
                    .then(data => {
                        const container = document.getElementById('daftarMahasiswa');
                        if (data.data.length === 0) {
                            container.innerHTML = '<p>Belum ada data mahasiswa.</p>';
                        } else {
                            let html = '';
                            data.data.forEach(mhs => {
                                html += `
                                    <div class="mahasiswa-item">
                                        <h3>${mhs.nama}</h3>
                                        <p><strong>NIM:</strong> ${mhs.nim}</p>
                                        <p><strong>Jurusan:</strong> ${mhs.jurusan}</p>
                                        <p><strong>Semester:</strong> ${mhs.semester}</p>
                                        <p><strong>Tanggal Daftar:</strong> ${mhs.tanggal_daftar}</p>
                                        <button onclick="hapusMahasiswa(${mhs.id})">Hapus</button>
                                    </div>
                                `;
                            });
                            container.innerHTML = html;
                        }
                    });
                }
                
                function hapusMahasiswa(id) {
                    if (confirm('Yakin ingin menghapus mahasiswa ini?')) {
                        fetch('/api/mahasiswa/' + id, {
                            method: 'DELETE'
                        })
                        .then(response => response.json())
                        .then(result => {
                            if (result.status === 200) {
                                loadMahasiswa();
                                document.getElementById('message').innerHTML = 
                                    '<p class="success">Mahasiswa berhasil dihapus!</p>';
                            }
                        });
                    }
                }
            </script>
        </div>
    </body>
    </html>
    """
    kembalikan html

# API untuk mendapatkan semua mahasiswa
@server.route('/api/mahasiswa', 'GET')
fungsi get_mahasiswa(request):
    kembalikan {
        'status': 200,
        'data': data_mahasiswa,
        'total': panjang(data_mahasiswa)
    }

# API untuk menambah mahasiswa baru
@server.route('/api/mahasiswa', 'POST')
fungsi tambah_mahasiswa(request):
    coba:
        data = request.get('json', {})
        
        # Validasi data
        jika bukan data.get('nama') atau bukan data.get('nim'):
            kembalikan {
                'status': 400,
                'message': 'Nama dan NIM harus diisi'
            }
        
        # Cek NIM duplikat
        untuk mhs dalam data_mahasiswa:
            jika mhs['nim'] == data['nim']:
                kembalikan {
                    'status': 400,
                    'message': 'NIM sudah terdaftar'
                }
        
        # Buat mahasiswa baru
        mahasiswa_baru = {
            'id': generate_id(),
            'nama': data['nama'],
            'nim': data['nim'],
            'jurusan': data.get('jurusan', 'Teknik Informatika'),
            'semester': data.get('semester', 1),
            'tanggal_daftar': tanggal_indonesia()
        }
        
        data_mahasiswa.append(mahasiswa_baru)
        
        kembalikan {
            'status': 200,
            'message': 'Mahasiswa berhasil ditambahkan',
            'data': mahasiswa_baru
        }
    
    kecuali Exception sebagai e:
        kembalikan {
            'status': 500,
            'message': f'Server error: {str(e)}'
        }

# API untuk menghapus mahasiswa
@server.route('/api/mahasiswa/<int:id>', 'DELETE')
fungsi hapus_mahasiswa(request):
    # Extract ID from path (simplified)
    path_parts = pisah('/', request['path'])
    id_mahasiswa = int(path_parts[-1])
    
    untuk i, mhs dalam enumerate(data_mahasiswa):
        jika mhs['id'] == id_mahasiswa:
            data_mahasiswa.pop(i)
            kembalikan {
                'status': 200,
                'message': 'Mahasiswa berhasil dihapus'
            }
    
    kembalikan {
        'status': 404,
        'message': 'Mahasiswa tidak ditemukan'
    }

# API untuk statistik
@server.route('/api/statistik', 'GET')
fungsi get_statistik(request):
    jika panjang(data_mahasiswa) == 0:
        kembalikan {
            'status': 200,
            'data': {
                'total_mahasiswa': 0,
                'per_jurusan': {},
                'per_semester': {}
            }
        }
    
    # Hitung statistik per jurusan
    per_jurusan = {}
    per_semester = {}
    
    untuk mhs dalam data_mahasiswa:
        jurusan = mhs['jurusan']
        semester = mhs['semester']
        
        jika jurusan dalam per_jurusan:
            per_jurusan[jurusan] += 1
        kalau_tidak:
            per_jurusan[jurusan] = 1
        
        jika semester dalam per_semester:
            per_semester[semester] += 1
        kalau_tidak:
            per_semester[semester] = 1
    
    kembalikan {
        'status': 200,
        'data': {
            'total_mahasiswa': panjang(data_mahasiswa),
            'per_jurusan': per_jurusan,
            'per_semester': per_semester
        }
    }

# Tambah beberapa data contoh
tulis("Menambahkan data contoh...")
data_mahasiswa.extend([
    {
        'id': generate_id(),
        'nama': 'Ahmad Fauzi',
        'nim': '12345678',
        'jurusan': 'Teknik Informatika',
        'semester': 5,
        'tanggal_daftar': tanggal_indonesia()
    },
    {
        'id': generate_id(),
        'nama': 'Siti Nurhaliza',
        'nim': '12345679',
        'jurusan': 'Sistem Informasi',
        'semester': 3,
        'tanggal_daftar': tanggal_indonesia()
    },
    {
        'id': generate_id(),
        'nama': 'Budi Santoso',
        'nim': '12345680',
        'jurusan': 'Teknik Komputer',
        'semester': 7,
        'tanggal_daftar': tanggal_indonesia()
    }
])

tulis(str(panjang(data_mahasiswa))
tulis("\nMemulai server web...")
tulis("Buka browser dan akses: http://localhost:8080")
tulis("Tekan Ctrl+C untuk menghentikan server")

# Jalankan server
server.run()
