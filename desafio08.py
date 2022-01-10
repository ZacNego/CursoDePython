medida = float(input('Uma distânca e metros: '))
km = medida*(1/1000)
hm = medida*(1/100)
dam = medida*(1/10)
dm = medida*10
cm = medida*100
mm = medida*1000
print('km: {}\nHm: {}\nDam: {}\nm: {}\ndm: {}\ncm: {}\nmm: {}'.format(km, hm, dam, medida, dm, cm, mm))
