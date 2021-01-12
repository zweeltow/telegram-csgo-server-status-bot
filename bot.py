# -*- coding: utf-8 -*-

import logging
import time
import json

import telebot
from telebot import types

import config
import strings

from apps.timer import TimerDrop
from apps.valve_api import ValveServersDataCentersAPI
from apps import file_manager


bot = telebot.TeleBot(config.BOT_TOKEN)
telebot.logger.setLevel(logging.DEBUG) # setup logger
me = config.OWNER # short way to contact the developer

api_dc = ValveServersDataCentersAPI()
timer_drop = TimerDrop()

JSON_FILE_PATH = "/root/tgbot/telegram-csgo-server-status-bot/cache.json"



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
dc_ru = types.KeyboardButton('Дата-центры')
markup_ru.add(status_ru, matchmaking_ru, devcount_ru, timer_ru, dc_ru)

# DC RU
markup_DC_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
Europe_ru = types.KeyboardButton('Европа')
Asia_ru = types.KeyboardButton('Азия')
Africa_ru = types.KeyboardButton('Южная Африка')
South_America_ru = types.KeyboardButton('Южная Америка')
Australia_ru = types.KeyboardButton('Австралия') 
USA_ru =  types.KeyboardButton('США')
Back_button_ru = types.KeyboardButton('⏪ Назад')
markup_DC_ru.add(Australia_ru, Asia_ru, Europe_ru, USA_ru, South_America_ru, Africa_ru, Back_button_ru)

# DC Europe Russian
markup_DC_EU_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
eu_West_ru = types.KeyboardButton('Запад')
eu_East_ru = types.KeyboardButton('Восток')
eu_North_ru = types.KeyboardButton('Север')
markup_DC_EU_ru.add(eu_East_ru, eu_West_ru, eu_North_ru)

# DC Asia Russian
markup_DC_Asia_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
india_ru = types.KeyboardButton('Индия')
emirates_ru = types.KeyboardButton('Эмираты')
china_ru = types.KeyboardButton('Китай')
singapore_ru = types.KeyboardButton('Сингапур')
hong_kong_ru = types.KeyboardButton('Гонконг')
japan_ru = types.KeyboardButton('Япония')
markup_DC_Asia_ru.add(hong_kong_ru, india_ru, china_ru, singapore_ru, emirates_ru, japan_ru)

# DC USA Russian
markup_DC_USA_ru = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
usa_Northwest_ru = types.KeyboardButton('Сeвер')
usa_Southwest_ru = types.KeyboardButton('Юг')
markup_DC_USA_ru.add(usa_Northwest_ru, usa_Southwest_ru)

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
    
    
def send_about_problem_bot(message):
    """If anything goes wrong"""
    if message.from_user.language_code == "ru":
        text = strings.wrongBOT_ru
    else:
        text = strings.wrongBOT_en
        
    bot.send_message(message.chat.id, text)




def get_status():
    """Get the status of CS:GO servers"""
    
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    gcCache = cacheFile['game_coordinator']
    slCache = cacheFile['sessionsLogon']
    pcCache = cacheFile['online_player_count']
    tsCache = cacheFile['time_server']
    p24Cache = cacheFile['peak_24_hours']
    paCache = cacheFile['peak_all_time']
    uqCache = cacheFile['unique_monthly']
    
    if gcCache == 'Normal':
        if slCache == 'normal':
            status_text_en = strings.statusNormal_en.format(slCache, pcCache, int(p24Cache), int(paCache), int(uqCache), tsCache)
            status_text_ru = strings.statusNormal_ru.format(pcCache, int(p24Cache), int(paCache), int(uqCache), tsCache)
        elif not slCache == 'normal':
            status_text_en = strings.statusNormal_en.format(slCache, pcCache, int(p24Cache), int(paCache), int(uqCache), tsCache)
            status_text_ru = strings.statusNormalSL_ru.format(pcCache, int(p24Cache), int(paCache), int(uqCache), tsCache)
    else:
            status_text_en = strings.statusWrong_en.format(tsCache)
            status_text_ru = strings.statusWrong_ru.format(tsCache)

    return status_text_en, status_text_ru


def get_matchmaking():
    """Get information about online servers, active players and more about matchmaking servers"""
    
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    tsCache = cacheFile['time_server']
    sCache = cacheFile['scheduler']
    scCache = cacheFile['online_server_count']
    apCache = cacheFile['active_player_count']
    ssCache = cacheFile['search_seconds_avg']
    spCache = cacheFile['searching_players']
    
    if sCache == 'normal':
        mm_text_en = strings.mmNormal_en.format(scCache, apCache, spCache, ssCache, tsCache)
        mm_text_ru = strings.mmNormal_ru.format(scCache, apCache, spCache, ssCache, tsCache)
    elif not sCache == 'normal':
        mm_text_en = strings.mmWrong_en.format(tsCache)
        mm_text_ru = strings.mmWrong_ru.format(tsCache)

    return mm_text_en, mm_text_ru


def get_devcount():
    """Get the count of online devs"""
    
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    tsCache = cacheFile['time_server']
    dcCache = cacheFile['dev_player_count']

    devcount_text_en = strings.devCount_en.format(dcCache, tsCache)
    devcount_text_ru = strings.devCount_ru.format(dcCache, tsCache)

    return devcount_text_en, devcount_text_ru


def get_timer():
    """Get the time left until exp and drop cap reset"""
    delta_days, delta_hours, delta_mins, delta_secs = timer_drop.get_delta()

    timer_text_en = strings.timer_en.format(delta_days, delta_hours, delta_mins, delta_secs)
    timer_text_ru = strings.timer_ru.format(delta_days, delta_hours, delta_mins, delta_secs)

    return timer_text_en, timer_text_ru
    
    
    

def send_status(message):
    """Send the status of CS:GO servers"""
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        try:
            status_text_en, status_text_ru = get_status()

            if message.from_user.language_code == 'ru':
                text = status_text_ru
                markup = markup_ru
            else:
                text = status_text_en
                markup = markup_en

            bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="html")

        except Exception as e:
            bot.send_message(me, f'❗️{e}')
            send_about_problem_bot(message)
    else:
        send_about_problem_valve_api(message)


def send_matchmaking(message):
    """Send information about online servers, active players and more about matchmaking servers"""
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        try:
            mm_text_en, mm_text_ru = get_matchmaking()

            if message.from_user.language_code == 'ru':
                text = mm_text_ru
                markup = markup_ru
            else:
                text = mm_text_en
                markup = markup_en

            bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="html")

        except Exception as e:
            bot.send_message(me, f'❗️{e}')
            send_about_problem_bot(message)
    else:
        send_about_problem_valve_api(message)        


def send_devcount(message):
    """Send the count of online devs"""
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        try:
            devcount_text_en, devcount_text_ru = get_devcount()

            if message.from_user.language_code == 'ru':
                    text = devcount_text_ru
                    markup = markup_ru
            else:    
                    text = devcount_text_en
                    markup = markup_en

            bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="html") 

        except Exception as e:
            bot.send_message(me, f'❗️{e}')
            send_about_problem_bot(message)
    else:
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
        send_about_problem_bot(message)
        

def dc(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        try:
            if message.from_user.language_code == 'ru':
                text = '📶 Выберите интересующий регион, чтобы получить информацию о дата-центрах:'
                markup = markup_DC_ru
            else:
                text = '📶 Select the region you are interested in, to get information about the data centers:'
                markup = markup_DC
            
            bot.send_message(message.chat.id, text, reply_markup=markup)

        except Exception as e:
            bot.send_message(me, f'❗️{e}')
            send_about_problem_bot(message)
    else:
        send_about_problem_valve_api(message)


def dc_africa(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server']    
    if wsCache == 'Normal':
        capacity, load = api_dc.africa_South()
        if message.from_user.language_code == 'ru':
            text = strings.dc_africa_ru.format(load, capacity, tsCache)
        else:
            text = strings.dc_africa_en.format(load, capacity, tsCache)
            
        bot.send_message(message.chat.id, text)
    else:
        send_about_problem_valve_api(message)
    

def dc_australia(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server']  
    if wsCache == 'Normal':
        capacity, load = api_dc.australia()
        if message.from_user.language_code == 'ru':
            text = strings.dc_australia_ru.format(load, capacity, tsCache)
        else:
            text = strings.dc_australia_en.format(load, capacity, tsCache)           
        bot.send_message(message.chat.id, text)
    else:
        send_about_problem_valve_api(message)
    

def dc_europe(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        if message.from_user.language_code == 'ru':
            text = '📍 Укажите регион...'
            markup = markup_DC_EU_ru            
        else:
            text = '📍 Specify the region...'
            markup = markup_DC_EU
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_eu_north(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity, load = api_dc.eu_North()
        if message.from_user.language_code == 'ru':
            text = strings.dc_north_eu_ru.format(load, capacity, tsCache)
            markup = markup_DC_ru 
        else:
            text = strings.dc_north_eu_en.format(load, capacity, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_eu_west(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity, load, capacity_Spain, load_Spain = api_dc.eu_West()
        if message.from_user.language_code == 'ru':
            text = strings.dc_west_eu_ru.format(load, capacity, load_Spain, capacity_Spain, tsCache)
            markup = markup_DC_ru 
        else:
            text = strings.dc_west_eu_en.format(load, capacity, load_Spain, capacity_Spain, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)
    

def dc_eu_east(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity_East, capacity_Poland, load_East, load_Poland = api_dc.eu_East()
        if message.from_user.language_code == 'ru':
            text = strings.dc_east_eu_ru.format(load_East, capacity_East, load_Poland, capacity_Poland, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_east_eu_en.format(load_East, capacity_East, load_Poland, capacity_Poland, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_asia(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        if message.from_user.language_code == 'ru':
            text = '📍 Укажите страну...'
            markup = markup_DC_Asia_ru
        else:
            text = '📍 Specify the country...'
            markup = markup_DC_Asia
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_usa(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
        if message.from_user.language_code == 'ru':
            text = '📍 Укажите регион...'
            markup = markup_DC_USA_ru
        else:
            text = '📍 Specify the region...'
            markup = markup_DC_USA
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_usa_north(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest = api_dc.usa_North()
        if message.from_user.language_code == 'ru':        
            text = strings.dc_north_us_ru.format(load_US_Northcentral, capacity_US_Northcentral, load_US_Northeast, capacity_US_Northeast, load_US_Northwest, capacity_US_Northwest, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_north_us_en.format(load_US_Northcentral, capacity_US_Northcentral, load_US_Northeast, capacity_US_Northeast, load_US_Northwest, capacity_US_Northwest, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_usa_south(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest = api_dc.usa_South()
        if message.from_user.language_code == 'ru':        
            text = strings.dc_south_us_ru.format(load_US_Southwest, capacity_US_Southwest, load_US_Southeast, capacity_US_Southeast, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_south_us_en.format(load_US_Southwest, capacity_US_Southwest, load_US_Southeast, capacity_US_Southeast, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_south_america(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil = api_dc.sa()
        if message.from_user.language_code == 'ru':  
            text = strings.dc_south_america_ru.format(load_Brazil, capacity_Brazil, load_Chile, capacity_Chile, load_Peru, capacity_Peru, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_south_america_en.format(load_Brazil, capacity_Brazil, load_Chile, capacity_Chile, load_Peru, capacity_Peru, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_india(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity, capacity_East, load, load_East = api_dc.india()
        if message.from_user.language_code == 'ru':  
            text = strings.dc_india_ru.format(load, capacity, load_East, capacity_East, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_india_en.format(load, capacity, load_East, capacity_East, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_japan(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity, load = api_dc.japan()
        if message.from_user.language_code == 'ru':
            text = strings.dc_japan_ru.format(load, capacity, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_japan_en.format(load, capacity, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_china(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou = api_dc.china()
        if message.from_user.language_code == 'ru':
            text = strings.dc_china_ru.format(load_Shanghai, capacity_Shanghai, load_Tianjin, capacity_Tianjin, load_Guangzhou, capacity_Guangzhou, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_china_en.format(load_Shanghai, capacity_Shanghai, load_Tianjin, capacity_Tianjin, load_Guangzhou, capacity_Guangzhou, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_emirates(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server'] 
    if wsCache == 'Normal':
        capacity, load = api_dc.emirates()
        if message.from_user.language_code == 'ru':
            text = strings.dc_emirates_ru.format(load, capacity, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_emirates_en.format(load, capacity, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_singapore(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server']
    if wsCache == 'Normal':
        capacity, load = api_dc.singapore()
        if message.from_user.language_code == 'ru':
            text = strings.dc_singapore_ru.format(load, capacity, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_singapore_en.format(load, capacity, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)


def dc_hong_kong(message):
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    tsCache = cacheFile['time_server']
    if wsCache == 'Normal':
        capacity, load = api_dc.hong_kong()
        if message.from_user.language_code == 'ru':
            text = strings.dc_hong_kong_ru.format(load, capacity, tsCache)
            markup = markup_DC_ru
        else:
            text = strings.dc_hong_kong_en.format(load, capacity, tsCache)
            markup = markup_DC
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        send_about_problem_valve_api(message)
 

def back(message):
    if message.from_user.language_code == 'ru':
        markup = markup_ru
    else: markup = markup_en

    bot.send_message(message.chat.id, '👌', reply_markup=markup)


@bot.inline_handler(lambda query: True)
def send_inline(inline_query):
    """Inline mode"""
    cacheFile = file_manager.readJson(JSON_FILE_PATH)
    wsCache = cacheFile['valve_webapi']
    if wsCache == 'Normal':
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

                r = types.InlineQueryResultArticle('1', title_status, input_message_content = types.InputTextMessageContent(status_r), thumb_url='https://telegra.ph/file/57ba2b279c53d69d72481.jpg', description=description_status)
                r2 = types.InlineQueryResultArticle('2', title_mm, input_message_content = types.InputTextMessageContent(mm_r), thumb_url='https://telegra.ph/file/8b640b85f6d62f8ed2900.jpg', description=description_mm)
                r3 = types.InlineQueryResultArticle('3', title_dev, input_message_content = types.InputTextMessageContent(dev_r), thumb_url='https://telegra.ph/file/24b05cea99de936fd12bf.jpg', description=description_dev)
                r4 = types.InlineQueryResultArticle('4', title_timer, input_message_content = types.InputTextMessageContent(timer_r), thumb_url='https://telegra.ph/file/6948255408689d2f6a472.jpg', description=description_timer)
                bot.answer_inline_query(inline_query.id, [r, r2, r3, r4], cache_time=15)

                log_inline(inline_query)

            except Exception as e:
                bot.send_message(config.OWNER, f'❗️Error: {e}\n\n↩️ inline_query')
                print(e)

        except Exception as e:
            bot.send_message(me, f'❗️{e}')
    else:
        try:
            timer_text_en, timer_text_ru = get_timer()

            try:
                if inline_query.from_user.language_code == 'ru':
                    wrong_r = strings.wrongAPI_ru
                    timer_r = timer_text_ru

                else:
                    wrong_r = strings.wrongAPI_en
                    timer_r = timer_text_en
                
                # text part
                if inline_query.from_user.language_code == 'ru': 
                    title_un = 'Нет данных'
                    title_timer = 'Сброс ограничений'

                    description_un = 'Не получилось связаться с API Valve'
                    description_timer = 'Время до сброса ограничений опыта и дропа'
                    
                else:
                    title_un = 'No data'
                    title_timer = 'Drop cap reset'

                    description_un = 'Unable to call Valve API'
                    description_timer = 'Time left until experience and drop cap reset'

                r = types.InlineQueryResultArticle('1', title_un, input_message_content = types.InputTextMessageContent(wrong_r), thumb_url='https://telegra.ph/file/b9d408e334795b014ee5c.jpg', description=description_un)
                r2 = types.InlineQueryResultArticle('2', title_timer, input_message_content = types.InputTextMessageContent(timer_r), thumb_url='https://telegra.ph/file/6948255408689d2f6a472.jpg', description=description_timer)

                bot.answer_inline_query(inline_query.id, [r, r2], cache_time=15)
                log_inline(inline_query)

            except Exception as e:
                bot.send_message(config.OWNER, f'❗️Error: {e}\n\n↩️ inline_query')
                print(e)
                
        except Exception as e:
            bot.send_message(me, f'❗️{e}')


@bot.message_handler(commands=['start'])
def welcome(message):
    """First bot's message"""
    log(message)
    if message.chat.type == "private":
        if message.from_user.language_code == 'ru':
            text = strings.cmdStart_ru.format(message.from_user.first_name)
            markup = markup_ru
        else:
            text = strings.cmdStart_en.format(message.from_user.first_name)
            markup = markup_en

        bot.send_message(message.chat.id, text, reply_markup=markup)

    else:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass


@bot.message_handler(commands=['feedback'])
def leave_feedback(message):
    """Send feedback"""
    log(message)
    if message.chat.type == "private":
        if message.from_user.language_code == 'ru':
            text = strings.cmdFeedback_ru 
        else:
            text = strings.cmdFeedback_en

        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup_del)
        bot.register_next_step_handler(message, get_feedback)
    else:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass

  
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
        
        if not config.TEST_MODE:
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
    if message.chat.type == "private":
        if message.from_user.language_code == 'ru':
            text = strings.cmdHelp_ru
            markup = markup_ru
        else:
            text = strings.cmdHelp_en
            markup = markup_en

        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup, disable_web_page_preview=True)
    else:
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass


@bot.message_handler(commands=['delkey'])
def delete_keyboard(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "👍", reply_markup=markup_del)
    time.sleep(10)
    bot.delete_message(message.chat.id, message.message_id+1)


@bot.message_handler(content_types=['text'])
def answer(message):
    """Answer of the bot"""
    log(message)
    try:
        if message.chat.type == "private":
            bot.send_chat_action(message.chat.id, 'typing')

            if message.text.lower() == 'status' or message.text.lower() == 'статус' or message.text.lower() == '/status':
                send_status(message)

            elif message.text.lower() == 'matchmaking' or message.text.lower() == 'матчмейкинг' or message.text.lower() == '/mm':
                send_matchmaking(message)
            
            elif message.text.lower() == 'online devs' or message.text.lower() == 'разработчиков в игре' or message.text.lower() == '/devcount':
                send_devcount(message)
    
            elif message.text.lower() == 'cap reset' or message.text.lower() == 'сброс ограничений' or message.text.lower() == '/timer':
                send_timer(message)

            elif message.text.lower() == 'data centers' or message.text.lower() == 'дата-центры' or message.text.lower() == '/dc':
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

            elif message.text.lower() == 'north' or message.text.lower() == 'сeвер' or message.text.lower() == '/usa_north':
                dc_usa_north(message)

            elif message.text.lower() == 'south' or message.text.lower() == 'юг' or message.text.lower() == '/usa_south':
                dc_usa_south(message)

            elif message.text.lower() == 'nоrth' or message.text.lower() == 'север' or message.text.lower() == '/eu_north':
                dc_eu_north(message)

            elif message.text.lower() == 'west' or message.text.lower() == 'запад' or message.text.lower() == '/eu_west':
                dc_eu_west(message)

            elif message.text.lower() == 'east' or message.text.lower() == 'восток' or message.text.lower() == '/eu_east':
                dc_eu_east(message)

            elif message.text.lower() == 'india' or message.text.lower() == 'индия' or message.text.lower() == '/india':
                dc_india(message)

            elif message.text.lower() == 'japan' or message.text.lower() == 'япония' or message.text.lower() == '/japan':
                dc_japan(message)

            elif message.text.lower() == 'china' or message.text.lower() == 'китай' or message.text.lower() == '/china':
                dc_china(message)

            elif message.text.lower() == 'emirates' or message.text.lower() == 'эмираты' or message.text.lower() == '/emirates':
                dc_emirates(message)

            elif message.text.lower() == 'singapore' or message.text.lower() == 'сингапур' or message.text.lower() == '/singapore':
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
