import input_n
import main
import log

from telegram import __version__ as TG_VER
from telegram import Update
from telegram.ext import (ContextTypes)
 

def excep_check_zero():
    try:
        input_n.x / input_n.y
        return True
    except ZeroDivisionError:
        return False

async def enter_data_error (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text ('Неверный пункт меню! Повторите ввод!')
    ent_menu = update.message.text
    return check_menu(ent_menu, 4)





def check_menu (type_menu, quan) -> int:
    while True:
        try:
            while int(type_menu) not in range (1, quan):
                log.universal_logger("Неверный пункт меню", data_description = "Ошибка ввода")
                return enter_data_error
            return int(user_data)
        except ValueError:
            log.universal_logger("Неверный формат ввода меню", data_description = "Ошибка ввода")
            error_mes = 'Неверный формат! Повторите ввод!'
            return error_mes

async def if_zero (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text ('Ошибка! Деление на ноль. Повторите ввод данных')
    log.universal_logger("Деление на 0", data_description = "Ошибка")
    main.next_act
    

async def check_int (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    while True:
        try:
            user_data = enter_data
            return int(user_data)
        except ValueError:
            await update.message.reply_text ('\nНеверный формат! Повторите ввод:')
            log.universal_logger("Неверный формат ввода данных", data_description = "Ошибка ввода")


async def check_float (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    while True:
        try:
            user_data = enter_data
            return float(user_data)
        except ValueError:
            await update.message.reply_text ('\nНеверный формат! Повторите ввод:')
            log.universal_logger("Неверный формат ввода данных", data_description = "Ошибка ввода")