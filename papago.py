import os
import sys
import urllib.request
import json

class Translator:

  def __init__(self, client_id="your_key", client_secret="your_key"):
    self.client_id = client_id
    self.client_secret = client_secret

  def translate(self, input_text, source='ko', target='en'):

    encText = urllib.parse.quote(input_text)
    data = "source={}&target={}&text={}".format(source, target, encText)
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", self.client_id)
    request.add_header("X-Naver-Client-Secret", self.client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
      response_body = json.loads(response.read().decode("utf-8"))
      translated_text = response_body["message"]["result"]["translatedText"]
      return translated_text
    else:
      return "Error Code:" + rescode