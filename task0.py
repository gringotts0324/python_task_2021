#task0-1
name1 = "ねずこ"
name2 = "ぜんいつ"
print(f"{name1}と{name2}は仲間です")

#task0-2
if name2 != "むざん":
    print("仲間ではありません")

#task0-3
name = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]
name.append("ぜんいつ")

#task0-4
for i in name:
    print(i)

#task0-5
# 長方形の面積を求める関数。一辺の長さが引数。
def area(side1, side2):
    area = side1 * side2
    print(area)

area(3, 7)

#task0-6
def character(cname):
    if cname in name:
        print(f"{cname}は含まれます")
    else:
        print(f"{cname}は含まれません")

#動作確認
character("ぎゆう")
character("ハリーポッター ")