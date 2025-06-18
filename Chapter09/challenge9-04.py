import csv

list=[["トップ ガン","リスキー ビジネス","マイノリティ レポート"],["タイタニック","ザ レヴェナント","インセプション"],["トレーニング デイ","マン オン ファイア","フライト"]]

with open("chjp.csv","w") as f:
    spamwriter = csv.writer(f, delimiter=",")
    for inlist in list:
        spamwriter.writerow(inlist)

