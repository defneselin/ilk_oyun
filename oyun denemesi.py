def giriş(mermi,can):
    if int(mermi) < int(can):
        print('mermi alman senin için iyi olacaktır.')
    elif int(mermi) > int(can):
        print('can almalısın bence.')
    elif int(mermi) == int(can):
        print('hiç bir şey almadan geç.')

def satın_alma(alışveriş,ekleme):
    if miktar > 20:
        print('çok fazla almaya çalıştığın için ekleme yapılamadı')
    elif miktar == 0:
        print('bol şans!')
    elif miktar > 0:
        Y = miktar
        print(str(Y) + ' tane eklenerek işlem gerçekleştrildi.')
        X = miktar + int(ekleme)
        print(str(X) + ' tane mermin veya canın oldu!')

karakter = input('karakterini seç\n (karakterler: SOVA REYNA PHOENX SKY RAZE SAGE KİLLJOY ve JETT)\n (sadece SAGE,RAZE veya JETT kilitli değil)')
if karakter == 'SAGE':
    print('150 canın var. Ve hiç mermin yok')
    giriş(0,150)
    alışveriş = input('mermi almak ister misin?')
    miktar = int(alışveriş)
    ekleme = 0
    satın_alma(miktar,ekleme)
elif karakter == 'RAZE':
    print('200 mermi 125 canın var.')
    giriş(200,125)
    alışveriş = input('can almak ister misin?')
    miktar = int(alışveriş)
    ekleme = 125
    satın_alma(miktar,ekleme)
elif karakter == 'JETT':
    print('100 mermi 100 canın var.')
    giriş(100,100)
    alışveriş = input('can veya mermi almak için ödeme yapmalısın\n (ilk girişte ödeme yapamazsın)')
else:
    print('bu karakteri ilk girişte açamazsın')
    
