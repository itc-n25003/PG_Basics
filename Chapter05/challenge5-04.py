kana = {"身長":"158！",
        "誕生日":"2.14！",
        "血液型":"A型！"
       }

answer = input("何を聞く？:")
if answer in kana:
    result =kana[answer]
    print(result)
