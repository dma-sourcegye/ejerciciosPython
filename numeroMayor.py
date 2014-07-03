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
#ESTE SCRIPT NO ES MIO LO COPIÉ DE OTRA PERSONA LA CUAL NO RECUERDO SU NOMBRE NI LA PÁGINA DE DONDE LO SAQUÉ
#si este script no les funciona pueden probar codificar los ascii a utf-8 o solamente borrar las letras con tilde
