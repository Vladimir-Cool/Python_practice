from simplecrypt import decrypt, DecryptionException


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    with open ('passwords.txt', ) as password:
        for pas in password:
            print(pas)
            try:
                new_file = decrypt(pas, encrypted).decode('utf8')
                print(new_file)
            except DecryptionException:
                print('Ошибка')
