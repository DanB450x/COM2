import numpy as np;
import math
#-----------------------------------------------------------------------------------------------------------------------------
opcion = 0

while opcion != 3:
    print("1. Codificar")
    print("2. Transmitir")
    print("3. Terminar proceso")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("-------------------------------------------------------------------")
        print("SELECCIONAR TIPO DE CODIFICACIÓN:\n\nCESAR, PRESIONAR 1.\n\nHILL, PRESIONAR 2")
        print("-------------------------------------------------------------------")

        numero = int(input("DIGITE UNA OPCIÓN: " ))
        if numero==1:    
            texto = input("INTRODUCIR MENSAJE > ").upper()
            n = int(input("DESPLAZAMIENTO > "))
            abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            cifrado = ""
            for l in texto:
                if l in abc:
                    pos_letra = abc.index(l)
                    nueva_pos = (pos_letra + n) % len(abc)
                    cifrado+= abc[nueva_pos]
                else:
                    cifrado+= l
            print("MENSAJE CIFRADO: ", cifrado)
            print("--------------------------------------------------------------")
            print("MENSAJE CIFRADO EN BINARIO")
            string = cifrado
            binary_converted = ' '.join(format(ord(c), 'b') for c in string)
            print(binary_converted)

            print("--------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------
        elif numero==2:

            def imprimir_matriz(charar):
                for i in range(2):
                    for j in range(2):
                        print(int(charar[i][j]), "\t", end='')
                    print("\n");

#            Rta=int(input("CIFRADO HILL.\n\n1. CIFRAR\n\n"))
#            if Rta==1:
                #Solicitar Datos
            Texto = input("INTRODUCIR MENSAJE: ");
            Texto = Texto.upper().replace(" ", "");
            print("INTRODUCIR LA CLAVE (MATRIZ 2x2)");
            Clave = np.empty((4, 4));
            msj="";
            m_crip=np.zeros((math.ceil(len(Texto)/2),2))

            for i in range(2):
                for j in range(2):
                    msj="Posición "+str(i)+","+str(j)+": ";
                    Clave[i][j] = input(msj);

            imprimir_matriz(Clave)
            diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
            abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

            cipher="";
            i=0
            j=0
            while True:
                try:
                    if (np.size(m_crip) / 2 == j):
                        break
                    #print(Texto[i], " - ", Texto[i+1])
                    m_crip[j][0]=diccionario_letras[Texto[i]]
                    m_crip[j][1]=diccionario_letras[Texto[i+1]]
                    i+=2
                    j+=1
                
                except:
                    print(Texto[i])
                    m_crip[j][0] = diccionario_letras[Texto[i]]
                    break
            #for i in range(m_crip.length)

            c1 = 0
            c2 = 0
            m1 = 0
            m2 = 0

            cipher=np.zeros(m_crip.shape)
            print("MENSAJE CIFRADO ")
            salida = ""
            for i in range(int(np.size(m_crip)/2)):

                m1 = m_crip[i][0]
                m2 = m_crip[i][1]
                c1 = Clave[0][0]*m1 + Clave[1][0]*m2
                c2 = Clave[0][1] * m1 + Clave[1][1] * m2
                cipher[i][0]=c1%26
                cipher[i][1] = c2%26

                k = abecedario[int(cipher[i][0])]
                l = abecedario[int(cipher[i][1])]

                salida += k + l
                #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
            print(salida)
            print("MENSAJE CIFRADO EN BINARIO")

            string = salida
            binary_converted = ' '.join(format(ord(c), 'b') for c in string)
            print(binary_converted)
            print("--------------------------------------------------------------")

#-------------------------------------------------------------------------------------------------------------------------------
    elif opcion==2:
        def calcRedundantBits(m): 
        
            for i in range(m): 
                if(2**i >= m + i + 1): 
                    return i 
    
        def posRedundantBits(data, r): 
        
            j = 0
            k = 1
            m = len(data) 
            res = '' 

            for i in range(1, m + r+1): 
                if(i == 2**j): 
                    res = res + '0'
                    j += 1
                else: 
                    res = res + data[-1 * k] 
                    k += 1

            return res[::-1] 

        def calcParityBits(arr, r): 
            n = len(arr) 

            for i in range(r): 
                val = 0
                for j in range(1, n + 1): 

                    if(j & (2**i) == (2**i)): 
                        val = val ^ int(arr[-1 * j]) 

                arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 
            return arr 

        def detectError(arr, nr): 
            n = len(arr) 
            res = 0

            for i in range(nr): 
                val = 0
                for j in range(1, n + 1): 
                    if(j & (2**i) == (2**i)): 
                        val = val ^ int(arr[-1 * j]) 

                res = res + val*(10**i) 

            return int(str(res), 2) 

        data = input('INGRESE EN MENSAJE EN BINARIO: ' )

        m = len(data) 
        r = calcRedundantBits(m) 

        arr = posRedundantBits(data, r) 

        arr = calcParityBits(arr, r) 

        print("EL DATO TRANSMITIDO: " + arr) 

        arr = input('INGRESE EL DATO TRANSMITIDO CON ERROR: ')
        #print("EL DATO TRANSMITIDO CON ERROR: " + arr) 
        correction = detectError(arr, r) 
        print("EL ERROR ESTÁ EN LA POSICIÓN: "+ str(correction)) 
        print("--------------------------------------------------------------")
    else:
        print("FIN")