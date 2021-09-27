from logging import Manager
import discord 
from discord.ext import commands
from discord import Embed, Color
import os
import time   
from discord import Colour
import datetime 
from discord.utils import get

from discord.user import ClientUser

Client = discord.Client()
bot_prefix="!"
client = commands.Bot(command_prefix=bot_prefix)
TOKEN = 'TU TOKEN'

#Eventos

@client.event
async def on_ready():
    game=discord.Game('Troy Bot -/- Usa !informacion')
    await client.change_presence(status=discord.Status.idle, activity=game)
    print(f"""
/$$$$$$$              /$$                              
| $$__  $$            | $$                              
| $$  \ $$  /$$$$$$  /$$$$$$          /$$$$$$  /$$   /$$
| $$$$$$$  /$$__  $$|_  $$_/         /$$__  $$| $$  | $$
| $$__  $$| $$  \ $$  | $$          | $$  \ $$| $$  | $$
| $$  \ $$| $$  | $$  | $$ /$$      | $$  | $$| $$  | $$
| $$$$$$$/|  $$$$$$/  |  $$$$/      | $$$$$$$/|  $$$$$$$
|_______/  \______/    \___/        | $$____/  \____  $$
                                    | $$       /$$  | $$
                                    | $$      |  $$$$$$/
                                    |__/       \______/ 
    Bot Ready
    """)

#Informacion Lenjuages de programacion

@client.command()
async def python(ctx):
    embed = discord.Embed(title="Que Es Python?", description="Python es un lenguaje de programación multiplataforma, es muy conocida por sus codigos legibles y facil de escribir, con python puedes hacer tus primeros proyectos como: Tool de hacking, Bots de discord, videojuegos, etc")
    await ctx.send(embed=embed)
    
@client.command()
async def nodejs(ctx):
    embed = discord.Embed(title="Que Es Node.js", description="Node.js es un entorno en tiempo de ejecución multiplataforma, de código abierto, para la capa del servidor basado en el lenguaje de programación JavaScript, asíncrono, con E/S de datos en una arquitectura orientada a eventos y basado en el motor V8 de Google.")
    await ctx.send(embed=embed)
##################################################################################

@client.command()
async def informacion(ctx):
    embed = discord.Embed(title="Help", description="Help el bot cuenta con 3 comandos !python !nodejs !informacion se iran metiendo mas.")
    await ctx.send(embed=embed)
###########################################################



client.run("Token")