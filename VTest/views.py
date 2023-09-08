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
