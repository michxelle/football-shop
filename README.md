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

------------------------------------------------------------------------
TUGAS 4
------------------------------------------------------------------------

**Step by step mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya**
1. [Dalam views.py] Meng-import UserCreationForm dan messages,authenticate, login, AuthenticationForm, dan logout 
2. [Dalam views.py] Membuat fungsi register yang menerima parameter request. Fungsi ini akan menampilkan form registrasi dan memproses data yang di-submit dari form tersebut
3. Membuat file register.html di dalam direktori main/templates yang berfungsi sebagai template halaman registrasi
4. [Dalam views.py] Membuat fungsi login_user yang menerima parameter request. Fungsi ini akan menampilkan form login dan memproses data yang di-submit dari form tersebut
5. Membuat file login.html di dalam direktori main/templates yang berfungsi sebagai template halaman login
6. [Dalam views.py] Membuat fungsi logout_user yang menerima parameter request. Fungsi ini akan mengakhiri sesi login pengguna dan mengarahkan mereka kembali ke halaman login
7. [Dalam main.html] Menambahkan tombol "Logout" yang akan redirect ke halaman login
8. [Dalam main/urls.py] Meng-import fungsi register, login_user, dan logout_user
9. [Dalam main/urls.py] Menambahkan path() baru dengan endpoint /register/, /login/, dan /logout/

**Step by step menghubungkan model Product dengan User**
1. [Dalam models.py] Meng-import User dari django.contrib.auth.models
2. [Dalam models.py] Menambahkan field user pada model Product untuk menghubungkan setiap produk dengan pengguna yang membuatnya
3. Melakukan "python manage.py makemigrations" untuk membuat migrasi model dan "python manage.py migrate" untuk menerapkan migrasi ke database local
4. [Dalam views.py] Mengubah fungsi create_product, yaitu save(commit = False), lalu menambahkan atribut user dengan request.user sebelum menyimpan objek Product ke database
5. [Dalam views.py] Meng-import login_required dari django.contrib.auth.decorators
6. [Dalam views.py] Menambahkan decorator @login_required di atas fungsi show_main agar hanya pengguna yang sudah login yang dapat mengakses halaman utama
7. [Dalam views.py] Menambahkan filter user=request.user pada Product.objects.all() di dalam fungsi show_main agar aplikasi punya 2 opsi untuk menampilkan produk, yaitu menampilkan semua produk atau hanya produk milik user yang sedang login
8. [Dalam main.html] Menambahkan tombol di atas daftar produk yang memungkinkan pengguna untuk memilih antara "All Products" atau "My Products"
9. [Dalam product_detail.html] Menampilkan nama user yang membuat produk pada halaman detail produk
10. [Dalam forms.py] Mengganti fields = '__all__' pada kelas Meta di dalam ProductForm dan menjadi exclude = ['user'] pada kelas Meta di dalam ProductForm agar field user tidak ditampilkan pada form

**Step by step menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi**
1. [Dalam views.py] Meng-import HttpResponseRedirect, reverse, dan datetime
2. [Dalam views.py] Menambahkan cookies last_login pada fungsi login_user yang berisi waktu saat pengguna berhasil login
3. [Dalam views.py] Menambahkan 'last_login' pada context fungsi show_main
4. [Dalam views.py] Membuat fungsi logout_user menghapus cookies last_login saat pengguna logout
5. [Dalam main.html] Menampilkan username pengguna yang sedang login dan waktu last_login pada halaman utama aplikasi

**Step by step membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal**
1. Mengaktifkan virtual environment
2. Menjalankan server dengan perintah "python manage.py runserver"
3. Membuka halaman registrasi
4. Membuat dua akun pengguna dengan mengisi form registrasi. Akun pertama dengan username "user1" dan akun kedua dengan username "user2". Password untuk kedua akun adalah "mysecurepassword123"
5. Melakukan login dengan akun pertama
6. Menambahkan tiga data dummy produk menggunakan form yang telah dibuat sebelumnya
7. Melakukan logout
8. Melakukan login dengan akun kedua
9. Menambahkan tiga data dummy produk menggunakan form yang telah dibuat sebelumnya
10. Melakukan logout

**Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**
Django AuthenticationForm adalah sebuah form yang disediakan oleh Django untuk menangani proses autentikasi pengguna, yaitu login. Form ini sudah memiliki field standar, seperti username dan password, serta metode validasi yang memastikan bahwa data yang dimasukkan sesuai dengan kredensial yang ada di database. Kelebihan dari AuthenticationForm adalah kemudahan penggunaannya karena sudah terintegrasi dengan sistem autentikasi Django sehingga developer tidak perlu membuat form login dari awal. Selain itu, form ini juga sudah dilengkapi dengan fitur keamanan. Namun, kekurangannya adalah keterbatasan dalam kustomisasi tampilan dan fungsionalitas form. Jika aplikasi membutuhkan fitur login yang lebih kompleks atau tampilan yang sangat spesifik, developer perlu membuat form kustom sendiri.


**Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?**
Perbedaan antara autentikasi dan otorisasi adalah:
- Autentikasi adalah proses verifikasi identitas pengguna, yaitu memastikan bahwa pengguna adalah pengguna yang sebenarnya. Contohnya adalah proses login di mana pengguna memasukkan username dan password untuk membuktikan identitasnya.
- Otorisasi adalah proses menentukan hak akses atau izin yang dimiliki oleh pengguna setelah mereka terautentikasi. Contohnya adalah menentukan apakah pengguna yang sudah login memiliki izin untuk mengakses halaman tertentu atau melakukan tindakan tertentu dalam aplikasi.

Django mengimplementasikan kedua konsep tersebut melalui sistem autentikasi dan otorisasi bawaan. Untuk autentikasi, Django menyediakan model User, form login (AuthenticationForm), dan mekanisme session untuk melacak status login pengguna. Untuk otorisasi, Django menggunakan sistem permissions dan groups yang memungkinkan developer untuk mengatur hak akses pengguna berdasarkan peran atau grup tertentu. Dengan demikian, setelah pengguna terautentikasi, Django dapat memeriksa apakah mereka memiliki izin yang diperlukan untuk mengakses sumber daya tertentu dalam aplikasi.

**Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**
Kelebihan session:
- Lebih aman karena data disimpan di server sehingga tidak mudah diakses atau dimanipulasi oleh pengguna.
- Dapat menyimpan data yang lebih besar dibandingkan cookies karena tidak ada batasan ukuran seperti pada cookies.
- Dapat menyimpan data kompleks seperti objek atau array.

Kekurangan session:
- Membutuhkan penyimpanan di server. Hal ini dapat menjadi beban jika ada banyak pengguna.
- Session akan hilang jika server di-restart atau jika pengguna menutup browser (tergantung pada konfigurasi).

Kelebihan cookies:
- Data disimpan di sisi klien sehingga tidak membebani server.
- Dapat bertahan lebih lama (tergantung pada pengaturan masa berlaku) sehingga dapat digunakan untuk menyimpan preferensi pengguna.
- Mudah diakses oleh aplikasi web untuk keperluan tertentu.

Kekurangan cookies:
- Kurang aman karena data disimpan di sisi klien dan dapat dimanipulasi oleh pengguna.
- Ada batasan ukuran data yang dapat disimpan (sekitar 4KB).
- Cookies dikirimkan dengan setiap request ke server. Hal ini dapat menambah overhead pada komunikasi jaringan. Overhead adalah tambahan data yang harus dikirimkan dalam setiap permintaan HTTP yang dapat memperlambat kinerja aplikasi web, terutama jika cookies berukuran besar atau jika ada banyak cookies yang dikirimkan.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**
Penggunaan cookies tidak selalu aman secara default dalam pengembangan web karena cookies dapat diakses dan dimanipulasi oleh pengguna. Risiko potensial yang harus diwaspadai termasuk pencurian cookies (cookie theft) melalui serangan Cross-Site Scripting (XSS) atau Cross-Site Request Forgery (CSRF), serta risiko penyalahgunaan data yang disimpan dalam cookies. 

Untuk mengatasi risiko tersebut, Django menyediakan beberapa mekanisme keamanan, seperti:
- Menyediakan opsi HttpOnly pada cookies yang mencegah akses cookies melalui JavaScript sehingga mengurangi risiko pencurian cookies melalui XSS.
- Menyediakan opsi Secure pada cookies yang memastikan cookies hanya dikirim melalui koneksi HTTPS sehingga melindungi data dari penyadapan.
- Menggunakan CSRF tokens untuk melindungi aplikasi dari serangan CSRF.
- Menyediakan pengaturan untuk mengatur masa berlaku cookies sehingga cookies tidak bertahan lebih lama dari yang diperlukan.

------------------------------------------------------------------------
TUGAS 5
------------------------------------------------------------------------

**Step by step mengimplementasikan fungsi untuk menghapus dan mengedit product**
1. [Dalam views.py] Membuat fungsi edit_product yang menerima parameter request dan product_id. Fungsi ini akan menampilkan form yang sudah terisi dengan data produk yang akan diedit dan memproses data yang di-submit dari form tersebut
2. [Dalam views.py] Membuat fungsi delete_product yang menerima parameter request dan product_id. Fungsi ini akan menghapus produk yang sesuai dengan product_id dari database
3. [Dalam main/urls.py] Meng-import fungsi edit_product dan delete_product
4. [Dalam main/urls.py] Menambahkan path() baru dengan endpoint /product/str:product_id/edit/ dan /product/str:product_id/delete/
5. [Dalam edit_product.html] Membuat file HTML baru bernama edit_product.html yang meng-extend base.html. File ini berfungsi sebagai template halaman form edit produk
6. [Dalam main.html] Menambahkan tombol "Edit" dan "Delete" yang akan redirect ke halaman edit produk
7. [Dalam main.html] Mengadakan konfirmasi sebelum menghapus produk

**Step by step mengustomisasi desain halaman login, register, tambah product, edit product, dan detail product menggunakan CSS atau CSS framework (Tailwind)**
1.	[Dalam direktori utama] Membuat direktori static di dalamnya
2.	[Dalam direktori static] Membuat direktori css di dalamnya
3.	[Dalam direktori static/css] Membuat file styles.css yang berisi kode CSS untuk mengatur tampilan halaman web
4. [Dalam settings.py] Menambahkan middleware WhiteNoiseMiddleware ke dalam MIDDLEWARE agar file static dapat diakses
5. [Dalam settings.py] Menambahkan STATIC_URL, STATICFILES_DIRS, dan STATIC_ROOT agar file static dapat diakses
6. [Dalam base.html] Menambahkan link ke file styles.css agar semua halaman yang meng-extend base.html dapat menggunakan file CSS tersebut
7.	[Dalam setiap file HTML] Menambahkan class CSS pada tag HTML 
8. [Dalam styles.css] Menambahkan custom CSS untuk mengatur tampilan form, tombol, dan layout.

**Step by step Kustomisasi halaman daftar product menjadi lebih menarik dan responsive**
1. [Dalam main.html] Mengubah struktur HTML untuk menampilkan produk dalam bentuk grid
2. [Dalam main.html] Menambahkan class CSS pada elemen grid untuk mengatur tampilannya
3. Membuat file product_card.html di dalam direktori templates yang berisi kode HTML untuk menampilkan informasi produk dalam bentuk card
4. [Dalam product_card.html] Menambahkan class CSS pada elemen card untuk mengatur tampilannya
5. [Dalam main.html] Menggunakan include dalam for loop untuk memasukkan product_card.html ke dalam main.html sehingga setiap produk ditampilkan dalam bentuk card

**Step by step untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut**
1. [Dalam product_card.html] Menambahkan tombol "Edit" dan "Delete" pada setiap card produk
2. [Dalam product_card.html] Menambahkan link pada tombol "Edit" dan "Delete" yang mengarah ke fungsi edit_product dan delete_product

**Step by step membuat navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop yang ada hamburger menu pada tampilan mobile**
1. Membuat file navbar.html di dalam direktori templates yang berisi kode HTML untuk menampilkan navigation bar
2. [Dalam navbar.html] Menambahkan kode untuk tampilan desktop dan mobile, termasuk hamburger menu untuk tampilan mobile
3. [Dalam base.html] Menggunakan include untuk memasukkan navbar.html ke dalam base.html

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
Urutan prioritas pengambilan CSS selector adalah sebagai berikut:
1. Inline CSS (menggunakan atribut style pada elemen HTML)
2. ID selectors (menggunakan tanda # diikuti dengan nama ID)
3. Class selectors (menggunakan tanda . diikuti dengan nama class)
4. Element selectors (menggunakan nama elemen HTML seperti div, p, h1, dll)
5. Universal selector (menggunakan tanda *)
Jika terdapat konflik antara beberapa selector, maka selector dengan prioritas lebih tinggi yang akan diterapkan. Jika dua selector memiliki prioritas yang sama, maka yang terakhir didefinisikan dalam kode CSS yang akan diterapkan.

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**
Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas situs web menyesuaikan diri dengan berbagai ukuran layar dan perangkat yang digunakan oleh pengguna. Dengan semakin beragamnya perangkat yang digunakan untuk mengakses internet, seperti smartphone, tablet, laptop, dan desktop, responsive design memastikan bahwa pengalaman pengguna tetap optimal tanpa perlu membuat versi terpisah untuk setiap jenis perangkat. Hal ini akan meningkatkan aksesibilitas, SEO (Search Engine Optimization), dan kepuasan pengguna.

Contoh aplikasi yang sudah menerapkan responsive design adalah Google. Aplikasi ini menyesuaikan tampilannya dengan baik pada berbagai perangkat sehingga pengguna dapat dengan mudah mengakses dan berinteraksi dengan konten aplikasi tanpa terjadinya masalah dengan tampilan aplikasi.

Sebaliknya, contoh aplikasi yang belum menerapkan responsive design adalah SIAK-NG (Sistem Informasi Akademik UI). Jika diakses melalui smartphone, tampilan SIAK-NG sering kali terlalu kecil, elemen-elemen tidak menyesuaikan layar, dan pengguna harus melakukan zoom manual untuk membaca informasi atau menekan tombol. Hal ini membuat pengalaman pengguna menjadi kurang nyaman, terutama bagi mahasiswa yang sering mengakses SIAK-NG melalui perangkat mobile. Kurangnya responsive design pada aplikasi seperti ini dapat mengurangi aksesibilitas dan menyulitkan pengguna dalam mendapatkan informasi yang dibutuhkan.

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
Perbedaan antara margin, border, dan padding adalah:
- Margin adalah ruang di luar border elemen yang memisahkan elemen tersebut dari elemen lain di sekitarnya. Margin digunakan untuk mengatur jarak antar elemen.
- Border adalah garis yang mengelilingi elemen dan memisahkan padding dari margin. Border digunakan untuk memberikan batas visual pada elemen.
- Padding adalah ruang di dalam border elemen yang memisahkan konten elemen dari border. Padding digunakan untuk memberikan jarak antara konten elemen dan tepi elemen itu sendiri.
Intinya, urutan dari dalam ke luar adalah konten -> padding -> border -> margin.

Cara untuk mengimplementasikan ketiga hal tersebut adalah dengan menggunakan properti CSS berikut:
- Untuk mengatur margin, gunakan properti margin, misalnya: margin: 10px (untuk margin 10px di semua sisi)
- Untuk mengatur border, gunakan properti border, misalnya: border: 2px solid black (untuk border hitam dengan ketebalan 2px)
- Untuk mengatur padding, gunakan properti padding, misalnya: padding: 15px (untuk padding 15px di semua sisi)

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
Flexbox (Flexible Box Layout) adalah metode layout satu dimensi yang digunakan untuk mengatur elemen dalam satu baris atau kolom. Flexbox memungkinkan elemen untuk menyesuaikan ukuran dan posisi mereka secara fleksibel berdasarkan ruang yang tersedia. Kegunaan flexbox termasuk mengatur tata letak yang responsif, menyusun elemen secara horizontal atau vertikal, dan mengelola ruang antar elemen dengan mudah. 

Grid layout adalah metode layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Grid layout memberikan kontrol yang lebih besar atas tata letak yang kompleks dengan memungkinkan elemen untuk menempati beberapa baris atau kolom sekaligus. Kegunaan grid layout termasuk membuat tata letak halaman yang kompleks, mengatur elemen dalam struktur yang terorganisir/lebih rapi, dan menciptakan desain yang responsif dengan mudah.