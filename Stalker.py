# See readme.md for instructions on running this code.
import zulip
import time
import json
import threading
from typing import Any, Dict

class Stalker(object):
     # def __init__(self):
     #    self.client = zulip.Client(config_file="~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker/zuliprc")

    config_file = "~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker/zuliprc"

    no_user_found_url = "https://i.makeagif.com/media/2-18-2016/M3yKm-.gif"
    duane_url = "https://media1.tenor.com/images/ba099f1221f54328c7c7d5f6a11d6e03/tenor.gif?itemid=7543160"
    we_got_him_url = "https://media.tenor.com/images/4feaf73d3b8f5b4f3ee0a1423355dcc0/tenor.gif"

    def usage(self) -> str:
        return '''
        This is a sophisticated bot, that uses advance algorithms and machine learning
        to calculate exact time when a user will be online and messages back, when that
        time comes.
        '''

    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:
        content = message['content']
        email = Stalker.find_email(self, content)
        if email == "no user found":
            bot_handler.send_reply(message, "Sorry, toks naudotojas nebuvo rastas")
            bot_handler.send_reply(message, Stalker.no_user_found_url)

        else:
            threading.Thread(target=Stalker.wait_for_user, args=(self, email, 0, bot_handler, message)).start()
            bot_handler.send_reply(message, "Stalkinu auką")

    def find_email(self,message: Dict[str, Any]) -> str:
        client = zulip.Client(config_file=Stalker.config_file)
        members = client.get_members()
        for member in members['members']:
            if not (member['is_bot']) and member['full_name'] in message:
                return  member['email']
        return 'no user found'

    def wait_for_user(self, email: str, i: int, bot_handler: Any, message: Dict[str, Any]):
        i = i + 1
        client = zulip.Client(config_file=Stalker.config_file)
        waiting_user = client.get_user_presence(email)
        if waiting_user['presence']['aggregated']['status'] == "active":
            bot_handler.send_reply(message, Stalker.we_got_him_url)
        elif i == 15:
            bot_handler.send_reply(message, "atsibodo laukti")
        else:
            time.sleep(20)
            return Stalker.wait_for_user(self, email, i, bot_handler, message)

handler_class = Stalker
