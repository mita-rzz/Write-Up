# XLMRat Lab

#### 1. The attacker successfully executed a command to download the first stage of the malware. What is the URL from which the first malware stage was installed?
 
Ans: first stage malware adalah bagian pertama sebelum malware melakukan serangan yaitu bagian pendownloadan malware tersebut 

Untuk mengetahui nya pertama tama memfilter paket  agar yang ditampilkan hanya khusus untuk http karena terjadi pendownload-an malware lewat url biasanya dilakukan dengan protocol http. filter dilakukan dengan mengetik:
    ```bash
    http 
    ``` 
    Setlah difilter paket nya menjadi sedikit dan menjadi lebih mudah untuk di identifikasi 
    Pertama tama Mengidentifikasi paket berdasarkan urutan nya. yang pertama adalah get /xml.txt lalu kita inspect dengan:
    
-  mengklik kanan pada paket
- memilih follow 
-  memilih TCP STREAM
        
 Setelah itu maka akan terlihat payload data atau percakapan antara client dan server secara lengkap. pada bagian ini akan terdapat banyak informasi seperti Request Respont dan isi dari paket nya yaitu isi dari xml.txt. dari isi xml.txt dapat diketahui isi nya adalah command yang digunakan untuk mendownload file lain yang berbentuk jpg. 

Lalu kita melihat bagian HTTP untuk mdm.jpg. dengan menggunakan langkah yang sama untuk Mengidentifikasi paket nya dengan cara sebelumnya kita dapat melihat isi paket nya yaitu command berupa malware (dapat diketahui dari apa yang dilakukan script tersebut) karena sudah diketahui bahwa ini adalah malware maka tugas selanjutnya adalah mencari link yang digunakan untuk menginstal nya. Link nya dapat diambil dari link yang ada di xml.txt atau dengan mengklik dua kali pada paket ini maka akan nampak link request nya yaitu **http://45.126.209.4:222/mdm.jpg** 

#### 2. Which hosting provider owns the associated IP address?
Ans: Untuk Mengetahui hosting provider yang digunakan dapat dilakukan dengan mengecek nya di website seperti iplocation. Dengan menggunakan alaman ip yang sudah ada sebelumnya lalu digunakan sebagai input di web iplocation maka akan terlihat provider yang digunakan yaitu **reliableSite.net**.


#### 3. By analyzing the malicious scripts, two payloads were identified: a loader and a secondary executable. What is the SHA256 of the malware executable?
Ans: Karena sudah diketahui bahwa mdg.jpg adalah bagian yang malware yang di install maka langkah selanjutnya adalah menganalisis isi dari paket paket mdm.jpg dengan :
- mengklik kanan pada paket
- memilih follow 
- memilih HTTP

setelah itu akan nampak script yang ada, lalu mengecek script dari bagian awal yaitu hexString_bbb . pengecekan dilakukan dengan mensalin isi dari hexString_bbb lalu memasukkan nya kedalam cyber chef dan memilih operasi from hex . Setelah itu akan terlihat script tersebut menghasilkan sebuah  file mencurigakan dalam bentuk exe file. karena itu adalah malware dari pada mengambil executable file nya kita lebih baik mengambil hashing nya untuk mengecek nilai SHA256 nya di virustotal (di cyber chef tidak ada hash 256)  untuk hash yang dipilih bebas tapi saya memilih MD 5 dan didapat hash nya 
yaitu 88e8cee71f454bc1fa6b3a7741a3bd7d.
<img width="1855" height="938" alt="image" src="https://github.com/user-attachments/assets/a74a1d01-0dc9-4c78-84c3-4446da182054" />


Setalah itu hash tersebut dimasukkan di https://www.virustotal.com/ dengan memasukkan nya di bagian search URL. Setelah itu selanjutnya memilih bagian Details. Dibagian ini akan   terlihat basic properties salah satunya adalah versi SHA256 yaitu **1eb7b02e18f67420f42b1d94e74f3b6289d92672a0fb1786c30c03d68e81d798** 
<img width="1857" height="943" alt="image" src="https://github.com/user-attachments/assets/dd965660-afc1-4337-8fbf-fb06d31767cb" />

#### 4. What is the malware family label based on Alibaba?
Ans: Untuk mengetahui malware family label dapat dilihat di virus total bagian DETECTION. Malware family dapat dilihat di tabel  Security vendors' analysis karena yang diminta adalah alibaba maka perlu melihat tabel yang bertuliskan alibaba dimana di kanan nya akan terlihat label nya dan family nya. untuk family nya adalah **AsyncRat**.
<img width="1842" height="944" alt="image" src="https://github.com/user-attachments/assets/9074ef3c-7c32-4750-ba4f-437e0e7b639c" />

#### 5. What is the timestamp of the malware's creation?
Ans: Untuk mengetahui nya dapat dilakukan dengan mengecek pada bagian details lalu lihat pada history disana akan nampak kapan malware ini dibuat yaitu 
2023-10-30 15:08:44 UTC .

<img width="1845" height="944" alt="image" src="https://github.com/user-attachments/assets/09390156-8709-483d-a1e1-9310fdf04dab" />

#### 6.Which LOLBin is leveraged for stealthy process execution in this script? Provide the full path.
Ans: LOLBins (Living Off the Land Binaries) adalah istilah dalam keamanan siber yang merujuk pada berkas (file), alat (tools), atau biner sah/resmi yang sudah terpasang bawaan di sistem operasi (terutama Windows), yang disalahgunakan oleh penyerang untuk melakukan aktivitas jahat  . LOLBins biasa digunakan agar antivirus tidak curiga karena penamaan yang mirip dengan file asli bawaan windows. Untuk mengetahu nya dapat dilakukan dengan menganalisa kumpulan paket pada dengan cara :
- mengklik kanan pada paket
- memilih follow 
- memilih HTTP
lalu melihat isi dari paket tersebut dan menemukan
```bash
$NK = $Fu.GetType('N#ew#PE#2.P#E'-replace  '#', '') 
$MZ = $NK.GetMethod('Execute')
$NA = 'C:\W#######indow############s\Mi####cr'-replace  '#', ''
$AC = $NA + 'osof#####t.NET\Fra###mework\v4.0.303###19\R##egSvc#####s.exe'-replace  '#', ''
$VA = @($AC, $NKbb)
```
dimana di syntax di atas menentukan file asli windows yang digunakan. jika kita menghilangkan # maka akan menemukan **C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe** yaitu pathj dari LOLBin yang digunakan. 

#### 7.The script is designed to drop several files. List the names of the files dropped by the script.
Ans: untuk mengetahu nya dapat dilakukan dengan melihat paket paket yang dihasilkan dari proses nomor 6. didalam script tersebut dapat dilihat ada beberapa file yang di write di script tersebut yaitu 
```bash
[IO.File]::WriteAllText("C:\Users\Public\Conted.ps1", $Content)
[IO.File]::WriteAllText("C:\Users\Public\Conted.bat", $Content)
[IO.File]::WriteAllText("C:\Users\Public\Conted.vbs", $Content)

```
jadi jawabannya adalah Conted.vbs,Conted.ps1,Conted.bat 

    
        

