import base64
import Config.Config as config
import hashlib
import hmac
import hug
import json
import linebot
import Search.googleSearch as googleSearch

con = config.Config()

@hug.post('/')
def router(body):
    action = body['events'][0]['message']['text'].split()[0]
    replyToken = body['events'][0]['replyToken']

    if action == 'google':
        text = body['events'][0]['message']['text'][7:]
        googleSearchFunction(replyToken, text)
    else:
        return None

# @hug.post('/googleSearch')
def googleSearchFunction(replyToken, text):
    channelAccessToken = con.get('chatWar', 'CHANNEL_ACCESS_TOKEN')
    reply_token = replyToken
    responseText = googleSearch.googleSearch(text)

    client = linebot.LineBotApi(channelAccessToken)
    message = linebot.models.TextMessage(text = responseText)
    client.reply_message(reply_token, message)

if __name__ == '__main__':
    print('test')