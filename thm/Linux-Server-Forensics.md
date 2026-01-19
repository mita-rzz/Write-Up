
# Linux Server Forensics 

- Task 6 :

    Pada task ini akan diminta untuk mencari password yang digunakan oleh penyusup untuk login. Pencarian dilakukan dengan mengecek pada folder /etc/passwd dan ditemukan hash dari password yang digunakan oleh penyusup nya. karena password nya dalam bentuk hash maka perlu di ubah jadi teks dengan brute fore menggunakan hashcat dengan code:
 
    ```bash
  hashcat -m 1500 -a 3 hai.txt --force
 
    ``` 
    untuk melakukan bruteforce dari aaaaaaaa - zzzzzzzz. setelah itu ditemukan bahwa passwordnya adalah mrcake 
     

- Task 7 : 
    #### Name one of the non-standard HTTP Requests.? 
    Untuk menjawabnya perlu untuk menganalisis file access.log http request yang standard itu seperti http request yang sudah umum ada atau digunakan seperti POST GET dan lain sebagainya. untuk mencari yang tidak standard dapat dilakukan dengan menganalisis nya satu persatu atau menggunakan linux command yaitu
    ```bash
     grep -a -v 'GET' ./access.log | grep -a -v 'POST'
    ``` 
    command diatas digunakan untuk mencari HTTP request yang bukan 'GET' dan bukan 'POST' sehingga dapat diketahui http request yang tidak standard. yaitu GXWR

    #### At what time was the Nmap scan performed? (format: HH:MM:SS)
  untuk mengetahui kapan Nmap dilakukan dapat dilihat dari kapan request tidak biasa dilakukan. yaitu 13:30:15

- Task 8:
  ####  What username and hostname combination can be found in one of the authorized_keys files? (format: username@hostname)

  Untuk menjawab nya kita perlu untuk masuk ke file authorized_keys. pertama tama kita akan mencari dimana file tersebut berada dengan menggunakan command :
  ```bash
      sudo find / -name authorized_key
  ```

  setelah itu akan nampak hasilnya dan tinggal melihat isi  file nya dengan command:

  ```
  sudo cat ./root/.ssh/authorized_keys

  ```
  setelah dijalankan maka akan nampak hasilnya yaitu kali@kali

- Task 9 :
  ####    What is the first command present in root's bash_history file?
  Untuk menjawab nya kita perlu untuk melihat isi file bash_history di folder root. karena tidak bisa mengubah directory jadi root maka kita menggunakan 
  ```bash
    sudo ls -la ./root
  ```
    untuk mengecek apakah ada file bash_history di folder root dan ternyata ada.
    Membuka file nya dengan menggunakan command 

  ```bash
    sudo cat  ./root/.bash_history
  ```
  dengan menjalankan command diatas akan dihasilkan history nya dan dapat diketahui first command pertama root adalah nano /etc/passwd

- Task 11:
  #### Figure out what's going on and find the flag.

  Untuk menjawab nya pertama-tama perlu untuk melihat layanan  apa saja yang berjalan di server tersebut dengan menggunakan 
  
  ```bash
    systemctl --type=service --state=active
  ```  
  setelah dijalankan akan muncul banyak layanan yang sedang aktif. Kita perlu untuk melihat layanan mana yang mencurigakan. dan didapatlah layanan IpManager.Service. Layanan ini mencurigakan karena layanan ini berbeda dari standar layanan linux yaitu terdapat huruf besar dan nama IpManager bukan lah nama yang standar digunakan di layanan Linux. Karena sudah ditemukan kita perlu mengecek informasi lebih lanjut tentang layanan itu dengan menggunakan:
    
    ```bash
    systemctl status IpManager.Service.
  ```
    setelah di jalankan akan muncul informasi lebih lanjut seperti letak file yang menjalankan layanan tersebut yaitu bin//bash /etc/network/ZGtsam5hZG1ua2Fu.sh. Langkah selanjutnya adalah melihat file tersebut dengan menjalankan :
     ```bash
    cat bin/bash/etc/network/ZGtsam5hZG1ua2Fu.sh
  ```
  dan akan muncul flag nya yaitu [gh0st_1n_the_machine].

  


