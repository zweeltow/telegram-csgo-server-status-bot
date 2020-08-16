# -*- coding: utf-8 -*-

import logging

import telebot
import config

from telebot import types
from valve_api import ValveServersAPI, ValveServersDataCentersAPI


TEST = False

if TEST == True: bot = telebot.TeleBot(config.TESTBOT) # token of the test bot
else: bot = telebot.TeleBot(config.CSGOBETABOT) # token of the bot
telebot.logger.setLevel(logging.DEBUG) # setup logger
me = config.OWNER # short way to diolog with me
api = ValveServersAPI()
api_dc = ValveServersDataCentersAPI()


"""Setup keyboard"""
# English
markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
Status = types.KeyboardButton('Status')
Matchmaking = types.KeyboardButton('Matchmaking')
DC = types.KeyboardButton('Data Centers')
markup.add(Status, Matchmaking, DC)

# DC
markup_DC = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
Europe = types.KeyboardButton('Europe')
Asia = types.KeyboardButton('Asia')
Africa = types.KeyboardButton('South Africa')
South_America = types.KeyboardButton('South America')
Australia = types.KeyboardButton('Australia')
USA =  types.KeyboardButton('USA')
Back_button = types.KeyboardButton('⏪ Back')
markup_DC.add( Asia, Australia, Europe, South_America, Africa, USA, Back_button)

# DC Asia
markup_DC_Asia = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
India = types.KeyboardButton('India')
Emirates = types.KeyboardButton('Emirates')
China = types.KeyboardButton('China')
Singapore = types.KeyboardButton('Singapore')
Hong_Kong = types.KeyboardButton('Hong Kong')
Japan = types.KeyboardButton('Japan')
markup_DC_Asia.add(India, Emirates, China, Singapore, Hong_Kong, Japan)

# DC Europe
markup_DC_EU = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
EU_West = types.KeyboardButton('EU West')
EU_East = types.KeyboardButton('EU East')
EU_North = types.KeyboardButton('EU North')
markup_DC_EU.add(EU_East, EU_North, EU_West)

# DC USA
markup_DC_USA = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
USA_Northwest = types.KeyboardButton('USA North')
USA_Southwest = types.KeyboardButton('USA South')
markup_DC_USA.add(USA_Northwest, USA_Southwest)

# DC USA

# DC Back
markup_DC_Back = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
Back_button = types.KeyboardButton('⏪ Back')
markup_DC_Back.add(Back_button)

# Russian
markup_ru = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
Status_ru = types.KeyboardButton('Статус')
Matchmaking_ru = types.KeyboardButton('Матчмейкинг')
DC_ru = types.KeyboardButton('Дата-центры')
markup_ru.add(Status_ru, Matchmaking_ru, DC_ru)

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
    """Bot send messages to depveloper about who used inline mode"""
    bot.send_message(config.OWNER, f'[<a href="tg://user?id={inline_query.from_user.id}">{inline_query.from_user.id}</a>] {inline_query.from_user.first_name} "{inline_query.from_user.username}" {inline_query.from_user.last_name} used <b>inline</b>', parse_mode='html', disable_notification=True)


def send_about_problem_valve_api(message):
    """Answer of bot if Valve's API don't answered"""
    
    if message.from_user.language_code == "ru":
        text = '💀 Проблемы с API Valve, бот не может получить информацию, пожалуйста, подождите несколько минут.'
    else:
        text = "💀 Issues with Valve's API, the bot can't get information, please, try again later."

    bot.send_message(message.chat.id, text)


def send_about_problem_valve_inline(inline_query):
    # if inline_query.from_user.language_code == "ru":
    #     bot.send_message(message.chat.id, '💀 Проблемы с API Valve, бот не может получить информацию, пожалуйста, подождите несколько минут.')
    # else:
    #     bot.send_message(message.chat.id, "💀 Issues with Valve's API, the bot can't get information, please, try again later.")
    try:
        r = types.InlineQueryResultArticle('1', "Issues with Valve's API, try again later", input_message_content = "💀 Issues with Valve's API, the bot can't get information, please, try again later.\n\n❤️ @csgobetabot", description="The bot can't get information")
        bot.answer_inline_query(inline_query.id, [r])

    except Exception as e:
        bot.send_message(config.OWNER, f'❗️Error: {e}\n\ninline_query')
        print(e)


def status(message):
    """Get information about status of CS:GO server"""
    try:
        SessionsLogon, player_count, time_server = api.status()
        bot.send_chat_action(message.chat.id, 'typing')
        if SessionsLogon == 'normal':
            if message.from_user.language_code == 'ru':
                text = f'✅ Сервера в нормальном состоянии:\n\n— Количество игроков: {player_count}.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                markup_local = markup_ru
            else:    
                text = f'✅ Server status is normal:\n\n— Player count: {player_count}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                markup_local = markup
        else:
            if message.from_user.language_code == 'ru':
                text = f'❌ Сервера в ненормальном состоянии.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                markup_local = markup_ru
            else:
                text = f'❌ Server status is not normal.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                markup_local = markup

        bot.send_message(message.chat.id, text, reply_markup=markup_local) 
    except Exception as e:
        bot.send_message(me, f'❗️{e}')
        send_about_problem_valve_api(message)


def matchmaking(message):
    """Get information about Online servers, Active players and more about matchmaking servers"""
    try:
        scheduler, online_servers, online_players, time_server, search_seconds_avg, searching_players = api.matchmaking()
        bot.send_chat_action(message.chat.id, 'typing')
        if scheduler == 'normal':
            if message.from_user.language_code == 'ru':
                text = f'✅ Планировщик матчмейкинга в нормальном состоянии:\n\n— Онлайн серверов: {online_servers};\n— Активных игроков: {online_players};\n— Игроков в поиске: {searching_players};\n— Среднее время поиска: {search_seconds_avg} сек.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                markup_local = markup_ru
            else:
                text = f'✅ Matchmaking scheduler status is normal:\n\n— Online servers: {online_servers};\n— Active players: {online_players};\n— Searching players: {searching_players};\n— Average search seconds: {search_seconds_avg} sec.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                markup_local = markup
        elif not scheduler == 'normal':
            if message.from_user.language_code == 'ru':
                text = f'❌ Планировщик матчмейкинга в ненормальном состоянии.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                markup_local = markup_ru
            else:
                text = f'❌ Matchmaking scheduler status is not normal.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                markup_local = markup
    
        bot.send_message(message.chat.id, text, reply_markup=markup_local)
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
    # if not capacity == 'full':
        # bot.send_message(me, f'🎉 Тут capacity не full, а {capacity}.')
    text = f'🌍 South Africa DCʼ status is OK:\n\n— Location: Johannesburg;\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text)


def dc_australia(message):
    capacity, load, time_server = api_dc.australia()
    # if not capacity == 'full':
        # bot.send_message(me, f'🎉 Тут capacity не full, а {capacity}.')
    text = f'🇦🇺 Australia DCʼ status is OK:\n\n— Location: Sydney;\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text)


def dc_europe(message):
    text = '📍 Specify the region...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_EU)


def dc_eu_north(message):
    capacity, load, time_server = api_dc.eu_North()
    text = f'🇪🇺 North Europe DCʼ status is OK:\n\n— Location: Stockholm;\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_eu_west(message):
    capacity, load, capacity_Spain, load_Spain, time_server = api_dc.eu_West()
    text = f'🇪🇺 West Europe DCʼ status is OK:\n\n— Location: Luxembourg;\n— Load: {load};\n— Capacity: {capacity}.\n\n🇪🇸 Spain DCʼ status is OK:\n\n— Location: Mardid;\n— Load: {load_Spain};\n— Capacity: {capacity_Spain}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_eu_east(message):
    capacity_East, capacity_Poland, load_East, load_Poland, time_server = api_dc.eu_East()
    text = f'🇪🇺 East Europe DCʼ status is OK:\n\n— Location: Vienna;\n— Load: {load_East};\n— Capacity: {capacity_East}.\n\n🇵🇱 Poland DCʼ status is OK:\n\n— Location: Warsaw;\n— Load: {load_Poland};\n— Capacity: {capacity_Poland}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_asia(message):
    text = '📍 Specify the country...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_Asia)


def dc_usa(message):
    text = '📍 Specify the region...'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC_USA)


def dc_usa_north(message):
    capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest, time_server = api_dc.usa_North()
    text = f'🇺🇸 Northcentral DCʼ status is OK:\n\n— Location: Chicago;\n— Load: {load_US_Northcentral};\n— Capacity: {capacity_US_Northcentral}.\n\n🇺🇸 Northeast DCʼ status is OK:\n\n— Location: Sterling;\n— Load: {load_US_Northeast};\n— Capacity: {capacity_US_Northeast}.\n\n 🇺🇸 Northwest DCʼ status is OK:\n\n— Location: Moses Lake;\n— Load: {load_US_Northwest};\n— Capacity: {capacity_US_Northwest}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_usa_south(message):
    capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest, time_server = api_dc.usa_South()
    text = f'🇺🇸 Southwest DCʼ status is OK:\n\n— Location: Los Angeles;\n— Load: {load_US_Southwest};\n— Capacity: {capacity_US_Southwest}.\n\n 🇺🇸 Southeast DCʼ status is OK:\n\n— Location: Atlanta;\n— Load: {load_US_Southeast};\n— Capacity: {capacity_US_Southeast}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_south_america(message):
    capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil, time_server = api_dc.sa()
    text = f'🇧🇷 Brazil DCʼ status is OK:\n\n— Location: Sao Paulo;\n— Load: {load_Brazil};\n— Capacity: {capacity_Brazil}.\n\n🇨🇱 Chile DCʼ status is OK:\n\n— Location: Santiago;\n— Load: {load_Chile};\n— Capacity: {capacity_Chile}.\n\n🇵🇪 Peru DCʼ status is OK:\n\n— Location: Lima;\n— Load: {load_Peru};\n— Capacity: {capacity_Peru}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_india(message):
    capacity, capacity_East, load, load_East, time_server = api_dc.india()
    text = f'🇮🇳 India DCʼ status is OK:\n\n— Location: Mumbai;\n— Load: {load};\n— Capacity: {capacity}.\n\n🇮🇳 East India DCʼ status is OK:\n\n— Location: Chennai;\n— Load: {load_East};\n— Capacity: {capacity_East}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_japan(message):
    capacity, load, time_server = api_dc.japan()
    text = f'🇯🇵 Japan DCʼ status is OK:\n\n— Location: Tokyo;\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_china(message):
    capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou, time_server = api_dc.china()
    text = f'🇨🇳 China DCʼ status is OK: \n\n— Location: Shanghai;\n— Load: {load_Shanghai};\n— Capacity: {capacity_Shanghai}.\n\n— Location: Tianjin;\n— Load: {load_Tianjin};\n— Capacity: {capacity_Tianjin}.\n\n— Location: Guangzhou;\n— Load: {load_Guangzhou};\n— Capacity: {capacity_Guangzhou}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_emirates(message):
    capacity, load, time_server = api_dc.emirates()
    text = f'🇦🇪 Emirates DCʼ status is OK:\n\n— Location: Dubai;\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_singapore(message):
    capacity, load, time_server = api_dc.singapore()
    text = f'🇸🇬 Singapore DCʼ status is OK:\n\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)


def dc_hong_kong(message):
    capacity, load, time_server = api_dc.hong_kong()
    text = f'🇭🇰 Hong Kong DCʼ status is OK:\n\n— Load: {load};\n— Capacity: {capacity}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
    bot.send_message(message.chat.id, text, reply_markup=markup_DC)
 

def back(message):
    if message.from_user.language_code == 'ru':
        markup_local = markup_ru
    else: markup_local = markup

    bot.send_message(message.chat.id, '👌', reply_markup=markup_local)


@bot.inline_handler(lambda query: True)
def status_inline(inline_query):
    """Inline mode"""
    try:        
        SessionsLogon, player_count, time_server = api.status()
        scheduler, online_servers, online_players, time_server, search_seconds_avg, searching_players = api.matchmaking()
        try:
            if SessionsLogon == 'normal':
                if inline_query.from_user.language_code == 'ru':
                    status_r = f'✅ Сервера в нормальном состоянии:\n\n— Количество игроков: {player_count}.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                else:    
                    status_r = f'✅ Server status is normal:\n\n— Player count: {player_count}.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
            else:
                if inline_query.from_user.language_code == 'ru':
                    status_r = f'❌ Сервера в ненормальном состоянии.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                else:    
                    status_r = f'❌ Server status is not normal.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'

            if scheduler == 'normal':
                if inline_query.from_user.language_code == 'ru':
                    mm_r = f'✅ Планировщик матчмейкинга в нормальном состоянии:\n\n— Онлайн серверов: {online_servers};\n— Активных игроков: {online_players};\n— Игроков в поиске: {searching_players};\n— Среднее время поиска: {search_seconds_avg} сек.\n\nОбновлено {time_server} (UTC−8, летом UTC−7).'
                else:
                    mm_r = f'✅ Matchmaking scheduler status is normal:\n\n— Online servers: {online_servers};\n— Active players: {online_players};\n— Searching players: {searching_players};\n— Average search seconds: {search_seconds_avg} sec.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'

            elif not scheduler == 'normal':
                if inline_query.from_user.language_code == 'ru':
                    mm_r = f'❌ Планировщик матчмейкинга в ненормальном состоянии.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
                else:
                    mm_r = f'❌ Matchmaking scheduler status is not normal.\n\nLatest update on {time_server} (UTC−8, summer UTC−7).'
            if inline_query.from_user.language_code == 'ru': 
                titleStatus = 'Статус'
                titleMM = 'Матчмейкинг'

                descriptionStatus = 'Проверить доступность серверов'
                descriptionMM = 'Показать количество играющих'
            else:
                titleStatus = 'Status'
                titleMM = 'Matchmaking'

                descriptionStatus = 'Check the availability of the servers'
                descriptionMM = 'Show the count of players currently playing'

            r = types.InlineQueryResultArticle('1', titleStatus, input_message_content = types.InputTextMessageContent(status_r), description=descriptionStatus)
            r2 = types.InlineQueryResultArticle('2', titleMM, input_message_content = types.InputTextMessageContent(mm_r), description=descriptionMM)
            bot.answer_inline_query(inline_query.id, [r, r2], cache_time=10)
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
        text = f'👋🏼 Привет, {message.from_user.first_name}!\nЭтот бот предназначен для проверки количества онлайн игроков и доступности CS:GO серверов.\n\nДля большей информации воспользуйтесь /help.'
        markup_local = markup_ru
    else:
        text = f'👋🏼 Hey, {message.from_user.first_name}!\nThis bot is designed to check the number of online players and the availability of CS:GO servers.\n\nFor more information type /help.'
        markup_local = markup

    bot.send_message(message.chat.id, text, reply_markup=markup_local)


@bot.message_handler(commands=['feedback'])
def leave_feedback(message):
    """Send feedback"""
    log(message)

    if message.from_user.language_code == 'ru':
        text = '💬 Пожалуйста, расскажите о Ваших <b>пожеланиях</b> или <b>проблемах</b>, с которыми Вы столкнулись, используя бота.\n\nИспользуйте /cancel, чтобы отменить команду.\n\nЕсли Вы желаете диалога с разработчиком, то возможно общение в личной переписке: @zweel.'
    else:
        text = "💬 Please tell us about your <b>suggestions</b> or <b>problems</b> that you have encountered using our bot.\n\nUse /cancel to cancel this command.\n\nIf you need a dialogue with the developer, you can PM: @zweel <i>(But I'm bad at English 🙂)</i>."
    
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup_del)
    bot.register_next_step_handler(message, get_feedback)


def get_feedback(message):
    """Get feedback from user of bot"""
    if message.text == '/cancel':
        log(message)
        if message.from_user.language_code == 'ru':
            markup_local = markup_ru
        else:
            markup_local = markup
        bot.send_message(message.chat.id, '👍', reply_markup=markup_local)

    else:
        bot.send_message(config.OWNER, f'🆔 <a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>:', parse_mode='html', disable_notification=True)
        bot.forward_message(config.OWNER, message.chat.id, message.message_id)
        
        if TEST == False:
            bot.forward_message(config.AQ, message.chat.id, message.message_id)

        if message.from_user.language_code == 'ru':
            text = 'Отлично! Ваше сообщение отправлено.'
            markup_local = markup_ru
        else:
            text = 'Awesome! Your message has been sent.'
            markup_local = markup

        bot.send_message(message.chat.id, text, reply_to_message_id=message.message_id,reply_markup=markup_local)


@bot.message_handler(commands=['help'])
def help(message):
    """/help message"""
    log(message)
    if message.from_user.language_code == 'ru':
        text = 'ℹ️ Этот бот разработан каналом @csgobeta и предназначен для проверки количества онлайн игроков и доступности CS:GO серверов.\n\n<b>Доступные команды:</b>\n/status – проверить доступность серверов\n/mm – показать количество онлайн игроков\n/dc – посмотреть состояние дата-центра (на английском языке)\n/feedback – оставить фидбэк про бота\n/help – получить это сообщение\n\nОбратите внимание, что этот бот также работает автоматически, нет необходимости добавлять его куда-либо. Просто откройте любой из Ваших чатов и введите ‘<code>@csgobetabot </code>ʼ в поле сообщения. Затем нажмите на результат для отправки.'
        markup_local = markup_ru
    else:
        text = 'ℹ️ This bot is designed by @csgobeta to check the number of online players and the availability of CS:GO servers.\n\n<b>Here are the available commands:</b>\n/status – сheck the availability of the servers\n/mm – show the count of players currently playing\n/dc – see the status of a specific data center\n/feedback – leave feedback about the bot\n/help – get this message\n\nNote that this bot also works automatically, no need to add it anywhere. Simply open any of your chats and type ‘<code>@csgobetabot </code>‘ in the message field. Then tap on a result to send.'
        markup_local = markup

    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup_local)


@bot.message_handler(content_types=['text'])
def answer(message):
    """Answer of the bot"""
    log(message)
    try:
        if message.text.lower() == 'status' or message.text.lower() == 'статус' or message.text.lower() == '/status':
            status(message)


        elif message.text.lower() == 'matchmaking' or message.text.lower() == 'матчмейкинг' or message.text.lower() == '/mm':
            matchmaking(message)


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


        elif message.text.lower() == 'usa north' or message.text.lower() == 'северные сша' or message.text.lower() == '/usa_north':
            dc_usa_north(message)

        elif message.text.lower() == 'usa south' or message.text.lower() == 'южные сша' or message.text.lower() == '/usa_south':
            dc_usa_south(message)


        elif message.text.lower() == 'eu north' or message.text.lower() == 'северная европа' or message.text.lower() == '/eu_north':
            dc_eu_north(message)


        elif message.text.lower() == 'eu west' or message.text.lower() == 'западная европа' or message.text.lower() == '/eu_west':
            dc_eu_west(message)

        elif message.text.lower() == 'eu east' or message.text.lower() == 'восточная европа' or message.text.lower() == '/eu_east':
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
                text = '🤷‍♀️ Ничего не найдено, пожалуйста, воспользуйтесь одной из приведённых команд:'
                markup_local = markup_ru
            else: 
                text = '🤷‍♀️ Nothing found, please use one of the following commands:'
                markup_local = markup

            bot.send_message(message.chat.id, text, reply_markup=markup_local)
    
    except Exception as e:
        bot.send_message(me, f'❗️{e}')

# Polling
bot.polling()