# Forensic: An unusual sighting
## Informasi

 - As the preparations come to an end, and The Fray draws near each day, our newly established team has started work on refactoring the new CMS application for the competition. However, after some time we noticed that a lot of our work mysteriously has been disappearing! We managed to extract the SSH Logs and the Bash History from our dev server in question. The faction that manages to uncover the perpetrator will have a massive bonus come competition!

 - scenario file : http://ctf.hackthebox.com/challenges/31867/download?expires=1768635995&signature=5e31cb821d8ee99ffff20befd7b4679f0c81fadd731b023654179b6fd8dfaf76

 


## Step

1. Mengakses tantangan dengan menjalankan : 
```bash
 nc 94.237.52.235 32571
```
2. Akan diminta untuk memasukkan IP addr dan port dari server SSH. IP dan port dapat dilihat pada file  sshd.log dimana pada setiap koneksi terdapat informasi dimana IP dan port yang  dihubungi oleh client. IP nya adalah 100.107.36.130 dan PORT nya 2221.
3. Akan diminta untuk memasukkan kapan loginberhasil pertama kali dilakukan. Hal itu dapat diketahui dengan melihat informasi yang ada di file sshd.log. Login berhasil dapat ditandai dengan diterima nya password yang client dikirimkan . Login pertama kali nya adalah pada saat 2024-02-13 11:29:50. 
4. Akan diminta untuk memasukkan kapan login tidak biasa dilakukan. Untuk mengetahui nya dapat dilakukan dengan memperhatikan bash_history.txt dan memperhatikan log yang terjadi. Setelah diperhatikan dapat dilihat ada hal tidak biasa yaitu terjadi download file yang terindikasi malware dari internet dan file tersebut langsung dijalankan. karena sudah diketahui rentang waktu nya maka tinggal melihat kapan login yang mendekati waktu tersebut di sshd.log untuk diketahui kapan login pertama nya dan akhirnya diketahui yaitu pada 2024-02-19 04:00:14
5. akan diminta untuk memasukkan fingerprint dari attacker. untuk menjawabnya perlu untuk menganalisis file sshd.log. fingerprint dapat di lihat pada informasi public key setelah ip mencurigakan itu melakukan koneksi dengan server.
6. Akan diminta untuk mengetahui command pertama yang dilakukan oleh attacker. hal ini dapat diketahui dari bash_history.txt dan melihat history sejak ip mencurigakan itu sudah terhubung dengan server dan diketahui command nya "whoami"
7. akan diminta memasukkan command terakhir. hal itu dapat diketahui dari log terakhir sebelum waktunya ip mencurigakan itu keluar. command itu adalah ./setup  
8. Flag muncul


