import pandas as pd

#csvを読み込んで、カラム名が「名前」のカラムをリスト化
data = pd.read_csv("kimetsu.csv")
list = data["名前"].tolist()

source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ", "むいちろう"]

#csvから読み込んだ名前がソースリストにない場合のみ、追加
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
        
if __name__ == "__main__":
    search()

df = pd.DataFrame(source)
df.rename(columns = {0: "名前"}, inplace=True)
df.to_csv("kimetsu2.csv")