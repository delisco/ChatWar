import hug
import Search.googleSearch as googleSearch
import json
import linebot
import base64
import hashlib
import hmac

CHANNEL_ACCESS_TOKEN = 'Myk71sup6Hpu/KZ/9bAgUCiE0u//EolU3I6Exwx7JvlsJN4SRu3YCEASV16nGAwqEic+PGc+uutjC+uLYEZQ04ERYwbmROkvUFcrMUICu6ndEP1EioNzdQtbk/kRMR7PQeatI5aOg+ApNlKqqbRSrQdB04t89/1O/w1cDnyilFU='

class MessageResponse(object):
    messageType = ''
    messageText = ''

    def __init__(self, responseType = 'text', responseText = 'test'):
        self.messageType = responseType
        self.messageText = responseText

@hug.post('/googleSearch')
def googleSearchFunction(body):
    print(body)
    client = linebot.LineBotApi(CHANNEL_ACCESS_TOKEN)
    reply_token = body['events'][0]['replyToken']
    message = MessageResponse('text', body['chat-war'][0]['message']['text'])
    client.reply_message(reply_token, message)

if __name__ == '__main__':
    print('test')