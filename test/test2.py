import MeCab

m = MeCab.Tagger()
te = m.parse('영등포구청역에 있는 맛집 좀 알려주세요.')
print(te)