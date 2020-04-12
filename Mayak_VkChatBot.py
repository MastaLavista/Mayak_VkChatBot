from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
import random


def main():
    vk_session = vk_api.VkApi(
        token='token', # Вынесено в .gitignore
        api_version='5.90')

    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=None)

    keyboard.add_button('Купить', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Продать', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Получить скидку', color=VkKeyboardColor.PRIMARY)

    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == 'Начать' and event.from_user:  # Если написали в ЛС
                vk.messages.send(  # Отправляем сообщениe
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Выбери интересующую категорию',
                    keyboard=keyboard.get_keyboard())

            if event.text == 'Купить' and event.from_user:  # Если написали в ЛС
                vk.messages.send(  # Отправляем сообщениe
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Здесь можно посмотреть товары по категориям: https://vk.com/market-73747588. Если тебя заинтересовал товар, то пришли его сюда, мы тебе ответим.                                                               Не нашёл нужного товара? Напиши нам об этом!',
                    keyboard=keyboard.get_keyboard()
                )
            elif event.text == 'Продать' and event.from_user:
                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Если надо продать вещь, заполни краткую анкету, и консультант свяжется с тобой в ближайшее время :) https://vk.com/app5708398_-73747588',
                    keyboard=keyboard.get_keyboard()
                )
            elif event.text == 'Получить скидку' and event.from_user:
                vk.messages.send(  # Отправляем собщение
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    message='Твой личный промокод, который даёт пожизненную скидку 5% на наши и так низкие цены: VK431Sk5.                        Всё, что нужно сделать - это приехать в любой из наших магазинов и продиктовать промокод менеджеру, чтобы получить приятную скидку 5%.',
                    keyboard=keyboard.get_keyboard()
                )
            elif event.text == 'Убери кнопки' and event.from_user:
                vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message='Окей',
                        keyboard=keyboard.get_empty_keyboard()
                )

if __name__ == '__main__':
    main()