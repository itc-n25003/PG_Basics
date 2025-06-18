import csv

list=[["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("ch.csv","w") as f:
    spamwriter = csv.writer(f, delimiter=",")
    for inlist in list:
        spamwriter.writerow(inlist)




