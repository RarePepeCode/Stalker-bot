# See readme.md for instructions on running this code.
import zulip, time
from typing import Any, Dict

class StalkerBot(object):
    def __init__(self):
        self.client = zulip.Client(config_file="~/python-zulip-api/zulip_bots/zulip_bots/bots/Stalker_bot/zuliprc")

    def usage(self) -> str:
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for "Hello World".
        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def handle_message(self, message: Dict[str, Any], bot_handler: Any) -> None:

        email = find_email(message)
        if email == 'no user found':
            bot_handler.send_reply("Sorry, toks naudotojas nebuvo rastas")
        else:
            bot_handler.send_reply(wait_for_user(email))


    def find_email(self,message: Dict[str, Any]) -> str:

        members = self.client.get_members()

        for member in members['members']:
            if not (member['is_bot']) and member['full_name'] in message:
                return  member['email']
        return 'no user found'

    def wait_for_user(self, email: string):
        waiting_user = client.get_user_presence(email)
        if waiting_user['status'] == "active":
            return "HES BACK"
        else:
            time.sleep(20)
            return wait_for_user(email)

handler_class = Stalker_bot
