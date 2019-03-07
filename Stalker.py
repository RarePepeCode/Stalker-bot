# See readme.md for instructions on running this code.
import zulip
import time
import json
from typing import Any, Dict

class Stalker(object):
     # def __init__(self):
     #    self.client = zulip.Client(config_file="~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker/zuliprc")

    def usage(self) -> str:
        return '''
        This is a sophisticated bot, that uses advance algorithms and machine learning
        calculates exact time when a user will be online and messages back, when that
        time comes.
        '''



    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:
        content = message['content']
        email = find_email(self, content)
        print (email)
        if email == "no user found":
            bot_handler.send_reply(message, "Sorry, toks naudotojas nebuvo rastas")
        else:
            bot_handler.send_reply(message, "Stalkinu auką")
            answer = wait_for_user(self, email, 0)
            bot_handler.send_reply(message, answer)

def find_email(self,message: Dict[str, Any]) -> str:
    client = zulip.Client(config_file="~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker/zuliprc")
    members = client.get_members()
    for member in members['members']:
        if not (member['is_bot']) and member['full_name'] in message:
            return  member['email']
    return 'no user found'

def wait_for_user(self, email: str, i: int):
    i = i + 1
    client = zulip.Client(config_file="~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker/zuliprc")
    waiting_user = client.get_user_presence(email)
    print(waiting_user)
    if waiting_user['presence']['aggregated']['status'] == "active":
        return "HE/SHE is BACK"
    elif i == 15:
        return  "atsibodo laukti"
    else:
        time.sleep(20)
    return wait_for_user(self, email, i)


handler_class = Stalker
