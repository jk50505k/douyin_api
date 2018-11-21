from flask import Flask, g
from flask_restful import reqparse, Api, Resource
from flask_httpauth import HTTPTokenAuth
from comment import *
from favorite import *
from follower import *
from search1 import *
import time
import os
# Flask相关变量声明
app = Flask(__name__)
api = Api(app)

# RESTfulAPI的参数解析 -- put / post参数解析
parser_put = reqparse.RequestParser()

# 操作（post / get）资源列表
class commentTodoList(Resource):#评论

    def get(self):
        try:
            parser_put.add_argument("aweme_id", type=str, required=True, help="error")
            parser_put.add_argument("cursor", type=str, required=True, help="error")
        
            args = parser_put.parse_args()
            aweme_id = args['aweme_id']
            cursor = args['cursor']
            info = {"info": apiComment(getID(aweme_id),cursor )}
            parser_put.remove_argument("aweme_id")
            parser_put.remove_argument("cursor")
            return info, 200
        except:
            parser_put.remove_argument("aweme_id")
            parser_put.remove_argument("cursor")
            return 400


class favoriteTodoList(Resource):#喜欢

    def get(self):
        try:
            parser_put.add_argument("max_cursor", type=str, required=True, help="error")
            parser_put.add_argument("user_id", type=str, required=True, help="error")
            args = parser_put.parse_args()
            user_id = args['user_id']
            max_cursor = args['max_cursor']
            info = {"info": apiFavorite(getParam(user_id),max_cursor)}
            parser_put.remove_argument("max_cursor")
            parser_put.remove_argument("user_id")
            return info ,200
        except:
            parser_put.remove_argument("max_cursor")
            parser_put.remove_argument("user_id")
            return 400
class followerTodoList(Resource):#粉丝

    def get(self):
        try:
            parser_put.add_argument("user_id", type=str, required=True, help="error")
            parser_put.add_argument("max_time", type=str, required=True, help="error")
            args = parser_put.parse_args()
            user_id = args['user_id']
            max_time = args['max_time']
            info = {"info": apiFollower(getParam(user_id),max_time)}
            parser_put.remove_argument("max_time")
            parser_put.remove_argument("user_id")
            return info ,200
        except:
            parser_put.remove_argument("max_time")
            parser_put.remove_argument("user_id")
            return 400

class getaweme_id(Resource):#获取视频id
    def get(self):
        parser_put.add_argument("url", type=str, required=True, help="error")
        args = parser_put.parse_args()
        url = args['url']
        aweme_id={"aweme_id":getID(url)}
        parser_put.remove_argument("url")
        return aweme_id,200

class user_id(Resource):#获取用户id
    def get(self):
        parser_put.add_argument("link", type=str, required=True, help="error")
        args = parser_put.parse_args()
        link = args['link']
        user_id={"user_id":getParam(link)}
        parser_put.remove_argument("link")
        return user_id,200
    
class search(Resource):#搜索关键字
    def get(self):
        try:
            parser_put.add_argument("keyword", type=str, required=True, help="error")
            parser_put.add_argument("offset", type=str, required=True, help="error")
            args = parser_put.parse_args()
            keyword=args['keyword']
            offset=args['offset']
            info={"info":apiSearch(keyword,offset)}
            parser_put.remove_argument("keyword")
            parser_put.remove_argument("offset")
            return info,200
        except:
            parser_put.remove_argument("keyword")
            parser_put.remove_argument("offset")
            return 400
            
        
class index(Resource):#主页
    def get(self):
        return 'This is DouYin API',200

# 设置路由，即路由地址为http://127.0.0.1:5000/
api.add_resource(commentTodoList, "/comment/")
api.add_resource(favoriteTodoList,'/favorite/')
api.add_resource(getaweme_id,'/getid/')
api.add_resource(followerTodoList,'/follower/')
api.add_resource(user_id,'/user/')
api.add_resource(search,'/search/')
api.add_resource(index,'/')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)



