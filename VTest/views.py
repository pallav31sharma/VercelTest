import json

import openai
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.api_key = "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"

def home(request):
    return HttpResponse("hello")


# api for getting the response of the message using chatgpt
@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
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
