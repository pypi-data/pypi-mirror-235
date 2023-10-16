import discord
from CharmCord.CharmErrorHandling import CharmCordErrors


async def createChannel(args, context):
    """
    Ex. $createChannel[GuildID;Type;Channel Name;Position?;Topic?;NSFW?;SlowMode?]
    :param args: Guild ID, Channel type, Channel name,
    :param context: Discord Context
    :return: Setter to create discord channel
    """
    from CharmCord.Classes.CharmCord import bots
    guild_id, type, channel_name, pos, topic, nsfw, slow_mode = str(args).split(";")
    try:
        guild = bots.fetch_guild(int(guild_id))
    except ValueError:
        CharmCordErrors(
            f"Invalid guild id ({guild_id}) provided for $createChannel | In command {context.command.name}")
    context.create_text_channel()
