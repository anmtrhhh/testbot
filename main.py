import nextcord as nc
from nextcord.ext import commands
import os,datetime,asyncio
from random import *
from time import *

intents = nc.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='/',intents=intents)
guild = bot.get_guild(1121471135733776454)
swers = ['shit','fuck','hoe','ass','bitch']
TOKEN = 'MTEyMTQ3NDgzMTM4OTU2MDg5NA.G25yZ7.kc_b7D27wDllxgHH6_qmz1iUhaqPdjfTDsWppk'
secs = 0

@bot.event
async def on_ready():
    os.system('cls')
    guild = bot.get_guild(1130229967607832738)
    print('#=============================================#')
    print(f'logged as {bot.user.name}\nID: {bot.user.id}\nlogged in: {guild.name}')
    print('#=============================================#')
    txtf = open('log.txt','a', encoding='utf-8')
    txtf.write(f'\n#=================#\n{bot.user.name} is connected in {guild.name} at [{datetime.datetime.now()}]\n#=================#\n\n')


@bot.event
async def on_message(message):
    #writes all messages in the text file
    txtf = open('log.txt','a', encoding='utf-8')
    txtf.write(f'{message.author} sent \"{message.content}\" in channel ({message.channel.name}) at [{datetime.datetime.now()}]\n')
    # Check if the message author is not a bot
    if not message.author.bot:
        # Check if the message content meets your conditions
        msg = message.content
        msg = msg.split()
        for word in msg:
            if word in swers:
                # Delete the message
                await message.delete()
                # Send a warning or notification
                await message.channel.send(f'{message.author.mention}, bro said a swer not cool bro')
    if not message.author.bot:
         if 'uwu' == message.content:
              await message.channel.send('owo')
    if message.author.bot and message.content == 'bruh':
        await message.channel.send('bruh')
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    # Create an embed message
    txtf = open('log.txt','a', encoding='utf-8')
    txtf.write(f'{member.name} joined the server at [{datetime.datetime.now()}]')    
    embed = nc.Embed(
        title=f"Welcome to the hood dawg",
        description=f"{member.name} is here yall",
        color=nc.Color.green()
    )
    
    # Set the thumbnail of the embed (optional)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(
         name= 'uh',value='idk enjoy and stuff'
    )
    # Send the embed message to a specific channel
    channel = bot.get_channel(1162696442239012934)
    await channel.send(embed=embed)
    await channel.send(f'{member.mention} be nice and don\'t cause problems *pat pat*')
    print(f'{member.name} entered')


@bot.event
async def on_member_remove(member):  
   # Create an embed message
    embed = nc.Embed(
        title=f"naaaah bro is out",
        description=f"good bye :cry::wave: {member.name}",
        color=nc.Color.blue()
    )
    txtf = open('log.txt','a', encoding='utf-8')
    txtf.write(f'{member.name} leaved the server at [{datetime.datetime.now()}]')
    # Set the thumbnail of the embed (optional)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(
         name= '*sob*',value='sad'
    )
    # Send the embed message to a specific channel
    channel = bot.get_channel(1162696442239012934)
    await channel.send(embed=embed)    
    print(f'{member.name} leaved')

    
#==================================================================#

@bot.command()
async def logd(ctx):
    with open('log.txt','w') as file:
        file.write('')
    await ctx.send('the log file has been cleared')


@bot.command()
async def log(ctx):

    log_contents = ""
    try:
        with open("log.txt", "r", encoding='utf-8') as file:
            log_contents = file.read()
    except FileNotFoundError:
        await ctx.send("Log file not found.")
        return
    if ctx.channel.name == 'log':
        if log_contents:
            await ctx.send(log_contents)
        else:
            await ctx.send('the file is empty')
    else:
        await ctx.send('you can only run this command in log')


@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def avatar(ctx, user: nc.User = None):
    if user is None:
        avatar_url = ctx.author.avatar.url
        await ctx.send(avatar_url)
    else:
        # If a mention is provided, send the mentioned user's avatar
        avatar_url = user.avatar.url
        await ctx.send(avatar_url)

@bot.command()
@commands.has_permissions(manage_messages=True)  # Only allow users with the "manage_messages" permission to use this command
async def remove(ctx, amount=5):  # Set the default amount to 5 if no argument is provided
    await ctx.channel.purge(limit=amount + 1)  # Delete the specified number of messages, including the command itself
    await ctx.send(f'{amount} messages remove.')
    sleep(3)
    await ctx.channel.purge(limit = 1)

@bot.command()
async def play(ctx):
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()

    def disconnect_after_playing(error):
        coro = voice_client.disconnect()
        fut = nc.asyncio.run_coroutine_threadsafe(coro, bot.loop)
        try:
            fut.result()
        except:
            pass
    voice_client.play(nc.FFmpegPCMAudio('voice2.mp3'), after=disconnect_after_playing)

@bot.command()
async def game(ctx):
    # Create an embed object for the message
    embed = nc.Embed(title=choice(['do math lil nigga','slove this lil nigga','find the solution nigga']), description="nigger", color=0x00ff00)
    embed.add_field(name="Question", value="1+1 = ?", inline=False)
    
    # List of image URLs to choose from
    image_urls = [
        "https://media.istockphoto.com/id/1310060658/vector/thinking-emoticon-question-face-emoji-with-eyeglasses-vector-illustration.jpg?s=612x612&w=0&k=20&c=pNujEuBbCFfBGUPFNznD6gMVAJ_uGeFYMmjpPuby9Eg=",
        "https://www.publicdomainpictures.net/pictures/280000/nahled/emoji-guy.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvZtgqb3hMfLgE6bjYYEnu-iMOGvT7xSYCxw&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyrCJdMg3568Qv0n98KE1bWbNgwcIuI5yYYg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnZKOTSbFL_H9m84SN-62k87xrsinW-p2DWg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNCJhexnCSDPlw-er7pKTr4ueUeMM8nM4NhA&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTemanxKQ7QxJhWX89yngcqWDKbGs8u16zCwg&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpsUvz3skKMVMjPGJqFAJ3rh7AUXkhWzx84R9KwLHHqrvfeJ-0C0kirQx7OjY-HkOSS-g&usqp=CAU",
        "https://thumbs.dreamstime.com/z/emoticon-shh-22756645.jpg"
        # Add more image URLs as needed
    ]
    
    # Select a random image from the list
    random_image_url = choice(image_urls)
    embed.set_thumbnail(url=random_image_url)
    
    await ctx.send(embed=embed)

    def check(m):
        # Check if the message is in the same channel, the content is '2', and it's from the same user
        return m.channel == ctx.channel and m.content == '2' and m.author == ctx.author

    try:
        message = await bot.wait_for('message', timeout=5.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('boho nigga')
    else:
        await ctx.send(f'{message.author.mention} wins lol')


bot.run(TOKEN)