from aiohttp.client import ClientSession
import sys, os, asyncio, shutil, colorama, encodings.idna, time, random
from colorama import Fore
import pymongo
from pymongo.errors import OperationFailure
from pypresence.presence import AioPresence
from tasksio import TaskPool
from aiohttp import client_exceptions
from sys import exit

if sys.platform == 'win32':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)

colorama.init(convert=True)

clear = lambda: os.system("cls")
if sys.platform == "linux":
    clear = lambda: os.system("clear")

class OWL():
    def __init__(self, rpc: AioPresence):
        self.tokens = []
        self.rpc = rpc

        # Checker
        self.checking = False
        self.checked = []
        self.totalChecked = []
        # Checker

        # Proxy Support
        self.proxies = []
        self.proxyless = True
        # Proxy Support

        self.center = shutil.get_terminal_size().columns
        for token in open("tokens.txt"):
            if token != '':
                self.tokens.append(
                    token.replace("\n", "").replace('\r\n',
                                                    '').replace('\r', ''))
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Do you want with proxies? [Y = proxies, N = proxyless]: ' + Fore.RESET, end='')
        resp = input()
        if resp.lower() == 'y':
            for proxy in open("proxies.txt"):
                if proxy != '':
                    split = proxy.replace("\n", "").replace('\r\n',
                                                    '').replace('\r', '').split(":")
                    if len(split) == 2:
                        self.proxies.append(f"http://{split[0]}:{split[1]}")
                    elif len(split) == 4:
                        self.proxies.append(f"http://{split[2]}:{split[3]}@{split[0]}:{split[1]}")

    async def start(self):
        try:
            await self.rpc.update(state="Main Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText()
        print((Fore.BLUE + '[' + Fore.CYAN + '1' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Server Joiner' + Fore.RESET +
               '             ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '2' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Server Leaver' + Fore.RESET +
               '             ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '3' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Channel Spammer' + Fore.RESET +
               '            ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '4' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Nickname Changer' + Fore.RESET +
               '          ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '5' + Fore.BLUE + '] ' +
               Fore.CYAN + 'DM Spammer' + Fore.RESET +
               '                 ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '6' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Friend Spammer' + Fore.RESET +
               '            ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '7' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Typing Spammer' + Fore.RESET +
               '            ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '8' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Bio Changer' + Fore.RESET +
               '                ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '9' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Webhook Spammer' + Fore.RESET +
               '            ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '10' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Reaction Spammer' + Fore.RESET +
               '          ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '11' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Token Checker' + Fore.RESET +
               '             ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '12' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Contact & Info' + Fore.RESET +
               '            ').center(self.center))
        print((Fore.BLUE + '[' + Fore.CYAN + '13' + Fore.BLUE + '] ' +
               Fore.CYAN + 'Exit' + Fore.RESET +
               '                     ').center(self.center))
        print(" ")

        async def askChoice():
            print('                                         ' + Fore.BLUE +
                  '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                  'Your Choice > ' + Fore.RESET + '',
                  end='')
            choice = input()
            if choice.__eq__('1'):
                await self.screen1()
            elif choice.__eq__('2'):
                await self.screen2()
            elif choice.__eq__('3'):
                await self.screen3()
            elif choice.__eq__('4'):
                await self.screen4()
            elif choice.__eq__('5'):
                await self.screen5()
            elif choice.__eq__('6'):
                await self.screen6()
            elif choice.__eq__('7'):
                await self.screen7()
            elif choice.__eq__('8'):
                await self.screen8()
            elif choice.__eq__('9'):
                await self.screen9()
            elif choice.__eq__('10'):
                await self.screen10()
            elif choice.__eq__('11'):
                await self.screen11()
            elif choice.__eq__('12'):
                await self.screen12()
            elif choice.__eq__('13'):
                print('\n                                       ' + Fore.BLUE +
                      '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                      "Thank you for using Owl Spammer")
                exit()
            else:
                print('\n                                       ' + Fore.BLUE +
                      '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                      'Invalid Choice!\n')
                await askChoice()

        await askChoice()

    async def screen1(self):
        try:
            await self.rpc.update(state="Server Joiner Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen1')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide guild invite: ',
              end='')
        guildInv = input()
        if guildInv == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Do you want to bypass rules screen? [Y/N]: ',
              end='')
        bypassRulesScreen = input()
        if bypassRulesScreen == '0':
            await self.start()
        if bypassRulesScreen.lower() == 'y':
            bypassRulesScreen = True
        else:
            bypassRulesScreen = False
        if 'discord.gg' in guildInv or 'discord.com' in guildInv:
            guildInv = guildInv.replace('https://discord.com/invite/',
                                        '').replace('https://discord.gg/',
                                                    '').replace(
                                                        'discord.gg/', '')
        try:
            await self.rpc.update(state="Using Server Joiner", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.joinServer(token, guildInv, bypassRulesScreen))
        await asyncio.sleep(5)
        await self.start()

    async def joinServer(self, token, guildInv, bypassRuleScreen = False):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            try:
                async with session.post("https://discord.com/api/v9/invites/%s" %
                                        (guildInv), proxy=randomProxy) as req:
                    if req.status == 429:
                        print('\n                                       ' +
                            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                            '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                            Fore.RESET)
                    else:
                        try:
                            json = await req.json()
                            if 'message' in json:
                                if 'verify' in json['message']:
                                    print(
                                        '\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                        '] ' + Fore.CYAN +
                                        f'{tk} is unverified and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                elif 'Unauthorized' in json['message']:
                                    print(
                                        '\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                        '] ' + Fore.CYAN +
                                        f'{tk} is not a real token and removed from list!\n'
                                        + Fore.RESET)
                                    if token in self.tokens:
                                        self.tokens.remove(token)
                                elif 'banned' in json['message']:
                                    print('\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} is banned from the server!\n' +
                                        Fore.RESET)
                                elif 'Maximum number of guilds reached' in json[
                                        'message']:
                                    print(
                                        '\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                        '] ' + Fore.CYAN +
                                        f'{tk} has 100 servers and couldn\'t join!\n' +
                                        Fore.RESET)
                                else:
                                    print('\n                                       ' +
                                        Fore.BLUE + '[' + Fore.CYAN + '/' +
                                        Fore.BLUE + '] ' + Fore.CYAN +
                                        f'{tk} failed to join the server!\n' +
                                        Fore.RESET)
                            else:
                                json = await req.json()
                                print('\n                                       ' +
                                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                    '] ' + Fore.CYAN + f'{tk} joined the server!\n' +
                                    Fore.RESET)
                                if bypassRuleScreen == True:
                                    async with session.get("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/member-verification?with_guild=false&invite_code=" + guildInv) as req2:
                                        if req2.status == 200:
                                            j = await req2.json()
                                            async with session.put("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/requests/@me", json=j) as req3:
                                                if req3.status == 201:
                                                    print('\n                                       ' +
                                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                        '] ' + Fore.CYAN + f'{tk} bypassed rules screen!\n' +
                                                        Fore.RESET)
                                                else:
                                                    print('\n                                       ' +
                                                        Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                        '] ' + Fore.CYAN + f'{tk} failed to bypass rules screen!\n' +
                                                        Fore.RESET)
                                        else:
                                            print('\n                                       ' +
                                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                                '] ' + Fore.CYAN + f'{tk} failed to bypass rules screen!\n' +
                                                Fore.RESET)
                        except client_exceptions.ContentTypeError:
                            pass
            except client_exceptions.ClientHttpProxyError:
                print('\n                                       ' +
                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                    '] ' + Fore.CYAN + f'{tk} failed to join the server, Proxy Error!\n' +
                    Fore.RESET)
                pass
            except client_exceptions.ClientConnectorError:
                print('\n                                       ' +
                    Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                    '] ' + Fore.CYAN + f'{tk} failed to join the server, Failed to connect to discord.com!\n' +
                    Fore.RESET)
                pass

    async def screen2(self):
        try:
            await self.rpc.update(state="Server Leaver Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen2')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide guild id: ',
              end='')
        guildId = input()
        if guildId == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using Server Leaver", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.leaveServer(token, guildId))
        await asyncio.sleep(5)
        await self.start()

    async def leaveServer(self, token, guildId):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.delete(
                    "https://discord.com/api/v9/users/@me/guilds/%s" %
                (guildId), proxy=randomProxy) as req:
                if req.status == 429:
                    print('\n                                       ' +
                          Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                          '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                          Fore.RESET)
                elif req.status == 204:
                    print('\n                                       ' +
                          Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                          '] ' + Fore.CYAN + f'{tk} left the server!\n' +
                          Fore.RESET)
                else:
                    json = await req.json()
                    if 'message' in json:
                        if 'verify' in json['message']:
                            print(
                                '\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif 'Unauthorized' in json['message']:
                            print(
                                '\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN +
                                f'{tk} is not a real token and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif 'Unknown Guild' in json['message']:
                            pass
                        else:
                            print('\n                                       ' +
                                  Fore.BLUE + '[' + Fore.CYAN + '/' +
                                  Fore.BLUE + '] ' + Fore.CYAN +
                                  f'{tk} failed to leave the server!\n' +
                                  Fore.RESET)

    async def screen3(self):
        try:
            await self.rpc.update(state="Channel Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen3')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide channel id: ',
              end='')
        chId = input()
        if chId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide message: ',
              end='')
        msg = input()
        if msg == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN + 'Amount: ',
              end='')
        amount = input()
        if amount == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'You want to reply to a message? [Y/N]: ',
              end='')
        replyQues = input()
        replyMsg = None
        if replyQues.lower() == 'y':
            print('\n                                       ' + Fore.BLUE +
                  '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                  'Please provide reply message id: ',
                  end='')
            replyMsg = input()
        try:
            await self.rpc.update(state="Using Channel Spammer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(
                    self.channelSpammer(token, chId, msg, amount, replyMsg))
        await asyncio.sleep(5)
        await self.start()

    async def channelSpammer(self,
                             token,
                             chId,
                             msg,
                             amount="1",
                             replyMsg=None):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)
        j = {"content": msg}
        if replyMsg != None:
            j['message_reference'] = {
                "channel_id": chId,
                "message_id": replyMsg
            }
        for i in range(int(amount)):

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.post(
                        "https://discord.com/api/v9/channels/%s/messages" %
                    (chId),
                        json=j, proxy=randomProxy) as req:
                    if req.status == 429:
                        print('\n                                       ' +
                              Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                              '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                              Fore.RESET)
                    elif req.status == 200:
                        print('\n                                       ' +
                              Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                              '] ' + Fore.CYAN + f'{tk} sent message!\n' +
                              Fore.RESET)
                    else:
                        json = await req.json()
                        if 'message' in json:
                            if 'verify' in json['message']:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Unauthorized' in json['message']:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is not a real token and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif 'Missing Access' in json['message']:
                                pass
                            else:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to send message!\n' +
                                    Fore.RESET)

    async def screen4(self):
        try:
            await self.rpc.update(state="Nickname Changer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen4')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide guild id: ',
              end='')
        guildId = input()
        if guildId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide new nickname: ',
              end='')
        nick = input()
        if nick == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using Nickname Changer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.nicknameChanger(token, guildId, nick))
        await asyncio.sleep(5)
        await self.start()

    async def nicknameChanger(self, token, guildId, nick):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.patch(
                    "https://discord.com/api/v9/guilds/%s/members/@me/nick" %
                (guildId),
                    json={"nick": nick}, proxy=randomProxy) as req:
                if req.status == 429:
                    print('\n                                       ' +
                          Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                          '] ' + Fore.CYAN + f'{tk} is rate limited!\n' +
                          Fore.RESET)
                elif req.status == 200:
                    print('\n                                       ' +
                          Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                          '] ' + Fore.CYAN + f'{tk} changed nickname!\n' +
                          Fore.RESET)
                else:
                    json = await req.json()
                    if 'message' in json:
                        if 'verify' in json['message']:
                            print(
                                '\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif 'Unauthorized' in json['message']:
                            print(
                                '\n                                       ' +
                                Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                                '] ' + Fore.CYAN +
                                f'{tk} is not a real token and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif 'Unknown Guild' in json['message']:
                            pass
                        else:
                            print('\n                                       ' +
                                  Fore.BLUE + '[' + Fore.CYAN + '/' +
                                  Fore.BLUE + '] ' + Fore.CYAN +
                                  f'{tk} failed to nick!\n' + Fore.RESET)

    async def screen5(self):
        try:
            await self.rpc.update(state="DM Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen5')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide user id: ',
              end='')
        userId = input()
        if userId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide message: ',
              end='')
        msg = input()
        if msg == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN + 'Amount: ',
              end='')
        amount = input()
        if amount == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using DM Spammer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.dmSpammer(token, userId, msg, amount))
        await asyncio.sleep(5)
        await self.start()

    async def dmSpammer(self, token, userId, msg, amount="1"):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        async with ClientSession(headers=headers) as session:
            for i in range(int(amount)):

                randomProxy = ''
                if self.proxyless == False:
                    randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

                async with session.post(
                        "https://discord.com/api/v9/users/@me/channels",
                        json={"recipient_id": userId}, proxy=randomProxy) as r:
                    if r.status == 200:
                        json = await r.json()
                        id = json["id"]
                        async with session.post(
                                "https://discord.com/api/v9/channels/%s/messages"
                                % (id),
                                json={"content": msg}) as r:
                            text = await r.text()
                            if "content" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} successfully sent message!\n' +
                                    Fore.RESET)
                            elif "You need to verify your account" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is unverified and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            elif "Unauthorized" in text:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} is invalid and removed from list!\n'
                                    + Fore.RESET)
                                if token in self.tokens:
                                    self.tokens.remove(token)
                            else:
                                print(
                                    '\n                                       '
                                    + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                    Fore.BLUE + '] ' + Fore.CYAN +
                                    f'{tk} failed to send message!\n' +
                                    Fore.RESET)
                    else:
                        print('\n                                       ' +
                              Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE +
                              '] ' + Fore.CYAN +
                              f'{tk} failed to send message!\n' + Fore.RESET)

    async def screen6(self):
        try:
            await self.rpc.update(state="Friend Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen6')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide the type [a = add/r = remove]: ',
              end='')
        type = input()
        if type == '0':
            await self.start()
        if type == 'a' or type == 'add':
            type = 'add'
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide user tag: ',
                end='')
            userTag = input()
            if userTag == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Friend Spammer", details="Sexy Spammer", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.friendSpammer(token, userTag, type))
            await asyncio.sleep(5)
            await self.start()
        elif type == 'r' or type == 'remove':
            type = 'remove'
            print('\n                                       ' + Fore.BLUE + '[' +
                Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
                'Please provide user id: ',
                end='')
            userId = input()
            if userId == '0':
                await self.start()
            try:
                await self.rpc.update(state="Using Friend Spammer", details="Sexy Spammer", large_image="default")
            except:
                pass
            async with TaskPool(5_000) as pool:
                for token in self.tokens:
                    await pool.put(self.friendSpammer(token, userId, type))
            await asyncio.sleep(5)
            await self.start()

    async def friendSpammer(self, token, userTag_Or_id, type = 'add'):
        if type == 'add':
            userName = userTag_Or_id.split('#')[0]
            userDiscrim = userTag_Or_id.split('#')[1]
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.post(
                        "https://discord.com/api/v9/users/@me/relationships",
                        json={"discriminator": userDiscrim, "username": userName}, proxy=randomProxy) as r:
                    
                    if r.status == 204:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} successfully friended!\n' +
                            Fore.RESET)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t friend, invalid user!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to friend!\n' +
                                Fore.RESET)
        elif type == 'remove':
            headers = {
                "Authorization":
                token,
                "accept":
                "*/*",
                "accept-language":
                "en-US",
                "connection":
                "keep-alive",
                "cookie":
                f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
                "DNT":
                "1",
                "origin":
                "https://discord.com",
                "sec-fetch-dest":
                "empty",
                "sec-fetch-mode":
                "cors",
                "sec-fetch-site":
                "same-origin",
                "referer":
                "https://discord.com/channels/@me",
                "TE":
                "Trailers",
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
                "X-Super-Properties":
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }
            tk = token
            try:
                tk = token[:25] + "*" * 34
            except:
                tk = "*" * len(token)

            randomProxy = ''
            if self.proxyless == False:
                randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

            async with ClientSession(headers=headers) as session:
                async with session.delete(
                        "https://discord.com/api/v9/users/@me/relationships/" + userTag_Or_id, proxy=randomProxy) as r:
                    
                    if r.status == 204:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} successfully unfriended!\n' +
                            Fore.RESET)
                    elif r.status == 400:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} couldn\'t unfriend, invalid id!\n' +
                            Fore.RESET)
                    else:
                        text = await r.text()
                        if "You need to verify your account" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is unverified and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        elif "Unauthorized" in text:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} is invalid and removed from list!\n'
                                + Fore.RESET)
                            if token in self.tokens:
                                self.tokens.remove(token)
                        else:
                            print(
                                '\n                                       '
                                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                                Fore.BLUE + '] ' + Fore.CYAN +
                                f'{tk} failed to unfriend!\n' +
                                Fore.RESET)
    
    async def screen7(self):
        try:
            await self.rpc.update(state="Typing Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen7')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide the channel id: ',
              end='')
        chId = input()
        if chId == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using Typing Spammer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.typingSpammer(token, chId))
        await asyncio.sleep(5)
        await self.start()
        
    async def typingSpammer(self, token, chId):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.post(
                    "https://discord.com/api/v9/channels/" + chId + '/typing', proxy=randomProxy) as r:
                
                if r.status == 204:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} successfully started typing!\n' +
                        Fore.RESET)
                elif r.status == 400:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} couldn\'t start typing!\n' +
                        Fore.RESET)
                else:
                    text = await r.text()
                    if "You need to verify your account" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is unverified and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif "Unauthorized" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is invalid and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    else:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} failed to start typing!\n' +
                            Fore.RESET)

    async def screen8(self):
        try:
            await self.rpc.update(state="Bio Changer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen8')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide the new bio: ',
              end='')
        bio = input()
        if bio == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using Bio Changer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.bioChanger(token, bio))
        await asyncio.sleep(5)
        await self.start()
    
    async def screen9(self):
        try:
            await self.rpc.update(state="Webhook Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen9')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide the webhook url: ',
              end='')
        webhookUrl = input()
        if webhookUrl == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide the message: ',
              end='')
        msg = input()
        if msg == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Amount: ',
              end='')
        amount = input()
        try:
            await self.rpc.update(state="Using Webhook Changer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for i in range(int(amount)):
                await pool.put(self.webhookSpammer(webhookUrl, msg))
        await asyncio.sleep(5)
        await self.start()
    
    async def webhookSpammer(self, webhookUrl, msg):
        headers = {
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.post(
                    webhookUrl, proxy=randomProxy, json={"content": msg}) as r:
                if r.status == 204:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Successfully sent message!\n' +
                        Fore.RESET)
                else:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Failed to send message!\n' +
                        Fore.RESET)

    async def screen10(self):
        try:
            await self.rpc.update(state="Reaction Spammer Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen10')
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide channel id: ',
              end='')
        chId = input()
        if chId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide message id: ',
              end='')
        msgId = input()
        if msgId == '0':
            await self.start()
        print('\n                                       ' + Fore.BLUE + '[' +
              Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
              'Please provide reaction (for normal use \:emoji:, for others use name:id): ',
              end='')
        emoji = input()
        if emoji == '0':
            await self.start()
        try:
            await self.rpc.update(state="Using Reaction Spammer", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.reactionSpammer(token, chId, msgId, emoji))
        await asyncio.sleep(5)
        await self.start()

    async def reactionSpammer(self, token, chId, msgId, emoji):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.put(
                    "https://discord.com/api/v9/channels/%s/messages/%s/reactions/%s/@me" % (
                        chId,
                        msgId,
                        emoji
                    ), proxy=randomProxy) as r:
                
                if r.status == 204:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} successfully reacted!\n' +
                        Fore.RESET)
                elif r.status == 404:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} couldn\'t react, {r.reason}!\n' +
                        Fore.RESET)
                elif r.status == 400:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} couldn\'t react, Unknown Emoji!\n' +
                        Fore.RESET)
                else:
                    text = await r.text()
                    if "You need to verify your account" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is unverified and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif "Unauthorized" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is invalid and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    else:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} failed to react!\n' +
                            Fore.RESET)

    async def bioChanger(self, token, bio):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.patch(
                    "https://discord.com/api/v9/users/@me", json={"bio": bio}, proxy=randomProxy) as r:
                
                if r.status == 200:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} successfully changed bio!\n' +
                        Fore.RESET)
                elif r.status == 400:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} couldn\'t change bio!\n' +
                        Fore.RESET)
                else:
                    text = await r.text()
                    if "You need to verify your account" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is unverified and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif "Unauthorized" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is invalid and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    else:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} failed to change bio!\n' +
                            Fore.RESET)

    async def screen11(self):
        try:
            await self.rpc.update(state="Token Checker Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen11')
        print(
            '                                       '
            + Fore.BLUE + '[' + Fore.CYAN + '/' +
            Fore.BLUE + '] ' + Fore.CYAN +
            f'Checking Tokens...' +
            Fore.RESET)
        try:
            await self.rpc.update(state="Using Token Checker", details="Sexy Spammer", large_image="default")
        except:
            pass
        async with TaskPool(5_000) as pool:
            for token in self.tokens:
                await pool.put(self.tokenChecker(token))
        while self.checked == False:
            pass
        else:
            print(
                '                                       '
                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                Fore.BLUE + '] ' + Fore.CYAN +
                f'Checked tokens. Valid = {len(self.checked)} ~ Total = {len(self.totalChecked)}' +
                Fore.RESET)
            print(
                '                                       '
                + Fore.BLUE + '[' + Fore.CYAN + '/' +
                Fore.BLUE + '] ' + Fore.CYAN +
                f'Do you want to save them in separate file? [Y/N]: ' +
                Fore.RESET, end='')
            resp = input()
            if resp.lower() == 'y':
                added = 0
                with open('owl-data/checked.txt', 'w') as f:
                    for t in self.checked:
                        f.write(t + '\n')
                        added += 1
                while added != len(self.checked):
                    pass
                else:
                    print(
                        '                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Saved new tokens in owl-data/checked.txt.' +
                        Fore.RESET)
                    print(
                        '                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Do you want to go back? [Y/N]: ' +
                        Fore.RESET, end='')
                    r = input()
                    if r.lower() == 'y':
                        self.checked = []
                        self.totalChecked = []
                        await self.start()
                    else:
                        self.exit()
            else:
                added = 0
                open('tokens.txt', 'w').close()
                with open('tokens.txt', 'w') as f:
                    for t in self.checked:
                        f.write(t + '\n')
                        added += 1
                while added != len(self.checked):
                    pass
                else:
                    print(
                        '                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Replaced with new tokens in tokens.txt.' +
                        Fore.RESET)
                    print(
                        '                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'Do you want to go back? [Y/N]: ' +
                        Fore.RESET, end='')
                    r = input()
                    if r.lower() == 'y':
                        self.checked = []
                        self.totalChecked = []
                        await self.start()
                    else:
                        self.exit()
        
    async def tokenChecker(self, token):
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if self.proxyless == False:
            randomProxy = self.proxies[random.randint(0, len(self.proxies)-1)]

        self.totalChecked.append(token)
        async with ClientSession(headers=headers) as session:
            async with session.get(
                    "https://discord.com/api/v9/users/@me/library", proxy=randomProxy) as r:
                
                if r.status == 200:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} is valid!\n' +
                        Fore.RESET)
                    self.checked.append(token)
                elif r.status == 400:
                    print(
                        '\n                                       '
                        + Fore.BLUE + '[' + Fore.CYAN + '/' +
                        Fore.BLUE + '] ' + Fore.CYAN +
                        f'{tk} couldn\'t check!\n' +
                        Fore.RESET)
                else:
                    text = await r.text()
                    if "You need to verify your account" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is locked and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    elif "Unauthorized" in text:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} is invalid and removed from list!\n'
                            + Fore.RESET)
                        if token in self.tokens:
                            self.tokens.remove(token)
                    else:
                        print(
                            '\n                                       '
                            + Fore.BLUE + '[' + Fore.CYAN + '/' +
                            Fore.BLUE + '] ' + Fore.CYAN +
                            f'{tk} failed to check!\n' +
                            Fore.RESET)

    async def screen12(self):
        try:
            await self.rpc.update(state="Contact & Info Screen", details="Sexy Spammer", large_image="default")
        except:
            pass
        clear()
        self.sendText('screen12')
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
              Fore.CYAN + 'Contact: https://discord.gg/2aF8RDJxct')
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
              Fore.CYAN + 'Website: https://sites.google.com/view/owlspammer/home')
        print(" ")
        print(
            Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' + Fore.CYAN +
            'Info: Hello User, This is Owl Spammer, a new spammer for discord. This tool is for spamming discord\'s api and troll servers/users. We want this to be famous and yeah, hope you like it <3.'
        )
        print(" ")
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
              Fore.CYAN + 'Do you want to go back? [Y/N] > ',
              end='')
        goBack = input()
        if goBack == '0':
            await self.start()
        elif goBack.lower() == 'y':
            await self.start()
        else:
            print(" ")
            self.exit()

    def exit(self):
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                  Fore.CYAN + "Thank you for using Owl Spammer")
        exit()

    def sendText(self, screen='main'):
        print(Fore.CYAN, end='')
        print(
            '   ____           _    _____                                           '
            .center(self.center))
        print(
            '  / __ \         | |  / ____|                                          '
            .center(self.center))
        print(
            ' | |  | |_      _| | | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ '
            .center(self.center))
        print(
            ' | |  | \ \ /\ / / |  \___ \| \'_ \ / _` | \'_ ` _ \| \'_ ` _ \ / _ \ \'__|'
            .center(self.center))
        print(
            ' | |__| |\ V  V /| |  ____) | |_) | (_| | | | | | | | | | | |  __/ |   '
            .center(self.center))
        print(
            '  \____/  \_/\_/ |_| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_| v2'
            .center(self.center))
        print(
            '                            | |                                        '
            .center(self.center))
        if screen == 'main':
            print(
                '                            |_|                                        '
                .center(self.center))

        elif screen == 'screen1':
            print(
                '         Server Joiner      |_|                                        '
                .center(self.center))
        elif screen == 'screen2':
            print(
                '         Server Leaver      |_|                                        '
                .center(self.center))
        elif screen == 'screen3':
            print(
                '        Channel Spammer     |_|                                        '
                .center(self.center))
        elif screen == 'screen4':
            print(
                '        Nickname Changer    |_|                                        '
                .center(self.center))
        elif screen == 'screen5':
            print(
                '           DM Spammer       |_|                                        '
                .center(self.center))
        elif screen == 'screen6':
            print(
                '         Friend Spammer     |_|                                        '
                .center(self.center))
        elif screen == 'screen7':
            print(
                '         Typing Changer      |_|                                        '
                .center(self.center))
        elif screen == 'screen8':
            print(
                '          Bio Changer       |_|                                        '
                .center(self.center))
        elif screen == 'screen9':
            print(
                '        Webhook Spammer     |_|                                        '
                .center(self.center))
        elif screen == 'screen10':
            print(
                '        Reaction Spammer    |_|                                        '
                .center(self.center))
        elif screen == 'screen11':
            print(
                '          Token Checker     |_|                                        '
                .center(self.center))
        elif screen == 'screen12':
            print(
                '         Contact & Info     |_|                                        '
                .center(self.center))
        print(Fore.RESET)
        print((Fore.MAGENTA + '                            Developed by ' +
               Fore.BLUE + 'Geb ♡#0001' + Fore.MAGENTA + ',' + Fore.BLUE +
               ' StarlexDev#7902' + Fore.RESET).center(self.center))
        print(' ')

class Auth():
    async def start(self):
        try:
            client_id = '867789446769934386'
            rpc = AioPresence(client_id)
            await rpc.connect()
        except:
            pass
        owl = OWL(rpc)
        await owl.start()
        time.sleep(0.2)
        alreadyPut == true
        if alreadyPut == true:
            print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                    Fore.CYAN + 'Please provide your serial number from order: ' + Fore.RESET, end='')
            serialNmbr = input()
            try:
                print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                            Fore.CYAN + 'Checking...' + Fore.RESET)
                mongo = pymongo.MongoClient(f'mongodb+srv://{serialNmbr}:owlspammer@rikocluster.5sh7t.mongodb.net/OwlSpammer?retryWrites=true&w=majority')
                mongo.admin.command('ping')
                time.sleep(0.5)
                with open(f'{appdata}/OwlSpammer/serial_number.txt', 'w') as f:
                    f.write('# DO NOT SEND IT TO ANYONE\n' + serialNmbr)
                try:
                    await rpc.update(state="Waiting for Proxy Confirmation...", details="Sexy Spammer", large_image="default")
                except:
                    pass
                mongo.close()
                owl = OWL(rpc)
                await owl.start()
            except OperationFailure:
                self.exit()
    def exit(self):
        print(Fore.BLUE + '[' + Fore.CYAN + '/' + Fore.BLUE + '] ' +
                        Fore.CYAN + 'Not a correct serial number!' + Fore.RESET)
        exit()

auth = Auth()
loop = asyncio.get_event_loop()
loop.run_until_complete(auth.start())