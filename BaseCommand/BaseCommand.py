import requests


def BaseCommand(word):

    if word == 'help':
        print("現有功能：\n1.google搜尋，請試著使用 ./google \"關鍵字\" ，將顯示10筆搜尋結果。如想了解詳細設定參數請輸入 --man google 。\n2.stackoverflow搜尋，請試著使用 ./stackoverflow \"關鍵字\" ，將顯示10筆搜尋結果。\n3.圖戰功能，請試著使用 ./imagewar \"關鍵字\" ，將顯示最相關圖片。 \n4.熱門網站導址，請試著使用 ./apple ，將顯示最相似且熱門的導址。")

keyword = input()
BaseCommand(keyword)
