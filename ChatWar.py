import base64
import Config.Config as config
import hashlib
import hmac
import hug
import json
import linebot
import Search.googleSearch as googleSearch

con = config.Config()

@hug.post('/googleSearch')
def googleSearchFunction(body):
    channelAccessToken = con.get('chatWar', 'CHANNEL_ACCESS_TOKEN')
    reply_token = body['events'][0]['replyToken']
    text = googleSearch.googleSearch(body['events'][0]['message']['text'])

    client = linebot.LineBotApi(channelAccessToken)
    message = linebot.models.TextMessage(text = text)
    client.reply_message(reply_token, message)

if __name__ == '__main__':
    print('test')