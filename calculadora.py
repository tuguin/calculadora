class calculator:
    continuar=0
    while(continuar==0):
        a=int(input("valor de a "))
        b=int(input("valor de b "))
        soma=a+b
        sub=a-b
        multi=a*b
        div=a/b
        potencia=1
        
        while (a!=0):
            potencia=potencia*b
            a=a-1
        escolha=int(input("soma 1 sub 2 div 3 multi 4 potencia 5 "))
        print("resultado " )
        if (escolha==1):
            print(soma)
        if(escolha==2):
            print(sub)
        if(escolha==3):
            print(div)
        if(escolha==4):
            print(multi)
        if(escolha==5):
            print(potencia)

        print("------------")
        continuar=int (input("sim 0 não 1 "))


    


   
    



    