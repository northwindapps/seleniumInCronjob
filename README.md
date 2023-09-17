# seleniumInCronjob

オークションサイトでの入札作業を自動化するツール
<h5>機能概要:wishlist.pyで入札アイテムを取得→bid.pyで入札を実行</h5>

<h3>(1).env設定:</h3>

EMAIL=アカウントに使用しているEメール

PASS=パスワード


<h3>(2)crontabを利用したスケジュール設定:</h3>

```
*/1 * * * * cd /path/to/the/project/folder && /path/to/python /path/to/scraping/file >> /path/to/log/file 2>&1
``` 

app.py

start: gunicorn app:app
ps aux |grep gunicorn | awk '{ print $2 }' |xargs kill -HUP
sudo gunicorn  wsgi

