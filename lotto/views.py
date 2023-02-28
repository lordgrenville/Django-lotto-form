import json
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render

def validate_number(number):
    """Check input is acceptable"""
    try:
        num = int(number)
    except ValueError:
        return False
    return (num >= 2500) & (num <= 3540)

def ajax(request):
    if request.method == 'POST':
        form_input = request.POST['lotto_number']
        if validate_number(form_input):
            url = 'https://pais.co.il/lotto/showMoreResults.aspx?fromIndex=0&amount=49&fromNumber='
            url += f'{form_input}&toNumber={form_input}'
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            nums = [div.text.strip('\n') for div in soup.find_all('li', attrs={'class': "loto_info_num archive"})][::-1]
            lucky_num = soup.find('div', attrs={'class': "loto_info_num strong archive"}).find_all('div')[-1].text

            return HttpResponse(json.dumps({'results': nums + [lucky_num]}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'results': "Sorry, your input is invalid"}), content_type="application/json")


def form(request):
    return render(request, "form.html")
