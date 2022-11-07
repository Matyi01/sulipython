import matplotlib.pyplot as plt

#x = [1,10]
#y = [10,1]
#plt.plot(x,y)
#plt.show()

#y = 6x^2 + 4x - 16

xPont = []
yPont = []
for x in range(-10,10):
    xPont.append(x)
    yPont.append(6*x**2 + 4*x - 16)

plt.plot(xPont,yPont)

#y = 16x^2 - 3 + 16

xPont = []
yPont = []
for x in range(-10,10):
    xPont.append(x)
    yPont.append(16*x**2 - 3*x + 16)

plt.plot(xPont,yPont)

plt.show()
