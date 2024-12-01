from aiogram import *
from aiogram.filters.command import *
from aiogram.types import *
import asyncio
import DataBase
import logger

API_token = '7807029832:AAGyFBwhHP_ZDfJc4xtYzyqxuoE3LIsh-UA'

bot = Bot(token=API_token)
dp = Dispatcher()

log = logger.setup_logger('bot_logger', 'bot.log')


@dp.message(F.text.lower() == 'в начало')
@dp.message(F.text.lower() == 'меню')
@dp.message(Command('start'))
async def startm(message: types.Message):
    log.info('User started the bot')

    dalee = InlineKeyboardButton(text='Далее', callback_data='dalee')
    row = [dalee]
    rows = [row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)

    await message.reply(
        'Привет! Этот бот поможет вам найти нормативные акты в сфере ИБ. Если тебе нужно начать с начала, напиши мне "меню" или "в начало".',
        reply_markup=markup)


@dp.callback_query(F.data == 'dalee')
async def dalee(call: CallbackQuery):
    log.info('User proceeded to the next step')

    energy = InlineKeyboardButton(text='Энергетика⚡', callback_data='energy')
    neft = InlineKeyboardButton(text='Нефтянная и газовая промышленность⛽', callback_data='neft')
    dobich = InlineKeyboardButton(text='Добыча ископаемых⛏️', callback_data='dobich')
    stoit = InlineKeyboardButton(text='Строительство🏗️', callback_data='stoit')
    traid = InlineKeyboardButton(text='Торговля и Ритейл🛒', callback_data='traid')
    gruz = InlineKeyboardButton(text='Грузоперевозки🚛', callback_data='gruz')
    trans = InlineKeyboardButton(text='Транспорт🚌', callback_data='trans')
    banks = InlineKeyboardButton(text='Банки и финансы💰', callback_data='banks')
    med = InlineKeyboardButton(text='Медицина и фармацевтика⚕️', callback_data='med')
    since = InlineKeyboardButton(text='Наука🔬', callback_data='since')
    gos = InlineKeyboardButton(text='Государственный сектор🏛️', callback_data='gos')
    telev = InlineKeyboardButton(text='Телекоммуникации и Медиа📡', callback_data='telev')

    row1 = [energy, neft]
    row2 = [dobich, stoit]
    row3 = [traid, gruz]
    row4 = [trans, banks]
    row5 = [med, gos]
    row6 = [telev, since]
    rows = [row1, row2, row3, row4, row5, row6]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)

    await call.message.reply('Выберите сферу деятельности:', reply_markup=markup)


@dp.callback_query(F.data == 'energy')
async def energy(call: CallbackQuery):
    log.info('User selected "Энергетика⚡"')

    energy_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='energy_ssib')
    energy_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='energy_pka')
    energy_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='energy_isg')
    enegry_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='energy_gos')
    energy_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[energy_ssib], [energy_pka], [energy_isg], [enegry_gos], [energy_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Энергетика⚡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" энергктика')

    energy_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='energy_ssib_gis')
    energy_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='energy_ssib_ispdn')
    energy_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='energy_ssib_kii')
    energy_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='energy_ssib_autist')
    energy_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='energy')

    rows = [[energy_ssib_gis], [energy_ssib_ispdn], [energy_ssib_kii], [energy_ssib_autist], [energy_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" ENERGY')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='energy_ssib_gis')
    energy_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='energy_ssib_ispdn')
    energy_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='energy_ssib_kii')
    energy_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='energy_ssib_autist')
    energy_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='energy')

    rows = [[energy_ssib_gis], [energy_ssib_ispdn], [energy_ssib_kii], [energy_ssib_autist], [energy_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" ENERGY')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='energy_ssib_gis')
    energy_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='energy_ssib_ispdn')
    energy_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='energy_ssib_kii')
    energy_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='energy_ssib_autist')
    energy_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='energy')

    rows = [[energy_ssib_gis], [energy_ssib_ispdn], [energy_ssib_kii], [energy_ssib_autist], [energy_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" ENERGY')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='energy_ssib_gis')
    energy_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='energy_ssib_ispdn')
    energy_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='energy_ssib_kii')
    energy_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='energy_ssib_autist')
    energy_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='energy')

    rows = [[energy_ssib_gis], [energy_ssib_ispdn], [energy_ssib_kii], [energy_ssib_autist], [energy_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" ENERGY')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='energy_ssib_gis')
    energy_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='energy_ssib_ispdn')
    energy_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='energy_ssib_kii')
    energy_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='energy_ssib_autist')
    energy_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='energy')

    rows = [[energy_ssib_gis], [energy_ssib_ispdn], [energy_ssib_kii], [energy_ssib_autist], [energy_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'energy_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" энергетика')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='energy_ssib')
    energy_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='energy_pka')
    energy_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='energy_isg')
    enegry_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='energy_gos')
    energy_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[energy_ssib], [energy_pka], [energy_isg], [enegry_gos], [energy_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Энергетика⚡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'energy_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" энергетика')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='energy_ssib')
    energy_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='energy_pka')
    energy_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='energy_isg')
    enegry_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='energy_gos')
    energy_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[energy_ssib], [energy_pka], [energy_isg], [enegry_gos], [energy_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Энергетика⚡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'energy_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" energy')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['1', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    energy_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='energy_ssib')
    energy_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='energy_pka')
    energy_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='energy_isg')
    enegry_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='energy_gos')
    energy_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[energy_ssib], [energy_pka], [energy_isg], [energy_nazad], [enegry_gos]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Энергетика⚡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'neft')
async def energy(call: CallbackQuery):
    log.info('User selected "Нефтянная и газовая промышленность⛽"')

    neft_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='neft_ssib')
    neft_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='neft_pka')
    neft_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='neft_isg')
    neft_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='neft_gos')
    neft_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[neft_ssib], [neft_pka], [neft_isg], [neft_gos], [neft_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Нефтянная и газовая промышленность⛽. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'neft_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" энергктика')

    neft_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='neft_ssib_gis')
    neft_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='neft_ssib_ispdn')
    neft_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='neft_ssib_kii')
    neft_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='neft_ssib_autist')
    neft_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='neft')

    rows = [[neft_ssib_gis], [neft_ssib_ispdn], [neft_ssib_kii], [neft_ssib_autist], [neft_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'neft_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='neft_ssib_gis')
    neft_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='neft_ssib_ispdn')
    neft_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='neft_ssib_kii')
    neft_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='neft_ssib_autist')
    neft_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='neft')

    rows = [[neft_ssib_gis], [neft_ssib_ispdn], [neft_ssib_kii], [neft_ssib_autist], [neft_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'neft_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='neft_ssib_gis')
    neft_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='neft_ssib_ispdn')
    neft_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='neft_ssib_kii')
    neft_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='neft_ssib_autist')
    neft_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='neft')

    rows = [[neft_ssib_gis], [neft_ssib_ispdn], [neft_ssib_kii], [neft_ssib_autist], [neft_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'neft_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='neft_ssib_gis')
    neft_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='neft_ssib_ispdn')
    neft_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='neft_ssib_kii')
    neft_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='neft_ssib_autist')
    neft_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='neft')

    rows = [[neft_ssib_gis], [neft_ssib_ispdn], [neft_ssib_kii], [neft_ssib_autist], [neft_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'neft_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='neft_ssib_gis')
    neft_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='neft_ssib_ispdn')
    neft_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='neft_ssib_kii')
    neft_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='neft_ssib_autist')
    neft_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='neft')

    rows = [[neft_ssib_gis], [neft_ssib_ispdn], [neft_ssib_kii], [neft_ssib_autist], [neft_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'neft_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='neft_ssib')
    neft_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='neft_pka')
    neft_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='neft_isg')
    neft_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='neft_gos')
    neft_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[neft_ssib], [neft_pka], [neft_isg], [neft_gos], [neft_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Нефтянная и газовая промышленность⛽. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'neft_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='neft_ssib')
    neft_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='neft_pka')
    neft_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='neft_isg')
    neft_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='neft_gos')
    neft_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[neft_ssib], [neft_pka], [neft_isg], [neft_gos], [neft_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Нефтянная и газовая промышленность⛽. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'neft_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" neft')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['2', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    neft_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='neft_ssib')
    neft_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='neft_pka')
    neft_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='neft_isg')
    neft_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='neft_gos')
    neft_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[neft_ssib], [neft_pka], [neft_isg], [neft_gos], [neft_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Нефтянная и газовая промышленность⛽. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'dobich')
async def energy(call: CallbackQuery):
    log.info('User selected "Добыча ископаемых⛏️"')

    dobich_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='dobich_ssib')
    dobich_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='dobich_pka')
    dobich_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='dobich_isg')
    dobich_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='dobich_gos')
    dobich_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[dobich_ssib], [dobich_pka], [dobich_isg], [dobich_gos], [dobich_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Добыча ископаемых⛏️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" dobich')

    dobich_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='dobich_ssib_gis')
    dobich_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='dobich_ssib_ispdn')
    dobich_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='dobich_ssib_kii')
    dobich_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='dobich_ssib_autist')
    dobich_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dobich')

    rows = [[dobich_ssib_gis], [dobich_ssib_ispdn], [dobich_ssib_kii], [dobich_ssib_autist], [dobich_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='dobich_ssib_gis')
    dobich_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='dobich_ssib_ispdn')
    dobich_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='dobich_ssib_kii')
    dobich_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='dobich_ssib_autist')
    dobich_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dobich')

    rows = [[dobich_ssib_gis], [dobich_ssib_ispdn], [dobich_ssib_kii], [dobich_ssib_autist], [dobich_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='dobich_ssib_gis')
    dobich_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='dobich_ssib_ispdn')
    dobich_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='dobich_ssib_kii')
    dobich_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='dobich_ssib_autist')
    dobich_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dobich')

    rows = [[dobich_ssib_gis], [dobich_ssib_ispdn], [dobich_ssib_kii], [dobich_ssib_autist], [dobich_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='dobich_ssib_gis')
    dobich_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='dobich_ssib_ispdn')
    dobich_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='dobich_ssib_kii')
    dobich_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='dobich_ssib_autist')
    dobich_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dobich')

    rows = [[dobich_ssib_gis], [dobich_ssib_ispdn], [dobich_ssib_kii], [dobich_ssib_autist], [dobich_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='dobich_ssib_gis')
    dobich_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='dobich_ssib_ispdn')
    dobich_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='dobich_ssib_kii')
    dobich_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='dobich_ssib_autist')
    dobich_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dobich')

    rows = [[dobich_ssib_gis], [dobich_ssib_ispdn], [dobich_ssib_kii], [dobich_ssib_autist], [dobich_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='dobich_ssib')
    dobich_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='dobich_pka')
    dobich_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='dobich_isg')
    dobich_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='dobich_gos')
    dobich_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[dobich_ssib], [dobich_pka], [dobich_isg], [dobich_gos], [dobich_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Добыча ископаемых⛏️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='dobich_ssib')
    dobich_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='dobich_pka')
    dobich_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='dobich_isg')
    dobich_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='dobich_gos')
    dobich_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[dobich_ssib], [dobich_pka], [dobich_isg], [dobich_gos], [dobich_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Добыча ископаемых⛏️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'dobich_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" dobich')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['3', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    dobich_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒',
                                       callback_data='dobich_ssib')
    dobich_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='dobich_pka')
    dobich_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='dobich_isg')
    dobich_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='dobich_gos')
    dobich_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[dobich_ssib], [dobich_pka], [dobich_isg], [dobich_gos], [dobich_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Добыча ископаемых⛏️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'stoit')
async def energy(call: CallbackQuery):
    log.info('User selected "Строительство🏗️"')

    stoit_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='stoit_ssib')
    stoit_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='stoit_pka')
    stoit_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='stoit_isg')
    stoit_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='stoit_gos')
    stoit_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[stoit_ssib], [stoit_pka], [stoit_isg], [stoit_gos], [stoit_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Строительство🏗️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" stoit')

    stoit_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='stoit_ssib_gis')
    stoit_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='stoit_ssib_ispdn')
    stoit_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='stoit_ssib_kii')
    stoit_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='stoit_ssib_autist')
    stoit_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='stoit')

    rows = [[stoit_ssib_gis], [stoit_ssib_ispdn], [stoit_ssib_kii], [stoit_ssib_autist], [stoit_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='stoit_ssib_gis')
    stoit_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='stoit_ssib_ispdn')
    stoit_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='stoit_ssib_kii')
    stoit_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='stoit_ssib_autist')
    stoit_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='stoit')

    rows = [[stoit_ssib_gis], [stoit_ssib_ispdn], [stoit_ssib_kii], [stoit_ssib_autist], [stoit_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='stoit_ssib_gis')
    stoit_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='stoit_ssib_ispdn')
    stoit_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='stoit_ssib_kii')
    stoit_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='stoit_ssib_autist')
    stoit_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='stoit')

    rows = [[stoit_ssib_gis], [stoit_ssib_ispdn], [stoit_ssib_kii], [stoit_ssib_autist], [stoit_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='stoit_ssib_gis')
    stoit_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='stoit_ssib_ispdn')
    stoit_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='stoit_ssib_kii')
    stoit_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='stoit_ssib_autist')
    stoit_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='stoit')

    rows = [[stoit_ssib_gis], [stoit_ssib_ispdn], [stoit_ssib_kii], [stoit_ssib_autist], [stoit_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='stoit_ssib_gis')
    stoit_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='stoit_ssib_ispdn')
    stoit_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='stoit_ssib_kii')
    stoit_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='stoit_ssib_autist')
    stoit_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='stoit')

    rows = [[stoit_ssib_gis], [stoit_ssib_ispdn], [stoit_ssib_kii], [stoit_ssib_autist], [stoit_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='stoit_ssib')
    stoit_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='stoit_pka')
    stoit_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='stoit_isg')
    stoit_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='stoit_gos')
    stoit_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[stoit_ssib], [stoit_pka], [stoit_isg], [stoit_gos], [stoit_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Строительство🏗️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='stoit_ssib')
    stoit_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='stoit_pka')
    stoit_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='stoit_isg')
    stoit_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='stoit_gos')
    stoit_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[stoit_ssib], [stoit_pka], [stoit_isg], [stoit_gos], [stoit_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Строительство🏗️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'stoit_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" stoit')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['4', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    stoit_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='stoit_ssib')
    stoit_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='stoit_pka')
    stoit_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='stoit_isg')
    stoit_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='stoit_gos')
    stoit_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[stoit_ssib], [stoit_pka], [stoit_isg], [stoit_gos], [stoit_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Строительство🏗️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'traid')
async def energy(call: CallbackQuery):
    log.info('User selected "Торговля и Ритейл🛒"')

    traid_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='traid_ssib')
    traid_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='traid_pka')
    traid_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='traid_isg')
    traid_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='traid_gos')
    traid_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[traid_ssib], [traid_pka], [traid_isg], [traid_gos], [traid_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Торговля и Ритейл🛒. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'traid_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" dobich')

    traid_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='traid_ssib_gis')
    traid_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='traid_ssib_ispdn')
    traid_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='traid_ssib_kii')
    traid_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='traid_ssib_autist')
    traid_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='traid')

    rows = [[traid_ssib_gis], [traid_ssib_ispdn], [traid_ssib_kii], [traid_ssib_autist], [traid_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'traid_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='traid_ssib_gis')
    traid_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='traid_ssib_ispdn')
    traid_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='traid_ssib_kii')
    traid_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='traid_ssib_autist')
    traid_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='traid')

    rows = [[traid_ssib_gis], [traid_ssib_ispdn], [traid_ssib_kii], [traid_ssib_autist], [traid_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'traid_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='traid_ssib_gis')
    traid_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='traid_ssib_ispdn')
    traid_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='traid_ssib_kii')
    traid_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='traid_ssib_autist')
    traid_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='traid')

    rows = [[traid_ssib_gis], [traid_ssib_ispdn], [traid_ssib_kii], [traid_ssib_autist], [traid_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'traid_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='traid_ssib_gis')
    traid_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='traid_ssib_ispdn')
    traid_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='traid_ssib_kii')
    traid_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='traid_ssib_autist')
    traid_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='traid')

    rows = [[traid_ssib_gis], [traid_ssib_ispdn], [traid_ssib_kii], [traid_ssib_autist], [traid_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'traid_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='traid_ssib_gis')
    traid_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='traid_ssib_ispdn')
    traid_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='traid_ssib_kii')
    traid_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='traid_ssib_autist')
    traid_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='traid')

    rows = [[traid_ssib_gis], [traid_ssib_ispdn], [traid_ssib_kii], [traid_ssib_autist], [traid_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'traid_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='traid_ssib')
    traid_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='traid_pka')
    traid_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='traid_isg')
    traid_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='traid_gos')
    traid_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[traid_ssib], [traid_pka], [traid_isg], [traid_gos], [traid_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Торговля и Ритейл🛒. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'traid_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='traid_ssib')
    traid_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='traid_pka')
    traid_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='traid_isg')
    traid_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='traid_gos')
    traid_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[traid_ssib], [traid_pka], [traid_isg], [traid_gos], [traid_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Торговля и Ритейл🛒. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'traid_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" traid')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['5', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    traid_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='traid_ssib')
    traid_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='traid_pka')
    traid_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='traid_isg')
    traid_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='traid_gos')
    traid_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[traid_ssib], [traid_pka], [traid_isg], [traid_gos], [traid_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Торговля и Ритейл🛒. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gruz')
async def energy(call: CallbackQuery):
    log.info('User selected "Грузоперевозки🚛"')

    gruz_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gruz_ssib')
    gruz_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gruz_pka')
    gruz_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gruz_isg')
    gruz_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gruz_gos')
    gruz_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gruz_ssib], [gruz_pka], [gruz_isg], [gruz_gos], [gruz_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Грузоперевозки🚛. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" gruz')

    gruz_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gruz_ssib_gis')
    gruz_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gruz_ssib_ispdn')
    gruz_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gruz_ssib_kii')
    gruz_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gruz_ssib_autist')
    gruz_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gruz')

    rows = [[gruz_ssib_gis], [gruz_ssib_ispdn], [gruz_ssib_kii], [gruz_ssib_autist], [gruz_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gruz_ssib_gis')
    gruz_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gruz_ssib_ispdn')
    gruz_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gruz_ssib_kii')
    gruz_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gruz_ssib_autist')
    gruz_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gruz')

    rows = [[gruz_ssib_gis], [gruz_ssib_ispdn], [gruz_ssib_kii], [gruz_ssib_autist], [gruz_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gruz_ssib_gis')
    gruz_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gruz_ssib_ispdn')
    gruz_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gruz_ssib_kii')
    gruz_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gruz_ssib_autist')
    gruz_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gruz')

    rows = [[gruz_ssib_gis], [gruz_ssib_ispdn], [gruz_ssib_kii], [gruz_ssib_autist], [gruz_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gruz_ssib_gis')
    gruz_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gruz_ssib_ispdn')
    gruz_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gruz_ssib_kii')
    gruz_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gruz_ssib_autist')
    gruz_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gruz')

    rows = [[gruz_ssib_gis], [gruz_ssib_ispdn], [gruz_ssib_kii], [gruz_ssib_autist], [gruz_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gruz_ssib_gis')
    gruz_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gruz_ssib_ispdn')
    gruz_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gruz_ssib_kii')
    gruz_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gruz_ssib_autist')
    gruz_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gruz')

    rows = [[gruz_ssib_gis], [gruz_ssib_ispdn], [gruz_ssib_kii], [gruz_ssib_autist], [gruz_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gruz_ssib')
    gruz_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gruz_pka')
    gruz_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gruz_isg')
    gruz_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gruz_gos')
    gruz_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gruz_ssib], [gruz_pka], [gruz_isg], [gruz_gos], [gruz_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Грузоперевозки🚛. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gruz_ssib')
    gruz_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gruz_pka')
    gruz_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gruz_isg')
    gruz_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gruz_gos')
    gruz_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gruz_ssib], [gruz_pka], [gruz_isg], [gruz_gos], [gruz_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Грузоперевозки🚛. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gruz_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" gruz')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['6', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gruz_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gruz_ssib')
    gruz_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gruz_pka')
    gruz_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gruz_isg')
    gruz_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gruz_gos')
    gruz_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gruz_ssib], [gruz_pka], [gruz_isg], [gruz_gos], [gruz_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Грузоперевозки🚛. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'trans')
async def energy(call: CallbackQuery):
    log.info('User selected "Транспорт🚌"')

    trans_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='trans_ssib')
    trans_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='trans_pka')
    trans_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='trans_isg')
    trans_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='trans_gos')
    trans_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[trans_ssib], [trans_pka], [trans_isg], [trans_gos], [trans_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Транспорт🚌. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'trans_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" trans')

    trans_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='trans_ssib_gis')
    trans_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='trans_ssib_ispdn')
    trans_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='trans_ssib_kii')
    trans_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='trans_ssib_autist')
    trans_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='trans')

    rows = [[trans_ssib_gis], [trans_ssib_ispdn], [trans_ssib_kii], [trans_ssib_autist], [trans_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'trans_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='trans_ssib_gis')
    trans_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='trans_ssib_ispdn')
    trans_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='trans_ssib_kii')
    trans_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='trans_ssib_autist')
    trans_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='trans')

    rows = [[trans_ssib_gis], [trans_ssib_ispdn], [trans_ssib_kii], [trans_ssib_autist], [trans_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'trans_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='trans_ssib_gis')
    trans_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='trans_ssib_ispdn')
    trans_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='trans_ssib_kii')
    trans_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='trans_ssib_autist')
    trans_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='trans')

    rows = [[trans_ssib_gis], [trans_ssib_ispdn], [trans_ssib_kii], [trans_ssib_autist], [trans_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'trans_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='trans_ssib_gis')
    trans_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='trans_ssib_ispdn')
    trans_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='trans_ssib_kii')
    trans_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='trans_ssib_autist')
    trans_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='trans')

    rows = [[trans_ssib_gis], [trans_ssib_ispdn], [trans_ssib_kii], [trans_ssib_autist], [trans_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'trans_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='trans_ssib_gis')
    trans_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='trans_ssib_ispdn')
    trans_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='trans_ssib_kii')
    trans_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='trans_ssib_autist')
    trans_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='trans')

    rows = [[trans_ssib_gis], [trans_ssib_ispdn], [trans_ssib_kii], [trans_ssib_autist], [trans_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'trans_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='trans_ssib')
    trans_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='trans_pka')
    trans_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='trans_isg')
    trans_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='trans_gos')
    trans_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[trans_ssib], [trans_pka], [trans_isg], [trans_gos], [trans_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Транспорт🚌. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'trans_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='trans_ssib')
    trans_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='trans_pka')
    trans_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='trans_isg')
    trans_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='trans_gos')
    trans_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[trans_ssib], [trans_pka], [trans_isg], [trans_gos], [trans_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Транспорт🚌. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'trans_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" trans')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['7', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    trans_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='trans_ssib')
    trans_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='trans_pka')
    trans_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='trans_isg')
    trans_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='trans_gos')
    trans_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[trans_ssib], [trans_pka], [trans_isg], [trans_gos], [trans_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Транспорт🚌. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'banks')
async def energy(call: CallbackQuery):
    log.info('User selected "Банки и финансы💰"')

    banks_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='banks_ssib')
    banks_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='banks_pka')
    banks_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='banks_isg')
    banks_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='banks_gos')
    banks_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[banks_ssib], [banks_pka], [banks_isg], [banks_gos], [banks_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Банки и финансы💰. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'banks_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" banks')

    banks_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='banks_ssib_gis')
    banks_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='banks_ssib_ispdn')
    banks_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='banks_ssib_kii')
    banks_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='banks_ssib_autist')
    banks_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='banks')

    rows = [[banks_ssib_gis], [banks_ssib_ispdn], [banks_ssib_kii], [banks_ssib_autist], [banks_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'banks_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='banks_ssib_gis')
    banks_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='banks_ssib_ispdn')
    banks_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='banks_ssib_kii')
    banks_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='banks_ssib_autist')
    banks_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='banks')

    rows = [[banks_ssib_gis], [banks_ssib_ispdn], [banks_ssib_kii], [banks_ssib_autist], [banks_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'banks_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='banks_ssib_gis')
    banks_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='banks_ssib_ispdn')
    banks_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='banks_ssib_kii')
    banks_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='banks_ssib_autist')
    banks_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='banks')

    rows = [[banks_ssib_gis], [banks_ssib_ispdn], [banks_ssib_kii], [banks_ssib_autist], [banks_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'banks_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='banks_ssib_gis')
    banks_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='banks_ssib_ispdn')
    banks_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='banks_ssib_kii')
    banks_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='banks_ssib_autist')
    banks_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='banks')

    rows = [[banks_ssib_gis], [banks_ssib_ispdn], [banks_ssib_kii], [banks_ssib_autist], [banks_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'banks_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='banks_ssib_gis')
    banks_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='banks_ssib_ispdn')
    banks_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='banks_ssib_kii')
    banks_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='banks_ssib_autist')
    banks_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='banks')

    rows = [[banks_ssib_gis], [banks_ssib_ispdn], [banks_ssib_kii], [banks_ssib_autist], [banks_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'banks_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='banks_ssib')
    banks_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='banks_pka')
    banks_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='banks_isg')
    banks_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='banks_gos')
    banks_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[banks_ssib], [banks_pka], [banks_isg], [banks_gos], [banks_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Банки и финансы💰. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'banks_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='banks_ssib')
    banks_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='banks_pka')
    banks_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='banks_isg')
    banks_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='banks_gos')
    banks_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[banks_ssib], [banks_pka], [banks_isg], [banks_gos], [banks_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Банки и финансы💰. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'banks_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" banks')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['8', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    banks_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='banks_ssib')
    banks_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='banks_pka')
    banks_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='banks_isg')
    banks_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='banks_gos')
    banks_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[banks_ssib], [banks_pka], [banks_isg], [banks_gos], [banks_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Банки и финансы💰. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'med')
async def energy(call: CallbackQuery):
    log.info('User selected "Медицина и фармацевтика⚕️"')

    med_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='med_ssib')
    med_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='med_pka')
    med_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='med_isg')
    med_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='med_gos')
    med_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[med_ssib], [med_pka], [med_isg], [med_gos], [med_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Медицина и фармацевтика⚕️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'med_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" med')

    med_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='med_ssib_gis')
    med_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='med_ssib_ispdn')
    med_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='med_ssib_kii')
    med_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='med_ssib_autist')
    med_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='med')

    rows = [[med_ssib_gis], [med_ssib_ispdn], [med_ssib_kii], [med_ssib_autist], [med_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'med_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='med_ssib_gis')
    med_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='med_ssib_ispdn')
    med_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='med_ssib_kii')
    med_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='med_ssib_autist')
    med_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='med')

    rows = [[med_ssib_gis], [med_ssib_ispdn], [med_ssib_kii], [med_ssib_autist], [med_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'med_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='med_ssib_gis')
    med_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='med_ssib_ispdn')
    med_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='med_ssib_kii')
    med_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='med_ssib_autist')
    med_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='med')

    rows = [[med_ssib_gis], [med_ssib_ispdn], [med_ssib_kii], [med_ssib_autist], [med_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'med_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='med_ssib_gis')
    med_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='med_ssib_ispdn')
    med_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='med_ssib_kii')
    med_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='med_ssib_autist')
    med_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='med')

    rows = [[med_ssib_gis], [med_ssib_ispdn], [med_ssib_kii], [med_ssib_autist], [med_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'med_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='med_ssib_gis')
    med_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='med_ssib_ispdn')
    med_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='med_ssib_kii')
    med_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='med_ssib_autist')
    med_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='med')

    rows = [[med_ssib_gis], [med_ssib_ispdn], [med_ssib_kii], [med_ssib_autist], [med_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'med_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='med_ssib')
    med_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='med_pka')
    med_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='med_isg')
    med_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='med_gos')
    med_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[med_ssib], [med_pka], [med_isg], [med_gos], [med_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Медицина и фармацевтика⚕️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'med_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='med_ssib')
    med_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='med_pka')
    med_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='med_isg')
    med_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='med_gos')
    med_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[med_ssib], [med_pka], [med_isg], [med_gos], [med_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Медицина и фармацевтика⚕️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'med_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" med')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['9', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    med_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='med_ssib')
    med_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='med_pka')
    med_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='med_isg')
    med_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='med_gos')
    med_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[med_ssib], [med_pka], [med_isg], [med_gos], [med_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Медицина и фармацевтика⚕️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'since')
async def energy(call: CallbackQuery):
    log.info('User selected "Наука🔬"')

    since_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='since_ssib')
    since_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='since_pka')
    since_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='since_isg')
    since_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='since_gos')
    since_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[since_ssib], [since_pka], [since_isg], [since_gos], [since_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Наука🔬. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'since_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" med')

    since_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='since_ssib_gis')
    since_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='since_ssib_ispdn')
    since_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='since_ssib_kii')
    since_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='since_ssib_autist')
    since_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='since')

    rows = [[since_ssib_gis], [since_ssib_ispdn], [since_ssib_kii], [since_ssib_autist], [since_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'since_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='since_ssib_gis')
    since_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='since_ssib_ispdn')
    since_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='since_ssib_kii')
    since_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='since_ssib_autist')
    since_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='since')

    rows = [[since_ssib_gis], [since_ssib_ispdn], [since_ssib_kii], [since_ssib_autist], [since_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'since_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='since_ssib_gis')
    since_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='since_ssib_ispdn')
    since_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='since_ssib_kii')
    since_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='since_ssib_autist')
    since_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='since')

    rows = [[since_ssib_gis], [since_ssib_ispdn], [since_ssib_kii], [since_ssib_autist], [since_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'since_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='since_ssib_gis')
    since_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='since_ssib_ispdn')
    since_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='since_ssib_kii')
    since_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='since_ssib_autist')
    since_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='since')

    rows = [[since_ssib_gis], [since_ssib_ispdn], [since_ssib_kii], [since_ssib_autist], [since_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'since_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='since_ssib_gis')
    since_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='since_ssib_ispdn')
    since_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='since_ssib_kii')
    since_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='since_ssib_autist')
    since_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='since')

    rows = [[since_ssib_gis], [since_ssib_ispdn], [since_ssib_kii], [since_ssib_autist], [since_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'since_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='since_ssib')
    since_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='since_pka')
    since_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='since_isg')
    since_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='since_gos')
    since_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[since_ssib], [since_pka], [since_isg], [since_gos], [since_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Наука🔬. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'since_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='since_ssib')
    since_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='since_pka')
    since_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='since_isg')
    since_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='since_gos')
    since_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[since_ssib], [since_pka], [since_isg], [since_gos], [since_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Наука🔬. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'since_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" since')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['10', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    since_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='since_ssib')
    since_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='since_pka')
    since_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='since_isg')
    since_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='since_gos')
    since_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[since_ssib], [since_pka], [since_isg], [since_gos], [since_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Наука🔬. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Государственный сектор🏛️"')

    gos_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gos_ssib')
    gos_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gos_pka')
    gos_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gos_isg')
    gos_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gos_gos')
    gos_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gos_ssib], [gos_pka], [gos_isg], [gos_gos], [gos_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Государственный сектор🏛️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gos_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" gos')

    gos_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gos_ssib_gis')
    gos_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gos_ssib_ispdn')
    gos_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gos_ssib_kii')
    gos_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gos_ssib_autist')
    gos_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gos')

    rows = [[gos_ssib_gis], [gos_ssib_ispdn], [gos_ssib_kii], [gos_ssib_autist], [gos_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gos_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gos_ssib_gis')
    gos_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gos_ssib_ispdn')
    gos_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gos_ssib_kii')
    gos_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gos_ssib_autist')
    gos_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gos')

    rows = [[gos_ssib_gis], [gos_ssib_ispdn], [gos_ssib_kii], [gos_ssib_autist], [gos_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gos_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gos_ssib_gis')
    gos_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gos_ssib_ispdn')
    gos_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gos_ssib_kii')
    gos_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gos_ssib_autist')
    gos_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gos')

    rows = [[gos_ssib_gis], [gos_ssib_ispdn], [gos_ssib_kii], [gos_ssib_autist], [gos_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gos_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Вет подходящих документов.')

    gos_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gos_ssib_gis')
    gos_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gos_ssib_ispdn')
    gos_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gos_ssib_kii')
    gos_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gos_ssib_autist')
    gos_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gos')

    rows = [[gos_ssib_gis], [gos_ssib_ispdn], [gos_ssib_kii], [gos_ssib_autist], [gos_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gos_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='gos_ssib_gis')
    gos_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='gos_ssib_ispdn')
    gos_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='gos_ssib_kii')
    gos_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='gos_ssib_autist')
    gos_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='gos')

    rows = [[gos_ssib_gis], [gos_ssib_ispdn], [gos_ssib_kii], [gos_ssib_autist], [gos_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'gos_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gos_ssib')
    gos_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gos_pka')
    gos_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gos_isg')
    gos_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gos_gos')
    gos_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gos_ssib], [gos_pka], [gos_isg], [gos_gos], [gos_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Государственный сектор🏛️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gos_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gos_ssib')
    gos_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gos_pka')
    gos_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gos_isg')
    gos_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gos_gos')
    gos_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gos_ssib], [gos_pka], [gos_isg], [gos_gos], [gos_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Государственный сектор🏛️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'gos_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" gos')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['11', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    gos_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='gos_ssib')
    gos_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='gos_pka')
    gos_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='gos_isg')
    gos_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='gos_gos')
    gos_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[gos_ssib], [gos_pka], [gos_isg], [gos_gos], [gos_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Государственный сектор🏛️. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'telev')
async def energy(call: CallbackQuery):
    log.info('User selected "Телекоммуникации и Медиа📡"')

    telev_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='telev_ssib')
    telev_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='telev_pka')
    telev_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='telev_isg')
    telev_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='telev_gos')
    telev_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[telev_ssib], [telev_pka], [telev_isg], [telev_gos], [telev_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Телекоммуникации и Медиа📡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'telev_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" telev')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'telev_ssib_gis')
async def energy(call: CallbackQuery):
    log.info('User selected "ГИС🌐" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '1'], '1')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'telev_ssib_ispdn')
async def energy(call: CallbackQuery):
    log.info('User selected "ИСПДН🔒" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '1'], '2')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'telev_ssib_kii')
async def energy(call: CallbackQuery):
    log.info('User selected "КИИ🔐" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '1'], '3')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'telev_ssib_autist')
async def energy(call: CallbackQuery):
    log.info('User selected "АСУТП🔧" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '1'], '4')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Выберите объект защиты', reply_markup=markup)


@dp.callback_query(F.data == 'telev_gos')
async def energy(call: CallbackQuery):
    log.info('User selected "Интеграция с ГосСОПКА👾" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '4'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='telev_ssib')
    telev_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='telev_pka')
    telev_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='telev_isg')
    telev_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='telev_gos')
    telev_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[telev_ssib], [telev_pka], [telev_isg], [telev_gos], [telev_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Телекоммуникации и Медиа📡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'telev_pka')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к аттестации📜" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '2'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='telev_ssib')
    telev_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='telev_pka')
    telev_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='telev_isg')
    telev_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='telev_gos')
    telev_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[telev_ssib], [telev_pka], [telev_isg], [telev_gos], [telev_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Телекоммуникации и Медиа📡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'telev_isg')
async def energy(call: CallbackQuery):
    log.info('User selected "Подготовка к категорированию📊" telev')

    await call.message.reply('Собираем список нужных нормативных актов...')

    spis = DataBase.get_act(['12', '3'], '0')
    if spis:
        for i in range(len(spis)):
            await call.message.reply(f'{spis[i][0][0]} \n'
                                     f'{spis[i][0][1]} \n'
                                     f'{spis[i][0][2]}')
            if spis[i][1]:
                for w in range(len(spis[i][1])):
                    await call.message.reply(f'{spis[i][1][w][0]} \n'
                                             f'{spis[i][1][w][1]} \n'
                                             f'{spis[i][1][w][2]}')
    else:
        await call.message.reply('Нет подходящих документов.')

    telev_ssib = InlineKeyboardButton(text='Создание системы информационной безопасности🔒', callback_data='telev_ssib')
    telev_pka = InlineKeyboardButton(text='Подготовка к аттестации📜', callback_data='telev_pka')
    telev_isg = InlineKeyboardButton(text='Подготовка к категорированию📊', callback_data='telev_isg')
    telev_gos = InlineKeyboardButton(text='Интеграция с ГосСОПКА👾', callback_data='telev_gos')
    telev_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='dalee')

    rows = [[telev_ssib], [telev_pka], [telev_isg], [telev_gos], [telev_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('Вы выбрали Телекоммуникации и Медиа📡. Выберите вашу цель:', reply_markup=markup)


@dp.callback_query(F.data == 'energy_ssib')
async def energy(call: CallbackQuery):
    log.info('User selected "Выбрать объект защиты🔒" энергктика')

    telev_ssib_gis = InlineKeyboardButton(text='ГИС🌐', callback_data='telev_ssib_gis')
    telev_ssib_ispdn = InlineKeyboardButton(text='ИСПДН🔒', callback_data='telev_ssib_ispdn')
    telev_ssib_kii = InlineKeyboardButton(text='КИИ🔐', callback_data='telev_ssib_kii')
    telev_ssib_autist = InlineKeyboardButton(text='АСУТП🔧', callback_data='telev_ssib_autist')
    telev_ssib_nazad = InlineKeyboardButton(text='Назад⬅️', callback_data='telev')

    rows = [[telev_ssib_gis], [telev_ssib_ispdn], [telev_ssib_kii], [telev_ssib_autist], [telev_ssib_nazad]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await call.message.reply('выберите объект защиты', reply_markup=markup)


async def main():
    log.info('Bot started working')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
