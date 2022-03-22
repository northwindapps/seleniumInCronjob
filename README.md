# seleniumInCronjob

オークションサイトでの入札作業を自動化するツール

<h3>(1).env設定:</h3>

EMAIL=アカウントに使用しているEメール

PASS=パスワード


<h3>(2)crontabを利用したスケジュール設定:</h3>

```
*/1 * * * * cd /path/to/the/project/folder && /path/to/python /path/to/scraping/file >> /path/to/log/file 2>&1
``` 
