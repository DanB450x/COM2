import numpy as np;
import math
#-----------------------------------------------------------------------------------------------------------------------------
opcion = 0

while opcion != 3:
    print("1. Decodificación")
    print("2. Recepción")
    print("3. Terminar proceso")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("-------------------------------------------------------------------")
        print("SELECCIONAR TIPO DE DECODIFICACIÓN:\n\nCESAR, PRESIONAR 1.\n\nHILL, PRESIONAR 2")
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
                    nueva_pos = (pos_letra - n) % len(abc)
                    cifrado+= abc[nueva_pos]
                else:
                    cifrado+= l
            print("MENSAJE CIFRADO: ", cifrado)
            print("--------------------------------------------------------------")
           
            # Defining BinarytoDecimal() function 
            def BinaryToDecimal(binary): 
                    
                    # Using int function to convert to 
                    # string 
                    string = int(binary, 2) 
                    
                    return string 
                    
            # Driver's code 
            # initializing binary data 
            tex = input("ingrese: ")
            bin_data = tex

            # print binary data 
            print("The binary value is:", bin_data) 

            # initializing a empty string for 
            # storing the string data 
            str_data =' '

            # slicing the input and converting it 
            # in decimal and then converting it in string 
            for i in range(0, len(bin_data), 7): 
                    
                    # slicing the bin_data from index range [0, 6] 
                    # and storing it in temp_data 
                    temp_data = bin_data[i:i + 7] 
                    
                    # passing temp_data in BinarytoDecimal() function 
                    # to get decimal value of corresponding temp_data 
                    decimal_data = BinaryToDecimal(temp_data) 
                    
                    # Deccoding the decimal value returned by 
                    # BinarytoDecimal() function, using chr() 
                    # function which return the string corresponding 
                    # character for given ASCII value, and store it 
                    # in str_data 
                    str_data = str_data + chr(decimal_data) 

            # printing the result 
                    print("The Binary value after string conversion is:", str_data)

#print("--------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------
        elif numero==2:

            def imprimir_matriz(charar):
                for i in range(2):
                    for j in range(2):
                        print(int(charar[i][j]), "\t", end='')
                    print("\n");

            print("--------------------------------------------------------------")
#            else:
                #Descifrar
                # Solicitar Datos
            Texto = input("INTRODUCIR MENSAJE: ");
            Texto = Texto.upper().strip().replace(" ", "");
            print("INTRODUCIR LA CLAVE (MATRIZ 2x2)");
            Clave = np.empty((4, 4));
            msj = "";
            m_crip = np.zeros((math.ceil(len(Texto) / 2), 2))

            for i in range(2):
                for j in range(2):
                    msj="Posición"+str(i)+","+str(j)+": ";
                    Clave[i][j] = input(msj);

            imprimir_matriz(Clave)
            diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3,'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
            abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

                #Inversa de una matriz A^-1=1/[A] * (A*)^T
                #Sacar determinante
            Determinante=Clave[0][0]*Clave[1][1]-Clave[0][1]*Clave[1][0]
            Adjunta=np.zeros((2,2))
            Adjunta[0][0] = Clave[1][1]
            Adjunta[1][1] = Clave[0][0]
            Adjunta[0][1] = -1*Clave[1][0]
            Adjunta[1][0] = -1*Clave[0][1]

            TAdj = np.zeros((2,2))
            TAdj[0][0] = Adjunta[0][0]
            TAdj[1][1] = Adjunta[1][1]
            TAdj[0][1] = Adjunta[1][0]
            TAdj[1][0] = Adjunta[0][1]

            Determinante=Determinante%26
            InClave = np.zeros((2, 2))
            InClave[0][0]= ((1/Determinante)*TAdj[0][0])%26
            InClave[0][1]= ((1 / Determinante) * TAdj[0][1])%26
            InClave[1][0]= ((1 / Determinante) * TAdj[1][0])%26
            InClave[1][1]= ((1 / Determinante) * TAdj[1][1])%26

            i = 0
            j = 0
            while True:
                try:
                    if (np.size(m_crip) / 2 == j):
                        break
                    #print(Texto[i], " - ", Texto[i + 1])
                    m_crip[j][0] = diccionario_letras[Texto[i]]
                    m_crip[j][1] = diccionario_letras[Texto[i + 1]]
                    i +=2
                    j +=1

                except:
                    print(Texto[i])
                    m_crip[j][0] = diccionario_letras[Texto[i]]
                    break
            # for i in range(m_crip.length)

            c1 = 0
            c2 = 0
            m1 = 0
            m2 = 0

            descipher = np.zeros(m_crip.shape)
            print("MENSAJE DESCIFRADO: ")
            for i in range(int(np.size(m_crip) / 2)):
                m1 = m_crip[i][0]
                m2 = m_crip[i][1]
                c1 = InClave[0][0] * m1 + InClave[1][0] * m2
                c2 = InClave[0][1] * m1 + InClave[1][1] * m2
                descipher[i][0] = c1 % 26
                descipher[i][1] = c2 % 26

                    #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
                print(abecedario[int(descipher[i][0])], "", abecedario[int(descipher[i][1])], " ", end=''"\n\n")
            print("MENSAJE DESCIFRADO EN BINARIO: ")
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

        #data = input('INGRESE EN MENSAJE EN BINARIO: ' )

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