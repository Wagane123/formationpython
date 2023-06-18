def heursup(nbh,salaire):
    sumsup=0
    if(nbh<=39):
        sumsup=0
    elif(nbh<=44):
          sumsup=sumsup+[((nbh-39)*(50/100))*salaire]
    elif(nbh<=49):
         sumsup=sumsup+[(((nbh-39)*(50/100))+((nbh-44)*(75/100)))*salaire]
    else:
         sumsup=sumsup+[(((nbh-39)*(50/100))+((nbh-44)*(75/100))+((nbh-49)*(100/100)))*salaire]
nbh=int(input("veuillez saisir le nombre dheure"))      
salaire=float(input("veuillez saisir le salaire"))  
print(heursup(nbh,salaire)) 
              
               
