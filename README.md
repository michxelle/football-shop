**Nama aplikasi/shop = Footballed Co.**

**Link aplikasi PWS = https://laudya-michelle-footballshop.pbp.cs.ui.ac.id/**

------------------------------------------------------------------------
TUGAS 2
------------------------------------------------------------------------

**Step-by-step membuat proyek Django baru**

1. Membuat direktori baru Bernama football-shop agar semua file proyek tersimpan rapi dalam satu folder khusus
2. Membuka terminal dan masuk ke direktori football-shop
3. Membuat virtual environment dengan perintah *python -m venv env* agar dependencies proyek ini terpisah dari Python global yang ada di laptop
4. Mengaktifkan virtual environment dengan perintah *env\\Scripts\\activate*
5. Menginstall dependencies yang ada dalam file requirements.txt dengan perintah *pip install -r requirements.txt* supaya library yg dibutuhkan langsung tersedia (tidak perlu command install satu per satu)
6. Membuat proyek Django dengan nama football\_shop dengan perintah django-admin startproject football\_shop .
7. Pada direktori utama, saya membuat file .env dan menambahkan konfigurasi PRODUCTION=false pada file tersebut
8. Pada direktori utama, saya membuat file .env.prod dan melakukan konfigurasi production. SCHEMA yang digunakan adalah tugas\_individu
9. Melakukan beberapa konfigurasi pada settings.py, seperti library, konfigurasi ALLOWED\_HOSTS, PRODUCTION, dan DATABASES
10. Melakukan migrasi database dengan perintah python manage.py migrate
11. Menonaktifkan virtual environment karena proyek Django sudah berhasil dibuat



**Step-by-step mengunggah proyek ke repositori GitHub**

1. Membuat repositori GitHub Bernama football-shop
2. Menjalankan perintah git init di terminal direktori lokal football-shop untuk menjadikan folder ini sebagai repositori git
3. Menambahkan berkas README.md
4. Menambahkan berkas .gitignore dan mencantumkan berkas-berkas yang tidak akan di-push ke repo GitHub
5. Menghubungkan repositori lokal dengan repositori GitHub
6. Membuat branch utama bernama master
7. Melakukan add, commit, dan push dari direktori repositori lokal



**Step-by-step membuat aplikasi main**

1. Mengaktifkan virtual environment
2. Membuat aplikasi baru bernama main dengan perintah *python manage.py startapp main*
3. \[Dalam settings.py] Menambahkan 'main' ke INSTALLED\_APPS agar aplikasi main terdaftar dalam proyek



**Step-by-step membuat model pada aplikasi main dengan nama Product**

1. \[Dalam models.py] Membuat variable list CATEGORY\_CHOICES yang berisi tuple
2. \[Dalam models.py] Mendefinisikan model dengan nama Product yang memiliki atribut name, price, description, thumbnail, category, is\_featured, stock, dan brand
3. Melakukan python manage.py makemigrations untuk membuat migrasi model dan python manage.py migrate untuk menerapkan migrasi ke database local



**Step-by-step membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**

1. Membuat direktori baru, yaitu templates, dalam direktori main
2. \[Dalam direktori templates] Membuat file baru untuk tampilan web, yaitu main.html, yang berisi nama aplikasi, nama, dan kelas
3. \[Dalam views.py] Membuat function show\_main yang menerima request dan me-render tampilan main.html



**Step-by-step membuat sebuah routing pada urls.py aplikasi main**

1. Membuat file urls.py dalam direktori main
2. \[Dalam urls.py direktori main] Menambahkan routing dengan path('', show\_main, name='show\_main')



**Melakukan routing pada proyek**

1. \[Dalam urls.py direktori football-shop] Meng-import include dari django.urls
2. \[Dalam urls.py direktori football-shop] Menambahkan path *path('', include('main.urls'))* untuk aplikasi main agar URL diarahkan ke rute yang didefinisikan dalam urls.py main, yaitu ke fungsi show\_main



Sebelum di-deploy ke PWS, proyek saya push ke repositori GitHub terlebih dahulu.



Step-by-step membuat deployment ke PWS

1. Mengakses web PWS dan login dengan SSO
2. Membuat proyek baru Bernama footballshop
3. Saya masuk ke project details dan membuka environs
4. \[Dalam environs] Membuka raw editor, paste isi file .env.prod, lalu update all variables
5. \[Dalam settings.py] Menambahkan URL deployment PWS pada ALLOWED\_HOSTS sehingga menjadi seperti ini -> *ALLOWED\_HOSTS = \["localhost", "127.0.0.1", "laudya-michelle-footballshop.pbp.cs.ui.ac.id"]*
6. Melakukan git add, commit, dan push lagi ke repositori GitHub
7. Menjalankan command berikut :

   * git remote add pws https://pbp.cs.ui.ac.id/laudya.michelle/footballshop
   * git branch -M master
   * git credential-cache exit
   * git push pws master



**Link bagan Django request-response:** 

https://drive.google.com/file/d/16utn4HcQdcFPHNyEqhr61_2M9_B3rNSu/view?usp=sharing



**Penjelasan tentang kaitan urls.py, views.py, models.py, dan berkas html:**

* urls.py -> menentukan rute request dari client
* views.py -> mengatur logika aplikasi, ambil/olah data, lalu pilih template
* models.py -> menghubungkan aplikasi dengan database
* HTML (template) -> menampilkan data ke client sebagai response



**Peran settings.py dalam proyek Django**

File settings.py dalam proyek Django berperan sebagai pusat konfigurasi utama yang mengatur berbagai aspek aplikasi, seperti pengaturan database, daftar aplikasi yang digunakan, middleware, pengaturan keamanan,dll. Semua pengaturan global yang memengaruhi perilaku proyek Django didefinisikan di settings.py sehingga perubahan pada file ini akan berdampak pada seluruh aplikasi.



**Cara kerja migrasi database di Django**

Mekanisme migrasi database di Django bekerja dengan cara menerjemahkan perubahan yang dilakukan pada model python ke dalam bentuk perubahan struktur database. Ketika model diubah, perintah *makemigrations* digunakan untuk membuat file migrations yang berisi instruksi perubahan database, lalu perintah *migrate* dijalankan untuk menerapkan perubahan tersebut ke database secara otomatis.



**Alasan framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak**

Menurut saya, Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena framework ini menyediakan banyak fitur bawaan yang memudahkan pemula. Selain itu, dokumentasinya sangat lengkap dan komunitasnya besar sehingga mudah untuk mencari bantuan atau referensi. Struktur proyeknya juga jelas dan penggunaan prinsip best practice membuat Django sangat cocok untuk memahami konsep dasar pengembangan aplikasi web modern secara terstruktur dan efisien.

**Feedback untuk asdos**
Asdos sangat helpful dan selalu siap siaga di discord setiap ada sesi tutorial.

------------------------------------------------------------------------
TUGAS 3
------------------------------------------------------------------------
**Step by step menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID**
1.	[Dalam views.py] Meng-import HttpResponse, serializers, dan model Product yang telah dibuat sebelumnya
2.	[Dalam views.py] Membuat fungsi show_xml yang menerima parameter request. Fungsi ini akan mengambil semua objek dari model Product dan mengonversinya ke format XML
3.	[Dalam views.py] Membuat fungsi show_json yang menerima parameter request. Fungsi ini akan mengambil semua objek dari model Product dan mengonversinya ke format JSON
4.	[Dalam views.py] Membuat fungsi show_xml_by_id yang menerima parameter request dan product_id. Fungsi ini akan mencari satu objek Product yang memiliki primary key sesuai dengan product_id lalu mengonversinya jadi format XML.
5.	[Dalam views.py] Membuat fungsi show_json_by_id yang menerima parameter request dan product_id. Fungsi ini akan mencari satu objek Product yang memiliki primary key sesuai dengan product_id lalu mengonversinya jadi format JSON.

**Step by step membuat routing URL untuk masing-masing views yang telah ditambahkan**
1.	[Dalam urls.py direktori main] Meng-import keempat fungsi yang baru saja dibuat, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id
2.	[Dalam urls.py direktori main] Menambahkan 4 path() baru, yaitu untuk endpoint /xml/, /json/, /xml/str:product_id/, dan /json/str:product_id/

**Step by step membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek**
1.	[Dalam direktori utama] Membuat direktori templates dan membuat file base.html di dalamnya. Berkas ini digunakan sebagai base template yang dapat digunakan sebagai kerangka umum untuk halaman web lain di dalam proyek
2.	[Dalam main/settings.py] Mengubah isi key 'DIRS' pada TEMPLATES menjadi 'DIRS': [BASE_DIR / 'templates'] agar base.html terdeteksi sebagai file template
3.	[Dalam direktori main] Membuat file baru Bernama forms.py untuk membuat struktur form yang dapat menerima data Product baru
4.	[Dalam main/forms.py] Meng-import ModelForm dan Product
5.	[Dalam main/forms.py] Membuat kelas ProductForm yang menerima parameter ModelForm
6.	[Dalam main/forms.py] Membuat kelas Meta di dalam ProductForm yang digunakan untuk memberi tahu Django terkait Model dan field yang akan dimasukkan ke form
7.	[Dalam main/views.py] Meng-import redirect, get_object_or_404, dan ProductForm
8.	[Dalam main/views.py] Menambahkan Product.objects.all() pada fungsi show_main untuk mengambil semua objek Product yang ada di database
9.	[Dalam main/views.py] Menambahkan 'product_list': product_list pada context fungsi show_main
10.	[Dalam main/views.py] Menambahkan fungsi create_product yang berfungsi untuk menghasilkan form yang memungkinkan penambahan data Product secara otomatis saat data di-submit dari form
11.	[Dalam main/views.py] Menambahkan fungsi show_product. Fungsi ini memakai get_object_or_404(Product, pk=product_id) untuk mengambil objek Product yang sesuai dengan primary key. Jika objek tidak ditemukan, maka halaman 404 akan ditampilkan
12.	[Dalam main/urls.py] Meng-import fungsi create_product dan show_product, lalu menambahkan path() baru dengan endpoint /create_product/ dan /product/str:product_id/
13.	[Dalam main/templates/main.html] Mengubah kode yang ada di main.html agar meng-extend base.html
14.	[Dalam main/templates/main.html] Mengisi block content dengan menambahkan kode untuk tombol "+ Add Product" yang akan redirect ke halaman form dan menambahkan kode untuk tombol "View Details" untuk setiap Product yang akan redirect ke halaman detail product atau objek

**Step by step membuat halaman form untuk menambahkan objek model pada app sebelumnya**
1.	[Dalam main/templates] Membuat file HTML baru bernama create_product.html yang meng-extend base.html. File ini berfungsi sebagai template halaman form
2.	[Dalam football_shop/settings.py] Menambahkan entri url proyek pws pada CSRF_TRUSTED_ORIGINS

**Step by step membuat halaman yang menampilkan detail dari setiap data objek model**
1.	[Dalam main/templates] Membuat file HTML baru bernama product_detail.html yang meng-extend base.html. File ini berfungsi sebagai template halaman detail produk

**POSTMAN (link screenshot)**
https://drive.google.com/drive/folders/17Tgljj_z2FgR5oWvHLN5RMejGMoLYJx8?usp=sharing

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data delivery memungkinkan pertukaran informasi antara server dan client, atau antarsistem yang berbeda. Dengan adanya data delivery, aplikasi dapat menampilkan informasi yang dapat diperbarui sesuai kebutuhan pengguna secara real-time dan memfasilitasi integrasi dengan layanan atau aplikasi lain. Tanpa mekanisme pengiriman data yang baik, platform akan susah beradaptasi dengan kebutuhan pengguna yang terus berubah dan tidak dapat berkomunikasi secara efektif dengan sistem-sistem lain

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya, JSON lebih baik dibandingkan XML terutama untuk kebutuhan pengembangan aplikasi web yang modern. Saya menganggap JSON lebih baik daripada XML karena JSON memiliki struktur yang lebih sederhana dan mudah dipahami baik oleh manusia maupun mesin. JSON juga terintegrasi dengan JavaScript sehingga proses parsing dan manipulasi data menjadi lebih cepat dan efisien. Sementara itu, XML cenderung lebih kompleks formatnya sehingga kurang praktis untuk digunakan. Oleh karena itu, JSON menjadi lebih populer dan lebih banyak digunakan dibanding XML

**Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form sudah sesuai dengan aturan validasi yang ditentukan pada model atau form tersebut. Method ini akan mengembalikan/me-return nilai True jika data valid. Jika ada kesalahan, method akan mengembalikan/me-return nilai False. Kita membutuhkan method is_valid() karena dengan menggunakan method tersebut, kita dapat memastikan bahwa hanya data yang benar dan sesuai yang akan diproses atau disimpan ke database. Hal ini akan mencegah terjadinya error atau data yang tidak konsisten

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan Cross Site Request Forgery (CSRF). Token ini memastikan bahwa request yang dikirim ke server benar-benar berasal dari pengguna yang sah dan bukan dari pihak ketiga yang berusaha menyalahgunakan sesi pengguna. Jika csrf_token tidak ditambahkan, penyerang dapat membuat form palsu di situs lain yang mengirim request ke aplikasi kita atas nama pengguna tanpa sepengetahuan mereka. Hal ini dapat dimanfaatkan oleh penyerang untuk melakukan aksi berbahaya, seperti mengubah data atau melakukan transaksi tanpa izin dari pengguna.

**Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
Feedback untuk asdos di tutorial 2 : Asdos sangat membantu karena mereka stand-by di voice room discord dan siap membantu mahasiswa jika ada kendala