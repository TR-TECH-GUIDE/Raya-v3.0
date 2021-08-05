from datetime import datetime

from requests import get
from telegram import ParseMode
from telegram.ext import run_async
from telegram.ext.dispatcher import run_async

from Raya import dispatcher
from Raya.modules.disable import DisableAbleCommandHandler
from Raya.modules.helper_funcs.alternate import typing_action


@run_async
@typing_action
def github(update, context):
    message = update.effective_message
    text = message.text[len("/git ") :]
    usr = get(f"https://api.github.com/users/{text}").json()
    if usr.get("login"):
        text = f"*Username:* [{usr['login']}](https://github.com/{usr['login']})"

        whitelist = [
            "name",
            "id",
            "type",
            "location",
            "blog",
            "bio",
            "followers",
            "following",
            "hireable",
            "public_gists",
            "public_repos",
            "email",
            "company",
            "updated_at",
            "created_at",
        ]

        difnames = {
            "id": "Account ID",
            "type": "Account type",
            "created_at": "Account created at",
            "updated_at": "Last updated",
            "public_repos": "Public Repos",
            "public_gists": "Public Gists",
        }

        goaway = [None, 0, "null", ""]

        for x, y in usr.items():
            if x in whitelist:
                if x in difnames:
                    x = difnames[x]
                else:
                    x = x.title()

                if x == "Account created at" or x == "Last updated":
                    y = datetime.strptime(y, "%Y-%m-%dT%H:%M:%SZ")

                if y not in goaway:
                    if x == "Blog":
                        x = "Website"
                        y = f"[Here!]({y})"
                        text += "\n*{}:* {}".format(x, y)
                    else:
                        text += "\n*{}:* `{}`".format(x, y)
        reply_text = text
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    message.reply_text(
        reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


GITHUB_HANDLER = DisableAbleCommandHandler("git", github, admin_ok=True)

dispatcher.add_handler(GITHUB_HANDLER)
