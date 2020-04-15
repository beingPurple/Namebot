import discord
import time
from discord.ext import commands

bot = discord.Client()

@bot.event
async def on_ready(): #proof that it's working
    print("beep boop")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_update(before, after):
    if after.id != bot.user.id:

        splitAfter = after.nick
        splitAfter = splitAfter.split('-', 1)
        nameList = after.roles
        nameSize = len(nameList)
        i = 0
        nicList = "-"
        while i < nameSize:
            if str(nameList[i]) != '@everyone' \
                    and str(nameList[i]) != 'Exec'\
                    and str(nameList[i]) != 'Server Admin':
              nicList = nicList + " " + str(nameList[i])
            i += 1
        print("new member updated: ", before.nick, "roles: ", nicList)
        print("split after name: ", splitAfter)
        newNick = splitAfter[0] + nicList
        print("new name: ", newNick)
        await after.edit(nick=newNick)
        time.sleep(1)


bot.run('Njk5ODAyODc5ODc1MzUwNjM4.XpZvLw.HM5wEuXyFqmi-0BdY72D3e7YIwY') #an outdated token of course