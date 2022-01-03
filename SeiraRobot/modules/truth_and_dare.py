import html
import random
import SeiraRobot.modules.truth_and_dare_string as truth_and_dare_string
from SeiraRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SeiraRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("thuanhan", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("codam", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
