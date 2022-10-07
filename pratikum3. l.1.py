print("mari kita cek jenis segitiga ")

y= float(input('mauskan angka sisi alas'))
x=  float(input('masukan angka sisi tegak'))
z= float(input('masukan angka sisi miring'))
    
if x == y == z :
    print('s kamu adalah segitiga sama sisi')
elif x == y or y == z:
    print('kamu adalah segtiga sama kaki')
elif z == (x**2 + y**2 )**0.5 :
     print(' kamu adalah segitiga siku siku')
else:
    print('kamu adalah segitiga sembarangan' )     

