

dmy = [1,'r', 2]

a,b,c = dmy[:]
print(a,b,c)














##def return_time_births():
##        """Foydalanuvchidan tug'ilgan vaqtini so'rab
##        List ko'rinishida qaytaruvchi funksiya"""
##        ishora = True
##        while  ishora:
##        
##                def determine_the_day():
##                        while True:
##                                day = input("Qaysi kunda tug'ilgansiz kunni kiriting:\n")
##                                if day == '':
##                                        day = 0
##                                        break
##                                day = int(day)
##                                if day > 31 or day < 1:
##                                        print(f"Oylarda {day} - kun yo'q "
##                                              f"itimos to'g'ri kunni kiriting:\n")
##                                else:
##                                        break
##                        return day
##                day = determine_the_day()
##                if not day:
##                        break
##        return day




##print(return_time_births())





##a = 4
##
##def h():
##        a = 2
##        f = 9
##        return f
##        
##print(h())
##print(a)





##c = []
##h = []
##h.append({'a':2, 'b':4})
##
##
##def r_dict(**kw):
##        return kw
##
##
##lower_dict = 'json'
##l_d = 'born'
##
##h.append({lower_dict:r_dict(g=6, y=3, x=8)})
##h.append({l_d:r_dict(f=12, h=13, v=58)})
##
####print(s)
##for i in h:
##        for k, q in i.items():
##                print(k, q)



##x = {}
##
##x['json'] = s['json'].copy()
##
##for k, q in x.items():
##        print(k, q)













##s = {'a':2, 'b':4}
##
##
##def r_dict(**kw):
##        return kw
##
##
##lower_dict = 'json'
##l_d = 'born'
##
##s.update({lower_dict:r_dict(g=6, y=3, x=8)})
##s.update({l_d:r_dict(f=12, h=13, v=58)})
##
##print(s)
##
##for k, q in s.items():
##        print(k, q)
##
##
##x = {}
##
##x['json'] = s['json'].copy()
##
##for k, q in x.items():
##        print(k, q)




##def return_time_births():
##        time_births = []
##        ishora = True
##        while ishora:
##                stop = None
##                day = int(input("Qaysi kunda tug'ilgansiz kunni kiriting:\n"))
##                if day > 31 or day < 1:
##                        print("Oylarda {day} - kun yo'q "
##                              f"itimos to'g'ri kunni kiriting:\n")
##                else:
##                        while ishora:
##                                if stop:
##                                        break
##                                months = return_months()
##                                month = input("Qaysi oyda tug'ilgansiz oy nomini kiriting:\n").lower()
##                                if month not in months.keys():
##                                        print(f"{month.title()} nomli oy mavjud emas iltimos to'g'ri oyni kiriting")
##
##                                elif day in months[month]:
##                                        while ishora:
##                                                year = int(input("Qaysi yilda tug'ilgansiz yilni kiriting:\n"))
##                                                loccal_months = {}
##                                                if year in range(1896,2022,4):
##                                                        loccal_months = return_months()
##                                                if year not in range(1896,2022,4) and year in range(1896,2022):
##                                                        loccal_months = return_months(yanvar=31, fevral=28, mart=31, aprel=30,
##                                                                               may=31, iyun=30, iyul=31, avgust=31,
##                                                                               sentyabr=30, oktyabr=31, noyabr=30, dekabr=31)
##                                                if year > 2022:
##                                                        print(f"{year} - yil kelmagan itimos "
##                                                              f"to'g'ri yilni kiritng")
##
##                                                elif year < 1900:
##                                                        print(f"{year} - yilda tug'ilgan insonlar "
##                                                              f"qolmagan itimos to'g'ri yilni kiritng")
##
##                                                elif day in loccal_months[month]:
##                                                              if day in range(1,10):
##                                                                      day = '0' + str(day)
##                                                              month = months_numbers(month)
##                                                              time_births.append(str(day))
##                                                              time_births.append(str(month))
##                                                              time_births.append(str(year))
##                                                              ishora = False
##                                                else:
##                                                        print(f"{year} - yilning {month} oyida "
##                                                              f"{day} - kun yo'q iltimos "
##                                                              f"to'g'ri kunni kiriting:\n")
##                                                        stop = 1
##                                                        break
##                                        
##                                else:
##                                        print(f"{month.title()} oyida {day} - kunni yo'q "
##                                              f"iltimos to'g'ri kunni kiriting:\n")
##                                        break
##        return time_births






##def return_time_births(b_year, b_month_name, b_day):
##        time_births = []
##        months = {}
##        
##        if b_year in range(1900,2022,4):
##                time_births.append(b_year)
##
##
##                months.update(return_months("yanvar", 31))
##                months.update(return_months("fevral", 29))
##                months.update(return_months("mart", 31))
##                months.update(return_months("aprel", 30))
##                months.update(return_months("may", 31))
##                months.update(return_months("iyun", 30))
##                months.update(return_months("iyul", 31))
##                months.update(return_months("avgust", 31))
##                months.update(return_months("sentyabr", 30))
##                months.update(return_months("oktyabr", 31))
##                months.update(return_months("noyabr", 30))
##                months.update(return_months("dekabr", 31))
####                print(months)
##                                
##                if b_month_name in months.keys():
##                        time_births.append(b_month_name)
##
##                        
##                        if b_day in months[b_month_name]:
##                                time_births.append(b_day)
##                        else:
##                                print(f"{b_month_name} oyida {b_day} -  kun mavjud emas")
##                else:
##                        print(f"{b_month_name} nomli oy mavjud emas")
##                        
##        elif b_year not in range(1900,2022,4) and b_year in range(1900,2022):
##                time_births.append(b_year)
##                
##
##                months.update(return_months("yanvar", 31))
##                months.update(return_months("fevral", 28))
##                months.update(return_months("mart", 31))
##                months.update(return_months("aprel", 30))
##                months.update(return_months("may", 31))
##                months.update(return_months("iyun", 30))
##                months.update(return_months("iyul", 31))
##                months.update(return_months("avgust", 31))
##                months.update(return_months("sentyabr", 30))
##                months.update(return_months("oktyabr", 31))
##                months.update(return_months("noyabr", 30))
##                months.update(return_months("dekabr", 31))
####                print(months)
##                if b_month_name in months.keys():
##                        time_births.append(b_month_name)
##                        
##                        if b_day in months[b_month_name]:
##                                time_births.append(b_day)
##                        else:
##                                print(f"{b_month_name} oyida {b_day} -  kun mavjud emas")
##                else:
##                        print(f"{b_month_name} nomli oy mavjud emas")
##                        
##                        
##        elif b_year > 2022:
##                print(f"{b_year} yil kelmagan itimos to'g'ri yilni kiritng")
##
##        elif b_year < 1900:
##                print(f"{b_year} yilda tug'ilgan insonlar qolmagan itimos to'g'ri yilni kiritng")
##                
##        return time_births





###### while csikli bor



########def return_time_births():
########        time_births = []
########        months = {}
########        ishora = True
########        while ishora:
########                b_year = int(input("Yilni kiriting:\n"))
########        
########                if b_year in range(1900,2022,4):
########                        time_births.append(b_year)
########                        
########                        months.update(return_months(yanvar=31, fevral=29, mart=31, aprel=30,
########                                                    may=31, iyun=30, iyul=31, avgust=31,
########                                                    sentyabr=30, oktyabr=31, noyabr=30, dekabr=31))
########
########                        
########                        while ishora:
########                                b_month_name = input("oyni kiriting:\n").lower()
########                                                
########                                if b_month_name in months.keys():
########                                        time_births.append(b_month_name)
########                                        while ishora:
########                                                b_day = int(input("kuni kiriting:\n"))
########                                                if b_day in months[b_month_name]:
########                                                        time_births.append(b_day)
########                                                        ishora = False
########                                                else:
########                                                        print(f"{b_month_name} oyida {b_day}"
########                                                              f"-  kun mavjud emas")
########                                else:
########                                        print(f"{b_month_name} nomli oy mavjud emas")
########
########                                        
########                                        
########                elif b_year not in range(1900,2022,4) and b_year in range(1900,2022):
########                        time_births.append(b_year)
########                        
########
########                        months.update(return_months(yanvar=31, fevral=28, mart=31, aprel=30,
########                                                    may=31, iyun=30, iyul=31, avgust=31,
########                                                    sentyabr=30, oktyabr=31, noyabr=30, dekabr=31))
########                        
########                        while ishora:
########                                b_month_name = input("oyni kiriting:\n").lower()
########                                                
########                                if b_month_name in months.keys():
########                                        time_births.append(b_month_name)
########                                        while ishora:
########                                                b_day = int(input("kuni kiriting:\n"))
########                                                if b_day in months[b_month_name]:
########                                                        time_births.append(b_day)
########                                                        ishora = False
########                                                elif b_day == 29 and b_month_name == 'fevral':
########                                                        print(f"{b_year} - yilning {b_month_name}"
########                                                              f" oyi {b_day}"
########                                                              f" -  kundan iborat emas")
########                                                else:
########                                                        print(f"{b_month_name} oyida {b_day}"
########                                                              f"-  kun mavjud emas")
########                                else:
########                                        print(f"{b_month_name} nomli oy mavjud emas")
########                                
########                                
########                elif b_year > 2022:
########                        print(f"{b_year} yil kelmagan itimos to'g'ri yilni kiritng")
########
########                elif b_year < 1900:
########                        print(f"{b_year} yilda tug'ilgan insonlar qolmagan itimos to'g'ri yilni kiritng")
########                
########        return time_births
######
########print(return_time_births())

       


##def return_time_births():
##        time_births = []
##        day = int(input("Qaysi kunda tug'ilgansiz kiriting:\n"))
##        if day > 31 or day < 1:
##                print("Iltimos to'g'ri kunni kiriting:\n")
##        else:
##                months = return_months()
##                month = input("Qaysi oyda tug'ilgansiz oy nomini kiriting:\n")
##                if day in months[month]:
##                        year = int(input("Qaysi yilda tug'ilgansiz kiriting:\n"))
##                        loccal_months = {}
##                        if year in range(2022,1900,-4):
##                                loccal_months = return_months()
##                        elif year not in range(2022,1900,-4):
##                                loccal_months = return_months(yanvar=31, fevral=28, mart=31, aprel=30,
##                                                       may=31, iyun=30, iyul=31, avgust=31,
##                                                       sentyabr=30, oktyabr=31, noyabr=30, dekabr=31)
##                        elif year > 2022:
##                                print(f"{year} yil kelmagan itimos to'g'ri yilni kiritng")
##
##                        elif year < 1900:
##                                print(f"{year} yilda tug'ilgan insonlar qolmagan itimos to'g'ri yilni kiritng"
##                        
##                        if day in loccal_months[month]:
##                                if day in range(1,10):
##                                        day = '0' + str(day)
##                                month = months_numbers(month)
##                                time_births.append(str(day))
##                                time_births.append(str(month))
##                                time_births.append(str(year))
##                                
##                        else:
##                                print("Iltimos to'g'ri kunni kiriting:\n")
##                elif month not in months.keys():
##                        print(f"{month} nomli oy mavjud emas")
##                        
##                else:
##                        print("Iltimos to'g'ri kunni kiriting:\n")
##        return time_births
##
##
##print(return_time_births())  







##        d_y = int(input("kun:\n"))
##        month = input("oy nomini yozing:\n").lower()
##        y_r = int(input("yil:\n"))
##
##        namber = '0'    
##        if d_y in list(range(1,10)):
##                day = namber + str(d_y)
##        elif d_y in list(range(10,32)):
##                day = d_y
##        else:
##                print("Kunda xatolik bor")
##        months = ["yanvar", "fevral", "mart",  "aprel", 'may',
##                  'iyun', 'iyul', 'avgust', 'sentyabr', 'oktyabr', 'noyabr', 'dekabr']
##        if month in months:
##                for i in range(len(months)):
##                        if month == months[i]:
##                                if month in ["yanvar", "fevral", "mart",  "aprel", 'may',
##                          'iyul', 'iyun', 'avgust', 'sentabr']:
##                                        i = i+1
##                                        month_namber = namber + str(i)
##                                else:
##                                        i = int(i+1)
##                                        month_namber = i
##        else:
##                print("Bunday oy nomi yo'q")
##
##
##        if y_r in list(range(100001)):
##                year = y_r
##        else:
##                del y_r
##









##def year_m(par):
##        months = {}
##        if par in range(2024,1895,-4):
##                months = return_months()
##        elif par not in range(2024,1895,-4):
##                months = return_months(yanvar=31, fevral=28, mart=31, aprel=30,
##                                       may=31, iyun=30, iyul=31, avgust=31,
##                                       sentyabr=30, oktyabr=31, noyabr=30, dekabr=31)
##        return months
##
##
##
##
##
##
##
##def clean_up(par):
##        znaks = [',', '\n', '\t', '#', '(', ')', '_']
##        for z in znaks:
##                par = par.replace(z, '')
##        return par



##def return_months(name, finalday):
##        months = {}
##        i = []
##        for x in range(1,29):
##                i.append(x)
##        if finalday == 29:
##                i.append(29)
##        if finalday >= 30:
##                i.extend([29,30])
##        if finalday == 31:
##                i.append(31)
##        months[name] = i
##        return months




##izoh1 = persons.get(man)
##
##if izoh1 == None:
##        print("Bunday shaxs xaqida ma'lumot yo'q")
##else:
##        print(f"{man} - {izoh1}")








lugat = {
        'telefonlar' : {
                'ali':'iphone X',
                'vali':'galaxy S9',
                'olim':'nokia 3310',
                'orif':'mi 10 pro',
                'anvar':'pixel 3xl'
                },
        'davlatlar' : {'o\'zbekiston': 'Toshkent',
                     'rassiya':'Maskva',
                     'aqsh':'Vashington',
                     'germaniya':'Berlin',
                     'yaponiya':'Tokio',
                     'angliya':'London',
                     'italiya':'Rim',
                     'fransiya':'Parij',
                     'xitoy':'Pekin',
                     'turkiya':'Anqara',
                     'brazilya':'Brazilya',
                     'baa':'Abu-Dabi'
                     },
        'izoh' : {
                'integer':'Butun son',
                'string':'Matn',
                'float':'O\'nlik son',
                'booling':'Mantiqiy qiymat',
                'if':'Agar',
                'elif':'Bo\'lmasa',
                'else':'Aks holda',
                'upper':'Matnni katta harfga aylantirish',
                'lower':'Matnni kichik harfga aylantirish',
                'title':'Matnni har bir so\'zini bosh harfini katta harfga baylantiradi',
                'capitalize':'Matnni birinchi harfini katta harfga aylantiradi',
                'replace':'So\'z va harflarni almashtiradi',
                'sort':'Listni alifbo bo\'yicha tartiblaydi',
                'remove':'Listni elementini o\'chiradi',
                'reverse':'Listni tezkari ko\'rinishda chiqaradi',
                'insert':'Listni bir-biriga qo\'shadi',
                'pop':'Listni elementini index raqami qo\'yilgan holda o\'chiradi',
                'del':'har qanday o\'zgaruvchini o\'chiradi',
                'and':'va',
                'or':'yoki'
                }
        }



##qidiruv = input("Qaysi so'zni bilmoqchisiz:\n").lower()
##
##izoh1 = lugat.get(qidiruv)
##
##if izoh1 == None:
##        print("Bunday so'z mavjud emas")
##else:
##        print(f"{qidiruv} - {izoh1}")
        











##ishora = None
##for k, v in lugat.items():
##        if qidiruv in v:
##                ishora = v[qidiruv]
##
##if ishora:
##        print(f"{qidiruv} - {ishora}")
##else:
##        print("Bunday so'z mavjud emas")



##s = 1
##for k, v in lugat.items():
##        izoh = v.get(qidiruv)
##        
##        if izoh == None and s == len(lugat):
##                print("Bunday so'z mavjud emas")
##        elif izoh != None:
##                print(f"{qidiruv} - {izoh}")
##                s = 0
##        s += 1
                


##s = []
##for k, v in lugat.items():
##        izoh = v.get(qidiruv)
##        if izoh == None:
##                s.append(izoh)
##                if len(s) == len(lugat):
##                        print("Bunday so'z mavjud emas")
##        elif izoh != None:
##                print(f"{qidiruv} - {izoh}")
