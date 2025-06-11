num=[2,14,19,98,60,62,13,25,119]

while True:
    answer = input("数字 か qを入力してください:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入れてください！")
    if answer in num:
        print("正解")
    else:
        print("不正解")
