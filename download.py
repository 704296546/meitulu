# def test(range_i):
#     for i in range(range_i):
#         yield i
#     yield test2(i)
# def test2(i):
#     yield i
#
# t=test(10)
# for i in t:
#     print (i,end=' ')

# import os
#
# pp_dir = r'G:\sweety\girl\image\夏美酱\[YouMi尤蜜荟] Vol.270 性感女神@王雨纯透视内衣写真[65]\65.jpg'
# print(os.path.exists(pp_dir))


# import  pymongo
#
# myclient = pymongo.MongoClient('localhost', 27017)
# dd = myclient['sexsywomen']['test1']
# for i in range(10):
#     dd.update_one({'value': {'j': i}}, {'$set':{'value': {'j': i}}}, True)
# myclient.close()

# ff = open(r'G:\sweety\girl\image\夏美酱\1.txt', 'r')
# strname = ff.read().replace('\n','').replace(' ','').split(',')
# strname.sort()
# jk = 0
# for i in strname:
#     jk = jk + 1
#     print(i,jk)


site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))