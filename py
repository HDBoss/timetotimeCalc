import time
print("*---------------------------------------------------------------------------------------------------------------------------------------------------------------*")
print("[*] This is a calculator to calculate days into months, months into years, and all those other combonations.")
print("[*] You can convert with (nanoseconds), (microseconds), (milliseconds), (seconds), (minutes), (hours), (days), (weeks), (months), (years), (decades), (centuries), \n(milleniums), (megaannums), and (eons).")
print("[*] Type what is in the parenthesis.")
print("*---------------------------------------------------------------------------------------------------------------------------------------------------------------*")
def nanotomicro(a):
    return a / 1000
def nanotomilli(a):
    return a / 1000000
def nanotosec(a):
    return a / 1000000000
def nanotominute(a):
    return a / 60000000000
def nanotohour(a):
    return a / 3600000000000
def nanotoday(a):
    return a / 86400000000000
def nanotoweek(a):
    return a / 604800000000000
def nanotomonth(a):
    return a / 2628000000000000
def nanotoyear(a):
    return a / 31540000000000000
def nanotodecade(a):
    return a / 315400000000000000
def nanotocentury(a):
    return a / 3154000000000000000
def nanotomillenium(a):
    return a / 31540000000000000000
def nanotomegaannum(a):
    return a / 31540000000000000000000
def nanotoeon(a):
    return a / 31540000000000000000000000
def microtonano(a):
    return a * 1000
def microtomilli(a):
    return a / 1000
def microtosec(a):
    return a / 1000000
def microtominute(a):
    return a / 60000000
def microtohour(a):
    return a / 3600000000
def microtoday(a):
    return a / 86400000000
def microtoweek(a):
    return a / 604800000000
def microtomonth(a):
    return a / 2628000000000
def microtoyear(a):
    return a / 31540000000000
def microtodecade(a):
    return a / 315400000000000
def microtocentury(a):
    return a / 3154000000000000
def microtomillenium(a):
    return a / 31540000000000000
def microtomegaannum(a):
    return a / 31540000000000000000
def microtoeon(a):
    return a / 31540000000000000000000
def millitonano(a):
    return a * 1000000
def millitomicro(a):
    return a * 1000
def millitosec(a):
    return a / 1000
def millitominute(a):
    return a / 60000
def millitohour(a):
    return a / 3600000
def millitoday(a):
    return a / 86400000
def millitoweek(a):
    return a / 604800000
def millitomonth(a):
    return a / 2628000000
def millitoyear(a):
    return a / 31540000000
def millitodecade(a):
    return a / 315400000000
def millitocentury(a):
    return a / 3154000000000
def millitomillenium(a):
    return a / 31540000000000
def millitomegaannum(a):
    return a / 31540000000000000
def millitoeon(a):
    return a / 31540000000000000000
def sectonano(a):
    return a * 1000000000
def sectomicro(a):
    return a * 1000000
def sectomilli(a):
    return a * 1000
def sectominute(a):
    return a / 60
def sectohour(a):
    return a / 3600
def sectoday(a):
    return a / 86400
def sectoweek(a):
    return a / 604800
def sectomonth(a):
    return a / 2628000
def sectoyear(a):
    return a / 31540000
def sectodecade(a):
    return a / 315400000
def sectocentury(a):
    return a / 3154000000
def sectomillenium(a):
    return a / 31540000000
def sectomegaannum(a):
    return a / 31540000000000
def sectoeon(a):
    return a / 31540000000000000
def minutetonano(a):
    return a * 60000000000
def minutetomicro(a):
    return a * 60000000
def minutetomilli(a):
    return a * 60000
def minutetosec(a):
    return a * 60
def minutetohour(a):
    return a / 60
def minutetoday(a):
    return a / 1440
def minutetoweek(a):
    return a / 10080
def minutetomonth(a):
    return a / 43800
def minutetoyear(a):
    return a / 525600
def minutetodecade(a):
    return a / 5256000
def minutetocentury(a):
    return a / 52560000
def minutetomillenium(a):
    return a / 525600000
def minutetomegaannum(a):
    return a / 525600000000
def minutetoeon(a):
    return a / 525600000000000
def hourtonano(a):
    return a * 3600000000000
def hourtomicro(a):
    return a * 3600000000
def hourtomilli(a):
    return a * 3600000
def hourtosec(a):
    return a * 3600
def hourtominute(a):
    return a * 60
def hourtoday(a):
    return a / 24
def hourtoweek(a):
    return a / 168
def hourtomonth(a):
    return a / 730
def hourtoyear(a):
    return a / 8760
def hourtodecade(a):
    return a / 87600
def hourtocentury(a):
    return a / 876000
def hourtomillenium(a):
    return a / 8760000
def hourtomegaannum(a):
    return a / 8760000000
def hourtoeon(a):
    return a / 8760000000000
def daytonano(a):
    return a * 86400000000000
def daytomicro(a):
    return a * 86400000000
def daytomilli(a):
    return a * 86400000
def daytosec(a):
    return a * 86400
def daytominute(a):
    return a * 1440
def daytohour(a):
    return a * 24
def daytoweek(a):
    return a / 7
def daytomonth(a):
    return a / 30.4
def daytoyear(a):
    return a / 365
def daytodecade(a):
    return a / 3650
def daytocentury(a):
    return a / 36500
def daytomillenium(a):
    return a / 365000
def daytomegaannum(a):
    return a / 365000000
def daytoeon(a):
    return a / 365000000000
def weektonano(a):
    return a * 604800000000000
def weektomicro(a):
    return a * 604800000000
def weektomilli(a):
    return a * 604800000
def weektosec(a):
    return a * 604800
def weektominute(a):
    return a * 10080
def weektohour(a):
    return a * 168
def weektoday(a):
    return a * 7
def weektomonth(a):
    return a / 4.345
def weektoyear(a):
    return a / 52.143
def weektodecade(a):
    return a / 521
def weektocentury(a):
    return a / 5214
def weektomillenium(a):
    return a / 52143
def weektomegaannum(a):
    return a / 52143000
def weektoeon(a):
    return a / 52143000000
def monthtonano(a):
    return a * 2628000000000000
def monthtomicro(a):
    return a * 2628000000000
def monthtomilli(a):
    return a * 2.628000000
def monthtosec(a):
    return a * 2628000
def monthtominute(a):
    return a * 43800
def monthtohour(a):
    return a * 730
def monthtoday(a):
    return a * 30.4
def monthtoweek(a):
    return a * 4.345
def monthtoyear(a):
    return a / 12
def monthtodecade(a):
    return a / 120
def monthtocentury(a):
    return a / 1200
def monthtomillenium(a):
    return a / 12000
def monthtomegaannum(a):
    return a / 12000000
def monthtoeon(a):
    return a / 12000000000
def yeartonano(a):
    return a * 31540000000000000
def yeartomicro(a):
    return a * 31540000000000
def yeartomilli(a):
    return a * 31540000000
def yeartosec(a):
    return a * 31540000
def yeartominute(a):
    return a * 525600
def yeartohour(a):
    return a * 8760
def yeartoday(a):
    return a * 365
def yeartoweek(a):
    return a * 52.143
def yeartomonth(a):
    return a * 12
def yeartodecade(a):
    return a / 10
def yeartocentury(a):
    return a / 100
def yeartomillenium(a):
    return a / 1000
def yeartomegaannum(a):
    return a / 1000000
def yeartoeon(a):
    return a / 1000000000
def decadetonano(a):
    return a * 315400000000000000
def decadetomicro(a):
    return a * 315400000000000
def decadetomilli(a):
    return a * 315400000000
def decadetosec(a):
    return a * 315400000
def decadetominute(a):
    return a * 5256000
def decadetohour(a):
    return a * 87600
def decadetoday(a):
    return a * 3650
def decadetoweek(a):
    return a * 521
def decadetomonth(a):
    return a * 120
def decadetoyear(a):
    return a * 10
def decadetocentury(a):
    return a / 10
def decadetomillenium(a):
    return a / 100
def decadetomegaannum(a):
    return a / 100000
def decadetoeon(a):
    return a / 100000000
def centurytonano(a):
    return a * 3154000000000000000
def centurytomicro(a):
    return a * 3154000000000000
def centurytomilli(a):
    return a * 3154000000000
def centurytosec(a):
    return a * 3154000000
def centurytominute(a):
    return a * 52560000
def centurytohour(a):
    return a * 876000
def centurytoday(a):
    return a * 36500
def centurytoweek(a):
    return a * 5214
def centurytomonth(a):
    return a * 1200
def centurytoyear(a):
    return a * 100
def centurytodecade(a):
    return a * 10
def centurytomillenium(a):
    return a / 10
def centurytomegaannum(a):
    return a / 10000
def centurytoeon(a):
    return a / 10000000
def milleniumtonano(a):
    return a * 31540000000000000000
def milleniumtomicro(a):
    return a * 31540000000000000
def milleniumtomilli(a):
    return a * 31540000000000
def milleniumtosec(a):
    return a * 31540000000
def milleniumtominute(a):
    return a * 525600000
def milleniumtohour(a):
    return a * 8760000
def milleniumtoday(a):
    return a * 365000
def milleniumtoweek(a):
    return a * 52143
def milleniumtomonth(a):
    return a * 12000
def milleniumtoyear(a):
    return a * 1000
def milleniumtodecade(a):
    return a * 100
def milleniumtocentury(a):
    return a * 10
def milleniumtomegaannum(a):
    return a / 1000
def milleniumtoeon(a):
    return a / 1000000
def megaannumtonano(a):
    return a * 31540000000000000000000
def megaannumtomicro(a):
    return a * 31540000000000000000
def megaannumtomilli(a):
    return a * 31540000000000000
def megaannumtosec(a):
    return a * 31540000000000
def megaannumtominute(a):
    return a * 525600000000
def megaannumtohour(a):
    return a * 8760000000
def megaannumtoday(a):
    return a * 365000000
def megaannumtoweek(a):
    return a * 52143000
def megaannumtomonth(a):
    return a * 12000000
def megaannumtoyear(a):
    return a * 1000000
def megaannumtodecade(a):
    return a * 100000
def megaannumtocentury(a):
    return a * 10000
def megaannumtomillenium(a):
    return a * 1000
def megaannumtoeon(a):
    return a / 1000
def eontonano(a):
    return a * 31540000000000000000000000
def eontomicro(a):
    return a * 31540000000000000000000
def eontomilli(a):
    return a * 31540000000000000000
def eontosec(a):
    return a * 31540000000000000
def eontominute(a):
    return a * 525600000000000
def eontohour(a):
    return a * 8760000000000
def eontoday(a):
    return a * 365000000000
def eontoweek(a):
    return a * 52143000000
def eontomonth(a):
    return a * 12000000000
def eontoyear(a):
    return a * 1000000000
def eontodecade(a):
    return a * 100000000
def eontocentury(a):
    return a * 10000000
def eontomillenium(a):
    return a * 1000000
def eontomegaannum(a):
    return a * 1000
ask = True
while ask:
    a1 = input ("[*] What amount of time would you like to convert from? ")
    b1 = input ("[*] What amount of time would you like to convert to? ")
    a = float (input ("How many " + a1 + " would you like to convert? "))
    answer = daytomonth (a)
    if a1 == "days" and b1 == "months":
        answer = round (daytomonth (a))
        answer2 = daytomonth (a)
    elif a1 == "months" and b1 == "days":
        answer = monthtoday (a)
        answer2 = round (monthtoday (a))
    elif a1 == "months" and b1 == "years":
        answer = monthtoyear (a)
        answer2 = round (monthtoyear (a))
    elif a1 == "years" and b1 == "months":
        answer = yeartomonth (a)
        answer2 = round (yeartomonth (a))
    elif a1 == "days" and b1 == "years":
        answer = daytoyear (a)
        answer2 = round (daytoyear (a))
    elif a1 == "years" and b1 == "days":
        answer = yeartoday (a)
        print ("The answer to the equation was: ", answer, " " + b1 + ".")
    elif a1 == "nanoseconds" and b1 == "microseconds":
        answer = nanotomicro (a)
        answer2 = round (nanotomicro (a))
    elif a1 == "nanoseconds" and b1 == "milliseconds":
        answer = nanotomilli (a)
        answer2 = round (nanotomilli (a))
    elif a1 == "nanoseconds" and b1 == "seconds":
        answer = nanotosec (a)
        answer2 = round (nanotosec (a))
    elif a1 == "nanoseconds" and b1 == "minutes":
        answer = nanotominute (a)
        answer2 = round (nanotominute (a))
    elif a1 == "nanoseconds" and b1 == "hours":
        answer = nanotohour (a)
        answer2 = round (nanotohour (a))
    elif a1 == "nanoseconds" and b1 == "days":
        answer = nanotoday (a)
        answer2 = round (nanotoday (a))
    elif a1 == "nanoseconds" and b1 == "weeks":
        answer = nanotoweek (a)
        answer2 = round (nanotoweek (a))
    elif a1 == "nanoseconds" and b1 == "months":
        answer = nanotomonth (a)
        answer2 = round (nanotomonth (a))
    elif a1 == "nanoseconds" and b1 == "years":
        answer = nanotoyear (a)
        answer2 = round (nanotoyear (a))
    elif a1 == "nanoseconds" and b1 == "decade":
        answer = nanotodecade (a)
        answer2 = round (nanotodecade (a))
    elif a1 == "nanoseconds" and b1 == "centuries":
        answer = nanotocentury (a)
        answer2 = round (nanotocentury (a))
    elif a1 == "nanoseconds" and b1 == "milleniums":
        answer = nanotomillenium (a)
        answer2 = round (nanotomillenium (a))
    elif a1 == "nanoseconds" and b1 == "megaannums":
        answer = nanotomegaannum (a)
        answer2 = round (nanotomegaannum (a))
    elif a1 == "nanoseconds" and b1 == "eons":
        answer = nanotoeon (a)
        answer2 = round (nanotoeon (a))
    elif a1 == "microseconds" and b1 == "nanoseconds":
        answer = microtonano (a)
    elif a1 == "microseconds" and b1 == "milliseconds":
        answer = microtomilli (a)
        answer2 = round (microtomilli (a))
    elif a1 == "microseconds" and b1 == "seconds":
        answer = microtosec (a)
        answer2 = round (microtosec (a))
    elif a1 == "microseconds" and b1 == "minutes":
        answer = microtominute (a)
        answer2 = round (microtominute (a))
    elif a1 == "microseconds" and b1 == "hours":
        answer = microtohour (a)
        answer2 = round (microtohour (a))
    elif a1 == "microseconds" and b1 == "days":
        answer = microtoday (a)
        answer2 = round (microtoday (a))
    elif a1 == "microseconds" and b1 == "weeks":
        answer = microtoweek (a)
        answer2 = round (microtoweek (a))
    elif a1 == "microseconds" and b1 == "months":
        answer = microtomonth (a)
        answer2 = round (microtomonth (a))
    elif a1 == "microseconds" and b1 == "years":
        answer = microtoyear (a)
        answer2 = round (microtoyear (a))
    elif a1 == "microseconds" and b1 == "decades":
        answer = microtodecade (a)
        answer2 = round (microtodecade (a))
    elif a1 == "microseconds" and b1 == "centuries":
        answer = microtocentury (a)
        answer2 = round (microtocentury (a))
    elif a1 == "microseconds" and b1 == "milleniums":
        answer = microtomillenium (a)
        answer2 = round (microtomillenium (a))
    elif a1 == "microseconds" and b1 == "megaannums":
        answer = microtomegaannum (a)
        answer2 = round (microtomegaannum (a))
    elif a1 == "microseconds" and b1 == "eons":
        answer = microtoeon (a)
        answer2 = round (microtoeon (a))
    elif a1 == "milliseconds" and b1 == "nanoseconds":
        answer = millitonano (a)
    elif a1 == "milliseconds" and b1 == "microseconds":
        answer = millitomicro (a)
    elif a1 == "milliseconds" and b1 == "seconds":
        answer = millitosec (a)
        answer2 = round (millitosec (a))
    elif a1 == "milliseconds" and b1 == "minutes":
        answer = millitominute (a)
        answer2 = round (millitominute (a))
    elif a1 == "milliseconds" and b1 == "hours":
        answer = millitohour (a)
        answer2 = round (millitohour (a))
    elif a1 == "milliseconds" and b1 == "days":
        answer = millitoday (a)
        answer2 = round (millitoday (a))
    elif a1 == "milliseconds" and b1 == "weeks":
        answer = millitoweek (a)
        answer2 = round (millitoweek (a))
    elif a1 == "milliseconds" and b1 == "months":
        answer = millitomonth (a)
        answer2 = round (millitomonth (a))
    elif a1 == "milliseconds" and b1 == "years":
        answer = millitoyear (a)
        answer2 = round (millitoyear (a))
    elif a1 == "milliseconds" and b1 == "decades":
        answer = millitodecade (a)
        answer2 = round (millitodecade (a))
    elif a1 == "milliseconds" and b1 == "centuries":
        answer = millitocentury (a)
        answer2 = round (millitocentury (a))
    elif a1 == "milliseconds" and b1 == "milleniums":
        answer = millitomillenium (a)
        answer2 = round (millitomillenium (a))
    elif a1 == "milliseconds" and b1 == "megaannums":
        answer = millitomegaannum (a)
        answer2 = round (millitomegaannum (a))
    elif a1 == "milliseconds" and b1 == "eons":
        answer = millitoeon (a)
        answer2 = round (millitoeon (a))
    elif a1 == "seconds" and b1 == "nanoseconds":
        answer = sectonano (a)
    elif a1 == "seconds" and b1 == "microseconds":
        answer = sectomicro (a)
    elif a1 == "seconds" and b1 == "milliseconds":
        answer = sectomilli (a)
    elif a1 == "seconds" and b1 == "minutes":
        answer = sectominute (a)
        answer2 = round (sectominute (a))
    elif a1 == "seconds" and b1 == "hours":
        answer = sectohour (a)
        answer2 = round (sectohour (a))
    elif a1 == "seconds" and b1 == "days":
        answer = sectoday (a)
        answer2 = round (sectoday (a))
    elif a1 == "seconds" and b1 == "weeks":
        answer = sectoweek (a)
        answer2 = round (sectoweek (a))
    elif a1 == "seconds" and b1 == "months":
        answer = sectomonth (a)
        answer2 = round (sectomonth (a))
    elif a1 == "seconds" and b1 == "years":
        answer = sectoyear (a)
        answer2 = round (sectoyear (a))
    elif a1 == "seconds" and b1 == "decades":
        answer = sectodecade (a)
        answer2 = round (sectodecade (a))
    elif a1 == "seconds" and b1 == "centuries":
        answer = sectocentury (a)
        answer2 = round (sectocentury (a))
    elif a1 == "seconds" and b1 == "milleniums":
        answer = sectomillenium (a)
        answer2 = round (sectomillenium (a))
    elif a1 == "seconds" and b1 == "megaannums":
        answer = sectomegaannum (a)
        answer2 = round (sectomegaannum (a))
    elif a1 == "seconds" and b1 == "eons":
        answer = sectoeon (a)
        answer2 = round (sectoeon (a))
    elif a1 == "minutes" and b1 == "nanoseconds":
        answer = minutetonano (a)
    elif a1 == "minutes" and b1 == "microseconds":
        answer = minutetomicro (a)
    elif a1 == "minutes" and b1 == "milliseconds":
        answer = minutetomilli (a)
    elif a1 == "minutes" and b1 == "seconds":
        answer = minutetosec (a)
    elif a1 == "minutes" and b1 == "hours":
        answer = minutetohour (a)
        answer2 = round (minutetohour (a))
    elif a1 == "minutes" and b1 == "days":
        answer = minutetoday (a)
        answer2 = round (minutetoday (a))
    elif a1 == "minutes" and b1 == "weeks":
        answer = minutetoweek (a)
        answer2 = round (minutetoweek (a))
    elif a1 == "minutes" and b1 == "months":
        answer = minutetomonth (a)
        answer2 = round (minutetomonth (a))
    elif a1 == "minutes" and b1 == "years":
        answer = minutetoyear (a)
        answer2 = round (minutetoyear (a))
    elif a1 == "minutes" and b1 == "decades":
        answer = minutetodecade (a)
        answer2 = round (minutetodecade (a))
    elif a1 == "minutes" and b1 == "centuries":
        answer = minutetocentury (a)
        answer2 = round (minutetocentury (a))
    elif a1 == "minutes" and b1 == "milleniums":
        answer = minutetomillenium (a)
        answer2 = round (minutetomillenium (a))
    elif a1 == "minutes" and b1 == "megaannums":
        answer = minutetomegaannum (a)
        answer2 = round (minutetomegaannum (a))
    elif a1 == "minutes" and b1 == "eons":
        answer = minutetoeon (a)
        answer2 = round (minutetoeon (a))
    elif a1 == "hours" and b1 == "nanoseconds":
        answer = hourtonano (a)
    elif a1 == "hours" and b1 == "microseconds":
        answer = hourtomicro (a)
        print ("The answer to the equation was: ", answer, " " + b1 + ".")
    elif a1 == "hours" and b1 == "milliseconds":
        answer = hourtomilli (a)
        print ("The answer to the equation was: ", answer, " " + b1 + ".")
    elif a1 == "hours" and b1 == "seconds":
        answer = hourtosec (a)
        print ("The answer to the equation was: ", answer, " " + b1 + ".")
    elif a1 == "hours" and b1 == "minutes":
        answer = hourtominute (a)
        print ("The answer to the equation was: ", answer, " " + b1 + ".")
    elif a1 == "hours" and b1 == "days":
        answer = hourtoday (a)
        answer2 = round (hourtoday (a))
    elif a1 == "hours" and b1 == "weeks":
        answer = hourtoweek (a)
        answer2 = round (hourtoweek (a))
    elif a1 == "hours" and b1 == "months":
        answer = hourtomonth (a)
        answer2 = round (hourtomonth (a))
    elif a1 == "hours" and b1 == "years":
        answer = hourtoyear (a)
        answer2 = round (hourtoyear (a))
    elif a1 == "hours" and b1 == "decades":
        answer = hourtodecade (a)
        answer2 = round (hourtodecade (a))
    elif a1 == "hours" and b1 == "centuries":
        answer = hourtocentury (a)
        answer2 = round (hourtocentury (a))
    elif a1 == "hours" and b1 == "milleniums":
        answer = hourtomillenium (a)
        answer2 = round (hourtomillenium (a))
    elif a1 == "hours" and b1 == "megaannums":
        answer = hourtomegaannum (a)
        answer2 = round (hourtomegaannum (a))
    elif a1 == "hours" and b1 == "eons":
        answer = hourtoeon (a)
        answer2 = round (hourtoeon (a))
    elif a1 == "days" and b1 == "nanoseconds":
        answer = daytonano (a)
    elif a1 == "days" and b1 == "microseconds":
        answer = daytomicro (a)
    elif a1 == "days" and b1 == "milliseconds":
        answer = daytomilli (a)
    elif a1 == "days" and b1 == "seconds":
        answer = daytosec (a)
    elif a1 == "days" and b1 == "minutes":
        answer = daytominute (a)
    elif a1 == "days" and b1 == "hours":
        answer = daytohour (a)
    elif a1 == "days" and b1 == "weeks":
        answer = daytoweek (a)
        answer2 = round (daytoweek (a))
    elif a1 == "days" and b1 == "months":
        answer = daytoweek (a)
        answer2 = round (daytoweek (a))
    elif a1 == "days" and b1 == "years":
        answer = daytoyear (a)
        answer2 = round (daytoyear (a))
    elif a1 == "days" and b1 == "decades":
        answer = daytodecade (a)
        answer2 = round (daytodecade (a))
    elif a1 == "days" and b1 == "centuries":
        answer = daytocentury (a)
        answer2 = round (daytocentury (a))
    elif a1 == "days" and b1 == "milleniums":
        answer = daytomillenium (a)
        answer2 = round (daytomillenium (a))
    elif a1 == "days" and b1 == "megaannums":
        answer = daytomegaannum (a)
        answer2 = round (daytomegaannum (a))
    elif a1 == "days" and b1 == "eons":
        answer = daytoeon (a)
        answer2 = round (daytoeon (a))
    elif a1 == "weeks" and b1 == "nanoseconds":
        answer = weektonano (a)
    elif a1 == "weeks" and b1 == "microseconds":
        answer = weektomicro (a)
    elif a1 == "weeks" and b1 == "milliseconds":
        answer = weektomilli (a)
    elif a1 == "weeks" and b1 == "seconds":
        answer = weektosec (a)
    elif a1 == "weeks" and b1 == "minutes":
        answer = weektominute (a)
    elif a1 == "weeks" and b1 == "hours":
        answer = weektohour (a)
    elif a1 == "weeks" and b1 == "days":
        answer = weektoday (a)
    elif a1 == "weeks" and b1 == "months":
        answer = weektomonth (a)
        answer2 = round (weektomonth (a))
    elif a1 == "weeks" and b1 == "years":
        answer = weektoyear (a)
        answer2 = round (weektoyear (a))
    elif a1 == "weeks" and b1 == "decades":
        answer = weektodecade (a)
        answer2 = round (weektodecade (a))
    elif a1 == "weeks" and b1 == "centuries":
        answer = weektocentury (a)
        answer2 = round (weektocentury (a))
    elif a1 == "weeks" and b1 == "milleniums":
        answer = weektomillenium (a)
        answer2 = round (weektomillenium (a))
    elif a1 == "weeks" and b1 == "megaannums":
        answer = weektomegaannum (a)
        answer2 = round (weektomegaannum (a))
    elif a1 == "weeks" and b1 == "eons":
        answer = weektoeon (a)
        answer2 = round (weektoeon (a))
    elif a1 == "months" and b1 == "nanoseconds":
        answer = monthtonano (a)
    elif a1 == "months" and b1 == "microseconds":
        answer = monthtomicro (a)
    elif a1 == "months" and b1 == "milliseconds":
        answer = monthtomilli (a)
    elif a1 == "months" and b1 == "seconds":
        answer = monthtosec (a)
    elif a1 == "months" and b1 == "minutes":
        answer = monthtominute (a)
    elif a1 == "months" and b1 == "hours":
        answer = monthtohour (a)
    elif a1 == "months" and b1 == "days":
        answer = monthtoday (a)
    elif a1 == "months" and b1 == "weeks":
        answer = monthtoweek (a)
    elif a1 == "months" and b1 == "years":
        answer = monthtoyear (a)
        answer2 = round (monthtoyear (a))
    elif a1 == "months" and b1 == "decades":
        answer = monthtodecade (a)
        answer2 = round (monthtodecade (a))
    elif a1 == "months" and b1 == "centuries":
        answer = monthtocentury (a)
        answer2 = round (monthtocentury (a))
    elif a1 == "months" and b1 == "milleniums":
        answer = monthtomillenium (a)
        answer2 = round (monthtomillenium (a))
    elif a1 == "months" and b1 == "megaannums":
        answer = monthtomillenium (a)
        answer2 = round (monthtomillenium (a))
    elif a1 == "months" and b1 == "eons":
        answer = monthtoeon (a)
        answer2 = round (monthtoeon (a))
    elif a1 == "years" and b1 == "nanoseconds":
        answer = yeartonano (a)
    elif a1 == "years" and b1 == "microseconds":
        answer = yeartomicro (a)
    elif a1 == "years" and b1 == "milliseconds":
        answer = yeartomilli (a)
    elif a1 == "years" and b1 == "seconds":
        answer = yeartosec (a)
    elif a1 == "years" and b1 == "minutes":
        answer = yeartominute (a)
    elif a1 == "years" and b1 == "hours":
        answer = yeartohour (a)
    elif a1 == "years" and b1 == "days":
        answer = yeartoday (a)
    elif a1 == "years" and b1 == "weeks":
        answer = yeartoweek (a)
    elif a1 == "years" and b1 == "months":
        answer = yeartomonth (a)
    elif a1 == "years" and b1 == "decades":
        answer = yeartodecade (a)
        answer2 = round (yeartodecade (a))
    elif a1 == "years" and b1 == "centuries":
        answer = yeartodecade (a)
        answer2 = round (yeartocentury (a))
    elif a1 == "years" and b1 == "milleniums":
        answer = yeartomillenium (a)
        answer2 = round (yeartomillenium (a))
    elif a1 == "years" and b1 == "megaannums":
        answer = yeartomegaannum (a)
        answer2 = round (yeartomegaannum (a))
    elif a1 == "years" and b1 == "eons":
        answer = yeartoeon (a)
        answer2 = round (yeartoeon (a))
    elif a1 == "decades" and b1 == "nanoseconds":
        answer = decadetonano (a)
    elif a1 == "decades" and b1 == "microseconds":
        answer = decadetomicro (a)
    elif a1 == "decades" and b1 == "milliseconds":
        answer = decadetomilli (a)
    elif a1 == "decades" and b1 == "seconds":
        answer = decadetosec (a)
    elif a1 == "decades" and b1 == "minutes":
        answer = decadetominute (a)
    elif a1 == "decades" and b1 == "hours":
        answer = decadetohour (a)
    elif a1 == "decades" and b1 == "days":
        answer = decadetoday (a)
    elif a1 == "decades" and b1 == "weeks":
        answer = decadetoweek (a)
    elif a1 == "decades" and b1 == "months":
        answer = decadetomonth (a)
    elif a1 == "decades" and b1 == "years":
        answer = decadetoyear (a)
    elif a1 == "decades" and b1 == "centuries":
        answer = decadetocentury (a)
        answer2 = round (decadetocentury (a))
    elif a1 == "decades" and b1 == "milleniums":
        answer = decadetomillenium (a)
        answer2 = round (decadetomillenium (a))
    elif a1 == "decades" and b1 == "megaannums":
        answer = decadetomegaannum (a)
        answer2 = round (decadetomegaannum (a))
    elif a1 == "decades" and b1 == "eons":
        answer = decadetoeon (a)
        answer2 = round (decadetoeon (a))
    elif a1 == "centuries" and b1 == "nanoseconds":
        answer = centurytonano (a)
    elif a1 == "centuries" and b1 == "microseconds":
        answer = centurytomicro (a)
    elif a1 == "centuries" and b1 == "milliseconds":
        answer = centurytomilli (a)
    elif a1 == "centuries" and b1 == "seconds":
        answer = centurytosec (a)
    elif a1 == "centuries" and b1 == "minutes":
        answer = centurytominute (a)
    elif a1 == "centuries" and b1 == "hours":
        answer = centurytohour (a)
    elif a1 == "centuries" and b1 == "days":
        answer = centurytoday (a)
    elif a1 == "centuries" and b1 == "weeks":
        answer = centurytoweek (a)
    elif a1 == "centuries" and b1 == "months":
        answer = centurytomonth (a)
    elif a1 == "centuries" and b1 == "years":
        answer = centurytoyear (a)
    elif a1 == "centuries" and b1 == "decades":
        answer = centurytodecade (a)
    elif a1 == "centuries" and b1 == "milleniums":
        answer = centurytomillenium (a)
        answer2 = round (centurytomillenium (a))
    elif a1 == "centuries" and b1 == "megaannums":
        answer = centurytomegaannum (a)
        answer2 = round (centurytomegaannum (a))
    elif a1 == "centuries" and b1 == "eons":
        answer = centurytoeon (a)
        answer2 = round (centurytoeon (a))
    elif a1 == "milleniums" and b1 == "nanoseconds":
        answer = milleniumtonano (a)
    elif a1 == "milleniums" and b1 == "microseconds":
        answer = milleniumtomicro (a)
    elif a1 == "milleniums" and b1 == "milliseconds":
        answer = milleniumtomilli (a)
    elif a1 == "milleniums" and b1 == "seconds":
        answer = milleniumtosec (a)
    elif a1 == "milleniums" and b1 == "minutes":
        answer = milleniumtominute (a)
    elif a1 == "milleniums" and b1 == "hours":
        answer = milleniumtohour (a)
    elif a1 == "milleniums" and b1 == "days":
        answer = milleniumtoday (a)
    elif a1 == "milleniums" and b1 == "weeks":
        answer = milleniumtoweek (a)
    elif a1 == "milleniums" and b1 == "months":
        answer = milleniumtomonth (a)
    elif a1 == "milleniums" and b1 == "years":
        answer = milleniumtoyear (a)
    elif a1 == "milleniums" and b1 == "decades":
        answer = milleniumtodecade (a)
    elif a1 == "milleniums" and b1 == "centuries":
        answer = milleniumtocentury (a)
    elif a1 == "milleniums" and b1 == "megaannums":
        answer = milleniumtomegaannum (a)
        answer2 = round (milleniumtomegaannum (a))
    elif a1 == "milleniums" and b1 == "eons":
        answer = milleniumtoeon (a)
        answer2 = round (milleniumtoeon (a))
    elif a1 == "megaannums" and b1 == "nanoseconds":
        answer = megaannumtonano (a)
    elif a1 == "megaannums" and b1 == "microseconds":
        answer = megaannumtomicro (a)
    elif a1 == "megaannums" and b1 == "milliseconds":
        answer = megaannumtomilli (a)
    elif a1 == "megaannums" and b1 == "seconds":
        answer = megaannumtosec (a)
    elif a1 == "megaannums" and b1 == "minutes":
        answer = megaannumtominute (a)
    elif a1 == "megaannums" and b1 == "hours":
        answer = megaannumtohour (a)
    elif a1 == "megaannums" and b1 == "days":
        answer = megaannumtoday (a)
    elif a1 == "megaannums" and b1 == "weeks":
        answer = megaannumtoweek (a)
    elif a1 == "megaannums" and b1 == "months":
        answer = megaannumtomonth (a)
    elif a1 == "megaannums" and b1 == "years":
        answer = megaannumtoyear (a)
    elif a1 == "megaannums" and b1 == "decades":
        answer = megaannumtodecade (a)
    elif a1 == "megaannums" and b1 == "centuries":
        answer = megaannumtocentury (a)
    elif a1 == "megaannums" and b1 == "millennium":
        answer = megaannumtomillenium (a)
    elif a1 == "megaannums" and b1 == "eons":
        answer = megaannumtoeon (a)
        answer2 = round (megaannumtoeon (a))
    elif a1 == "eons" and b1 == "nanoseconds":
        answer = eontonano (a)
    elif a1 == "eons" and b1 == "microseconds":
        answer = eontomicro (a)
    elif a1 == "eons" and b1 == "milliseconds":
        answer = eontomilli (a)
    elif a1 == "eons" and b1 == "seconds":
        answer = eontosec (a)
    elif a1 == "eons" and b1 == "minutes":
        answer = eontominute (a)
    elif a1 == "eons" and b1 == "hours":
        answer = eontohour (a)
    elif a1 == "eons" and b1 == "days":
        answer = eontoday (a)
    elif a1 == "eons" and b1 == "weeks":
        answer = eontoweek (a)
    elif a1 == "eons" and b1 == "months":
        answer = eontomonth (a)
    elif a1 == "eons" and b1 == "years":
        answer = eontoyear (a)
    elif a1 == "eons" and b1 == "decades":
        answer = eontodecade (a)
    elif a1 == "eons" and b1 == "centuries":
        answer = eontocentury (a)
    elif a1 == "eons" and b1 == "milleniums":
        answer = eontomillenium (a)
    elif a1 == "eons" and b1 == "megaannums":
        answer = eontomegaannum (a)
    else:
        print ("Those are invalid inputs.")
    ask2 = True
    while ask2:
        a2 = input ("Do you want the accurate answer or the rounded answer?(accurate/round) ")
        if a2 == "accurate":
            print ("The answer to the equation was: ", answer, " " + b1 + ".")
            ask3 = True
            while ask3:
                a3 = input ("Would you like to convert again?(yes/no) ")
                if a3 == "yes":
                    print ("Ok.")
                    time.sleep (1)
                    ask3 = False
                    ask2 = False
                elif a3 == "no":
                    quit ()
                else:
                    print ("Invalid input.")
        elif a2 == "round":
            print ("The answer to the equation was: ", answer2, " " + b1 + ".")
            ask4 = True
            while ask4:
                a4 = input ("Would you like to convert again?(yes/no) ")
                if a4 == "yes":
                    print ("Ok.")
                    time.sleep (1)
                    ask2 = False
                    ask4 = False
                elif a4 == "no":
                    quit ()
                else:
                    print ("Invalid input.")
        else:
            print ("Invalid input.")
