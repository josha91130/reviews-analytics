

data = []
count = 0
with open('C:/Users/josha/Desktop/reviews-analytics/reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new),'筆資料小於100個字')

good = []
for g in data:
    if 'good' in g:
        good.append(g)
print('一共有', len(good),'筆資料有good')
print(good[0])






