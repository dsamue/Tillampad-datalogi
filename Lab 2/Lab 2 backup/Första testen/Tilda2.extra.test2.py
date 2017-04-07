# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from LinkedStack import LinkedStack

def trolla_tillbaka(svar):
    lista=svar.split(' ')
    stack=LinkedStack()
    ny_stack=LinkedStack()
    superny_stack=LinkedStack()
    
    for i in lista:
        stack.push(i)

    s=''
    
    while stack.isEmpty() != True:
        x=stack.pop()

        if stack.isEmpty() and ny_stack.isEmpty():
            supuerny_stack.push(x)

        elif stack.isEmpty() and not ny_stack.isEmpty():
            p=ny_stack.top
            
            while p!=None:
                x=ny_stack.pop()
                stack.push(x)
                p=p.next

        else:
            x
            y=stack.pop

'''            ....ej klart men kanske bättre att göra två olika fall för om det 
            är ett eller två objekt kvar i kön? '''
            
        
##        x=stack.pop()
##
##        if stack.isEmpty():
##            #s+= x + ' '
##            p=ny_stack.top
##            
##            if p != None:               
##                while p!= None:
##                    x=ny_stack.pop()
##                    stack.push(x)
##                    p=p.next
##
##            else:
##                s+= x + ' '
##                
##        else:           
##            y=stack.pop()
##            ny_stack.push(x)
##            s+= y + ' '
                    
    return(stacken)
  

def huvudprogram():
    print('Hej och välkommen till bakvända trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')
    
    while svar != '#':
        trolla_tillbaka(svar)
        svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')

    print('\nProgrammet är avslutat') 

huvudprogram()        
