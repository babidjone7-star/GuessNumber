import random

arr = list(range(10))
PlayerNum = 0
BotNum = 0

def NewStartGame():
   global BotNum
   global PlayerNum 
   print("Выберите любое число от 0 до 9,Бот загадал число")
   BotNum = random.choice(arr)
   PlayerNum = int(input("Твое число? "))
NewStartGame()
for i in arr: 
    if BotNum > PlayerNum:
        print("МОЕ ЧИСЛО БОЛЬШЕ!")
        PlayerNum = int(input("Неверно, сделай еще одну попытку.."))
    elif PlayerNum > BotNum:
        print("МОЕ ЧИСЛО МЕНЬШЕ!")
        PlayerNum = int(input("Неверно, сделай еще попытку.."))
    elif PlayerNum == BotNum:
        print("Ты Угадал!!")
        NewStartGame()
    if PlayerNum > 10 or PlayerNum < 0:
        print("Можно загадывать числа от 1 до 10..") 