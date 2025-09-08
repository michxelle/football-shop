**Nama aplikasi/shop = Footballed Co.**

**Link aplikasi PWS = https://laudya-michelle-footballshop.pbp.cs.ui.ac.id/**



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



**Link bagan Django request-response: https://drive.google.com/file/d/16utn4HcQdcFPHNyEqhr61\_2M9\_B3rNSu/view?usp=sharing**



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

