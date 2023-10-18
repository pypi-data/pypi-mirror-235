import matplotlib.pyplot as mpp

x = 2+5j
z = 1j
c = x*z

mpp.scatter(x.real,x.imag,color='pink')
mpp.scatter(c.real,c.imag)
mpp.show()