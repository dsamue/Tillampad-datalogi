# Tilda lab 2 - David Samuelsson Cmete2 - 20140130

from LinkedStack import LinkedStack

def trolla_tillbaka(svar):
    lista=svar.split(' ')
    stack=LinkedStack()
    ny_stack=LinkedStack()
    
    for i in lista:
        stack.push(i)

    s=''
    
    while stack.isEmpty() != True:   
        x=stack.pop()

        if stack.isEmpty():
            #s+= x + ' '
            p=ny_stack.top
            
            if p != None:               
                while p!= None:
                    x=ny_stack.pop()
                    stack.push(x)
                    p=p.next

            else:
                s+= x + ' '
                
        else:           
            y=stack.pop()
            ny_stack.push(x)
            s+= y + ' '
                    
    print(s)
  

def huvudprogram():
    print('Hej och välkommen till bakvända trollkarlsprogrammet!\nDu kan när som helst avsluta genom att trycka "#"')

    svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')
    
    while svar != '#':
        trolla_tillbaka(svar)
        svar=input('\nI vilken ordning vill du att korten ska komma ut?\n')

    print('\nProgrammet är avslutat') 

huvudprogram()        
