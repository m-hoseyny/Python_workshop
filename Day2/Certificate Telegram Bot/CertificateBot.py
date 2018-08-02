import telebot
from Authentication import Authentication as Auth
from DataBase import EvandExcelParser as EEP
import pandas as pd
TOKEN = '691564985:AAH-B1geClWEv-cUsosVs_PldlLfQSuvd00'

bot = telebot.TeleBot(TOKEN)
auth = Auth(path_file = 'users_telegram/')
auth.set_state_list(['start', 'get_identication', 'complete'])
eep = EEP(file_path='list.xlsx')

users_row = dict()

def identication_parser(message):
    if auth.get_state(message) == 'start':
        return 1
    else:
        return 0

def entername_stage(message):
    if auth.get_state(message) == 'get_identication':
        return 1
    else:
        return 0

@bot.message_handler(commands=['start'])
def start_command_response(message):
    print(message.chat)
    bot.send_message(message.chat.id, 'سلام. خوش آمدید.\nلطفا ایمیل یا شماره تلفن خود را وارد کنید')
    auth.set_state(message=message)

@bot.message_handler(func = identication_parser)
def get_identication(message):
    text = message.text
    user_number = None
    user_email = None
    if text.isnumeric():
        user_number = text
        bot.send_message(message.chat.id, 'اطلاعات ورودی:\n' + str(user_number))
    elif '@' in text:
        user_email = text
        bot.send_message(message.chat.id, 'اطلاعات ورودی:\n' + str(user_email))
    else:
        bot.send_message(message.chat.id, 'ورودی اشتباه است.لطفا شماره تلفن و یا ایمیل خود را وارد کنید.')
        return
    users_row[message.chat.id] = eep.verify_user(email=user_email, number=user_number)
    auth.next_state(message)

@bot.message_handler(func = entername_stage)
def get_fullname_from_user(message):
    Fullname = message.text
    eep.set_fullname(users_row[message.chat.id], Fullname)
    auth.next_state(message)
    bot.send_message(message.chat.id, 'اطلاعات شما وارد شد\n' + str(Fullname))
    eep.save_excel()

bot.polling(none_stop=True)


