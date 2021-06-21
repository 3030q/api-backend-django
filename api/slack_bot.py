import datetime
import json

import slack
import os
from pathlib import Path

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from rest_framework.decorators import api_view

from api import template_message
from api.models import App, AppStoreReviews, GooglePlayReviews, AppGalleryReviews
from api.reviews.review_serializer import AppStoreReviewSerializer, GooglePlayReviewSerializer, \
    AppGalleryReviewSerializer
from api.serializer import AppSerializer
from api_backend_parser import settings


@api_view(['Post'])
def hello(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    data = request.data
    print(data)
    if data['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in data:
        if data['type'] == 'url_verification':
            response_dict = {"challenge": data['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in data:
        event_msg = data['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)
    name, platform = tuple(data['text'].split())
    print(name, platform)
    response_msg = ":wave:, Hello aboba"
    client.chat_postMessage(channel='#reviewgator-chat', text=response_msg)
    return HttpResponse(status=200)


@api_view(['Post'])
def last_week_statistics(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    data = request.data
    print(data)
    if data['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in data:
        if data['type'] == 'url_verification':
            response_dict = {"challenge": data['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in data:
        event_msg = data['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)
    name, platform = tuple(data['text'].split())
    app = App.objects.filter(name=name, platform=platform).get()
    serialize_app = AppSerializer(app).data
    if platform == 'app_store':
        client.chat_postMessage(channel='#reviewgator-chat',
                                text='Нет возможности посмотреть статиску за неделю у этой платформы')
        return HttpResponse(status=200)
    elif platform == 'google_play':
        reviews = GooglePlayReviewSerializer(GooglePlayReviews.objects.filter(
            app_id=serialize_app['id'],
            posted_at__gt=datetime.datetime.now() - datetime.timedelta(days=7)
        ).all(), many=True).data
    else:
        reviews = AppGalleryReviewSerializer(AppGalleryReviews.objects.filter(
            app_id=serialize_app['id'],
            posted_at__gt=datetime.datetime.now() - datetime.timedelta(days=7)
        ).all(), many=True).data
    one_star = 0
    two_star = 0
    three_star = 0
    four_star = 0
    five_star = 0
    date = datetime.date.today()
    for review in reviews:
        if review['rating'] == '1':
            one_star += 1
        elif review['rating'] == '2':
            two_star += 1
        elif review['rating'] == '3':
            three_star += 1
        elif review['rating'] == '4':
            four_star += 1
        else:
            five_star += 1
    median_rating = one_star * 1 + two_star * 2 + three_star * 3 + four_star * 4 + five_star * 5

    response_message = template_message.last_week_statistics_template(
        one_star, two_star, three_star, four_star, five_star, name, date, median_rating
    )
    client.chat_postMessage(**response_message)
    return HttpResponse(status=200)
