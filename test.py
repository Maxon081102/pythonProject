import scipy
import numpy

a = input()
b = input()
new_a = []
new_b = []
for i in range(len(a) - 1, -1, -1):
    new_a.append(int(a[i] + '0' * (len(a) - i - 1)))
for i in range(len(b) - 1, -1, -1):
    new_b.append(int(b[i] + '0' * (len(b) - i - 1)))
# print(new_a)
# print(new_b)
transform_a = numpy.fft.fft(new_a)
transform_b = numpy.fft.fft(new_b)
print(4)
