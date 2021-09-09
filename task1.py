#task1-1, 1-2
source = []

name = input("キーワードを入力してください")

if name in source:
    print(f"{name}はリストに存在します")
else:
    print(f"{name}はリストに存在しません")
    source.append(name)
    



