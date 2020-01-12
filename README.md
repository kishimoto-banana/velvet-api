# velvet-api

はてなブログのはてなブックマーク（以下はてブ）数を予測するAPIです。

## 使用方法

### エンドポイント
- GET

```
/v1/prediction
```

### パラメータ
- url: 予測したいはてなブログのURL

### リクエスト例
```
/v1/prediction?url=https://pompom168.hatenablog.com/entry/2019/12/22/002407
```

## ローカルでの実行方法

以下は一時的な手順です。変更される可能性があります。

- リポジトリのclone
- モデルファイルの配置
  - 以下の4つのファイルをダウンロードして、 `models/` 以下の置いてください
    - https://velvet-public.s3-ap-northeast-1.amazonaws.com/classifier.pkl
    - https://velvet-public.s3-ap-northeast-1.amazonaws.com/regression.pkl
    - https://velvet-public.s3-ap-northeast-1.amazonaws.com/svd.pkl
    - https://velvet-public.s3-ap-northeast-1.amazonaws.com/vectorizer.pkl
- アプリケーションの実行
```bash
$ docker-compose up -d
```
- レスポンスの確認
```bash
$ curl http://localhost:8080/v1/prediction\?url=https://pompom168.hatenablog.com/entry/2019/12/22/002407
```
