#e8-1-2查詢個人資料與貼文數/按讚數
import facebook
token = 'EAACEdEose0cBAIdyNZCnXaStiG9OKkYZC5W7YZADwArlt2ZCdbkw4G9ZBAiJ4GPKTwNsmUzaWyHJcvLVXFEFN2iZCFXOZB3Yyy1358nZC9KuKMZBf9FsOUzTktMdRJYyZBciQHZAtArIjygBcQ2EYB8J7q9KOZBWo97FfZCTD1bVxU9ZBB41M6ihYoFZBsqOsKnKcFQBvkZD'
graph = facebook.GraphAPI(access_token = token)
me_info = graph.get_object('me')
print(me_info)
print('我的Facebook名字是：', me_info['name'])
posts = graph.get_connections(id = 'me', connection_name = 'posts')
print ("共有", len(posts['data']), "篇貼文")
for each in posts['data']:
#    if 'likes' in each: 
    print ('時間：', each['created_time'])
#    print ('內容：', each['message'])
#        likes = each['likes']['data'] # 
#        print('共有', len(likes), "個讚，按讚的人：")
#        for each_like in likes:
#            print ('Id:', each_like['id'],'Name:', each_like['name'])#print(posts)
groups = graph.get_connections(id = 'me', connection_name = 'groups')
print ("共有", len(groups['data']), "個社團")
print(groups['data'])


likes=graph.get_connections(id = 'me', connection_name = 'likes')
print ("共有", len(likes['data']), "個粉絲專頁")
for each_like in likes['data']:
    print(each_like['name'])
comments = graph.get_connections(id='1314847538599653_1369502673134139', connection_name='comments')
print ("共有", len(comments['data']), "個評論")
print(comments['data'])
friends = graph.get_connections(id='me', connection_name='friends')
print (friends)

