import os

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

load_dotenv()


@csrf_exempt
def basic_request(request):
    if request.method == "GET":
        return JsonResponse({"status": "GET Pass"}, safe=False)

    if request.method == "POST":
        return JsonResponse({"status": "POST Pass"}, safe=False)


@csrf_exempt
def tokenize(request):
    if request.method == "POST":
        try:
            sentence = request.POST["text"]
        except KeyError:
            return JsonResponse({"error": "Input not found"}, safe=False, status=500)

        url = "https://api.aiforthai.in.th/tlexplus"

        params = {"text": sentence}

        headers = {"Apikey": os.environ["AIFORTHAI_API_KEY"]}
        response = requests.get(url, params=params, headers=headers)

        return JsonResponse(
            {"student": "6410742370", "tokenize": response.json()}, safe=False
        )

    return JsonResponse({"error": "Method not allowed!"}, safe=False, status=403)


@csrf_exempt
def sentimental(request):
    if request.method == "POST":
        try:
            sentence = request.POST["text"]
        except KeyError:
            return JsonResponse({"error": "Input not found"}, safe=False, status=500)

        url = "https://api.aiforthai.in.th/ssense"

        params = {"text": sentence}

        headers = {"Apikey": os.environ["AIFORTHAI_API_KEY"]}
        response = requests.get(url, params=params, headers=headers)

        return JsonResponse(
            {"student": "6410742370", "sentiment": response.json()["sentiment"]},
            safe=False,
        )

    return JsonResponse({"error": "Method not allowed!"}, safe=False, status=403)


@csrf_exempt
def text2speech(request):
    if request.method == "POST":
        try:
            sentence = request.POST["text"]
        except KeyError:
            return JsonResponse({"error": "Input not found"}, safe=False, status=500)

        url = "https://api.aiforthai.in.th/vaja9/synth_audiovisual"

        params = {
            "input_text": sentence,
            "speaker": 1,
            "phrase_break": 0,
            "audio_visual": 0,
        }

        headers = {"Apikey": os.environ["AIFORTHAI_API_KEY"]}
        response = requests.post(url, json=params, headers=headers)

        return JsonResponse(
            {"student": "6410742370", "output": response.json()["wav_url"]},
            safe=False,
        )

    return JsonResponse({"error": "Method not allowed!"}, safe=False, status=403)


# Create your views here.
def ecommerce_index_view(request):
    """This function render index page of ecommerce views"""

    return HttpResponse("Welcome to 6410742370 Tinn Kanjananuwat views!")


def item_view(request, item_id):
    context_data = {"item_id": item_id}

    return render(request, "index.html", context=context_data)


def homepage(request):
    return HttpResponse("Homepage")


def category(request):
    return HttpResponse("Category")


def product(request):
    return HttpResponse("Product")


def checkout(request):
    return HttpResponse("Checkout")


def contact(request):
    return HttpResponse("Contact")
