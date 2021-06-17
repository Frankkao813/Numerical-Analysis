#polynominal Fit
import numpy as np
import matplotlib.pyplot as plt

# data to fit
x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840])
y = np.array([8.31, 8.67, 8.81, 8.91, 8.99, 9.05, 9.1, 9.14, 9.18, 9.21, 9.25, 9.27, 9.3, 9.32, 9.34, 9.35, 9.37, 9.38, 9.4, 9.41, 9.43, 9.44, 9.44, 9.45, 9.46, 9.47, 9.47, 9.47, 9.46])

#order of polynominal
n = 6

# an array to store polynominal matrix coefficient
#formula: y = a0 + a1*x + a2*x^2 + a3*x^3 + ...

R = np.zeros((n+1, n+2))
for i in range(n+1):
    R[i, n+1] = np.sum(np.power(x, i)* y)
    for j in range(n+1):
        pow = i + j
        R[i,j] = np.sum(np.power(x, pow))

# form of the matrix AX = Y
#extract A and Y
A = R[:,:n+1]
Y = R[:,n+1]

#coefficient of regression curve
result = np.linalg.solve(A,Y)

#plot regression curve and overlay curve and points
min_x = min(x)
max_x = max(x)
x_func = np.linspace(min_x,max_x,num = 100)
y_func = [] #in list

for j in range(len(x_func)):
    sum = 0
    for i in range(len(result)):
        sum += np.power(x_func[j], i)*result[i]
        #print(x_func[j], i, result[i])
    y_func.append(sum)
print(y_func)   
plt.plot(x_func,y_func)
line1, = plt.plot(x_func,y_func, color = 'blue')
line2, = plt.plot(x, y,'o')
plt.show()


