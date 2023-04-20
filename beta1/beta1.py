import math
for i in range(0, 19):
    print(i * 0.0496)


def data(t, N):
    print(math.log((N/t-49/300)/(3483/15-49/300),10))
    return math.log((N/t-49/300)/(3483/15-49/300),10)
data(30,4374)
data(30,3494)
data(40,3976)
data(45,3702)
data(35,2394)
data(35,2029)
data(35,1665)
data(40,1495)
data(45,1397)
data(50,1248)
data(65,1166)
data(80,1199)
data(80,847)
data(120,908)
data(120,638)
data(200,638)
data(300,637)
data(480,626)