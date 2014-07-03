print "Introduce 5 numeros:"
vector=[] #definimos una lista
#introducimos 5 numeros
for i in range(0,5):
    numero=int(raw_input('introduce no.  '+str(i+1)+': '))
    vector.append(numero)

print vector
mayor=0

for v in vector:
    if mayor<v:
        mayor=v

print 'mayor es: ',mayor

