import pandas as pd

def search():
    
    #csvを読み込んで、カラム名が「名前」のカラムをリスト化
    data = pd.read_csv("kimetsu.csv")
    source = []
    list = data["名前"].tolist()
    source.extend(list)
    
    #入力し、リストに追加
    word = input("鬼滅の登場人物の名前を入力してください")
    if word in source:
        print(f"{word}が見つかりました")
    else:
        print(f"{word}はリストに存在しません")
        source.append(word)
    
    # csvファイルに書き込み
    df = pd.DataFrame(source)
    df.rename(columns = {0: "名前"}, inplace=True)
    df.to_csv("kimetsu2.csv")
        
if __name__ == "__main__":
    search()

