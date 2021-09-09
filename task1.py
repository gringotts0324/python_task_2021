import pandas as pd
data = pd.read_csv("kimetsu.csv")
list = data["名前"].tolist()

source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ", "むいちろう"]

for name in list:
    if name in source:
        pass
    else:
        source.append(name)


def search():
    word = input("鬼滅の登場人物の名前を入力してください")
    if word in source:
        print(f"{word}が見つかりました")
    else:
        print(f"{word}はリストに存在しません")
        source.append(word)
    
search()

df = pd.DataFrame(source)
df.rename(columns = {0: "名前"}, inplace=True)
print(df)
df.to_csv("kimetsu2.csv")
