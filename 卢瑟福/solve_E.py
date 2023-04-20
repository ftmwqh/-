a = 0
b = 10
def f ( E ) :return (0.285+0.005* E ) * E **1.5 -1.61
d = 0.001
if f ( a ) * f ( b ) <0:
    while abs (a - b ) >d :
        x = ( a + b ) /2
        if abs ( f ( x ) ) <d :
            print ( x )
            break
        elif f ( a ) * f ( x ) <0:
            b = x
        else :
            a = x

