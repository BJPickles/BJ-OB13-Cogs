"""
MIT License

Copyright (c) 2021-present Obi-Wan3

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from redbot.core import commands


class Announcements(commands.Cog):
    """Announcement w/ Role Ping"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="announcement")
    @commands.has_any_role('Developer', 'Corporal', 'Corporal I', 'Corporal II', 'Corporal III', 'Corporal IV', 'Lieutenant', 'Lieutenant I', 'Lieutenant II', 'Lieutenant III', 'Lieutenant IV', 'Lieutenant V', 'Subcommander', 'Commander', '91AR Subcommander', '91AR Commander')
    @commands.guild_only()
    async def _announcement(self, ctx: commands.Context, channel: discord.TextChannel, role: discord.Role, *, message=""):
        """Send an announcement message to a specific channel with a role ping."""
        try:
            await ctx.guild.get_channel(channel.id).send(f"{role.mention} {message}", allowed_mentions=discord.AllowedMentions(roles=True))
            return await ctx.tick()
        except discord.Forbidden:
            return await ctx.send("I do not have permissions to send that message!")
