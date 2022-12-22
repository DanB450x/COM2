#Creamos el menú para realizar alguna tarea
option=int(input('Presione 1 para generar codigo Hammming  \nPresione 2 para encontrar el error del codigo Hamming \n'))

#Creamos una condicional para la opción escogida en el manú.
if(option==1):  # Genera el codigo Hamming
    print('Ingrese los bits de datos') #Pedimos que ingrese los bits (datos)
    d=input() #d = variable que ingresaremos
    data=list(d) #Converitmos los datos ingresados en "d" en una lista
    data.reverse() #El método reverse() no crea una nueva lista sino que invierte los elementos de la lista original.
    c,ch,j,r,h=0,0,0,0,[] #Creamos un diccionario para combinaciónes específicas de letras.


    #Entramos a un ciclo while hasta cumplir las condiciones dadas.
    #len = El método len() devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario.
    #pow = Es la forma de decir 2^(r)
    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1
    #------------------------------------------------------------------------
    #Según los valores obtenidos se seleccionara una acción por medio de condicionales for
    '''
    El ciclo for = es una estructura de control iterativa, que nos permite ejecutar de manera
    repetitiva un bloque de instrucciones, conociendo previamente un valor de inicio, un tamaño de paso
    y un valor final para el ciclo.
    '''
    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            '''
            #El append()método agrega un elemento al final de la lista.
            Agregamos este metodo para agrega un cero a "h"
            '''
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph] #Columna i : Fila i + ph
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('El codigo generado Hamming es:- ', end="") #Imprimimos resultados según los ciclos for
    print(int(''.join(map(str, h))))


elif(option==2): # Detectar el error en el código Hamming
    print('Ingrese el codigo Hamming recibido')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[] #Creamos lista de pariedad

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse() #El método reverse() no crea una nueva lista sino que invierte los elementos de la lista original.

    '''
    agrega un contador a un iterable y lo devuelve en forma de objeto enumerador. Este objeto enumerado se puede usar directamente
    para bucles o convertirse en una lista de tuplas usando el método list
    '''
    #Definimos las condiciones para saber si esxiste algún error.
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    if((error)==0):
        print('No hay ningún error en el codigo Hamming recibido')

    elif((error)>=len(h_copy)):
        print('No se puede detectar el error')

    else:
        print('El error esta en',error,'bit')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'


        #--------------------------------Corrigiendo errores-------------------------------------------------------
        elif(h_copy[error-1]=='1'): #Aquí definimos de que forma corregir el error detectado.
            h_copy[error-1]='0'
            print('Despues de corregir el codigo Hamming es:- ')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy)))) #El join()método toma todos los elementos en un iterable y los une en una cadena.

        #Ejemplo de map()
        '''
        map()
        devuelve un objeto de mapa (que es un iterador) de los resultados después de aplicar la función dada a cada elemento de un iterable dado (lista, tupla, etc.)
        Sintaxis:
        mapa(fun, iter)
        Parámetros:
        fun: Es una función a la que map pasa cada elemento de un iterable dado.
        iter: es un iterable que se va a mapear.
        NOTA: Puede pasar uno o más iterables a la función map ().
        '''
else:
    print('La opcion ingresada no existe')