import os
import discord
import random
from dotenv import load_dotenv

#arrays with all the different properties
eyeColor = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'white']
furLength = ['long', 'short']
Shirt = ['tube top', 'tank top', 'sleeveless shirt', 'V-neck shirt', 'T-shirt', 'princess vest', 'blouse',
         'western shirt', 'military', 'pin tuck', 'tuxedo', 'ruffle front', 'cossack', 'smock', 'peplum', 'sailor',
         'tunic', 'polo', 'henley shirt', 'turtleneck', 'hoodie', 'sweater']
Pants = ['straight', 'leggings', 'tapered', 'baggies', 'joggers', 'jeans', 'cargo', 'jean shorts', 'cargo shorts',
         'sport shorts', 'bermuda shorts']
Accessories = ['glasses/sunglasses', 'watch', 'necklace', 'ring', 'hat', 'handbag', 'shoes', 'scarf', 'mittens',
               'stockings']
#pissColor = ['yellow', 'red']
#Nanners = ['YES', 'NO']

#array of names of any categories that need a special RNG call for none
makeRNGForNone = [furLength, Shirt, Pants, Accessories]

#array containing the previous arrays
propArr = [eyeColor, furLength, Shirt, Pants, Accessories]

#names of the categories that will be printed out
varNames = ['Eye Color', 'Fur Length', 'Shirt', 'Pants', 'Accessories']

client = discord.Client(intents=discord.Intents.default())

async def makeGieeg(messages):
    varNameIndex = 0
    categoryName = varNames[varNameIndex]
    finalMessage = ''
    for i in propArr:
        randChoice = 'none'

#check if the specific category has a chance at being 'none' and run the RNG function
        for n in makeRNGForNone:
            if i == n:
                noneVar = 1
                if noneVar == random.randrange(1, 5):
                    randChoice = 'none'
                    break
            else:
                if i != Accessories:
                    randChoice = random.choice(i)
                else:
                    randChoice = ''

#check if the category is Accessories and run multiple RNG calls
        if i == Accessories and randChoice != 'none':
            numOfAcc = random.randrange(1, 4)
            for q in range(numOfAcc):
                if q == max(range(numOfAcc)):
                    randChoice += random.choice(i)
                else:
                    Choice = random.choice(i)
                    i.remove(Choice)
                    randChoice += Choice + ", "

        categoryName = varNames[varNameIndex]
        finalMessage += categoryName + " : " + randChoice + "\n"
        varNameIndex += 1
    await messages.channel.send(finalMessage)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!creategieeg':
        await makeGieeg(message)

client.run(os.getenv("TOKEN"))