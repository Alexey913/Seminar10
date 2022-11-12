import input_n
import log
import excep
import summ
import sub
import mult
import div

from time import sleep
import logging
from telegram import __version__ as TG_VER
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
 
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(f"This example is not compatible with your current PTB version {TG_VER}. To view the "\
        f"{TG_VER} version of this bot, "\
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)



reply_keyboard_start = [["Калькулятор"],\
                        ["Вывод логов"],\
                        ["Выход"]]

reply_keyboard_choice_num = [["Целые"],\
                            ["Вещественные"],\
                            ["Комплексные"],\
                            ["Главное меню"],\
                            ["Выход"]]

reply_keyboard_action = [["Сложение"],\
                        ["Вычитание"],\
                        ["Умножение"],\
                        ["Деление"],\
                        ["Целочисленное деление"],\
                        ["Остаток от деления"],\
                        ["Главное меню"],\
                        ["Выход"]]

reply_keyboard_action_comp = [["Сложение"],\
                            ["Вычитание"],\
                            ["Умножение"],\
                            ["Деление"],\
                            ["Главное меню"],\
                            ["Выход"]]

reply_keyboard_next_action = [["Продожить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]

markup_start = ReplyKeyboardMarkup(reply_keyboard_start, one_time_keyboard=True)
markup_choice_num = ReplyKeyboardMarkup(reply_keyboard_choice_num, one_time_keyboard=True)
markup_action = ReplyKeyboardMarkup(reply_keyboard_action, one_time_keyboard=True)
markup_action_comp = ReplyKeyboardMarkup(reply_keyboard_action_comp, one_time_keyboard=True)
markup_next_action = ReplyKeyboardMarkup(reply_keyboard_next_action, one_time_keyboard=True)


main_menu, numbers_menu, action_menu, action_menu_comp, next_action, end_prog = range(6)


type_menu_1 = ""
type_menu_2 = ""
type_menu_3 = ""
type_menu_4 = ""
answer = ""

async def main_m (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Калькулятор\nВывод логов\nВыход', reply_markup=markup_start)
    type_menu_1 = update.message.text
    context.user_data["choice"] = type_menu_1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    log.universal_logger("Вход в программу", data_description = "Запуск")
    await update.message.reply_text('Добро пожаловать в программу-калькулятор🔥')
    sleep(1)
    await update.message.reply_text('Для начала работы выбери пункт меню или введите команду', reply_markup=markup_start)
    return main_menu
    

async def choice_num (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text ('С какими числами будем работать?\n\
Целые\nВещественные\nКомплексные\nГлавное меню\nВыход',\
    reply_markup=markup_choice_num)
    type_menu_2 = update.message.text
    context.user_data["choice"] = type_menu_2
    # if type_menu_2 == "Комплексные":
    #     return action_menu_comp
    # else:
    return action_menu


async def choice_action_comp (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{input_n.x}" и "{input_n.y}"?\n\Сложение\nВычитание\nУмножение\nДеление\n\Главное меню\nНазад\nВыход',\
reply_markup=markup_action_comp)
    type_menu_3 = update.message.text
    context.user_data["choice"] = type_menu_3
    if type_menu_3 in range(1,4) or excep.excep_check_zero() is True:
        return res_action
    else:
        return excep.if_zero


async def choice_action (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text (f'Какое действие желаете выполнить с числами \
"{input_n.x}" и "{input_n.y}"?\nСумма\nВычитание\nУмножение\nДеление\n\
Целочисленное деление\nОстаток от деления\nГлавное меню\nНазад\
\nВыход', reply_markup=markup_action)
    type_menu_3 = update.message.text
    context.user_data["choice"] = type_menu_3
    if type_menu_3 in range(1,4) or excep.excep_check_zero() is True:
        return res_action
    else:
        return excep.if_zero

async def res_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if type_menu_3 == 1:
        result = summ.summ
    elif type_menu_3 == 2:
        result = sub.sub
    elif type_menu_3 == 3:    
        result = mult.mult
    elif type_menu_3 == 4:
        result = div.float_div
    elif type_menu_3 == 5:    
        if type_menu_2 != 3:
            result = div.floor_div
        else:
            log.universal_logger("Главное меню", data_description = "Возврат")
            return main_menu
    elif type_menu_3 == 6:
        if type_menu_2 != 3:
            result = div.mod_div()
        else:
            log.universal_logger('Меню ввода данных', data_description = "Повторный ввод")
            return numbers_menu
    elif type_menu_3 == 7:      
        if type_menu_2 != 3:
            log.universal_logger("Главное меню", data_description = "Возврат")
            return main_menu
        else:
            return end_prog
    elif type_menu_3 == 8:      
        log.universal_logger('Меню ввода данных', data_description = "Повторный ввод")
        return numbers_menu
    else:
        return end_prog
    await update.message.reply_text(f'{action(type_menu_3)} чисел {input_n.x} и {input_n.y} составляет {result}')



async def next_act(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(f'Продолжить вычисления с числами "{input_n.x}" и "{input_n.y}"?\n \
Продожить\nНовый ввод\nГлавное меню\nВыход',\
 reply_markup=markup_next_action)
    type_menu_4 = update.message.text
    context.user_data["choice"] = type_menu_4
    return next_action


def action (ent_menu):
    if type_menu_2 == 3:
        action = {1: "Сложение", 2: "Разность", 3: "Произведение", 4: "Частное"}
    else:
        action = {1: "Сложение", 2: "Разность", 3: "Произведение", 4: "Частное",
                  5: "Частное от целочисленного деления", 6: "Остаток от деления"}
    return action.get(ent_menu)
    
    
async def ending (update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_data = context.user_data
    log.universal_logger("по команде пользователя", data_description = "Выход") 
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]
    await update.message.reply_text(f"Выполнение программы завершено! Спасибо!", reply_markup=ReplyKeyboardRemove())
    clear_data()
    user_data.clear()
    return ConversationHandler.END


def clear_data():
    global type_menu_1
    type_menu_1 = ""
    global type_menu_2
    type_menu_2 = ""
    global type_menu_3
    type_menu_3 = ""
    global type_menu_4
    type_menu_4 = ""
    global answer
    answer = ""




def main() -> None:
    application = Application.builder().token("5700119796:AAGgdI8yBQOzkBCRKkAhz4DpxBH6FNxMRFU").build()
    conv_handler = ConversationHandler\
        \
        (entry_points=[CommandHandler("start", start)],\
        \
        states={main_menu: [MessageHandler(filters.Regex("^Калькулятор$"), choice_num),\
                            MessageHandler(filters.Regex("^Вывод логов$"), log.print_log),\
                            MessageHandler(filters.Regex("^Выход$"), ending)],\
                numbers_menu: [MessageHandler(filters.Regex("^Целые$"), input_n.int_num_1),\
                               MessageHandler(filters.Regex("^Вещественные$"), input_n.float_num),\
                               MessageHandler(filters.Regex("^Комплексные$"), input_n.complex_num),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],\
                action_menu: [MessageHandler(filters.Regex("^Сложение$"), summ.summ),\
                               MessageHandler(filters.Regex("^Вычитание$"), sub.sub),\
                               MessageHandler(filters.Regex("^Умножение$"), mult.mult),\
                               MessageHandler(filters.Regex("^Деление$"), div.float_div),\
                               MessageHandler(filters.Regex("^Целочисленное деление$"), div.floor_div),\
                               MessageHandler(filters.Regex("^Остаток от деления$"), div.mod_div),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],
                action_menu_comp: [MessageHandler(filters.Regex("^Сложение$"), summ.summ),\
                               MessageHandler(filters.Regex("^Вычитание$"), sub.sub),\
                               MessageHandler(filters.Regex("^Умножение$"), mult.mult),\
                               MessageHandler(filters.Regex("^Деление$"), div.float_div),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],
                action_menu: [MessageHandler(filters.Regex("^Сложение$"), summ.summ),\
                               MessageHandler(filters.Regex("^Вычитание$"), sub.sub),\
                               MessageHandler(filters.Regex("^Умножение$"), mult.mult),\
                               MessageHandler(filters.Regex("^Деление$"), div.float_div),\
                               MessageHandler(filters.Regex("^Целочисленное деление$"), div.floor_div),\
                               MessageHandler(filters.Regex("^Остаток от деления$"), div.mod_div),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)],
                next_action: [MessageHandler(filters.Regex("^Продолжить$"), choice_action),\
                               MessageHandler(filters.Regex("^Новый ввод$"), choice_num),\
                               MessageHandler(filters.Regex("^Главное меню$"), main_m),\
                               MessageHandler(filters.Regex("^Выход$"), ending)]},
                
        fallbacks=[MessageHandler(filters.Regex("^Выход$"), ending)])
 
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()


reply_keyboard_next_action = [["Продожить"],\
                            ["Новый ввод"],\
                            ["Главное меню"],\
                            ["Выход"]]