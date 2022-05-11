# rakuten_api_book

<h2>◆概要◆</h2>
Rakuten Developersの楽天ブック検索APIを活用し、<br>
商品ページまで遷移ができるサイトを構築しました。<br><br>

キーワードを入力し、検索をしたら楽天ブック検索APIに<br>
登録をしている商品を抽出することができます。

商品をクリックした後、商品の商品ページに遷移し、<br>
購入ボタンをクリックしたら商品ページに遷移する仕様になっています。

<h2>◆使用言語◆</h2>
HTML・CSS(Bootstrap)<br>
python(Django)

<h2>◆難しかった点◆</h2>
APIを読み込むことができず、うまく出力できなかった点です。<br>

解決策としては、Rakuten Developersにテスト環境があるので、<br>
URLが正しいかを確認し、正しい情報を変数(SEARCH_URL)に代入し、<br>
解決することができました。<br>
（app/views.py:8行目）

<h3>★検索結果画像★</h3>
<img src="https://user-images.githubusercontent.com/98627989/167808385-5d9cc6c6-9181-40db-8a50-a84cf0a28dab.png" width="300" height="250">

<h3>★商品詳細ページ★</h3>
<img src="https://user-images.githubusercontent.com/98627989/167810900-a7094c0d-86ee-4b71-a177-da3e6dc1bd1e.png" width="300" height="250">


