import numpy as np
import matplotlib.pyplot as plt
import math
def f(x, y):
    return (1/2)*(x**2 )+ (7/2)*(y**2);
def df(x, y) :
   return x , 7*y ;
def descente_pas_fixe(s) :
    iteration_max = 1000
    tol = 1e-6
    i = 0
    x0 = 7
    y0 = 1.5
    coordx = []
    coordy = []
    grad_x ,grad_y = df(x0 , y0)
    norme_grad = math.sqrt(grad_x**2 + grad_y**2) 
    while(abs(norme_grad) > tol):
        grad_x ,grad_y = df(x0 , y0)
        norme_grad = math.sqrt(grad_x**2 + grad_y**2)
        x0 = x0 - s*grad_x 
        y0 = y0 - s*grad_y
        coordx.append(x0)
        coordy.append(y0)
        i += 1
        if i > iteration_max:
            return None 
    return coordx ,coordy
def descente_pas_optimal():
    iteration_max=1000
    tol=1e-6
    x0=7
    y0=1.5
    i=0
    coordx = []
    coordy = []
    grad_x ,grad_y = df(x0 , y0)
    norme_grad = math.sqrt(grad_x**2 + grad_y**2) 
    while(abs(norme_grad)>tol):
        s = (x0**2 + 49*(y0**2))/( x0**2 + 343*(y0**2))
        coordx.append(x0)
        coordy.append(y0)
        grad_x ,grad_y = df(x0 , y0)
        norme_grad = math.sqrt(grad_x**2 + grad_y**2)
        i += 1
        if i > iteration_max:
            return None 
    return coord
if __name__ == "__main__":
    coordx_1 , coordy_1 = descente_pas_fixe(0.125)
    coordx_2 , coordy_2 = descente_pas_fixe(0.25)
   # points_abscisse_3 , points_ordonnée_3 = descente_pas_optimal()
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    plt.plot(coordx_1 , coordy_1 ) 
    X , Y = np.meshgrid( coordx_2 ,  coordy_2)
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    plt.plot(  coordx_2 , coordy_2 ,color = 'black') 
    #X , Y = np.meshgrid(points_abscisse_3 , points_ordonnée_3)
    Z = (1/2)*(X**2) + (7/2)*(Y**2)
    #plt.plot( points_abscisse_3 ,points_ordonnée_3 ,'+-' , color = 'red') 
    plt.show()
    print(X,Y,Z)
