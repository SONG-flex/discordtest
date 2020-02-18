import discord
import os



client = discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="METEOR 서버"))

    @client.event
    async def on_message(message):
        id = message.author.id
        if message.content.startswith("???"):
            await message.channel.send("<@{}> \n에베베베ㅔㅂ".format(id))

        elif message.content.startswith("?도우미"):
            await message.channel.send("<@{}> \n> 도우미를 호출하셨습니다.".format(id))
            await message.author.send(" > 도우미 호출명령어로 호출하셨습니다.")
            await message.author.send("> 명령어를 보시려면 ?명령어를 쳐주세요.")

        
        elif message.content.startswith("?명령어"):
            await message.author.send(embed=discord.Embed(title="명령어", description="안녕, ?도우미", color=0x00ff00))
    

        elif message.content.startswith("/사진"):
            pic = message.content.split(" ")[1]
            await message.channel.send(file=discord.File(pic))
    
    
        elif message.content.startswith("!명령어"):
            await message.channel.send("<@{}> \n[할말]".format(id))
        
        elif message.content.startswith("!인증"):
            author = message.author
            role = discord.utils.get(message.guild.roles, name="💎국민💎")
            await author.add_roles(role)
            await message.channel.send("<@{}> \n ``메테오 서버에 오신것을 환영합니다.``".format(id))
    

        if message.content.startswith("?뮤트"):
            author = message.guild.get_member(int(message.content[4:22]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.add_roles(role)
         
        if message.content.startswith("?언뮤트"):
            author = message.guild.get_member(int(message.content[5:23]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.remove_roles(role)


token=os.environ["TOKEN"]
client.run(token)
