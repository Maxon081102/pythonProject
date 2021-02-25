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
# print(transform_a)
# print(transform_b)
transform_a = transform_a.real
transform_b = transform_b.real
# print(transform_a)
# print(transform_b)
c = []
for i in range(min(len(transform_a), len(transform_b))):
    c.append(transform_a[i] * transform_b[i])
c_new = numpy.fft.ifft(c)
c_new = c_new.real
# print(c_new)
c = 0
for i in range(len(c_new)):
    c += c_new[i]
print(c)
print(int(a)*int(b))