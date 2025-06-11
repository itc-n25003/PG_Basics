num=[2,14,19,98,60,62,13,25,119]

while True:
    answer = input("write some number or q:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("don't write alphabet.")
    if answer in num:
        print("OK")
    else:
        print("try again")
