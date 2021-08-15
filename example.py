from goto import goto, label

a = 5
b = 0
# complicated loops
while a > 3:
    for i in range(a+1):
        for j in range(a, i+a):
            while j < 10:
                # oh no I need to break now! but if I use break it will 
                # break only the parent loop
                # welp goto has you covered
                b = j * 2
                goto .stop  
label .stop
print('value of b',b)