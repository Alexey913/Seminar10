import log
import excep
import main


from telegram import __version__ as TG_VER
from telegram import Update
from telegram.ext import (ContextTypes)

x = 0
y = 0

async def int_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите число 1:')
    global x
    a = update.message.text
    x = int(a)
    return int_num_2

async def int_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите число 2:')
    global y
    b = update.message.text
    y = int(b)
    log.universal_logger((x,y), data_description = "Ввод данных")
    return main.action_menu



async def float_num_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите число 1:')
    global x
    a = update.message.text
    x = float(a)
    return float_num_2

async def float_num_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:    
    await update.message.reply_text('Введите число 2:')
    global y
    b = update.message.text
    y = float(b)
    return main.action_menu


async def complex_num_1 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите действительную часть числа 1:')
    global d_1
    d_1 = update.message.text
    d_1 = float(d_1)
    return complex_num_2

async def complex_num_2 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите мнимую часть числа 1:')
    global x
    m_1 = update.message.text
    m_1 = float(m_1)
    x = complex(d_1, m_1)
    return complex_num_3


async def complex_num_3 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите действительную часть числа 2:')
    global d_2
    d_2 = update.message.text
    d_2 = float(d_2)
    return complex_num_4

async def complex_num_4 (update: Update, context: ContextTypes.DEFAULT_TYPE) -> float:
    await update.message.reply_text('Введите мнимую часть числа 2:')
    global y
    m_2 = update.message.text
    m_2 = float(m_2)
    y = complex(d_2, m_2)
    return main.action_menu