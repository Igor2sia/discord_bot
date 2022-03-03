import discord
import asyncpraw
import asyncio
import config

bot = discord.Client()
reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                    client_secret=config.settings['SECRET_CODE'],
                    user_agent='random_raddit_bot/0.0.1')

mems = []
TIMEOUT = 5
ID_CHANEL = 948243897933516810
SUBREDDIT_NAME = 'memes'
POST_LIMIT = 1

@bot.event
async def on_ready():
    print('Мемчики полетели')
    channel = bot.get_channel(ID_CHANEL)
    while True:
        await asyncio.sleep(TIMEOUT)
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit=POST_LIMIT)
        item = await memes_submissions.__anext__()
        if item.title not in mems:
            mems.append(item.title)
            await channel.send(item.url)

bot.run(config.settings['DISCORD_TOKEN'])
