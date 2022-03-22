# seleniumInCronjob

オークションサイトでの入札作業を自動化するツール

.env設定:
EMAIL=アカウントに使用しているEメール
PASS=パスワード


crontabを利用したスケジュール設定:
```
*/1 * * * * cd /path/to/the/project/folder && /path/to/python /path/to/scraping/file >> /path/to/log/file 2>&1
``` 
