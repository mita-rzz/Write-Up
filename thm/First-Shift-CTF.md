# First Shift CTF
## Task 3
### Challenge Description
Pada task ini terdapat peringatan pada dashboard SOC yaitu adanya login vpn yang tidak wajar dari email susan.martin@probablyfine.thm  dengan IP 37.19.201.132  dari singapore.  Ternyata Susan pernah menginstall "security check" pada saat menggunakan wifi public. Ternyata setelah di hash didapat b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630.
Question:
#### 1. What is the ASN number related to the IP?
Ans: 
Autonomous System Number (ASN) adalah angka unik 16-bit atau 32-bit yang mengidentifikasi jaringan besar, ISP, atau organisasi di internet secara global, memungkinkan mereka bertukar informasi perutean (routing) menggunakan protokol BGP. ASN dapat ditemukan dengan :
1. Masuk ke URL TryDetectThis
2. Memasukkan alamat ip dari vpn login ke tab pencarian 
3. Nomor ASN dapat dilihat pada IP Overview  yaitu **212238**
   
   <img width="1857" height="941" alt="image" src="https://github.com/user-attachments/assets/2c8bb235-dfe6-4f21-9630-16497cfd2f46" />

#### 2. Which service is offered from this IP? 
Ans: 
Karena IP ini digunakan dalam koneksi melalui VPN maka servis yang ditawarkan oleh IP ini juga adalah **VPN**

#### 3. What is the filename of the file related to the hash?
Ans:
Untuk mengetahui nama file yang related dengan hash tersebut dapat dilakukan dengan:

1. Masuk ke URL TryDetectThis
2. Memasukkan HASH dari "security check"  
3. Melihat pada file detail lalu ke bagian File name
Dari file name tersebut ditemukan jawaban nya yaitu **zY9sqWs.exe**

<img width="1836" height="883" alt="image" src="https://github.com/user-attachments/assets/bbd2ed72-e62b-490d-8539-9b529d2710fc" />


#### 4. What is the threat signature that Microsoft assigned to the file?
Ans:
Threat signature adalah pola, pengidentifikasi unik, atau karakteristik khusus yang terkait dengan aktivitas berbahaya, seperti malware, serangan siber, atau intrusi. Threat signature berbeda beda tergantung vendor yang menganalisis nya. untuk mengetahui threat signature dari microsoft dapat dilihat pada bagian vendor Analysis lalu mencari pada bagian Micorsoft. Menurut microsoft threat signature nya adalah **Trojan:Win32/LummaStealer.PM!MTB**

<img width="1806" height="912" alt="image" src="https://github.com/user-attachments/assets/b015b1cc-e148-46e4-912b-70ecba54ccb7" />

#### 5.  One of the contacted domains is part of a large malicious infrastructure cluster.Based on its HTTPS certificate, how many domains are linked to the same campaign?
Ans:
Untuk mengetahui sebuah domain itu bagian dari large malicious infrastructure cluster dapat dilakukan dengan mengecek nya satu persatu. pada kolom detection terdapat beberapa nilai yaitu nilai dari berapa antivirus yang menyatakan domain ini berbahaya. Jadi pengecekan dapat dimulai dulu dari domain yang di anggap mencurigakan oleh antivirus tersebut terlebih dahulu.
Untuk melakukan pengecekan dapat dilakukan dengan :

1. Menyalin id  domain yang di inginkan
2. melakukan pencarian di TryDetectThis menggunakan id domain tersebut.
3. Melihat pada tabel HTTPS Certificate Data.
 
 gadgethgfub.icu di nyatakan sebagai   large malicious infrastructure cluster karena nama yang tidak biasa untuk domain, menggunakan ekstensi domain yang murah (biasanya digunakan hacker) dan memiliki banyak domain yang terhubung dengan domain tersebut. pada HTTPS certificate terdapat **151** domain yang terhubung dengan domain tersebut.

#### 6. The file matches one of the YARA rules made by "kevoreilly". What line is present in the rule's "condition" field?
Ans:  
YARA rules adalah alat open-source yang digunakan analis keamanan untuk mengidentifikasi, mengklasifikasikan, dan mendeteksi malware atau file mencurigakan berdasarkan pola tekstual atau biner (string, heksadesimal). sedangkan condition di yara rules adalah jantung logikanya. Di sinilah  ditentukan  syarat apa saja yang harus terpenuhi agar sebuah file cocok dengan rule yang  dibuat. singkatnya condition adalah kondisi dimana sebuah file dianggap maware.
Untuk mengetahui nya dapat dilakukan dengan cara:
1. Membuka TryDetectThis dan sudah memasukkan hash yang dicurigai di awal (b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630)
2. Melihat pada bagian Detections and Reports.
   <img width="1856" height="927" alt="image" src="https://github.com/user-attachments/assets/73771a2f-2721-44a6-9cc9-91d2943da63d" />
4. Masuk pada URL github yang ada. (setelah dibuka akan terlihat yara rules)
5. Mengambil jawabannya tepat dibawah tulisan condition: dan didapat jawabannya adalah **uint16(0) == 0x5a4d and any of them**
   <img width="1820" height="637" alt="image" src="https://github.com/user-attachments/assets/0ad19d00-b1c0-4980-b6b1-fff9662efb38" />

#### 7. The file is also mentioned in one of the TI reports. What is the title of the report mentioning this hash?
Ans: 
untuk laporan TI yang menyinggung tentang hash (b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630) dapat dilihat dengan:
1.  membuka TryDetectThis dengan memasukkan hash b8e02f2bc0ffb42e8cf28e37a26d8d825f639079bf6d948f8debab6440ee5630
2.  Memilih report pada bagian Detections and Reports.
3.  judul dari laporan yang menyinggung hash tersebut dapat dilihat di kolom Report Name yaitu **Behind the Curtain: How Lumma Affiliates Operate**

#### 8. Which team did the author of the malware start collaborating with in early 2024?
Ans: 
tim yang melakukan kolaborasi dengan penulis malware tersebut dapat dilihat pada laporan TI sebelumnya yaitu dengan nama Behind the Curtain: How Lumma Affiliates Operate. Untuk memudahkan pencarian dapat menggunakan bilah pencarian dengan mencari menggunakan kata "2024". setelah pencarian dapat ditemukan bahwa tim yang melakukan kolaborasi adalah tim **GhostSocks**  

<img width="1855" height="892" alt="image" src="https://github.com/user-attachments/assets/ef8d1acd-bde3-4cf9-a7d5-de61acc819ac" />
#### 9. A Mexican-based affiliate related to the malware family also uses other infostealers. Which mentioned infostealer targets Android systems?
Ans:
Infostealer (pencuri informasi) adalah jenis malware yang dirancang khusus untuk menginfeksi perangkat, lalu mencuri data sensitif seperti kredensial login (username/password), data perbankan, cookie browser, dan file penting secara diam-diam, kemudian mengirimkannya ke penyerang. 
Untuk mengetahui infostealer lain yang digunakan dapat diketahui lewat laporan TI dengan judul  



