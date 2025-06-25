ss={1:"山羊座",2:"水瓶座",3:"魚座",4:"牡羊座",5:"牡牛座",6:"双子座",7:"蟹座",8:"獅子座",9:"乙女座",10:"天秤座",11:"蠍座",12:"射手座",13:"山羊座"}

def se():
    m=input("何月生まれ？")
    d=input("何日生まれ？")
    m=int(m)
    d=int(d)
    mes=ss[m]+"ですね！"
    mes2=ss[m+1]+"ですね！"
    if m==1:
        if d <20:
            print(mes)
        else:
            print(mes2)
    elif m==2:
        if d < 19:
            print(mes)
        else:
            print(mes2)
    elif m==3:
        if d < 21:
            print(mes)
        else:
            print(mes2)
    elif m==4:
        if d < 20:
            print(mes)
        else:
            print(mes2)
    elif m==5:
        if d < 21:
            print(mes)
        else:
            print(mes2)
    elif m==6:
        if d < 22:
            print(mes)
        else:
            print(mes2)
    elif m==7:
        if d < 23:
            print(mes)
        else:
            print(mes2)
    elif m==8:
        if d < 23:
            print(mes)
        else:
            print(mes2)
    elif m==9:
        if d < 23:
            print(mes)
        else:
            print(mes2)
    elif m==10:
        if d < 24:
            print(mes)
        else:
            print(mes2)
    elif m==11:
        if d < 23:
            print(mes)
        else:
            print(mes2)
    elif m==12:
        if d < 22:
            print(mes)
        else:
            print(mes2)


se()
