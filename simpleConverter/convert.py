

def convert(s, t):
    if(s == "C" or s == "c"):
        print "You choose to convert celcius to fahrenheit"
        f = 5 * (t-32) / 9
        return f
        
    elif(s == "F" or s == "f"):
        print "You choose to convert fahrenheit to celcius"
        c = (t*(9.0/5)+32)
        return c
        
    else:
        print "Sorry. You entered wrong scale"
        return False

scale = raw_input("Give me the scale: ")
temperature = int(raw_input("Give me the temperature: "))

converted = convert (scale, temperature)

print converted