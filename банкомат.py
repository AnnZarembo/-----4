from num2words import num2words

def convert_num(col_vo):
    if col_vo < 1 or col_vo > 100000:
        return "Сумма должна быть от 1 до 100 000"


    words = num2words(col_vo,lang='ru')
    p_rasrad = col_vo % 10
    if p_rasrad == 1 and col_vo % 100 != 11:
        valuta = "рубль"
    elif (col_vo%100<10 or col_vo%100>=20) and 2<=p_rasrad<=4:
        valuta="рубля"
    else:
        valuta="рублей"
    resultat = words.capitalize()+" "+valuta
    return resultat


col_vo=int(input("Введите сумму от 1 до 100000:"))
resultat=convert_num(col_vo)
print(resultat)