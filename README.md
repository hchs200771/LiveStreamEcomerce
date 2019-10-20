# LiveStreamEcomerce
目標：直播+1可以連結到購買平台

- [工作分派](https://hackmd.io/@ozZXqJH5Q8G53mDL_0Eh5Q/rJwUtmPdr)

## Server environment dependency
1. python3
2. pip install -r requirements.txt
3. docker
4. PostgreSQL

## Deploy to Heroku
可將 repo 裡指定目錄個別 deploy 到 Heroku

1. set remote
```
heroku git:remote -a {your_heroku_app_name}
```

2. push folder
```
git subtree push --prefix {your_folder} heroku master
```
