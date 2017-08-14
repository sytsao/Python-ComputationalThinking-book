#e8-1-1 利用facebook Graph API貼文
import facebook
token = 'EAACEdEose0cBAHSKgqYqC3s1jEsiHo0EsyFYeWwgfC851WGYr6vaVLDDiv2f5R7qS5Sc7Lw8MrnvWhJIAlIhTYfFgAoO7SCMrxj1ZB7zrP9jtRSc8NiYT78ZAOOkDzPKtY0GgSA5pp0XaBmrcpLB2EwOGKqB6Tg9Tyo7lj9UvqkS4GDhdjU1jdx0nNhGoZD'
graph = facebook.GraphAPI(access_token = token)
graph.put_object("me", "feed", message='Hello')
