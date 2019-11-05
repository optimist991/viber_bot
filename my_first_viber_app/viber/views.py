from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage

from viberbot.api.viber_requests import ViberMessageRequest

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



viber = Api(BotConfiguration(
    name='Bot',
    avatar='',
    auth_token='4a863d3a5927d7bc-5e73d41cb6759a41-1d6be75cdd414276'
))


@csrf_exempt
def set_webhook(request):
    event_types = ['failed', 'subscribed', 'unsubscribed', 'conversation_started']
    url = f'https://{settings.ALLOWED_HOSTS[0]}/viber/callback/'
    viber.set_webhook(url, webhook_events=event_types)
    return HttpResponse('Ok')


@csrf_exempt
def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse('webhook_Off')


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)

        if isinstance(viber_request, ViberMessageRequest):
            if isinstance(viber_request.message, TextMessage):
                viber.send_messages(viber_request.sender.id, [TextMessage(text='Это текст')])
                print(viber_request.message)
            elif isinstance(viber_request.message, PictureMessage):
                viber.send_messages(viber_request.sender.id, [TextMessage(text='Это картинка')])
                print(viber_request.message.media)
        # viber.send_messages(
        #     viber_request.sender.id,
        #     TextMessage(text='ok')
        # )

    return HttpResponse(status=200)





