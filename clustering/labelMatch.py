import numpy
from munkres import Munkres
import math


# SIGNIFICADO DOS PARaMETROS
# bd = labels_true (rotulos do conjunto de dados)
# od = predict (rotulos preditos pelo algoritmo)
# nk = numero de clusters do conjunto de dados

def compute_err(bd, od, nk):
    xor = numpy.zeros((nk, nk))
    for i in range(nk):
        for j in range(nk):
            tmp1 = float(numpy.logical_and((bd == i), (od == j)).sum())
            tmp2 = float((od == j).sum())
            xor[i, j] = tmp2 - tmp1
    return xor


# SIGNIFICADO DOS PARAMETROS
# gold = labels_true (rotulos do conjunto de dados)
# predict = predict (rotulos preditos pelo algoritmo)
# nk = numero de clusters do conjunto de dados

def labelmatch(gold, predict, nk):
    size = gold.shape
    cost = compute_err(gold, predict, nk)
    out = numpy.zeros((size))
    m = Munkres()
    indexes = m.compute(cost)
    for row, col in indexes:
        inds = (predict == col).nonzero()
        out[inds] = row
    return (out)


# SIGNIFICADO DOS PARAMETROS
# particle = array de coordenadas dos centroides de cada cluster
# K = numero de clusters
# dataset = conjunto de dados

def rotulos(particle, K, dataset, data):
    rotulo = numpy.zeros(data.namostras) #gera array do tamanho da amostra com zeros
    for i in range(0, data.namostras): #percorre todos os valores
        melhor = float("inf") #starta com infinito o melhor valor
        for r in range(0, K): #para cada cluster
            distancia = 0
            for k in range(0, data.ndim):
                distancia = distancia + pow(particle[r][k] - dataset[i][k], 2)
            distancia = math.sqrt(distancia)
            if (distancia < melhor):
                melhor = distancia
                etiqueta = r
        rotulo[i] = etiqueta
    return rotulo