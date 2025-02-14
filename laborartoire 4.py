#continuer de travailler sur le code
#possible de changer
#deux for,deux while
#trois input de l'utilisateur
#beaucoup de print
#trois bloc if
#un break
#un continue
#else


while True:
    import time
    import os
    import random

    print("voici un programme   qui vous permet de ne plus avoir de virus sur votre ordinateur")
    système_d_exploitation = input ("veuiller rentrer votre système d'exploitation pour mieux optimiser notre logiciel")
    if système_d_exploitation == "windows":  
        nom_d_utilisateur= input ("veuiller rentrer votre nom d'utilisateur pour confirmer votre identité")
        if nom_d_utilisateur == "admin": #rentrer admin si vous ne vouler pas quitter la page
            action=input(" que vouler vous faire aujourd'hui? (aller sur internet/imprimer document les document d'adoption de kiwi)")
            if action == "aller sur internet":
                dette_99_site_paris_de_kiwi = input ("rentrez le site que vous vouler visiter sur le web")
                while dette_99_site_paris_de_kiwi != "https://www.dette99/paris/de/kiwi_de_couse_de_kiwi.com":
                    print("erreur 404 page not found")
                    print("votre connection est de la merde ne rester pas sur l'intenet du cégep")
                else:
                   #liste des kiwi participant
                   coureur=["anaximandre","grézilda","auguste","killer","jipitou","tibert-vitese","canne-berge","bélzébut","turbo-diesel kiwi","usen kiwi-bolt"]  
                   print("bienveue au grand site de paris sur les course de kiwi")
                   #tu choisi ton kiwi
                   kiwi_selectionner=input("sur que lle kiwi miser sur votre kiwi préféré (anaximandre,grézilda,auguste,killer,jipitou,tibert-vitese,canne-berge,bélzébut,)")
                   random.shuffle(coureur)#mélanger l'ordre des kiwi dans la liste
                   for kiwi in coureur:
                       print(coureur)
                       

            else:
                    print("Bravo pour votre nouveau kiwi/n le kiwi est un animal merveilleux qui peut se ranger dans une valise de smart assez facillement. ")
            
       
            
      
        else:
            repetion = 0 
            while repetion<15:
                print("erreur")
                repetion=repetion+1
                print("redémarage du système")
            exit()

    elif système_d_exploitation == "linux":  #si on choisit linux
            print("vous avez choisi un bon systeme")
            nom_d_utilisateur_linux = input("veuiller rentrer votre nom d'utilisateur pour confirmer votre identité")
            if nom_d_utilisateur_linux == "admin": #rentrer admin si vous ne vouler pas quitter la page
                mot_de_passe = input("veuiller rentrer votre mot de passe pour confirmer votre identité")
                while mot_de_passe != "123456":
                    print("mot de passe incorrect")
                    error =0
                    while error < 60:
                     time.sleep(3)
                     print("error 404 page not found")
                     error = error +1
                

                    
             
    else:
            print("pourquoi choisir du apple?") 
            print("j'aime pas les gens qui choisissent apple")
            time.sleep(3)
            print("je vais donc vous punir d'avoir choisi cette compagnie et éteindre cotre ordinateur")
            os.system("shutdown /s /t 1") 
    print("le programe est terminée!")

    print("merci d'avoir utilisé notre logiciel")
    while True: 
        réponse = input(' voulez vous regarder pour de nouvelle mise à jour? (oui/non): ')
        if réponse in ('oui', 'non'):
            break
        print("invalid input.")

    if réponse == 'oui':
        continue
    else:
        print("au revoir")
        break
