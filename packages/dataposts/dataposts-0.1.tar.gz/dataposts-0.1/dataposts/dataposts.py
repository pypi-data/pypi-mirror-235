print("""
       d8b                                                                       
      88P              d8P                                         d8P          
     d88            d888888P                                    d888888P        
 d888888   d888b8b    ?88'   d888b8b  ?88,.d88b, d8888b  .d888b,  ?88'   .d888b,
d8P' ?88  d8P' ?88    88P   d8P' ?88  `?88'  ?88d8P' ?88 ?8b,     88P    ?8b,   
88b  ,88b 88b  ,88b   88b   88b  ,88b   88b  d8P88b  d88   `?8b   88b      `?8b 
`?88P'`88b`?88P'`88b  `?8b  `?88P'`88b  888888P'`?8888P'`?888P'   `?8b  `?888P' 
                                        88P'                                    
                                       d88                                      
                                       ?8P                                      

Module DataPosts -- Made by V / Lou du Poitou -- (c) 2023 -- https://dataposts.hostycd.com/                              
""")

def help(category:str=None):
    if category == None:
        print("Module DataPosts --> HOME : \n --- \nVous venez d'utiliser la commande : help(category:str=None)\nLes différentes catégories sont : \n 1 ==> Connection \n 2 ==> User \n 3 ==> Admin \n 4 ==> Settings \n 0 ==> Exit \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)
    elif category == "1" or category.lower().strip() == "connection":
        print("Module DataPosts --> CONNECTION : \n --- \nLa fonction connect(email, password, keep:bool, fonction=None, time=None)\nPermet d'obtenir les informations d'authentification, pour permettre de \nlancer le bot et de pouvoir l'utiliser.\nExemple syntaxe :\n\n def bot(can_run):\n    dataposts.user.getUserInfos(can_run)\n\n can_run = dataposts.connect(\"email@email.com\", \"password123\", True, bot, 10)\n\nIci le programme permet d'obtenir les informations utilisateurs toutes les 15 \nsecondes. \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)
    elif category == "2" or category.lower().strip() == "user":
        print("Module DataPosts --> USER : \n --- \nLes différentes fonctions : \n\n following(user_id, can_run)\n unfollowing(user_id, can_run)\n updateBio(bio, can_run)\n checkPost(post_id, can_run)\n uncheckPost(post_id, can_run)\n getUsers(can_run)\n getPosts(can_run)\n getUserInfos(can_run)\n createPost(title, message, hashtag1, hashtag2, can_run)\n commentPost(text, post_id, can_run)\n deletePost(post_id, can_run)\n deleteComment(post_id, comment_id, can_run)\n singularlyPost(post_id, can_run)\n singularlyComment(post_id, comment_id, can_run)\n editPost(post_id, message, can_run)\n editComment(post_id, comment_id, text, can_run) \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)
    elif category == "3" or category.lower().strip() == "admin":
        print("Module DataPosts --> ADMIN : \n --- \nAccessibles seulement si votre compte est admin.\nLes différentes fonctions : \n\n certifUser(user_id, can_run)\n uncertifUser(user_id, can_run)\n banUser(user_id, can_run)\n unbanUser(user_id, can_run)\n adminDeletePost(post_id, can_run)\n adminDeleteComment(post_id, comment_id)\n adminUser(user_id, can_run)\n unadminUser(user_id, can_run) \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)
    elif category == "4" or category.lower().strip() == "settings":
        print("Module DataPosts --> SETTINGS : \n --- \nLes fonctions qu'utilise connect().\nLes différentes fonctions : \n\n login(email, password)\n verifyToken(infos)\n keepAlive(keep:bool, can_run, fonction=None, time:int=None) \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)
    elif category == "0" or category.lower().strip() == "exit":
        print("Module DataPosts --> EXIT : \n --- \nVous venez de quitter la commande d'help !\n Y retourner ? \n ==> help(category:str=None) \n --- \n")
        pass
    else:
        print("Module DataPosts --> HOME : \n --- \nLes différentes catégories sont : \n 1 ==> Connection \n 2 ==> User \n 3 ==> Admin \n 4 ==> Settings \n 0 ==> Exit \n --- \n")
        cat = str(input(">>> Sur quelle catégorie voulez-vous avoir de l'aide ? "))
        help(cat)

# Commande d'aide ==> help() #

import requests
from time import sleep

link = "https://dataposts.hostycd.com"

class settings:
    def login(email, password):
        url = f"{link}/api/authentification/login"

        data = {
            "email": email,
            "password": password
        }

        s = requests.Session()
        s.headers.update({
            "content-type": "application/json"
        })
        
        r = s.post(url=url, json=data)
        if "errors" in str(r.content):
            return (False, str(r.content)[2:-1], r.status_code)
        else:
            token = str(str(r.cookies).split("jwt=")[1].split(" for")[0]) ; user = str(r.content)[11:-3]
            return (True, token, user, r.status_code)

    def verifToken(infos):
        if infos[0] == False: return (False, infos[1], infos[2])
        url = f"{link}/token"
        
        s = requests.Session()

        s.cookies["jwt"] = infos[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.get(url=url, data=None)
        user_id = str(r.content)[3:-2]
        if len(str(r.content)[3:-2]) != 24: return (False, user_id, r.status_code)
        return (True, infos[1], user_id, r.status_code)
    
    def keepAlive(keep:bool, can_run, fonction=None, time:int=None):
        if time != None and time <= 2: return print("The time is too short !") ; exit()
        while keep:
            if fonction != None or time != None:
                sleep(time)
                fonction(can_run)
            else:
                pass
    
class user:
    def following(user_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/user/follow/{can_run[2]}"

        data = {
            "following": user_id
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.post(url=url, json=data)
        return str(r.content)[2:-1]

    def unfollowing(user_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/user/unfollow/{can_run[2]}"

        data = {
            "unfollowing": user_id
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.post(url=url, json=data)
        return str(r.content)[2:-1]

    def updateBio(bio, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/user/bio/{can_run[2]}"

        data = {
            "bio": bio
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.put(url=url, json=data)
        return str(r.content)[2:-1]

    def checkPost(post_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/check/{post_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def uncheckPost(post_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/uncheck/{post_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        s.headers.update({
            "content-type": "application/json"
        })

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def getUsers(can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/user"

        s = requests.Session()

        r = s.get(url=url)
        return str(r.content)[2:-1]

    def getPosts(can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post"

        s = requests.Session()

        r = s.get(url=url)
        return str(r.content)[2:-1]

    def getUserInfos(can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/user/{can_run[2]}"

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.get(url=url)
        return str(r.content)[2:-1]

    def createPost(title, message, hashtag1, hashtag2, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post"

        data = {
            "title": title,
            "message": message,
            "hashtags": list([hashtag1, hashtag2]),
            "posterId": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.post(url=url, json=data)
        return str(r.content)[2:-1]

    def commentPost(text, post_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/comment/{post_id}"
        
        data = {
            "commenterId": can_run[2],
            "text": text,
            "commenterPseudo": str(str(user.getUserInfos(can_run)).split("\"pseudo\":")[1].split(",")[0].replace("\"", ""))
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def deletePost(post_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/{post_id}"

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.delete(url=url)
        return str(r.content)[2:-1]

    def deleteComment(post_id, comment_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/delete-comment/{post_id}"

        data = {
            "comment": comment_id
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def singularlyPost(post_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/singularly/{post_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.put(url=url, json=data)
        return str(r.content)[2:-1]

    def singularlyComment(post_id, comment_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/singularly-comment/{post_id}"

        data = {
            "user": can_run[2],
            "comment": comment_id
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.put(url=url, json=data)
        return str(r.content)[2:-1]

    def editPost(post_id, message, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/{post_id}"

        data = {
            "message": message
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.put(url=url, json=data)
        return str(r.content)[2:-1]

    def editComment(post_id, comment_id, text, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/post/edit-comment/{post_id}"

        data = {
            "comment": comment_id,
            "text": text
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]
    
class admin:
    def certifUser(user_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/administration/certif/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def uncertifUser(user_id, can_run):
        if can_run[0] == False: return None
        url = f"{link}/api/administration/uncertif/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def banUser(user_id, can_run):
        url = f"{link}/api/administration/ban/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def unbanUser(user_id, can_run):
        url = f"{link}/api/administration/unban/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def adminDeletePost(post_id, can_run):
        url = f"{link}/api/administration/post/{post_id}"

        data = {
            "user": can_run[2]
        }

        s= requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.delete(url=url, json=data)
        return str(r.content)[2:-1]

    def adminDeleteComment(post_id, comment_id, can_run):
        url = f"{link}/api/administration/comment/{post_id}"

        data = {
            "user": can_run[2],
            "comment": comment_id
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def adminUser(user_id, can_run):
        url = f"{link}/api/administration/admin/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]

    def unadminUser(user_id, can_run):
        url = f"{link}/api/administration/unadmin/{user_id}"

        data = {
            "user": can_run[2]
        }

        s = requests.Session()

        s.cookies["jwt"] = can_run[1]

        r = s.patch(url=url, json=data)
        return str(r.content)[2:-1]
    
def connect(email, password, keep:bool, fonction=None, time:int=None):
    try:
        can_run = settings.verifToken(settings.login(email, password))
        if can_run[0] == True: print(f"Success to connect to ==> {can_run[2]} !\n----------------------------------------------------")
        elif can_run[0] == False: print(f"Failed to connect to ==> undefined !\n----------------------------------------------------")
        settings.keepAlive(keep, can_run, fonction, time)
        return can_run
    except:
        pass

## DataPosts (c) 2023 -- V / Lou du Poitou -- https://dataposts.hostycd.com ##