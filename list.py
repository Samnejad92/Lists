# list
# item1="python"
# item2="ionic"
# item3="kotlin"
# item4="JQuery"
# myList=[item1,item2,item3,item4]
# print(len(myList))
# print(myList[len(myList)-1])
# print(myList[-2])
# myRange=range(1,30)
# print(list(myRange))
# isExistsKotlin="kotlin" in myList
# print(isExistsKotlin)
myColors=["red","blue","green","grey","yellow","orange",3.6]
# for color in myColors:
#     if type(color) == str:
#         print(f"the color is: {color}")
#     else:
#         print(f"{color} is not a color")
# print('-----------------------------------')
# index=0
# while index < len(myColors):
#     color=myColors[index]
#     if type(color) == str:
#         print(f"the color is: {color}")
#     else:
#         print(f"{color} is not a color")
#     index+=1
# myCourses=["Python","Kotlin","Ionic"]
# myCourses.append("JQuery")
# myCourses.extend(["Jquery","Vue js"])
# myCourses.insert(1,"jquery")
# print(myCourses)
myCourses=["Python","Kotlin","Ionic"]
last_item = myCourses.pop()
first_item = myCourses.pop(0)
print(f"last item is {last_item}")
print(f"first item is {first_item}")
myCourses.remove("Kotlin")
# myCourses.clear()
print(myCourses)