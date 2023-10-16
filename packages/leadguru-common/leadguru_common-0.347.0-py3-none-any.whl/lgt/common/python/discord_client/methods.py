from enum import Enum


class DiscordMethods(str, Enum):
    USERS_GUILDS = 'users/@me/guilds'
    LOGIN = 'v9/auth/login'
