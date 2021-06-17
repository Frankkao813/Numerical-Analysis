import numpy as np
import matplotlib.pyplot as plt


def polynominalFit(x,y,n):

    '''
    x: x array
    y: y array
    n: highest power
    
    '''

    # Check length of the array. If number of element isn't the same, an exception will be raised.
    if len(x) != len(y):
        msg = 'numbers of element in x and y is not consistent'
        raise ValueError(msg)

    # construct an augmented array(matrix)
    R = np.zeros((n+1, n+2))

    for i in range(n+1):
        R[i, n+1] = np.sum(np.power(x, i)* y)
        for j in range(n+1):
            pow = i + j 
            R[i,j] = np.sum(np.power(x, pow))
    A = R[:,:n+1]
    Y = R[:,n+1]

    #coefficient of regression curve
    result = np.linalg.solve(A,Y)

    #plot regression curve and overlay curve and points
    min_x = min(x)
    max_x = max(x)
    x_func = np.linspace(min_x,max_x,num = 100)
    y_func = []

    for j in range(len(x_func)):
        sum = 0
        for i in range(len(result)):
            sum += np.power(x_func[j], i)*result[i]
            #print(x_func[j], i, result[i])
        y_func.append(sum)
    
    plt.ion()
    plt.plot(x_func,y_func)
    plt.title('I-t graph')
    plt.xlabel('t (sec)')
    plt.ylabel('I (mA)')
    line1, = plt.plot(x_func,y_func, color = 'blue')
    line2, = plt.plot(x, y,'o')
    plt.show()
   

    return result

def TrapIntegration(coeff, start, stop, step):
    
    '''
    coeff: the list of value obtained from polynominal fit
    start, stop: start, stop value
    using trapezoidal numerical integration method
    '''

    n = int((stop-start)/step)
    sum_first = 0
    for i in range(len(coeff)):
        sum_first += coeff[i] * (start ** i)
        sum_first += coeff[i] * (stop ** i)

    sum_second = 0
    for i in range(1,n+1):
        x = start + i * step
        for j in range(len(coeff)):
            sum_second += coeff[j] * (x ** j)

    return (step/2)*sum_first + step* sum_second



x = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840], dtype = np.float64)
y = np.array([8.31, 8.67, 8.81, 8.91, 8.99, 9.05, 9.1, 9.14, 9.18, 9.21, 9.25, 9.27, 9.3, 9.32, 9.34, 9.35, 9.37, 9.38, 9.4, 9.41, 9.43, 9.44, 9.44, 9.45, 9.46, 9.47, 9.47, 9.47, 9.46], dtype = np.float64)

#這邊要改
#可以試試看不同的次方，看哪個fit的結果會最準
coeff_polynominal = polynominalFit(x,y,15)

NumInteg = TrapIntegration(coeff_polynominal, min(x), max(x), 0.01)
print("The result of numerical Integration will be {} mC".format(NumInteg))

