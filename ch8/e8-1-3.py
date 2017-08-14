#e8-1-3取得按讚的粉絲團
import facebook
token = 'EAACEdEose0cBAIdyNZCnXaStiG9OKkYZC5W7YZADwArlt2ZCdbkw4G9ZBAiJ4GPKTwNsmUzaWyHJcvLVXFEFN2iZCFXOZB3Yyy1358nZC9KuKMZBf9FsOUzTktMdRJYyZBciQHZAtArIjygBcQ2EYB8J7q9KOZBWo97FfZCTD1bVxU9ZBB41M6ihYoFZBsqOsKnKcFQBvkZD'
graph = facebook.GraphAPI(access_token = token)
posts = graph.get_connections(id = 'me', connection_name = 'posts')
print ("共有", len(posts['data']), "篇貼文")
for index, each in enumerate(posts['data']):
    print("#", index+1)
    print('時間: ', each['created_time'])
#        print('使用者: ', each['from']['name'])
    if 'story' in each:
        print('描述: ', each['story'])
    if 'message' in each:
        print('內容：', each['message'])
    print('------------------------------------------')


