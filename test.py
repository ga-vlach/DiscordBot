import asyncio

async def yeah():

    aList = [1, 2, 3, 4]
    myList = []

    for number in aList:
        myList.append(number)

    await print(myList)

async def main():
    await yeah()
    #print(myList)
    #return print(myList)

asyncio.run(main())

#make a weather function ex. ?weather greece (shows embedded message of weather in athens)
#add a function that shows recipes based on ingredients listed