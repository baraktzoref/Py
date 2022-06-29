x = int(input("Please enter the phone prise:"))
x1 = 0
if x <= 4000:
    if x <= 1000:
        print (f'Phone prise is {x} - very cheap')
    elif x <= 2000:
        print (f'Phone prise is {x} - cheap')
    elif x <= 3000:
        print (f'Phone prise is {x} - normal')
    else:
        print (f'Phone prise is {x} - expensive')
elif x <= 5000:
    print (f'Phone prise is {x} - just iphone')
else:
    print (f'Phone prise is {x} - non relevant')

