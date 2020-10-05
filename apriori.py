from itertools import combinations

def leer(nombre = "archivo.txt"):
    matriz = []
    archivo = open(nombre)
    for linea in archivo:
        valores = str(linea).split(",")
        for i in range(len(valores)):
            valores[i] = int(valores[i])
        matriz.append(set(valores))
    return matriz

def numMaximo(matriz):
    mayor = 1
    for conjunto in matriz:
        aux = max(conjunto)
        if mayor < aux:
            mayor = aux
    return mayor

def transaccionMaxima(matriz):
    mayor = 1
    for conjunto in matriz:
        aux = len(conjunto)
        if mayor < aux:
            mayor = aux
    return mayor

def crearConjunto(numElementos):
    conjunto = []
    for i in range(1,numElementos+1):
        conjunto.append(i)
    return conjunto
    

def combinaciones(conjunto,numCombinaciones):
    arreglo = []
    for i in range(1,numCombinaciones+1):
        subarreglo = []
        for j in combinations(conjunto,i):
            subarreglo.append(set(j))
        arreglo.append(subarreglo)
    return arreglo

def apriori(archivo,combinaciones,confianzaUsuario):
    contador = 0
    iteracion = 1
    for conjunto in combinaciones:
        print("Iteracion",iteracion)
        for i in range(len(conjunto)):
            for subconjunto in archivo:
                if conjunto[i] <= subconjunto:
                    contador += 1
            if contador >= confianzaUsuario:
                print("Itemset:",conjunto[i],"Confianza",contador)
            contador=0
        iteracion += 1
    print("Fin")


if __name__ == "__main__":
    entrada = input("Proporcione nombre de archivo (Sin .txt) o enter para archivo ejemplo \n") + ".txt"
    if entrada != ".txt":
        archivo = leer(entrada)
    else:
        archivo = leer()
    num = numMaximo(archivo)
    maxTran = transaccionMaxima(archivo)
    conjunto = crearConjunto(num)
    comb = combinaciones(conjunto,maxTran)
    confianzaUsuario = int(input("Proporcione confianza: "))
    apriori(archivo,comb,confianzaUsuario)