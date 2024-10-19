from tree import *

#Khaled Esmail,cs302,Karla Fant

#main function

def main():
    aAvatar = Avatar()
    option = 0 # this option decides which derived class they will choose like champion or pokemon
    option2 = 0 # this option allows the user to choose which function they want from each class
    while(option != 4):
        print("Please enter which option you like")
        option = int(input("1.Avatar \n 2.Pokemon \n 3.Champion \n 4.Quit\n"))
        if(option == 1):
            while(option2 != 4): #nested while loop for the avatar class
                print("Please enter which option you like regarding your avatar")
                option2 = int(input("1.Starting Info \n 2.Display Info \n 3.Display History \n 4.Quit\n"))
                if(option2 == 1):
                    aAvatar.Avatar_insert()

                if(option2 == 2):
                    aAvatar.Avatar_display()

                if(option2 == 3):
                    aAvatar.Avatar_description()

                if(option2 == 4):
                    break

        if(option == 2):
            aPokemon = Pokemon()# pokemon object
            atree = tree()
            while(option2 != 4):
                print("Please enter which option you like regarding your pokemon")
                option2 = int(input("1.Starting Info \n 2.Display Info \n 3.Display History \n 4.Quit\n"))
                if(option2 == 1):
                    aPokemon.Pokemon_insert()
                    atree.add(aPokemon)

                if(option2 == 2):
                    atree.display(aPokemon)

                if(option2 == 3):
                    aPokemon.Pokemon_description()
                    
                if(option2 == 4):
                    break
        
        
        if(option == 3):
            aChampion = Champion()#champion object
            while(option2 != 4):
                print("Please enter which option you like regarding the champion")
                option2 = int(input("1.Starting Info \n 2.Display Info \n 3.Display History \n 4.Quit\n"))
                if(option2 == 1):
                    aChampion.Champion_insert()

                if(option2 == 2):
                    aChampion.Champion_display()

                if(option2 == 3):
                    aChampion.Champion_description
                    
                if(option2 == 4):
                    break
        
        if(option == 4):
            break


if  __name__ == "__main__":
    main()
