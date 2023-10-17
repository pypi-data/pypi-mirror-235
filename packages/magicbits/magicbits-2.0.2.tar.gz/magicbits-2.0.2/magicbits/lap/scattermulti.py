import matplotlib.pyplot as mp

a = [-2+4j,-1+2j,0+2j,1+2j,2+2j,-1+4j,0+4j,1+4j]

# Real Part of all complex numbers
x = [x.real for x in a]
# Imaginary part of all complex numbers
y = [x.imag for x in a]

# Scatter plotting using matplotlib
mp.scatter(x,y,color='red')
mp.show()

