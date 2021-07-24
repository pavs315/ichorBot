# ichorBot

Discord bot to mute users using commands in the chat. 

## Commands for usage:

```
.muteme                     | to mute yourself
.shut @User1 @User2         | mutes the mentioned user
.muteall                    | mutes everyone that is currently not muted
.unmuteall                  | unmutes everyone
 ```
 
## For hosting:

- Create a .env file in the code folder and paste your bot and guild tokens there-
```
   DISCORD_TOKEN=bot_token
   DISCORD_GUILD=guild_token
```
- Run the bot
`python3 bot.py`

## Caution: 
Works regardless of the server permissions.



