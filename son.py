


words = ["abadiy", "boqiy", "mangu", "cheksiz", "soya", "sharpa", 
"izsiz", "yashin", "quyosh", "yulduz", "yer", "oy", "bulut", "telefon", 
"anor", "olma", "gilos", "o'rik", "banan", "uzum", "anjir", "mandaring", 
"apilsin", "kivi", "shaftoli", "olho'ri", "mitiyarit", "sayyora", "osmon", 
"samo", "koyinot", "ufq", "borliq", "olam", "dunyo"]

# from random import choice as ch

# def get_words():
#     a = ch(words)
#     print(a)
#     return a 



# def display(par, par2):
#     m = ''
#     for i in par2:
#         if i in par:
#             m += i
#         else:
#             m += '-'
#     return m



# def play():
#     t_soz = get_words().upper()
#     print(f"Men {len(t_soz)} ta harfdan iborat so'z o'yladim. "
#     f"Topa olasizmi ?")
#     print(len(t_soz) * '-', '\n')
#     harflar = ''
#     soz = ''
#     c = 1
#     while True:
#         harf = input("Harf kiriting: ").upper()
#         if harf in t_soz and harf not in harflar:
#             harflar += harf
#             print(f"{harf} harfi to'g'ri.")
#             soz = display(harflar, t_soz)
#             print(soz)
#             print(f"Shu vaqatgacha kiritgan xarflaringiz: {harflar}\n")
#         elif harf not in t_soz and harf not in harflar:
#             harflar += harf
#             print(f"Bunday harf yo'q.\n{display(harflar, t_soz)}")
#             print(f"Shu vaqatgacha kiritgan xarflaringiz: {harflar}\n")
#             continue
#         elif harf in harflar:
#             if harf:
#                 print(f"Bu harfni oldin kiritgansiz. Boshqa harf kiriting.\n"
#                 f"{display(harflar, t_soz)}")
#             else:
#                 print(f"Iltimos harf kiriting. Bu harf emas.\n"
#                 f"{display(harflar, t_soz)}")
#             print(f"Shu vaqatgacha kiritgan xarflaringiz: {harflar}\n")
#             continue
#         if t_soz == soz:
#             print(f"Tabriklayman! {soz} so'zini {c} ta urinishda topdingiz.")
#             break
#         c += 1   
#         print(f"Shu vaqatgacha kiritgan xarflaringiz: {harflar}\n")

# play()

