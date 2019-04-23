import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='D')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    
@bot.command(pass_context=True)
async def ping():
    await bot.say(':ping_pong:')
    await bot.say('You pinged me haha')
    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    role=discord.utils.get(ctx.message.server.roles,name='Muted')
    
    await bot.add_roles(target,role)
    
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    await bot.send_message(target,'Warning!!')
    
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    await bot.kick(target)
    
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    await bot.ban(target)
   
bot.run('NTQ2NjI3MzgyMTUzNTc2NDU1.XL7VnQ._ZYePfJnwqMAuZi77AxIE1zgnXs')
