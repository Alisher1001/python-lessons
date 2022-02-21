
def clean_up_list(par):
        """O'zgaruvchidagi ortiqcha belgilarni olib tashlab
        List ko'rinishida qaytaruvchi funksiya"""
        znaks = [',', '\n', '\t', '-', '(', ')', '=', 'tili', 'til']
        
        for x in znaks:
                par = par.replace(x, '')
        return par.split()









def return_months(**kwargs):
        """Oylar va kuni Dict ko'rinishida qaytaruvchi funksiya"""
        months = {}
        if kwargs:
                for keys, values in kwargs.items():
                        i = []
                        for x in range(1,29):
                                i.append(x)
                        if values == 29:
                                i.append(29)
                        if values >= 30:
                                i.extend([29,30])
                        if values == 31:
                                i.append(31)
                        months[keys] = i
        else:
                kwargs = dict(yanvar=31, fevral=29, mart=31, aprel=30,
                              may=31, iyun=30, iyul=31, avgust=31,
                              sentyabr=30, oktyabr=31, noyabr=30, dekabr=31)
                for keys, values in kwargs.items():
                        i = []
                        for x in range(1,29):
                                i.append(x)
                        if values == 29:
                                i.append(29)
                        if values >= 30:
                                i.extend([29,30])
                        if values == 31:
                                i.append(31)
                        months[keys] = i

        return months








def months_numbers(par):
        """Oylar nomi o'rniga raqam qoyib qaytaruvchi funksiya"""
        x = dict(yanvar='01', fevral='02', mart='03', aprel='04',
        may='05', iyun='06', iyul='07', avgust='08',
        sentyabr='09', oktyabr='10', noyabr='11', dekabr='12')
        return x[par]









def return_time_births():
        """Foydalanuvchidan tug'ilgan vaqtini so'rab
        List ko'rinishida qaytaruvchi funksiya"""
        ishora = True
        while  ishora:
        
                def determine_the_day():
                        while True:
                                day = int(input("Qaysi kunda tug'ilgansiz kunni kiriting:\n"))
                                if day > 31 or day < 1:
                                        print(f"Oylarda {day} - kun yo'q "
                                              f"itimos to'g'ri kunni kiriting:\n")
                                else:
                                        break
                        return day
                day = determine_the_day()



                def determine_the_month(day):
                        while True:
                                months = return_months()
                                month = input("Qaysi oyda tug'ilgansiz oy nomini kiriting:\n").lower()
                                if month not in months.keys():
                                        print(f"{month.title()} nomli oy mavjud emas iltimos to'g'ri oyni kiriting")
                                elif day in months[month]:
                                        break
                                else:
                                        print(f"{month.title()} oyida {day} - kunni yo'q "
                                              f"iltimos to'g'ri kunni kiriting:\n")
                                        month = 0
                                        break
                        return month
                month = determine_the_month(day)


                if not month:
                        continue
                def determine_the_year(day, month):
                        time_births = []
                        while True:
                                year = int(input("Qaysi yilda tug'ilgansiz yilni kiriting:\n"))
                                loccal_months = {}
                                if year in range(1896,2022,4):
                                        loccal_months = return_months()
                                if year not in range(1896,2022,4) and year in range(1896,2022):
                                        loccal_months = return_months(yanvar=31, fevral=28, mart=31, aprel=30,
                                                                        may=31, iyun=30, iyul=31, avgust=31,
                                                                        sentyabr=30, oktyabr=31, noyabr=30, dekabr=31)
                                if year > 2022:
                                        print(f"{year} - yil kelmagan itimos "
                                                f"to'g'ri yilni kiritng")

                                elif year < 1900:
                                        print(f"{year} - yilda tug'ilgan insonlar "
                                                f"qolmagan itimos to'g'ri yilni kiritng")

                                elif day in loccal_months[month]:
                                        if day in range(1,10):
                                                day = '0' + str(day)
                                        time_births.append(str(day))
                                        month = months_numbers(month)
                                        time_births.append(str(month))
                                        time_births.append(str(year))
                                        break
                                else:
                                        print(f"{year} - yilning {month} oyida "
                                                f"{day} - kun yo'q iltimos "
                                                      f"to'g'ri kunni kiriting:\n")
                                        time_births = 0
                                        break
                        return time_births
                time_births = determine_the_year(day, month)
                if not time_births:
                        continue
                else:
                        ishora = False
                        
        return time_births









persons = {}
ishora = True
savol = "Yana ma'lumot kiritasizmi (ha/yo'q)\n"

while ishora:
        surname = input("Familyangizni kiriting:\n").lower()
        name = input("Ismingizni kiriting:\n").lower()
        nationality = clean_up_list(input(f"Hurmatli {surname.title()} {name.title()}"
                            f" fuqoroligingizni kiriting:\n").lower())
        print(f"Hurmatli {surname.title()} {name.title()} qachon tug'ilgansiz (kun/oy/yil):\n")

        dmy = return_time_births()
        day, month_namber, year = dmy
        information = input(f"Hurmatli {surname.title()} {name.title()} "
                                     f"ma'lumotingiz qanday:\n").lower()

        programming_languages = clean_up_list(input(f"Hurmatli {surname.title()} {name.title()} "
                                        f"qaysi dasturlash tillarini bilasiz:\n").lower())

        foreign_languages = clean_up_list(input(f"Hurmatli {surname.title()} {name.title()} "
                                        f"qaysi xorijiy tillarini bilasiz:\n").lower())
        
        def gender_reveal(surname, name):
                """Foydalanuvchidan jinsini so'rab qaytaruvchi funksiya"""
                while True:
                        question = input(f"Hurmatli {surname.title()} {name.title()} jinsingizni kiriting:\n").lower()
                        if question in ['erkak', 'ayol']:
                                break
                        else:
                                print(f"{question.title()} jinsi mavjud emas iltimos to'g'ri ma'lumotni kiriting")
                return question

        species = gender_reveal(surname, name)
        
        place = input(f"Hurmatli {surname.title()} {name.title()} qaysi joyda tug'ilgansiz:\n").lower()

        def do_dict(**kwargs):
                """O'zgaruvchilardagi ma'lumotlarni Dict ko'rinishida qaytaruvchi funksiya"""
                return kwargs

        searchs = surname + ' ' + name
        
        persons.update({searchs:do_dict(k_surname=surname, k_name=name,
        k_nationality=nationality, k_day=day,k_month_namber=month_namber,
        k_year=year, k_information=information,
        k_programming_languages=programming_languages, k_foreign_languages=foreign_languages,
        k_species=species, k_place=place)})
        
        print(persons)
                
        accuracy = input(savol).lower()

        if accuracy != 'ha':
                ishora = False


def print_screen(persons):
        """List dagi ma'lumotlarni konsolga chiqaruvchi funksiya"""
        for k, q in persons.items():
                print(f"{k.title()} haqida ma'lumotlar:")
                print(f"familya: \n{q['k_surname'].title()} \nism: \n{q['k_name'].title()}")
                print("fuqorolik:")
                for y in q["k_nationality"]:
                        print(f"{y.title()}", end='')
                print(f"\ntug'ilgan sana: \n{q['k_day']}.{q['k_month_namber']}.{q['k_year']} \n"
                f"jinsi: \n{q['k_species'].title()} \nma'lumoti: \n{q['k_information'].title()}")
                print("biladigan dasturlash tillari:")
                for x in q["k_programming_languages"]:
                        print(f"{x.upper()}")
                print("biladigan xorijiy tillari:")
                for x in q["k_foreign_languages"]:
                        print(f"{x.capitalize()}")
                print(f"tug'ilgan joy: \n{q['k_place'].title()}")
                        
                print(f'berilgan sana \n30.11.2021')
                print(f'amal qilish mudati \n01.01.2031')

print_screen(persons)










def search_man():
        """Foydalanuvchidan qaysi shaxs haqida ma'lumot kerak ekanligini so'rovchi funksiya"""
        while True:
                copy_p = {}
                man = input("Qaysi shaxs xaqida ma'lumot kerak\n"
                            "familya, ismini kiriting:\n").lower()
                if man in persons:
                        print(f"{man}\n{persons[man]}")
                        copy_p[man] = persons[man].copy()                        
                        print_screen(copy_p)
                else:
                        print("Bunday shaxs xaqida ma'lumot yo'q")
                question = input("Yana ma'lumot kerakmi ? (ha/yo'q)\n")
                if question != 'ha':
                        break

search_man()






