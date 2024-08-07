from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
import os
from dotenv import load_dotenv
from app.files.librian import *
import app.keyboards as kb
load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


cnt = [0]


class Stalker(StatesGroup):
    points = State()


class Question(StatesGroup):
    name = State()
    number = State()
    text = State()


@dp.callback_query(F.data == 'back_to_main')
async def echo(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('start.txt'), reply_markup=kb.main, parse_mode="Markdown")


@dp.message(CommandStart())
async def echo(message: Message):
    await message.answer(txt_to_str('start.txt'), reply_markup=kb.main, parse_mode="Markdown")
    stat = get_stat()
    if message.from_user.first_name not in stat["members"]:
        await bot.send_message(chat_id=841610537, text=f"New member: {message.from_user.first_name}")
    new_member(message.from_user.first_name)


@dp.callback_query(F.data == 'direction')
async def direction_group_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('direction.txt'), reply_markup=kb.direction_group, parse_mode="Markdown")


@dp.callback_query(F.data == '01')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('01'), parse_mode="Markdown")


@dp.callback_query(F.data == '09')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('09'), parse_mode="Markdown")


@dp.callback_query(F.data == '12')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('12'), parse_mode="Markdown")


@dp.callback_query(F.data == '15')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('15'), parse_mode="Markdown")


@dp.callback_query(F.data == '20')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('20'), parse_mode="Markdown")


@dp.callback_query(F.data == '22')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('22'), parse_mode="Markdown")


@dp.callback_query(F.data == '27')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('27'), parse_mode="Markdown")


@dp.callback_query(F.data == '38')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Направления из выбранной группы', reply_markup=await kb.directions('38'), parse_mode="Markdown")


@dp.callback_query(F.data.contains('.txt'))
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    cods = get_cods()
    for cod in cods:
        if cod in call.data:
            url = txt_to_str(cod, True)[txt_to_str(cod, True).rindex('-') + 2:]
            text = txt_to_str(cod, True)[:txt_to_str(cod, True).index('!') + 1]
            await call.message.answer(text, reply_markup=await kb.to_main(url=url), parse_mode="Markdown")
            break


@dp.callback_query(F.data == 'home')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.delete()
    file = FSInputFile('app/files/photo_2024-06-25_07-07-46.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('home.txt'), reply_markup=await kb.to_main(
        text='Регламент', url="https://priem.stankin.ru/obshchezhitie/"))


@dp.callback_query(F.data == 'career')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('jobs.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")


@dp.callback_query(F.data == 'contacts')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('contact.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")


@dp.callback_query(F.data == 'SPO')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('SPO.txt'), reply_markup=kb.SPO, parse_mode="Markdown")


@dp.callback_query(F.data == 'exams_how_much')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('what_exam_enlarged_group.txt'), reply_markup=kb.SPO, parse_mode="Markdown")


@dp.callback_query(F.data == 'exams_how')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('SPO_2.txt'), reply_markup=kb.SPO, parse_mode="Markdown")


@dp.callback_query(F.data == 'СТАНКИН')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давайте расскажу о моем университете', reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'dop')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Я могу рассказать про многое :)', reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'modul')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/6leqhrt4p9y-1024x626.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('modal.txt'), reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'rate')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('reiting.txt'), reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'VUC')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('VUC.txt'), reply_markup=kb.STANKIN, parse_mode="Markdown")


@dp.callback_query(F.data == 'volonter')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    volonetrs = [
        InputMediaPhoto(media=FSInputFile('app/files/0GYSpy4WiPc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/AWgELDlY7do.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/E-im7qZzEGU.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/tWi5R0nKfy0.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(volonetrs)
    await call.message.answer(txt_to_str('volonter.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'cyber')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    cybers = [
        InputMediaPhoto(media=FSInputFile('app/files/vJ4YtqdvqeA.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/YTTJl9qnp0s.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/zkhYjV0R2ys.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(cybers)
    await call.message.answer(txt_to_str('cyber.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'club')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/uwY3uEqgWGk.jpg')
    await call.message.answer_photo(file, caption=txt_to_str('club.txt'), reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'tip-top')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/4aijGPUSJgo.jpg')
    await call.message.answer_photo(file, caption='Фото с выступления группы tip-top', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'dance')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    dances = [
        InputMediaPhoto(media=FSInputFile('app/files/CDyp87Mg9Vc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/RfxdXh8YXmc.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/WNxCT-89Ni8.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/ynCTEkVNq4c.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(dances)
    await call.message.answer('Выступления танцоров', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'vocal')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    vocals = [
        InputMediaPhoto(media=FSInputFile('app/files/q-tx_UDvgH0.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/TW92znbSsIo.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/x6zIDxVvp_4.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/xMvq7I4SZTg.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(vocals)
    await call.message.answer('Выступления вокалистов', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'bolt')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Секунду, ищу фотографии...')
    bolts = [
        InputMediaPhoto(media=FSInputFile('app/files/Ld1P3UUGPGk.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/kvMLvsGXZKE.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/oSIZ2qSLnts.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/uf3-XTsSs1Y.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/UhaUIUDSlXk.jpg')),
        InputMediaPhoto(media=FSInputFile('app/files/XK_z1yb4PcE.jpg'))
    ]
    await call.message.delete()
    await call.message.answer_media_group(bolts)
    await call.message.answer('Фото с выступления Станкиновкого болта', reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'other_clubs')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('clubs.txt'), reply_markup=kb.CLUB, parse_mode="Markdown")


@dp.callback_query(F.data == 'prof')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('prof.txt'), reply_markup=kb.dop_menu, parse_mode="Markdown")


@dp.callback_query(F.data == 'ya_loh')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('ya_loh.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")


@dp.callback_query(F.data == 'build')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Всего СТАНКИН имеет 3 корпуса и 1 филиал', reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'osnov')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('vadkovcky.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'frez')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('frezer.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'libr')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('library.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'egor')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('egorevsky.txt'), reply_markup=kb.BUILD, parse_mode="Markdown")


@dp.callback_query(F.data == 'how_docs')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text('Вот все варианты подачи документов', reply_markup=kb.VARIANTS, parse_mode="Markdown")


@dp.callback_query(F.data == 'ochn')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('ochno.txt'), reply_markup=kb.VARIANTS, parse_mode="Markdown")


@dp.callback_query(F.data == 'dist')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('sdpd.txt'), reply_markup=kb.VARIANTS_2, parse_mode="Markdown")


@dp.callback_query(F.data == 'post')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.edit_text(txt_to_str('post servis.txt'), reply_markup=kb.VARIANTS, parse_mode="Markdown")


@dp.callback_query(F.data == 'chances')
async def direction_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await state.set_state(Stalker.points)
    await call.message.answer('Введите сумму ваших баллов ЕГЭ (Например: 255)')


@dp.message(Stalker.points)
async def direction_callback(message: Message, state: FSMContext):
    await state.update_data(points=message.text)
    await state.set_state(Stalker.points)
    data = await state.get_data()
    await state.clear()
    cods = get_cods()
    await message.answer('Исходя из данных на 2023 год, вы бы прошли на направления:')
    for cod in cods:
        if cod != '01.03.04.txt' and cod != '22.03.01.txt':
            with open(f'app/files/directions/{cod}', 'r', encoding='utf-8') as f:
                res = f.read()
                f.close()
            point = int(res[res.index('-') + 2:res.index('-') + 5])
            if point <= int(data["points"]):
                await message.answer(f"{res[:res.index(':')]}")
    await message.answer('Отслеживайте свое положение в списках нашего сайте', reply_markup=await kb.to_main(),
                         parse_mode="Markdown")


@dp.callback_query(F.data == 'rules')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давай разберемся', reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'lgot')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Выбираем льготу', reply_markup=kb.LGOTI, parse_mode="Markdown")


@dp.callback_query(F.data == 'celev')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('target quota.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")


@dp.callback_query(F.data == 'osob')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('special.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")


@dp.callback_query(F.data == 'otd')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('separate.txt'), reply_markup=kb.LGOTI, parse_mode="Markdown")


@dp.callback_query(F.data == 'vstupi')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('vstupi_kto.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'prior')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    file = FSInputFile('app/files/preemptive_right.txt')
    await call.message.answer_document(file,
                                       caption=txt_to_str('Описание приоритетного зачисления.txt'),
                                       reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'sys_prior')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('sistema prioritetov.txt'), reply_markup=await kb.to_main(text='Ранжированные списки', url='https://priem.stankin.ru/bakalavriatispetsialitet/ranked-lists/'), parse_mode="Markdown")


@dp.callback_query(F.data == 'ogranich')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('lim_bakalavrspec.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'ball')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('com_point.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'min_ball')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Давай разберемся', reply_markup=kb.VIBOR, parse_mode="Markdown")


@dp.callback_query(F.data == 'e')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('min_EGE.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 's')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('min_SPO.txt'), reply_markup=kb.RULES, parse_mode="Markdown")


@dp.callback_query(F.data == 'calc')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(f"Калькулятор индивидуальных баллов")
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")


@dp.callback_query(F.data.contains('b+'))
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    res = int(call.data[2:])
    cnt[0] = min(10, cnt[0] + res)
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")


@dp.callback_query(F.data == 'b//0')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    cnt[0] = 0
    await call.message.answer(
        f"Для добавления баллов используйте кнопки выше\nМаксимальное кол-во баллов: 10\nСумма баллов: {cnt[0]}",
        reply_markup=await kb.b(), parse_mode="Markdown")


@dp.callback_query(F.data == 'spiski')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer('Найти себя в списках легко!', reply_markup=kb.SPISKI, parse_mode="Markdown")


@dp.callback_query(F.data == 'kab')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(
        txt_to_str('kab.txt'),
        reply_markup=await kb.to_main(text='Личный кабинет', url='https://info.stankin.ru/lk/login'), parse_mode="Markdown")


@dp.callback_query(F.data == 'rang')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(
        txt_to_str('spi.txt'),
        reply_markup=
        await kb.to_main(text='Списки к приказу',
                         url='https://priem.stankin.ru/bakalavriatispetsialitet/ranked-lists-ext/?order=1'), parse_mode="Markdown")


@dp.callback_query(F.data == 'at')
async def direction_callback(call: CallbackQuery):
    await call.answer('')
    await call.message.answer(txt_to_str('at.txt'), reply_markup=await kb.to_main(), parse_mode="Markdown")


@dp.message(Command('stat'))
async def direction_callback(message: Message):
    stat = get_stat()
    await message.answer(f"Всего ботом пользовались {stat['cnt']} раз")
    await message.answer("Список пользователей")
    for item in stat["members"]:
        await message.answer(item)


@dp.callback_query(F.data == 'q1')
async def question_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('')
    await call.message.answer('Хорошо, я создам заявку, которую передам сотрудникам приемной комиссии')
    await call.message.answer('Как мы можем к вам обращаться? (ФИО)')
    await state.set_state(Question.name)


@dp.message(Question.name)
async def question_callback2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Напишите, пожалуйста, ваш номер телефона')
    await state.set_state(Question.number)


@dp.message(Question.number)
async def question_callback2(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer('Опишите вашу проблему')
    await state.set_state(Question.text)


@dp.message(Question.text)
async def question_callback2(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await state.clear()
    s = txt_to_str('Шаблон.txt')
    s = s.replace('"1"', str(data['name']))
    s = s.replace('"2"', str(data['number']))
    s = s.replace('"3"', str(data['text']))
    await bot.send_message(text=s, chat_id=-1002194571891)
    await message.answer('Ваша заявка передана!', reply_markup=await kb.to_main())
