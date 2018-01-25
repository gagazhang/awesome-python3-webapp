import orm
from models import User,Blog,Comment
import asyncio

loop = asyncio.get_event_loop()
async def test():
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop,host='10.4.67.111', port=3306,user='root', password='root',db='awesome')
    #没有设置默认值的一个都不能少
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

async def testBlog():
    await orm.create_pool(loop=loop, host='10.4.67.111', port=3306, user='root', password='root', db='awesome')
    m = Blog(user_id='11',user_name='user_name',user_image="about:blank",
              name="hello",summary="summary",content="content")
    await m.save()

async def testCommment():
    await  orm.create_pool(loop=loop,host='10.4.67.111',port=3306,user='root',
                           password='root',db='awesome')
    m = Comment(blog_id='11',user_id="userId",user_name='userName',
                user_image='about:blank',content="this is comment"
                )
    await m.save()

#把协程丢到事件循环中执行
loop.run_until_complete(testCommment())
