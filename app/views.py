from django.shortcuts import render
from django.views.generic import View
import json
import requests
from .forms import SearchForm

#楽天APIの書籍情報をSEARCH_URLに代入
SEARCH_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&applicationId=1050309127103218110' # ID変更

#解説1
def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = result['Items']
    return items
#解説1　--ここまで--

class IndexView(View):
    def get(self, request, *args, **kwargs):

        # フォームの内容を取得
        form = SearchForm(request.POST or None)
        
        return render(request, 'app/index.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        # 解説2
        if form.is_valid():
            keyword = form.cleaned_data['title']
            params = {
                'title': keyword,
                'hits': 28,
            }
        #解説2　--ここまで--

        # 解説3
            items = get_api_data(params)
            book_data = []
            for i in items:
                item = i['Item']
                title = item['title']
                image = item['largeImageUrl']
                isbn = item['isbn']
                query = {
                    'title': title,
                    'image': image,
                    'isbn': isbn
                }
                book_data.append(query)
        # 解説3 --ここまで--

            return render(request, 'app/book.html', {
                'book_data': book_data,
                'keyword': keyword
            })

        return render(request, 'app/index.html', {
            'form': 'form'
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):
        isbn = self.kwargs['isbn']
        params = {
            'isbn': isbn
        }

        items = get_api_data(params)
        items = items[0]
        item = items['Item']
        title = item['title']
        image = item['largeImageUrl']
        author = item['author']
        itemPrice = item['itemPrice']
        salesDate = item['salesDate']
        publisherName = item['publisherName']
        size = item['size']
        isbn = item['isbn']
        itemCaption = item['itemCaption']
        itemUrl = item['itemUrl']
        reviewAverage = item['reviewAverage']
        reviewCount = item['reviewCount']

        book_data = {
            'title': title,
            'image': image,
            'author': author,
            'itemPrice': itemPrice,
            'salesDate': salesDate,
            'publisherName': publisherName,
            'size': size,
            'isbn': isbn,
            'itemCaption': itemCaption,
            'itemUrl': itemUrl,
            'reviewAverage': reviewAverage,
            'reviewCount': reviewCount,
            'average': float(reviewAverage) * 20,
        }

        return render(request, 'app/detail.html', {
            'book_data': book_data
        })


#########################コード解説#########################

# ★解説1★

# ◆1-1◆

# api = requests.get(SEARCH_URL, params=params).text

# requests.get()メソッド
# ⇒サーバからHTML、XMLなどの情報を取得するのに使用

# 第一引数
# SEARCH_URL:取得したAPIのURLのページを指す。

# 第二引数
#クエリパラメータ(サーバに情報を送るためにURLの末尾につけ足す文字列)
#を取得している

# ◆1-2◆

# result = json.loads(api)
# ⇒jsonを辞書型配列に変換している

# loads関数:文字列を扱いやすい型に変換

# ◆1-3◆
# items = result['Items']

#楽天APIの商品に格納されているItemsの情報を
# 変数itemsに渡している。

# ★解説2★
# is_valid関数にてフォームのバリデーションを通したら
# form.cleaned_dataでフォームに入力したデータを
# 取得することができる

# ★解説3★
# API に送るパラメータが決まったら、
# API をコールして Json 形式でデータを取得

# リストになっているので、
# ループで回して必要なデータを
# book_dataに格納