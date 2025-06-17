import csv

with open("chjp.csv","w",encoding="utf-8",newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["トップ ガン","リスキー ビジネス","マイノリティ レポート"])
    w.writerow(["タイタニック","ザ レヴェナント","インセプション"])
    w.writerow(["トレーニング デイ","マン オン ファイア","フライト"])
