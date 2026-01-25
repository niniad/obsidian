# 依頼
Google CloabolatoryでSP-APIからGET_SALES_AND_TRAFFIC_REPORTのレポートを取得するプログラムのコードを書いてください。
レスポンスごとにブロックを分けてください。

# APIデータモデル概要
以下の順にAPIリクエストを実行することでデータを取得できる。
Step 1: create Report（POST)
Step 2: get Report（GET）
Step 3: get Report Document（GET）
# postman検証済みソースコードとレスポンス（python版)
## 変数設定
以下はgoogle colaboの環境変数に設定
client_id
client_secret
client_secret

以下はgoogle colaboのフォームで都度指定。
dataStartTime
dataEndTime
## create Report
### リクエスト

```
import requests
import json

url = "https://sellingpartnerapi-fe.amazon.com/reports/2021-06-30/reports"

payload = json.dumps({
  "marketplaceIds": [
    "A1VC38T7YXB528"
  ],
  "reportType": "GET_SALES_AND_TRAFFIC_REPORT",
  "dataStartTime": "2025-06-17T00:00:00.000Z",
  "dataEndTime": "2025-06-18T00:00:00.000-00:00",
  "reportOptions": {
    "dateGranularity": "DAY",
    "asinGranularity": "CHILD"
  }
})
headers = {
  'Content-Type': 'application/json',
  'x-amz-access-token': 'Atza|IwEBIG-u9ah-CoV8UHhi0f0vJRH35h8DHNfPzHrcTtfn_lZtUqWAWl9dmJOrYX2402NJrYIcOsrJf290hANMnq3n1YgmaKH0M8SiLxkv-M5vAoIJ7fqShB-tLYmBDxMAkcTOlEwprjZf_Y0DL_oCrzKZVgyLBB5LJQrvKRXc3v44JDalGt4mAZsYIyFJ8E3RSN5_36HtZQwIlSe84E8xRUD3FD0afaHahGytCHDJ1NDaYjU7_eqx7Xe5dbTyT7p4g0J6IRazABa4FZyMB8R4NNbEDT6g2dPlnImDZGrrOa4DfD-6-8VeCD_8KWT2s5v4afJLQd2GITX6Sdhqbo2p0972mYwqixT-ZzfnMn6pxIgyyhSNwA',
  'Cookie': 'session-id=133-7962032-2117249; session-id-time=2384280225l; session-token=o524zo2VbDL6n8+3xHZL35zhAqKF1WQet7T52utA5sjOGmyVWw4U/stwLhEEp9tQZ5qXcV68wTzAGL4dq79pBvuvL/1psBp0kZXQCUMCuMQ/QqsyodXWMyDW6S8St3qLgERiUg27AVQhCAEZvO98jDdI5+mXvn2D3Kr2giUFGjOEfpGJhs4g8SsOAHSB4pXinHhkpfb3sD624UKb9xnngFKi7oKhvdXnlBrukWMDAlEO4HJ8lv4HBYRVZjubm0gvpq0S6m2tWKt8lacQ+nY1wL5MIoVT9VsFUisLvwzeglAomeNCXWXE48ifCqXz4nleM/UJmN50bmjoR193KQ+A8tguluHjLiZe; ubid-main=131-1575605-8988613'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### レスポンス

```
{
    "reportId": "79805020382"
}
```
## get Report
### リクエスト
```
import requests

  

url = "https://sellingpartnerapi-fe.amazon.com/reports/2021-06-30/reports/79805020382"

  

payload = {}

headers = {

  'x-amz-access-token': 'Atza|IwEBIG-u9ah-CoV8UHhi0f0vJRH35h8DHNfPzHrcTtfn_lZtUqWAWl9dmJOrYX2402NJrYIcOsrJf290hANMnq3n1YgmaKH0M8SiLxkv-M5vAoIJ7fqShB-tLYmBDxMAkcTOlEwprjZf_Y0DL_oCrzKZVgyLBB5LJQrvKRXc3v44JDalGt4mAZsYIyFJ8E3RSN5_36HtZQwIlSe84E8xRUD3FD0afaHahGytCHDJ1NDaYjU7_eqx7Xe5dbTyT7p4g0J6IRazABa4FZyMB8R4NNbEDT6g2dPlnImDZGrrOa4DfD-6-8VeCD_8KWT2s5v4afJLQd2GITX6Sdhqbo2p0972mYwqixT-ZzfnMn6pxIgyyhSNwA',

  'Cookie': 'session-id=133-7962032-2117249; session-id-time=2384280225l; session-token=o524zo2VbDL6n8+3xHZL35zhAqKF1WQet7T52utA5sjOGmyVWw4U/stwLhEEp9tQZ5qXcV68wTzAGL4dq79pBvuvL/1psBp0kZXQCUMCuMQ/QqsyodXWMyDW6S8St3qLgERiUg27AVQhCAEZvO98jDdI5+mXvn2D3Kr2giUFGjOEfpGJhs4g8SsOAHSB4pXinHhkpfb3sD624UKb9xnngFKi7oKhvdXnlBrukWMDAlEO4HJ8lv4HBYRVZjubm0gvpq0S6m2tWKt8lacQ+nY1wL5MIoVT9VsFUisLvwzeglAomeNCXWXE48ifCqXz4nleM/UJmN50bmjoR193KQ+A8tguluHjLiZe; ubid-main=131-1575605-8988613'

}

  

response = requests.request("GET", url, headers=headers, data=payload)

  

print(response.text)
```
### レスポンス
```
{

    "reportType": "GET_SALES_AND_TRAFFIC_REPORT",

    "processingEndTime": "2025-10-21T12:00:55+00:00",

    "processingStatus": "DONE",

    "marketplaceIds": [

        "A1VC38T7YXB528"

    ],

    "reportDocumentId": "amzn1.spdoc.1.4.fe.6d476c8a-c1f5-4548-b367-6074f88fb16f.T8CPZ9JQS0RKL.44900",

    "reportId": "79805020382",

    "dataEndTime": "2025-06-18T00:00:00+00:00",

    "createdTime": "2025-10-21T12:00:45+00:00",

    "processingStartTime": "2025-10-21T12:00:50+00:00",

    "dataStartTime": "2025-06-17T00:00:00+00:00"

}
```
## get Report Document
### リクエスト
```
import requests

  

url = "https://sellingpartnerapi-fe.amazon.com/reports/2021-06-30/documents/amzn1.spdoc.1.4.fe.6d476c8a-c1f5-4548-b367-6074f88fb16f.T8CPZ9JQS0RKL.44900"

  

payload = {}

headers = {

  'x-amz-access-token': 'Atza|IwEBIG-u9ah-CoV8UHhi0f0vJRH35h8DHNfPzHrcTtfn_lZtUqWAWl9dmJOrYX2402NJrYIcOsrJf290hANMnq3n1YgmaKH0M8SiLxkv-M5vAoIJ7fqShB-tLYmBDxMAkcTOlEwprjZf_Y0DL_oCrzKZVgyLBB5LJQrvKRXc3v44JDalGt4mAZsYIyFJ8E3RSN5_36HtZQwIlSe84E8xRUD3FD0afaHahGytCHDJ1NDaYjU7_eqx7Xe5dbTyT7p4g0J6IRazABa4FZyMB8R4NNbEDT6g2dPlnImDZGrrOa4DfD-6-8VeCD_8KWT2s5v4afJLQd2GITX6Sdhqbo2p0972mYwqixT-ZzfnMn6pxIgyyhSNwA',

  'Cookie': 'session-id=133-7962032-2117249; session-id-time=2384280225l; session-token=o524zo2VbDL6n8+3xHZL35zhAqKF1WQet7T52utA5sjOGmyVWw4U/stwLhEEp9tQZ5qXcV68wTzAGL4dq79pBvuvL/1psBp0kZXQCUMCuMQ/QqsyodXWMyDW6S8St3qLgERiUg27AVQhCAEZvO98jDdI5+mXvn2D3Kr2giUFGjOEfpGJhs4g8SsOAHSB4pXinHhkpfb3sD624UKb9xnngFKi7oKhvdXnlBrukWMDAlEO4HJ8lv4HBYRVZjubm0gvpq0S6m2tWKt8lacQ+nY1wL5MIoVT9VsFUisLvwzeglAomeNCXWXE48ifCqXz4nleM/UJmN50bmjoR193KQ+A8tguluHjLiZe; ubid-main=131-1575605-8988613'

}

  

response = requests.request("GET", url, headers=headers, data=payload)

  

print(response.text)
```
### レスポンス
```
{

    "reportDocumentId": "amzn1.spdoc.1.4.fe.6d476c8a-c1f5-4548-b367-6074f88fb16f.T8CPZ9JQS0RKL.44900",

    "compressionAlgorithm": "GZIP",

    "url": "https://tortuga-prod-fe.s3-us-west-2.amazonaws.com/6d476c8a-c1f5-4548-b367-6074f88fb16f.amzn1.tortuga.4.fe.T8CPZ9JQS0RKL?response-content-encoding=identity&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251021T120102Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=AKIAX3R62LVBLSQALJU5%2F20251021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=2024485b2bc3fc3b3c17939bda7ca5177e31a94ab4b60eabdbb5048756fc334b"

}
```

79816020382