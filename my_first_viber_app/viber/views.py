from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage

from viberbot.api.viber_requests import ViberMessageRequest

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



viber = Api(BotConfiguration(
    name='Bot',
    avatar='',
    auth_token='4a863d3a5927d7bc-5e73d41cb6759a41-1d6be75cdd414276'
))


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        viber.send_messages(
            viber_request.sender.id,
            TextMessage(text='ok')
        )

    return HttpResponse(status=200)





