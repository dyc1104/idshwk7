import numpy as np
from PIL import Image


Carrier = Image.open('test.png')

a1, b1 = 200,250
Carrier_array = np.array(Carrier)
WaterMark_array1 = np.zeros((a1, b1), dtype='int8')
for i in range(a1):
    for j in range(b1):
        w = Carrier_array[i][j]
        if w % 2 == 1:
            WaterMark_array1[i][j] = 1


WaterMark_array1.dtype = 'bool'
# print(WaterMark_array1.shape)
I = Image.fromarray(WaterMark_array1)
I.save("extractWaterMark.png")
I.show()
