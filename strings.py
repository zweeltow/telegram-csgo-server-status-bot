"""Text of Commands"""
# English
cmdStart_en = "👋🏼 Hey, {}!\nThis bot is designed to check the number of online players and the availability of CS:GO servers.\n\nFor more information type /help."
cmdHelp_en = "ℹ️ This bot is designed by @csgobeta. Source code on <a href='https://github.com/zweeltow/telegram-csgo-server-status-bot'>GitHub</a>.\n\n<b>Here are the available commands:</b>\n/status – сheck the status of the servers\n/mm – show the amount of players currently playing\n/devcount - show the amount of devs in beta\n/timer - show the time left until cap reset\n/dc – see the status of a specific data center\n/feedback – leave feedback about the bot\n/help – get this message\n\nNote that this bot also works automatically, no need to add it anywhere. Simply open any of your chats and type ‘<code>@csgobetabot </code>‘ in the message field. Then tap on a result to send."
cmdFeedback_en = "💬 Please, tell us about your <b>suggestions</b> or <b>problems</b> that you have encountered using our bot.\n\nUse /cancel to cancel this command.\n\nIf you wish to contact the developer, please PM: @zweel <i>(But I'm bad at English 🙂)</i>."
# Russian
cmdStart_ru = "👋🏼 Привет, {}!\nЭтот бот предназначен для проверки количества онлайн игроков и доступности CS:GO серверов.\n\nДля большей информации воспользуйтесь /help."
cmdHelp_ru = "ℹ️ Этот бот разработан каналом @csgobeta. Исходный код на <a href='https://github.com/zweeltow/telegram-csgo-server-status-bot'>GitHub</a>.\n\n<b>Доступные команды:</b>\n/status – проверить доступность серверов\n/mm – показать количество онлайн игроков\n/devcount - показать количество разработчиков в бета-версии\n/timer - показать время до сброса ограничений\n/dc – посмотреть состояние определённого дата-центра (на английском языке)\n/feedback – оставить фидбэк про бота\n/help – получить это сообщение\n\nОбратите внимание, что этот бот также работает автоматически, нет необходимости добавлять его куда-либо. Просто откройте любой из Ваших чатов и введите ‘<code>@csgobetabot </code>ʼ в поле сообщения. Затем нажмите на результат для отправки."
cmdFeedback_ru = "💬 Пожалуйста, расскажите о Ваших <b>пожеланиях</b> или <b>проблемах</b>, с которыми Вы столкнулись, используя бота.\n\nИспользуйте /cancel, чтобы отменить команду.\n\nЕсли Вы желаете диалога с разработчиком, то возможно общение в личной переписке: @zweel."


"""Text of Status"""
# English
statusNormal_en = "✅ Server status is normal:\n\n• Connection: {};\n• Online players: {:,};\n• 24-hour peak: {:,};\n• All-time peak: {:,};\n• Monthly unique players: {:,}.\n\nLatest update: {} (UTC-8, summer UTC-7)."
statusWrong_en = "❌ Something went wrong with the servers.\n\nLatest update: {} (UTC-8, summer UTC-7)."
# Russian
statusNormal_ru = "✅ Сервера в нормальном состоянии:\n\n• Соединение: нормальное;\n• Онлайн игроков: {:,};\n• 24-часовой пик: {:,};\n• Рекордный пик: {:,};\n• Ежемесячные уникальные игроки: {:,}.\n\nОбновлено: {} (UTC−8, летом UTC−7)."
statusNormalSL_ru = "✅ Сервера в нормальном состоянии:\n\n• С соединением что-то не так.\n• Онлайн игроков: {:,};\n• 24-часовой пик: {:,};\n• Рекордный пик: {:,};\n• Ежемесячные уникальные игроки: {:,}.\n\nОбновлено: {} (UTC−8, летом UTC−7)."
statusWrong_ru = "❌ С серверами что-то не так.\n\nОбновлено: {} (UTC−8, летом UTC−7)."

"""Text of Dev count"""
# English
devCount_en = "🧑‍💻 Current online developers in the beta-version: {}.\n\nLatest update: {} (UTC-8, summer UTC-7)."
# Russian
devCount_ru = "🧑‍💻 Текущий онлайн разработчиков в бета-версии: {}.\n\nОбновлено: {} (UTC−8, летом UTC−7)."

"""Text of Timer"""
# English
timer_en = "⏳ Time left until experience and drop cap reset: {}d {}h {}m {}s."
# Russian
timer_ru = "⏳ Время до сброса ограничений опыта и дропа: {} д. {} ч. {} м. {} с."

"""Text of Matchmaking"""
# English
mmNormal_en = "✅ Matchmaking scheduler status is normal:\n\n• Online servers: {:,};\n• Active players: {:,};\n• Searching players: {:,};\n• Average search seconds: {:,}s.\n\nLatest update: {} (UTC-8, summer UTC-7)."
mmWrong_en = "❌ Something went wrong with the matchmaking scheduler.\n\nLatest update: {} (UTC-8, summer UTC-7)."
# Russian
mmNormal_ru = "✅ Планировщик матчмейкинга в нормальном состоянии:\n\n• Онлайн серверов: {:,};\n• Активных игроков: {:,};\n• Игроков в поиске: {:,};\n• Среднее время поиска: {:,} с.\n\nОбновлено: {} (UTC−8, летом UTC−7)."
mmWrong_ru = "❌ С планировщиком матчмейкинга что-то не так.\n\nLatest update: {} (UTC-8, summer UTC-7)."


"""Text of Wrong Request"""
# English
unknownRequest_en = "🤷‍♀️ Nothing found, please use one of the following commands:"
# Russian
unknownRequest_ru = "🤷‍♀️ Ничего не найдено, пожалуйста, воспользуйтесь одной из приведённых команд:"


"""Text of Wrong API"""
# English
wrongAPI_en = "💀 Issues with Valve's API, please try again later."
# Russian
wrongAPI_ru = "💀 Проблемы с API Valve, пожалуйста, попробуйте позже."


"""Text of something wrong"""
# English
wrongBOT_en = "🧐 Sorry, something’s not right. Please try again later."
# Russian
wrongBOT_ru = "🧐 Извините, что-то не так. Пожалуйста, попробуйте позже."

"""Text of new BuildID"""
#Russian
notiNewBuild_ru = "🆕 Обнаружено новое обновление Counter-Strike: Global Offensive. Пост со списком изменений выйдет в ближайшее время.\n\nID новой сборки: `{}`."


"""DC"""
