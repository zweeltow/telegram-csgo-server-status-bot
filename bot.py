# -*- coding: utf-8 -*-

import logging

import telebot
from telebot import types

import core.config
import core.strings

from app.timer_drop import Timer
from app.valve_api import ValveServersAPI, ValveServersDataCentersAPI
from app.online_peak import PeakOnline


TEST = False


if TEST: bot = telebot.TeleBot(config.TESTBOT) # the token of the test bot
else: bot = telebot.TeleBot(config.CSGOBETABOT) # the token of the bot
telebot.logger.setLevel(logging.DEBUG) # setup logger
me = config.OWNER # short way to contact the developer
api = ValveServersAPI()
api_dc = ValveServersDataCentersAPI()
timer_drop = Timer()
peak_count = PeakOnline()


"""Setup keyboard"""
# English
markup_en = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
status = types.KeyboardButton('Status')
matchmaking = types.KeyboardButton('Matchmaking')
devcount = types.KeyboardButton('Online devs')
timer = types.KeyboardButton('Cap reset')
dc = types.KeyboardButton('Data centers')
markup_en.add(status, matchmaking, devcount, timer, dc)

# DC
markup_DC = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
europe = types.KeyboardButton('Europe')
asia = types.KeyboardButton('Asia')
south_africa = types.KeyboardButton('South Africa')
south_america = types.KeyboardButton('South America')
australia = types.KeyboardButton('Australia')
usa =  types.KeyboardButton('USA')
back_button = types.KeyboardButton('⏪ Back')
markup_DC.add(asia, australia, europe, south_africa, south_america, usa, back_button)

# DC Asia
markup_DC_Asia = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
india = types.KeyboardButton('India')
emirates = types.KeyboardButton('Emirates')
china = types.KeyboardButton('China')
singapore = types.KeyboardButton('Singapore')
hong_kong = types.KeyboardButton('Hong Kong')
japan = types.KeyboardButton('Japan')
markup_DC_Asia.add(china, emirates, hong_kong, india, japan, singapore)

# DC Europe
markup_DC_EU = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
eu_West = types.KeyboardButton('West')
eu_East = types.KeyboardButton('East')
eu_North = types.KeyboardButton('Nоrth')
markup_DC_EU.add(eu_East, eu_North, eu_West)

# DC USA
markup_DC_USA = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
usa_Northwest = types.KeyboardButton('North')
usa_Southwest = types.KeyboardButton('South')
markup_DC_USA.add(usa_Northwest, usa_Southwest)

# DC Back
markup_DC_Back = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
back_button = types.KeyboardButton('⏪ Back')
markup_DC_Back.add(back_button)

# Russian
markup_ru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
status_ru = types.KeyboardButton('Статус')
matchmaking_ru = types.KeyboardButton('Матчмейкинг')
devcount_ru = types.KeyboardButton('Разработчиков в игре')
timer_ru = types.KeyboardButton('Сброс ограничений')
dc_ru = types.KeyboardButton('Дата-центры (Англ.)')
markup_ru.add(status_ru, matchmaking_ru, devcount_ru, timer_ru, dc_ru)

# DC RU
# markup_DC_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
# Europe_ru = types.KeyboardButton('Европа')
# Asia_ru = types.KeyboardButton('Азия')
# Africa_ru = types.KeyboardButton('Южная Африка')
# South_America_ru = types.KeyboardButton('Южная Америка')
# Australia_ru = types.KeyboardButton('Австралия') 
# USA_ru =  types.KeyboardButton('США')
# Back_button_ru = types.KeyboardButton('⏪ Назад')
# markup_DC_ru.add(Australia_ru, Asia_ru, Europe_ru, USA_ru, South_America_ru, Africa_ru, Back_button_ru)

"""Delete Keyboard"""
markup_del = types.ReplyKeyboardRemove(False)


def log(message):
    """The bot send messages to log channel"""
    bot.send_message(config.LOGCHANNEL, message)

#    if message.from_user.last_name == None:
#        text = f'[<a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>] {message.from_user.first_name} "{message.from_user.username}": {message.text}'
#    else:
#        text = log_message = f'[<a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>] {message.from_user.first_name} "{message.from_user.username}" {message.from_user.last_name}: {message.text}'
    
#    bot.send_message(config.OWNER, text, disable_web_page_preview=None, 
#                     reply_to_message_id=None, reply_markup=None, parse_mode='html', disable_notification=True)


def log_inline(inline_query):
    # bot.send_message(config.OWNER, f'[<a href="tg://user?id={inline_query.from_user.id}">{inline_query.from_user.id}</a>] {inline_query.from_user.first_name} "{inline_query.from_user.username}" {inline_query.from_user.last_name} used <b>inline</b>', parse_mode='html', disable_notification=True)
    bot.send_message(config.LOGCHANNEL, inline_query)

def send_about_problem_valve_api(message):
    """Answer of bot if Valve's API don't answer"""
    
    if message.from_user.language_code == "ru":
        text = strings.wrongAPI_ru
    else:
        text = strings.wrongAPI_en

    bot.send_message(message.chat.id, text)


def send_about_problem_valve_inline(inline_query):
    if inline_query.from_user.language_code == "ru":
        text = "💀 Проблемы с API Valve, пожалуйста, попробуйте позже.\n\n❤️ @csgobetabot"
        markup = markup_ru
    else:
        text = "💀 Issues with Valve's API, please try again later.\n\n❤️ @csgobetabot"
        markup = markup_en

    try:
        bot.send_message(inline_query.from_user.id, text, reply_markup=markup)

    except Exception as e:
        bot.send_message(config.OWNER, f'❗️Error: {e}\n\ninline_query')
        print(e)


def get_status():
    """Get the status of CS:GO servers"""
    sessionsLogon, player_count, time_server = api.status()
    peak24, peak_all = peak_count.get_peak()

    if sessionsLogon == 'normal':
            status_text_en = strings.statusNormal_en.format(player_count, peak24, peak_all, time_server)
            status_text_ru = strings.statusNormal_ru.format(player_count, peak24, peak_all, time_server)
    else:
            status_text_en = strings.statusWrong_en.format(time_server)
            status_text_ru = strings.statusWrong_ru.format(time_server)

    return status_text_en, status_text_ru


def get_matchmaking():
    """Get information about online servers, active players and more about matchmaking servers"""
    scheduler, online_servers, online_players, time_server, search_seconds_avg, searching_players = api.matchmaking()

    if scheduler == 'normal':
            mm_text_en = strings.mmNormal_en.format(online_servers, online_players, searching_players, search_seconds_avg, time_server)
            mm_text_ru = strings.mmNormal_ru.format(online_servers, online_players, searching_players, search_seconds_avg, time_server)
    elif not scheduler == 'normal':
            mm_text_en = strings.mmWrong_en.format(time_server)
            mm_text_ru = strings.mmWrong_ru.format(time_server)

    return mm_text_en, mm_text_ru


def get_devcount():
    """Get the count of online devs"""
    dev_player_count, time_server = api.devcount()

    devcount_text_en = strings.devCount_en.format(dev_player_count, time_server)
    devcount_text_ru = strings.devCount_ru.format(dev_player_count, time_server)

    return devcount_text_en, devcount_text_ru


def get_timer():
    """Get the time left until exp and drop cap reset"""
    delta_days, delta_hours, delta_mins, delta_secs = timer_drop.get_delta()

    timer_text_en = strings.timer_en.format(delta_days, delta_hours, delta_mins, delta_secs)
    timer_text_ru = strings.timer_ru.format(delta_days, delta_hours, delta_mins, delta_secs)

    return timer_text_en, timer_text_ru

def send_status(message):
    """Send the status of CS:GO servers"""
    try:
        status_text_en, status_text_ru = get_status()

        if message.from_user.language_code == 'ru':
            text = status_text_ru
            markup = markup_ru
        else:
            text = status_text_en
            markup = markup_en

        bot.send_message(message.chat.id, text, reply_markup=markup)

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)


def send_matchmaking(message):
    """Send information about online servers, active players and more about matchmaking servers"""
    try:
        mm_text_en, mm_text_ru = get_matchmaking()

        if message.from_user.language_code == 'ru':
            text = mm_text_ru
            markup = markup_ru
        else:
            text = mm_text_en
            markup = markup_en

        bot.send_message(message.chat.id, text, reply_markup=markup)

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)


def send_devcount(message):
    """Send the count of online devs"""
    try:
        devcount_text_en, devcount_text_ru = get_devcount()

        if message.from_user.language_code == 'ru':
                text = devcount_text_ru
                markup = markup_ru
        else:    
                text = devcount_text_en
                markup = markup_en

        bot.send_message(message.chat.id, text, reply_markup=markup) 

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)


def send_timer(message):
    """Send the time left until exp and drop cap reset"""
    try:
        timer_text_en, timer_text_ru = get_timer()

        if message.from_user.language_code == 'ru':
                text = timer_text_ru
                markup = markup_ru
        else:
                text = timer_text_en
                markup = markup_en

        bot.send_message(message.chat.id, text, reply_markup=markup) 

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)

def dc(message):
    try:
        if message.from_user.language_code == 'ru':
            text = '📶 Выберите интересующий регион, чтобы получить информацию о дата-центрах (на английском):'
            markup = markup_DC
        else:
            text = '📶 Select the region you are interested in, to get information about the data centers:'
            markup = markup_DC
        
        bot.send_message(message.chat.id, text, reply_markup=markup)

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)


def dc_africa(message):
    capacity, load, time_server = api_dc.africa_South()
    text = f'🇿🇦 South Africaʼs DC status:\n\n• Location: Johannesburg;\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text)


def dc_australia(message):
    capacity, load, time_server = api_dc.australia()
    text = f'🇦🇺 Australiaʼs DC status:\n\n• Location: Sydney;\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text)


def dc_europe(message):
    text = '📍 Specify the region...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_EU)


def dc_eu_north(message):
    capacity, load, time_server = api_dc.eu_North()
    text = f'🇸🇪 Swedenʼs DC status:\n\n• Location: Stockholm;\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_eu_west(message):
    capacity, load, capacity_Spain, load_Spain, time_server = api_dc.eu_West()
    text = f'🇱🇺 Luxembourgʼs DC status:\n\n• Location: Luxembourg;\n• Load: {load};\n• Capacity: {capacity}.\n\n🇪🇸 Spainʼs DC status:\n\n• Location: Mardid;\n• Load: {load_Spain};\n• Capacity: {capacity_Spain}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_eu_east(message):
    capacity_East, capacity_Poland, load_East, load_Poland, time_server = api_dc.eu_East()
    text = f'🇦🇹 Austriaʼs DC status:\n\n• Location: Vienna;\n• Load: {load_East};\n• Capacity: {capacity_East}.\n\n🇵🇱 Polandʼs DC status:\n\n• Location: Warsaw;\n• Load: {load_Poland};\n• Capacity: {capacity_Poland}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_asia(message):
    text = '📍 Specify the country...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_Asia)


def dc_usa(message):
    text = '📍 Specify the region...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_USA)


def dc_usa_north(message):
    capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest, time_server = api_dc.usa_North()
    text = f'🇺🇸 Northcentral DC status:\n\n• Location: Chicago;\n• Load: {load_US_Northcentral};\n• Capacity: {capacity_US_Northcentral}.\n\n🇺🇸 Northeast DC status:\n\n• Location: Sterling;\n• Load: {load_US_Northeast};\n• Capacity: {capacity_US_Northeast}.\n\n🇺🇸 Northwest DC status:\n\n• Location: Moses Lake;\n• Load: {load_US_Northwest};\n• Capacity: {capacity_US_Northwest}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_usa_south(message):
    capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest, time_server = api_dc.usa_South()
    text = f'🇺🇸 Southwest DC status:\n\n• Location: Los Angeles;\n• Load: {load_US_Southwest};\n• Capacity: {capacity_US_Southwest}.\n\n🇺🇸 Southeast DC status:\n\n• Location: Atlanta;\n• Load: {load_US_Southeast};\n• Capacity: {capacity_US_Southeast}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_south_america(message):
    capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil, time_server = api_dc.sa()
    text = f'🇧🇷 Brazilʼs DC status:\n\n• Location: Sao Paulo;\n• Load: {load_Brazil};\n• Capacity: {capacity_Brazil}.\n\n🇨🇱 Chileʼs DC status:\n\n• Location: Santiago;\n• Load: {load_Chile};\n• Capacity: {capacity_Chile}.\n\n🇵🇪 Peruʼs DC status:\n\n• Location: Lima;\n• Load: {load_Peru};\n• Capacity: {capacity_Peru}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_india(message):
    capacity, capacity_East, load, load_East, time_server = api_dc.india()
    text = f'🇮🇳 Indiaʼs DC status:\n\n• Location: Mumbai;\n• Load: {load};\n• Capacity: {capacity}.\n\n• Location: Chennai;\n• Load: {load_East};\n• Capacity: {capacity_East}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_japan(message):
    capacity, load, time_server = api_dc.japan()
    text = f'🇯🇵 Japanʼs DC status:\n\n• Location: Tokyo;\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_china(message):
    capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou, time_server = api_dc.china()
    text = f'🇨🇳 Chinaʼs DC status: \n\n• Location: Shanghai;\n• Load: {load_Shanghai};\n• Capacity: {capacity_Shanghai}.\n\n• Location: Tianjin;\n• Load: {load_Tianjin};\n• Capacity: {capacity_Tianjin}.\n\n• Location: Guangzhou;\n• Load: {load_Guangzhou};\n• Capacity: {capacity_Guangzhou}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_emirates(message):
    capacity, load, time_server = api_dc.emirates()
    text = f'🇦🇪 Emiratesʼ DC status:\n\n• Location: Dubai;\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_singapore(message):
    capacity, load, time_server = api_dc.singapore()
    text = f'🇸🇬 Singaporeʼs DC status:\n\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_hong_kong(message):
    capacity, load, time_server = api_dc.hong_kong()
    text = f'🇭🇰 Hong Kongʼs DC status:\n\n• Load: {load};\n• Capacity: {capacity}.\n\nLatest update: {time_server} (UTC-8, summer UTC-7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)
 

def back(message):
    if message.from_user.language_code == 'ru':
        markup = markup_ru
    else: markup = markup_en

    bot.send_message(message.chat.id, '👌', reply_markup=markup)


@bot.inline_handler(lambda query: True)
def send_inline(inline_query):
    """Inline mode"""
    try:
        status_text_en, status_text_ru = get_status()
        mm_text_en, mm_text_ru = get_matchmaking()
        devcount_text_en, devcount_text_ru = get_devcount()
        timer_text_en, timer_text_ru = get_timer()

        try:
            if inline_query.from_user.language_code == 'ru':
                status_r = status_text_ru
                mm_r = mm_text_ru
                dev_r = devcount_text_ru
                timer_r = timer_text_ru

            else:
                status_r = status_text_en
                mm_r = mm_text_en
                dev_r = devcount_text_en
                timer_r = timer_text_en
            
            # text part
            if inline_query.from_user.language_code == 'ru': 
                title_status = 'Статус'
                title_mm = 'Матчмейкинг'
                title_dev = 'Бета-версия'
                title_timer = 'Сброс ограничений'

                description_status = 'Проверить доступность серверов'
                description_mm = 'Показать количество активных игроков'
                description_dev = 'Показать количество онлайн разработчиков'
                description_timer = 'Время до сброса ограничений опыта и дропа'
                
            else:
                title_status = 'Status'
                title_mm = 'Matchmaking'
                title_dev = 'Beta version'
                title_timer = 'Drop cap reset'

                description_status = 'Check the availability of the servers'
                description_mm = 'Show the count of active players'
                description_dev = 'Show the count of in-game developers'
                description_timer = 'Time left until experience and drop cap reset'

            r = types.InlineQueryResultArticle('1', title_status, input_message_content = types.InputTextMessageContent(status_r), description=description_status)
            r2 = types.InlineQueryResultArticle('2', title_mm, input_message_content = types.InputTextMessageContent(mm_r), description=description_mm)
            r3 = types.InlineQueryResultArticle('3', title_dev, input_message_content = types.InputTextMessageContent(dev_r), description=description_dev)
            r4 = types.InlineQueryResultArticle('4', title_timer, input_message_content = types.InputTextMessageContent(timer_r), description=description_timer)

            bot.answer_inline_query(inline_query.id, [r, r2, r3, r4], cache_time=15)
            log_inline(inline_query)

        except Exception as e:
            bot.send_message(config.OWNER, f'❗️Error: {e}\n\n↩️ inline_query')
            print(e)

    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_inline(inline_query)


@bot.message_handler(commands=['start'])
def welcome(message):
    """First bot's message"""
    log(message)
    if message.from_user.language_code == 'ru':
        text = strings.cmdStart_ru.format(message.from_user.first_name)
        markup = markup_ru
    else:
        text = strings.cmdStart_en.format(message.from_user.first_name)
        markup = markup_en

    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(commands=['feedback'])
def leave_feedback(message):
    """Send feedback"""
    log(message)

    if message.from_user.language_code == 'ru':
        text = strings.cmdFeedback_ru 
    else:
        text = strings.cmdFeedback_en

    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup_del)
    bot.register_next_step_handler(message, get_feedback)


def get_feedback(message):
    """Get feedback from users"""
    if message.text == '/cancel':
        log(message)
        if message.from_user.language_code == 'ru':
            markup = markup_ru
        else:
            markup = markup_en
        bot.send_message(message.chat.id, '👍', reply_markup=markup)

    else:
        bot.send_message(config.OWNER, f'🆔 <a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>:', parse_mode='html', disable_notification=True)
        bot.forward_message(config.OWNER, message.chat.id, message.message_id)
        
        if not TEST:
            bot.send_message(config.AQ, f'🆔 <a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>:', parse_mode='html', disable_notification=True)
            bot.forward_message(config.AQ, message.chat.id, message.message_id)

        if message.from_user.language_code == 'ru':
            text = 'Отлично! Ваше сообщение отправлено.'
            markup = markup_ru
        else:
            text = 'Awesome! Your message has been sent.'
            markup = markup_en

        bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id,reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    """/help message"""
    log(message)
    if message.from_user.language_code == 'ru':
        text = strings.cmdHelp_ru
        markup = markup_ru
    else:
        text = strings.cmdHelp_en
        markup = markup_en

    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)


@bot.message_handler(content_types=['text'])
def answer(message):
    """Answer of the bot"""
    log(message)
    try:
        bot.send_chat_action(message.chat.id, 'typing')

        if message.text.lower() == 'status' or message.text.lower() == 'статус' or message.text.lower() == '/status':
            send_status(message)

        elif message.text.lower() == 'matchmaking' or message.text.lower() == 'матчмейкинг' or message.text.lower() == '/mm':
            send_matchmaking(message)
        
        elif message.text.lower() == 'online devs' or message.text.lower() == 'разработчиков в игре' or message.text.lower() == '/devcount':
            send_devcount(message)
 
        elif message.text.lower() == 'cap reset' or message.text.lower() == 'сброс ограничений' or message.text.lower() == '/timer':
            send_timer(message)

        elif message.text.lower() == 'data centers' or message.text.lower() == 'дата-центры (англ.)' or message.text.lower() == '/dc':
            dc(message)

        elif message.text.lower() == 'south africa' or message.text.lower() == 'южная африка' or message.text.lower() == '/south_africa':
            dc_africa(message)

        elif message.text.lower() == 'australia' or message.text.lower() == 'австралия' or message.text.lower() == '/australia':
            dc_australia(message)

        elif message.text.lower() == 'europe' or message.text.lower() == 'европа' or message.text.lower() == '/europe':
            dc_europe(message)

        elif message.text.lower() == 'asia' or message.text.lower() == 'азия' or message.text.lower() == '/asia':
            dc_asia(message)

        elif message.text.lower() == 'usa' or message.text.lower() == 'сша' or message.text.lower() == '/usa':
            dc_usa(message)

        elif message.text.lower() == 'south america' or message.text.lower() == 'южная америка' or message.text.lower() == '/south_america':
            dc_south_america(message)

        elif message.text.lower() == 'north' or message.text.lower() == 'северные сша' or message.text.lower() == '/usa_north':
            dc_usa_north(message)

        elif message.text.lower() == 'south' or message.text.lower() == 'южные сша' or message.text.lower() == '/usa_south':
            dc_usa_south(message)

        elif message.text.lower() == 'nоrth' or message.text.lower() == 'северная европа' or message.text.lower() == '/eu_north':
            dc_eu_north(message)

        elif message.text.lower() == 'west' or message.text.lower() == 'западная европа' or message.text.lower() == '/eu_west':
            dc_eu_west(message)

        elif message.text.lower() == 'east' or message.text.lower() == 'восточная европа' or message.text.lower() == '/eu_east':
            dc_eu_east(message)

        elif message.text.lower() == 'india' or message.text.lower() == 'индия' or message.text.lower() == '/india':
            dc_india(message)

        elif message.text.lower() == 'japan' or message.text.lower() == 'япония' or message.text.lower() == '/japan':
            dc_japan(message)

        elif message.text.lower() == 'china' or message.text.lower() == 'китай' or message.text.lower() == '/china':
            dc_china(message)

        elif message.text.lower() == 'emirates' or message.text.lower() == 'эмираты' or message.text.lower() == '/emirates':
            dc_emirates(message)

        elif message.text.lower() == 'singapore' or message.text.lower() == 'сингопур' or message.text.lower() == '/singapore':
            dc_singapore(message)

        elif message.text.lower() == 'hong kong' or message.text.lower() == 'гонконг' or message.text.lower() == '/hong_kong':
            dc_hong_kong(message)

        elif message.text == '⏪ Back' or message.text == '⏪ Назад':
            back(message)


        else:
            if message.from_user.language_code == 'ru':
                text = strings.unknownRequest_ru
                markup = markup_ru
            else: 
                text = strings.unknownRequest_en
                markup = markup_en

            bot.send_message(message.chat.id, text, reply_markup=markup)
    
    except Exception as e:
        bot.send_message(me, f'❗️{e}')

# Polling
bot.polling(True)
