# Open Source Zodiac Sign Calculator by  Venkatesh Vanjaku
# Original Source obtained from https://www.w3resource.com/python-exercises/python-conditional-exercise-38.php

print("#######################################################")
print("###############  ZODIAC SIGN CALCULATOR ###############")
print("#######################################################")

fullname = input("Enter your full name: ")
date = int(input("%s, on which date you born: " %fullname))

if date < 31:
    month = input("%s, on which month you born: " % fullname)
    try:
        if month == 'december' or month == 'December' or month == '12':
            sign = 'Sagittarius'\
                if (date < 22)\
                else 'Capricorn'

        elif month == 'january' or month == 'January' or month == '01' or month == '1':
            sign = 'Capricorn'\
                if (date < 20)\
                else 'Aquarius'

        elif month == 'february' or month == 'February' or month == '02' or month == '2':
            sign = 'Aquarius'\
                if (date < 19)\
                else 'Pisces'

        elif month == 'march' or month == 'March' or month == '03' or month == '3':
            sign = 'Pisces'\
                if (date < 21)\
                else 'Aries'

        elif month == 'april' or month == 'April' or month == '04' or month == '4':
            sign = 'Aries'\
                if (date < 20)\
                else 'Taurus'

        elif month == 'may' or month == 'May' or month == '05' or month == '5':
            sign = 'Taurus'\
                if (date < 21)\
                else 'Gemini'

        elif month == 'june' or month == 'June' or month == '06' or month == '6':
            sign = 'Gemini'\
                if (date < 21)\
                else 'Cancer'

        elif month == 'july' or month == 'July' or month == '07' or month == '7':
            sign = 'Cancer'\
                if (date < 23)\
                else 'Leo'

        elif month == 'august' or month == 'August' or month == '08' or month == '8':
            sign = 'Leo'\
                if (date < 23)\
                else 'Virgo'

        elif month == 'september' or month == 'September' or month == '09' or month == '9':
            sign = 'Virgo'\
                if (date < 23)\
                else 'Libra'

        elif month == 'october' or month == 'October' or month == '10':
            sign = 'Libra'\
                if (date < 23)\
                else 'Scorpio'

        elif month == 'november' or month == 'November' or month == '11':
            sign = 'scorpio'\
                if (date < 22)\
                else 'Sagittarius'

        print("[+] %s, your zodiac sign is %s"%(fullname, sign))

        print("##############  THANK YOU ★ VISIT AGAIN  ##############")

    except:
        print("######## Oops!, Something went wrong !! ########")
else:
    print("Invalid Date")
