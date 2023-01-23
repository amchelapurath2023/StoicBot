from json.tool import main
from multiprocessing.connection import wait
from tkinter import W
from nextcord.ext import commands
import datetime as dt
import asyncio
import discord
import calendar
from discord.ext import commands
from discord.ext.commands import bot

total_offset = 0

bot = commands.Bot(command_prefix="!")

def calendar_day_to_int(date):
    global total_offset
    days_in_year = 0
    for i in range(1,date.month):
        if i == 2:
            days_in_year += 29
        else:
            days_in_year += calendar.monthrange(date.year, i)[1]

    if (date.day == 22 and date.month == 1) or (date.day == 26 and date.month == 1) or (date.day == 28 and date.month == 1) or (date.day == 10 and date.month == 3) or (date.day == 25 and date.month == 4) or (date.day == 3 and date.month == 6) or (date.day == 14 and date.month == 6) or (date.day == 6 and date.month == 9) or (date.day == 9 and date.month == 9) or (date.day == 19 and date.month == 9) or (date.day == 23 and date. month == 9) or (date.day == 25 and date.month == 9) or (date.day == 9 and date.month == 11) or (date.day == 20 and date.month == 10) or (date.day == 21 and date.month == 12) or (date.day == 26 and date.month == 12):
        total_offset += 1
    if date.day == 2 and (date.month == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12):
        total_offset += 1
    return days_in_year + date.day + total_offset - 1

async def schedule_daily_message():
    year = dt.date.today().year
    date_dict = {}
    for month in range(1,13):
        for day in range(1, calendar.monthrange(year, month)[1]+1):
            date = dt.date(year, month, day)
            date_dict[date] = calendar_day_to_int(date)

    while True:
        today = dt.date.today()
        today_value = date_dict[today]
        print(today_value)
        now = dt.datetime.now()
        then = now+dt.timedelta(days=1)
        then = then.replace(hour=6, minute=0)
        print(then)
        wait_time = (then-now).total_seconds()
        print(wait_time)
        await asyncio.sleep(wait_time)


        channel = bot.get_channel(1066740381871521852)
        
        if today_value in [0, 21, 26, 35, 65, 74, 98, 122, 130, 162, 165, 195, 227, 259, 264, 268, 279, 284, 287, 295, 314, 328, 336, 360, 380]:
            await channel.send("Your Daily Stoic Message", file=discord.File("TrueDailyStoic/DailyStoicJournal"+str(today_value)+".png"))
            today_value = today_value+1
            await channel.send("", file=discord.File("TrueDailyStoic/DailyStoicJournal"+str(today_value)+".png"))
        else:
            await channel.send("Your Daily Stoic Message", file=discord.File("TrueDailyStoic/DailyStoicJournal"+str(today_value)+".png"))
    
    

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    await schedule_daily_message()

if __name__ == '__main__':
    bot.run("MTAwODIxMzEzNTE1NDQ5MTM5NA.GWNpwm.Rc6QiKXUQQS76RFDTd90Pg8mDZlwofZ5TIxmOg")
