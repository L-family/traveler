# traveler_end
> A Python project.
# Software
node : v8.11.2  
npm : 6.1.0  
vue : 2.9.6  
2018.9.21
   app初始化
   usermanage  用户管理
   base        旅居基地
   specialty   特产服饰、衣物
   news        新闻、小提示
2018.9.26   数据库设计
1.user
id-p,phone,password,profile(头像),status(状态),address,name(昵称)
2.base基地
id,name,address,phone,price,introduce,detail(.txt),picture
3.base-pict
id,baseid,picture
4.base-user
id,baseid,userid,status
5.specialty
id,name,birthpalace,picture,price,detail(.txt),mark(特产/服饰）
6.spec-pict
id,specid,picture
7.spec-user-cart
id,userid,specid,status,number
8.spec-user-star
id,id,userid,specid,status,
9.news
id,title,detail,mark(养生/文体艺术/笑道),picture
10.news-picture
id.newsid,picture
11.news-user
id,newsid,userid,status
