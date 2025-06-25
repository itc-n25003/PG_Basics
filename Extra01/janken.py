import random

rsp={0:"ジャンケン",1:"グー",2:"チョキ",3:"パー"}

def game():
    print("ジャンケン!")
    win="あなたの勝ちです"
    lose="あなたの負けです"
    plyr=rsp[0]
    npc=rsp[0]
    while plyr==npc:
        ran=random.randint(1,3)
        npc=rsp[ran]
        npcmes="相手は"+rsp[ran]+"です"
        num=input("グー(1)?/チョキ(2)?/パー(3)?")
        num=int(num)
        plyr=rsp[num]
        pcmes="あなたは"+rsp[num]+"です"
        print(pcmes)
        print(npcmes)
        if plyr == npc:
            print("あいこ!")
        elif plyr == "グー":
            if npc == "チョキ":
                print(win)
            else:
                print(lose)
        elif plyr == "チョキ":
            if npc == "パー":
                 print(win)
            else:
                 print(lose)
        else:
            if npc == "グー":
                print(win)
            else:
                print(lose)

game()
