# Tilda lab 1 -  David Samuelsson - cmete2 - 2014-01-24


class Gympapass:                # Klass för varje gympapass
    def __init__(self, lokal, tid, passtyp, rum, ledare, platser):
        self.lokal=lokal
        self.tid=tid
        self.passtyp=passtyp
        self.rum=rum
        self.ledare=ledare
        self.platser=platser

    def __str__(self):              #Någon anledning till att inte använda __repr__ ist?
        return self.passtyp # typ info?

    def __repr__(self):
        return self.passtyp

    def byt_lokal(self, ny_lokal):
        self.lokal=ny_lokal

    def boka_plats(self, antal):
        platser=self.platser
        lista=platser.split(' ')
        lista[0]=str(int(platser[0])+int(antal))     #uppdaterar antal bokade platser
        self.platser=lista[0]+' '+lista[1]+' '+lista[2]+' '+lista[3]

    def byt_ledare(self, ny_ledare):
        self.ledare=ny_ledare

    def visa_all_info(self):
        print('Lokal:',self.lokal,'\nTid:',self.tid,'\nPasstyp:',self.passtyp,'\nRum:',self.rum,'\nLedare:',self.ledare,'\nPatser:',self.platser,'\n')
        


def las_in_fil():
    infil=open('/Users/David/Desktop/egenlista.txt', 'r')      #får inte andra textfiler att funka?
    passinfo=[]
    passen=[]
    
    for rad in infil.readlines():
        rad=rad.strip('\n')

        if rad != '--------------':
            passinfo.append(rad)

        else:
            passobjekt=Gympapass(passinfo[0], passinfo[1], passinfo[2], passinfo[3], passinfo[4], (passinfo[5]))    
            passen.append(passobjekt)
            passinfo=[]

    return passen




def Huvudprogram():
    
    passen=las_in_fil()
    
    while True:
        
        print('-----------------------------------------\nHej och välkommen till Friskis & Svettis!')
        svar=input('Sök efter önskat pass: ')
        for i in range (len(passen)):

            if passen[i].passtyp==svar:
                print('\nPassnummer: ',i)
                passen[i].visa_all_info()

            else:
                None
                
        if status==1:                
            index=int(input('Vilket pass är du intresserad av? Ange passnummer: ')) 
            svar=int(input('\nVad vill du göra?   1:Boka pass   2:Byt lokal   3: Byt ledare \n' ))
            
        if svar ==1:
            svar=int(input('Hur många deltagare vill du boka? '))
            passen[index].boka_plats(svar)
            print('Bokningen är klar!')

        elif svar ==2:
            svar=input('Vilken lokal vill du byta till? ')
            passen[index].byt_lokal(svar)
            print('Lokalbyte utfört!')

        elif svar ==3:
            svar=input('Vilken ledare vill du byta till? ')
            passen[index].byt_ledare(svar)
            print('Byte av ledare utfört!')

        else:
            print('Fel typ av inmatning! Svara 1,2 eller 3. ')

            
                       
Huvudprogram()
            
##skicka in fil        
##boka redovisningstid

##En symbolisk länk är en pekare som pekar på en fysisk plats på datorn. Precis som en genväg.
##fixa lite dokumenterad felhantering i separat funktion om tid finns

##Be om hjälp hur jag ska göra? linux idle =2.7. Hur funkar emac + terminal och hur kör jag det hemma?
##Hur få text att funka? Kör på egen textfil sålänge. utf8 och inga åäö. i skolans fil blir bl.a é knasigt. 
