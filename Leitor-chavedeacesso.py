
print('''_ Insira a chave de acesso: 
''')
opção = 0

c1 = str(input("Chave: "))
n1 = c1[22:26]+c1[29:34]+", "

chaves = n1
######################################
print('Notas fiscais: \n')
print(chaves)

while   opção != 2:
    opção = int(input("\nDigite 1 para adicionar: "))
    if opção == 1:
        c2 = str(input("Chave: "))
        n2 = c2[22:26] + c2[29:34] + ","
        if c2 == c1:
            n2 = str("DUPLICADA, ")

        chaves2 = (n1+n2)
        ######################################
        print('Notas fiscais: \n')
        print(chaves2)

        while opção != 2:
            print("\nDigite 1 para adicionar: ")
            opção = int(input("Selecione; "))
            if opção == 1:
                c3 = str(input("Chave: "))
                n3 = c3[22:26] + c3[29:34] + ","
                if c3 == c2:
                    n3 = str("DUPLICADA, ")

                chaves3 = (n1+n2+n3)
                ######################################
                print('Notas fiscais: \n')
                print(chaves3)

                while opção != 2:

                    opção = int(input("\nDigite 1 para adicionar: "))
                    if opção == 1:
                        c4 = str(input("Chave: "))
                        n4 = c2[22:26] + c4[29:34] + ","
                        if c4 == c3:
                            n4 = str("DUPLICADA, ")

                        chaves4 = (n1 + n2 + n3 + n4)
                        ######################################
                        print('Notas fiscais: \n')
                        print(chaves4)
                        while opção != 2:

                            opção = int(input("\nDigite 1 para adicionar: "))
                            if opção == 1:
                                c5 = str(input("Chave: "))
                                n5 = c2[22:26] + c5[29:34] + ","
                                if c5 == c4:
                                    n5 = str("DUPLICADA, ")

                                chaves5 = (n1 + n2 + n3 + n4 + n5)
                                ######################################
                                print('Notas fiscais: \n')
                                print(chaves5)
                                while opção != 2:

                                    opção = int(input("\nDigite 1 para adicionar: "))
                                    if opção == 1:
                                        c6 = str(input("Chave: "))
                                        n6 = c2[22:26] + c6[29:34] + ","
                                        if c6 == c5:
                                            n6 = str("DUPLICADA, ")

                                        chaves6 = (n1 + n2 + n3 + n4 + n5 + n6)
                                        ######################################
                                        print('Notas fiscais: \n')
                                        print(chaves6)
                                        while opção != 2:

                                            opção = int(input("\nDigite 1 para adicionar: "))
                                            if opção == 1:
                                                c7 = str(input("Chave: "))
                                                n7 = c2[22:26] + c7[29:34] + ","

                                                chaves7 = (n1 + n2 + n3 + n4 + n5 + n6 + n7)
                                                ######################################
                                                print('Notas fiscais: \n')
                                                print(chaves7)
                                                while opção != 2:

                                                    opção = int(input("\nDigite 1 para adicionar: "))
                                                    if opção == 1:
                                                        c8 = str(input("Chave: "))
                                                        n8 = c2[22:26] + c6[29:34] + ","

                                                        chaves8 = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8)
                                                        ######################################
                                                        print('Notas fiscais: \n')
                                                        print(chaves8)
                                                        while opção != 2:

                                                            opção = int(input("\nDigite 1 para adicionar: "))
                                                            if opção == 1:
                                                                c9 = str(input("Chave: "))
                                                                print(' \n ')
                                                                n9 = c2[22:26] + c9[29:34] + ","

                                                                chaves9 = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9)
                                                                ######################################
                                                                print('Notas fiscais: \n')
                                                                print(chaves9)
                                                                while opção != 2:

                                                                    opção = int(input("\nDigite 1 para adicionar: "))
                                                                    if opção == 1:
                                                                        c10 = str(input("Chave: "))
                                                                        n10 = c2[22:26] + c10[29:34] + ","

                                                                        chaves10 = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)
                                                                        ######################################
                                                                        print('Notas fiscais: \n')
                                                                        print(chaves10)



print('\n\n=================================\nObrigado por usar a ferramenta!\n=================================\n\n')

