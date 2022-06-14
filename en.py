import numpy as np
from PIL import Image


Carrier = Image.open('carrier.png')
WaterMark = Image.open('watermark.png')


Carrier_array = np.array(Carrier)
WaterMark_array = np.array(WaterMark)

a, b = WaterMark_array.shape
a1, b1 = Carrier_array.shape

array1 = np.zeros((a, b), dtype=int)
for i in range(a):
    for j in range(b):
        array1[i][j] = Carrier_array[i][j]

for i in range(a):
    for j in range(b):
        w = Carrier_array[i][j]
        if w % 2 == 0 and WaterMark_array[i][j] >191 :
            Carrier_array[i][j] = Carrier_array[i][j] + 1
        elif w % 2 == 1 and WaterMark_array[i][j] <191:
            Carrier_array[i][j] = Carrier_array[i][j] - 1


array2 = np.zeros((a, b), dtype=int)
for i in range(a):
    for j in range(b):
        array2[i][j] = Carrier_array[i][j]


I = Image.fromarray(Carrier_array)
I.save("test.png")
I.show()
