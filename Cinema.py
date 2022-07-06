lugares=int(input("\nCINEMA VIDA NOVA \n\nDigite o total de lugares disponíveis: "))
posicao=()

vetor = [posicao]*lugares
print (vetor)

while True:
    assento = int(input("\nEscolha seu assento: "))

    if (assento <= lugares):
        if (vetor [assento-1]) == "X":
            print ("Assento número", assento, "está ocupado. Escolha outro.")
   
        else:
           vetor [assento-1] = "X"
           print ("Assento número", assento, "reservado com sucesso.")
     
    else:
        print("Esse assento não existe. Escolha um assento válido.")
    
    print(vetor)

    
  






    # if [assento] == ():
    #     vetor [assento] = "X"
    # print (vetor)
  

    # if [assento] == "X":        
    #    print("Assento ocupado. Escolha outro.")



 











# #     if vetor==desocupado:
# #           assento = int(input("\n Escolha mais um assento: "))
# #     # else:   
# #     #    print ("Assento",assento, "reservado. Escolha outro lugar") 
    
# #     # else:
# #     #     print("km")

# #     #  for cinema in vetor:
# #     #     print (cinema)

# #     #     assento = int(input("\n Escolha seu assento: "))
