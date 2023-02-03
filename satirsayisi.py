dosya = input("Dosya Adı Giriniz: ")

file1 = open(dosya, 'r')
Lines = file1.readlines()

bos_satir = 0
kareler = 0
uc_tirnak = 0
count = 0

flag = False
flag_count = 0
eksilt = []

for line in Lines:
    a = line.strip()
    if a == "":
        eksilt.append(1)
        count += 1
        bos_satir += 1
        continue
    elif a[0] == "#":
        eksilt.append(1)
        count += 1
        kareler += 1
        continue

    b = '"""'
    if str(line)[0:3] == b and not flag:
        flag_count = count
        flag = True
        count += 1
        continue
    elif str(line)[0:3] == b and flag:
        eksilt.append(count-flag_count+1)
        uc_tirnak += count-flag_count+1
        flag = False
        count += 1
        continue
    elif str(line)[-4:-1] == b and flag:
        eksilt.append(count-flag_count+1)
        uc_tirnak += count-flag_count+1
        flag = False
        count += 1
        continue

    count += 1
print("""    _              _       _   _ _ _
   / \  _   _ _ __(_)_ __ | |_(_) (_)
  / _ \| | | | '__| | '_ \| __| | | |
 / ___ \ |_| | |  | | | | | |_| | | |
/_/   \_\__, |_|  |_|_| |_|\__|_|_|_|
        |___/
 ____
|  _ \ __ _ _ __   ___  _ __ _   _ _ __  _   _ ____
| |_) / _` | '_ \ / _ \| '__| | | | '_ \| | | |_  /
|  _ < (_| | |_) | (_) | |  | |_| | | | | |_| |/ /
|_| \_\__,_| .__/ \___/|_|   \__,_|_| |_|\__,_/___|
           |_|""")


print(f"\n\nKodunuzun satır sayısı: {len(Lines)}\n")
print(f"Kodunuzun gerçek satır sayısı: {len(Lines) - sum(eksilt)}\n")
print(f"Kodunuza boşa giden kod satırı sayısı: {sum(eksilt)}\n\n")
print(f"Kodunuzda kare (#) kullanarak yaptığınız yorum satırı sayısı: {kareler}\n")
print(f'Kodunuzda üç tırnak (""") kullanarak yaptığınız yorum satırı sayısı: {uc_tirnak}\n')
print(f'Kodunuzda kullandığınız boş satır sayısı: {bos_satir}')
