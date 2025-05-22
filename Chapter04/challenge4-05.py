def number(x):
    """
    文字列をfloat型に変換して戻り値とする関数を書いてみよう。起こり得る例外
    をキャッチする例外処理を書こう。
    """
    return float(x)

x=input("数値を入れてください:")
try:
    print(float(x))

except ValueError:
    print("数字以外は処理できません")
