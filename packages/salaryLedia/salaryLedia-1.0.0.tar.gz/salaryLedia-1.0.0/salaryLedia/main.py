# x=salaryLedia bruto
# y=salaryLedia neto
# z=taksa


def paga_llog(x):
    if 0 < x <= 400:
        y = x
        print(y)
    elif 1500 > x > 400:
        z = x * 0.13
        y = x - z
        print(y)
    elif x >= 1500:
        z = x * 0.23
        y = x - z
        print(y)


paga_llog(2000)
