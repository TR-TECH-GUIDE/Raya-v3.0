from telegram import Update
from telegram.ext import CallbackContext, run_async

from Raya import dispatcher
from Raya.modules.disable import DisableAbleCommandHandler

EHI_STRINGS = "Here, new ehi files by @TheRayaRobot 👸\n\n👉 https://da.gd/yn1NQ"


@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS)


EHI_HANDLER = DisableAbleCommandHandler("ehi", ehi)
dispatcher.add_handler(EHI_HANDLER)
