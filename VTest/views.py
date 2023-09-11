import json

import openai
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

from dotenv import load_dotenv

# loading the enviorment
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')


def home(request):
    return HttpResponse("hello")


# api for getting the response of the message using chatgpt
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        return HttpResponse(os.environ.get('TEST_KEY'))
        message = {
            'role': 'user',
            'content': message
        }

        messages = [message]
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        # Return the response
        return JsonResponse({'response': response.choices[0].message.content})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
