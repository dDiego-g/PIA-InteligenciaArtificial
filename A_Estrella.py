import matplotlib.pyplot as plt
import time

# Funcion para leer los datos del archivo de texto
def leer():
    x = []
    y = []
    with open("datos.txt", "r") as f:
        for i in f.readlines():
            tmp = i.split(",")
            try:
                x.append(int(tmp[0]))
                y.append(int(tmp[1]))
            except:pass
        f.close()
    return x, y

# Funcion para mostrar la grafica
def show(fin):
    plt.xlim(-0.5, tamaño[0]+0.5)
    plt.ylim(-0.5, tamaño[1]+0.5)
    if(len(x) == 3):   
        labels = ('Mono', 'Silla', 'Platanos')
        sc = plt.scatter(x, y, c=range(3), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(3))
    elif (len(x) == 2 and fin is False):
        labels = ('Mono', 'Platanos')
        sc = plt.scatter(x, y, c=range(2), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(2))
    else:
        labels = ('Mono', ' ')
        sc = plt.scatter(x, y, c=range(2), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(2))
    cbar.ax.set_yticklabels(labels)
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    frame1.axes.yaxis.set_ticklabels([])
    #plt.savefig('Img/img' + str(movimientos) + '.jpg', dpi=100)
    plt.show()
    time.sleep(0.5)
    return sc

# Funcion para calcular el numero de movimientos desde la posicion hasta el destino actual
def calcular(xm, ym):
    if ruta[xm][ym] is None:
        ruta[xm][ym] = (abs(xm - x[1]) + abs(ym - y[1])) + (abs(xm - x[0]) + abs(ym - y[0]))
    return None

def aEstrella(x, y):
    minimo = 999999999999999999999999999
    calcular(x[0] + 1, y[0])
    calcular(x[0] - 1, y[0])
    calcular(x[0], y[0] + 1)
    calcular(x[0], y[0] - 1)
    calcular(x[0] + 1, y[0]+1)
    calcular(x[0] - 1, y[0]-1)
    calcular(x[0]-1, y[0] + 1)
    calcular(x[0]+1, y[0] - 1)
    for i in range(tamaño[0]+1):
        for j in range(tamaño[1]+1):
            try:
                if ruta[i][j] < minimo and ruta[i][j] is not None and (i, j) not in visitados:
                    minimo = ruta[i][j]
                    aux = i
                    aux2 = j
            except:
                continue
    return aux, aux2

start = time.time()
movimientos = 0
visitados = []
x, y = leer()
tamaño = (x.pop(0), y.pop(0))
ruta = [[None for j in range(tamaño[1] + 1)] for i in range(tamaño[0] + 1)]
sc = show(False)

try:
    while(x[0] != x[1] or y[0] != y[1]):
        x[0], y[0] = aEstrella(x, y)
        visitados.append((x[0], y[0]))
        sc.remove()
        sc = show(False)
        if(x[0] == x[1] and y[0] == y[1]):
            x.pop(1)
            y.pop(1)
            ruta = [[None for j in range(tamaño[1] + 1)] for i in range(tamaño[0] + 1)]
            visitados.clear()
        movimientos +=1
except:
    x.append(x[0])
    y.append(y[0])
    sc.remove()
    sc = show(True)
    end = time.time()
    print("Numero de movimientos - ", movimientos)
    print("Tiempo total - ", end - start)
