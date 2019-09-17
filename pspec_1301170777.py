IdCustomer='customer'
passCustomer='12345'
IdAdmin='admin'
passAdmin='12345'
Idowner='owner'
passowner='12345'

def pilihuser():
    print("Login as : \n","1. Admin\n",'2. Customer\n','3. Owner') 
    login=int(input('Pilih : '))
    if login==1:
        admin()
    elif login==2:
        customer()
    elif login==3:
        owner()
    else:
        print('Menu Tidak Tersedia')
        pilihuser()
#bagian admin
def admin():
    username=input('Username Admin : ')
    password=input('password Admin : ')
    if username==IdAdmin and password==passAdmin:
        menuadmin()
    else:
        print('Username atau Password yang anda masukan salah')
        admin()
def menuadmin():
    print('1. lihat villa yang diajukan\n2. hapus villa\n3. Logout')
    pilih=int(input('Pilih : '))
    if pilih==3:
        pilihuser()
    else:
        print ('maaf menu tidak tersedia saat ini')
        menuadmin()

def customer():
    username=input('Username User: ')
    password=input('password User: ')
    if username==IdCustomer and password==passCustomer:
        customermenu()
    else:
        print('User name atau password salah')
        Customer()
def customermenu():
    print('\t\t\tMenu Utama\nNama: Septha Anggara\tId customer: 1301170777')
    print('1. lihat daftar villa\t2. daftar transaksi\n3. Logout')
    x=int(input('pilih menu: '))
    if x==3:
        pilihuser()
    else:
        print('maaf menu tidak tersedia pada saat ini')
        customermenu()

def owner():
    username=input('Username owner : ')
    password=input('password owner : ')
    if username==Idowner and password==passowner:
        ownermenu()
    else:
        print('User name atau password salah')
        owner()
def ownermenu():
    print('\t\t\tMenu Utama\nNama: Dimas villa\tId owner: 1301170888')
    print('1. input data villa\t2. daftar villa\n3. daftar transaksi\n4. Logout')
    x=int(input('pilih menu: '))
    if x==4:
        pilihuser()
    else:
        print('maaf menu tidak tersedia pada saat ini')
        ownermenu()
pilihuser()

    
