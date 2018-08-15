import numpy as np

# Class begin
print("-------- Matriz normal python ----------")
a = [1, 2, 3]
b = [6, 7, 8]
c = a + b
print(c)

print("-------- Operadores en matrices np ----------")

h = [1.4, 1.6, 1.7, 1.9]
w = [58, 76, 89, 90]
#bmi = w / (h **2)

nph = np.array(h)
npw = np.array(w)
bmi = npw / (nph **2)

print (bmi)

print(bmi[2])

print(bmi[1:])

print(bmi[bmi>25])

# Shape regresa dimensiones de la matriz
print("-------- Funcion Shape ----------")
v = np.array([3, 1])
w = np.array([2, -4])
print (v + w)
print (v.shape)

x = np.array(range(1, 100, 2))
print (x)
print(x.shape)

e = 2 * v
print (e)
print("-------- Funcion Dot ----------")
b = np.array([2, 1])
s = np.array([-3, 2])
d = np.dot(b, s)
print(d)
print("-------- Funcion Cross ----------")
p = np.array([2, 3, 1])
q = np.array([1 ,2, -2])
r = np.cross(p,q)
print(r)

print("-------- Matrices multidimensionales ----------")
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[6,5,4],[3,2,1]])

print(A+B)

print("-------- Funcion dot en matrices n-dim ----------")

M1 = np.array([[1,2,3],[4,5,6]])
M2 = np.array([[9,8],[7,6],[5,4]])

print(M1)
print(M2)

print(np.dot(M1,M2))
# Misma operacion diferente notacion
# print(M1@M2)

print("-------- Otros operadores ----------")

N = np.array([4,5,6])
N1 = np.zeros((3,4))
N2 = N1.ravel()

print(N)
print(N1)
print(N2)