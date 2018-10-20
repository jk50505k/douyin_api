# douyin_api
提供查看抖音评论，点赞，粉丝的API接口，封装在本地服务器
## 接口文档
|接口地址    |    参数名    |  调用例子  |  返回参数|
| --------   | :------:   | :----: | :----:  |
| /comment/<br>  （视频评论） | aweme_id<br>(视频分享链接)<br>cursor<br>（起始的视频序号) |   http://127.0.0.1:5000/comment/?aweme_id=http://v.douyin.com/dQxxCw/&cursor=0   |  info ：数据 <br>more： 是否有下一页    |
| /favorite/ <br>（用户喜欢的视频）        | user_id<br>(用户主页分享链接) <br> max_cursor<br>(页号，第一页默认为0)     |   http://127.0.0.1:5000/favorite/?user_id=http://v.douyin.com/dv8GHj/&max_cursor=0   |    info： 数据 <br> more ：是否有下一页<br> max_cursor ：下一页的页号    |
| /follower/ <br >(用户的粉丝)        | $user_id<br>(用户主页分享链接)<br> max_time<br>(页号，入口页号默认为1538215804)    |   http://127.0.0.1:5000/follower/?user_id=http://v.douyin.com/dv8GHj/&max_time=1538215804    |     info： 数据 <br> more ：是否有下一页 <br>max_time ：下一页的页号 <br>firstPage:第一页页号   |

## 使用效果
粉丝<br>
![follower ]( https://github.com/jk50505k/douyin_api/blob/master/屏幕快照%202018-10-20%20下午11.41.12.png)
点赞的视频<br>
![favorite ](https://github.com/jk50505k/douyin_api/blob/master/屏幕快照%202018-10-20%20下午11.41.21.png)
评论<br>
![comment](https://github.com/jk50505k/douyin_api/blob/master/屏幕快照%202018-10-20%20下午11.41.28.png)
