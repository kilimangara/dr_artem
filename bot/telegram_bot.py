import logging
import random

import time
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

logger = logging.getLogger(__name__)
INTRO_TEXT = \
    'Понять, что тут написано, сможет только самый проницательный человек.\n' \
    '"mbis ti gnk qimj?"'

CORRECT_TEXT = "What do you want?"

FINAL_TEXT = "Я хочу, чтобы ты открыл страницу http://attemka.ru/numbers"

STICKERS_TO_RESPOND = [
    'CAADAgADKAADBOj5DnVj84ekB6fzAg',
    'CAADAgADKgADBOj5DpWe7-8YxLJYAg'
]


def messages_handler(bot, update):
    if not update.message:
        logger.info("Messages handler receives update without message")
        return
    chat_id = update.message.chat.id
    text = (update.message.text or '').strip()
    if text == CORRECT_TEXT:
        logger.info("correct text input")
        bot.send_message(chat_id=chat_id, text=FINAL_TEXT)
    else:
        logger.info("incorrect text input: %s", text)
        bot.send_sticker(chat_id=chat_id,
                         sticker=random.choice(STICKERS_TO_RESPOND))


def start_handler(bot, update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text=INTRO_TEXT)


def main():
    print('main started')
    random.seed(time.time())
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    updater = Updater('470843719:AAEKRN4PxMO5voWAoqPzjq7mY4h_1-kefhs')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_handler))
    dp.add_handler(MessageHandler(Filters.all, messages_handler))

    updater.start_polling()
    logger.info("Start polling")
    updater.idle()


if __name__ == '__main__':
    main()