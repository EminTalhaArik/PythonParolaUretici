from random import choice
kolayParola = [
    "a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","1","2","3","4","5","6","7","8","9","0"
]

ortaParola = [
    "a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","1","2","3","4","5","6","7","8","9","0",
    "A","B","C","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"
]

zorParola = [
    "a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","1","2","3","4","5","6","7","8","9","0",
    "A","B","C","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","#","£","$","+","!","%","½","&","/","*","|","=","^","?",
]

def parolaOlustur(passwordLength,password,parolaTuru):

    for i in range(passwordLength):
        password += choice(parolaTuru)

    return password
devam = True

print("-------------Parola Üreticisi----------------")


while devam:
    password = ""
    print("=================================================")

    passwordLength = int(input("Lütfen şifre uzunluğu giriniz : "))

    print("===============")
    print("===Zorluk Seviyesi===")
    print("1 - Kolay")
    print("2 - Orta")
    print("3 - Zor")
    print("===============")

    zorluk = int(input("LÜtfen Parolanızın zorluk seviyesini belirtiniz : "))

    if zorluk == 1:
        password = parolaOlustur(passwordLength,password,kolayParola)
        print("Parolanız : " + password)

    elif zorluk == 2:
        password = parolaOlustur(passwordLength,password,ortaParola)
        print("Parolanız : " + password)

    elif zorluk == 3:
        password = parolaOlustur(passwordLength,password,zorParola)
        print("Parolanız : " + password)
        
    else:
        print("Yanlış Veri Girişi")   

    print("===============")
   
    print("Yeni Parola oluşturmak istermisiniz ?")

    secim = int(input("1 - Evet 2 - Hayır "))

    if secim == 1:
        devam = True

    else:
        exit()