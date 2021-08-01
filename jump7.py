##Gues & items
allGuests = {'Alice':{'apples':5,'pretzels':12},'Bob':{'ham':3,'apples':2},'Carol':{'cups':3,'apple pies':1}}


##定义一个函数 来取食物的总和
def totalBrought(guests, food):
    numBrought = 0

    for v in guests.values():
        numBrought += v.get(food,0)
    return numBrought
foodset = set()
for v in allGuests.values():
    foodset |= set(v)

## 把食物打印出来

print('Number of things being brought:
')
for food in foodset:
    print('-{:20}    {}'.format(food,totalBrought(allGuests,food)))
