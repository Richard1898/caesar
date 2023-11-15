alfavits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def atšifrettekstarotacija(t, o):# iekodēs burtus
  r = ""
  for burts in t:#cikls lai parveidotu burtu
    if (alfavits.find(burts) == -1):#lai burtu A ,piemēram,izdara X uz vienu burtu pirms
      r += burts
    else:  
      r += (alfavits[(alfavits.find(burts) + o) % len(alfavits)])
  return r

def d(t, o):# dekodēs burtus
  r = ""
  for burts in t:# cikls lai parveidotu burtu
    if (alfavits.find(burts) == -1):#lai burtu X ,piemēram,izdara A uz vienu burtu atpakal
      r += burts
    else:
      r += (alfavits[(alfavits.find(burts) - o) % len(alfavits)])
  return r

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:#ievada noteikta moda iekodet vardu
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + atšifrettekstarotacija(text, rotation))
elif mode == 2:#ievada noteikta moda atsivret kodu
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3:#vairs nav modes ja ievada 3 tad nekas nedos
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
