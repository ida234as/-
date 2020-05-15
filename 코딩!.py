import discord
import asyncio
client = discord.Client()



@client.event
async def on_ready():
    print("로그인 완료!")
    print("와우 정상적으로 작동 했어요!")
    game = discord.Game("베타 1.0.1")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("명령어"):
        embed = discord.Embed(
            title="",
            description="",
            color=discord.Color.orange()
            )
        embed.set_thumbnail(url="https://i.pinimg.com/originals/f9/6a/1c/f96a1c21d01bb81c1ebb16c3b5373bdc.gif")
        embed.add_field(name="[기본 적인 명령어]아직 제작 단계", value="` `안녕` `ㅂㅇ` `넌누구야?` `", inline=True)
        #embed.add_field(name="_____", value="`ㅂㅇ`", inline=True)
        embed.set_footer(text="Copyright ⓒ 2020 Kingly Psychology")
        await message.channel.send(embed=embed)
    if message.content.startswith('안녕'):
        await message.channel.send('안녕하세요!')
    elif message.content.startswith('ㅂㅇ'):
        await message.channel.send('ㅂㅇㅂㅇ')
    if message.content.startswith('넌 누구야?'):
        await message.channel.send('난 봇이야 ㅋㅋ')





access_token = os.enriron["BOT_TOKEN"]
client.run(access_token)
