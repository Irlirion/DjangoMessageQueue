from django.core.serializers import json
from django.db.models import QuerySet
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import json

from mq_json.models import Client, Message


@csrf_exempt
def register(request):
    if request.method == 'POST':
        client = Client.objects.create()
        uuid = client.uuid
        json_data = {'uuid': uuid}
        return JsonResponse(json_data)
    return HttpResponseServerError('Only POST requests')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            message = Message()
            sender_client = Client.objects.get(uuid=data["from_uuid"])
            recipient_client = Client.objects.get(uuid=data["to_uuid"])
            message.sender_uuid = sender_client
            message.recipient_uuid = recipient_client
            message.message = data["message"]
            message.save()

            return JsonResponse({'status': 'OK'})
        except KeyError:
            return HttpResponseServerError("Bad json")
    return HttpResponseServerError('Only POST requests')

@csrf_exempt
def get_messages(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            messages_query = Message.objects.filter(recipient_uuid=data["uuid"])
            messages = [{"message": message.message, "from_uuid": message.sender_uuid.uuid} for message in messages_query]
            send_data = {"messages": messages}

            # Message.objects.filter(recipient_uuid=data["uuid"]).delete()

            return JsonResponse(send_data, safe=False)
        except KeyError:
            return HttpResponseServerError("Bad json")
    return HttpResponseServerError('Only POST requests')