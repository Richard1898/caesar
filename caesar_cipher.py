a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def e(t, o):# iekodēs burtus
  r = ""
  for c in t:#cikls lai parveidotu burtu
    if (a.find(c) == -1):#lai burtu A ,piemēram,izdara X uz vienu burtu pirms
      r += c
    else:  
      r += (a[(a.find(c) + o) % len(a)])
  return r

def d(t, o):# dekodēs burtus
  r = ""
  for c in t:# cikls lai parveidotu burtu
    if (a.find(c) == -1):#lai burtu X ,piemēram,izdara A uz vienu burtu atpakal
      r += c
    else:
      r += (a[(a.find(c) - o) % len(a)])
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
  print("Encrypted: " + e(text, rotation))
elif mode == 2:#ievada noteikta moda atsivret kodu
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3:#vairs nav modes ja ievada 3 tad nekas nedos
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
