# -* -coding:utf-8 -*-
from multiprocessing import Process
from histar.processor.baidu.worker import BaiduWork
from histar.processor.sina.worker import SinaWork
from histar.processor.qq.worker import QQWork
from histar.processor.xinhua.worker import XinhuaWork
from histar.processor.toutiao.worker import ToutiaoWork
from histar.processor.people.worker import PeopleWork
from histar.processor.mxh.worker import MXHWork
from histar.processor.qhtv.worker import QHTVWork
from histar.processor.chinanews.worker import ChinaNewsWork
from histar.processor.cntv.worker import CNTVWork, CNTVStarImageWork
from histar.processor.huabian.worker import HuabianWork
from histar.processor.szhk.worker import SZHKWork

if __name__ == '__main__':
    worker_list = []
    worker_list.append( ToutiaoWork(allow_request_count=100) ) #今日头条
    worker_list.append( XinhuaWork(past_news_need=True, page_limit=True, total_page_count=5) ) #今日头条
    worker_list.append( QQWork('http://ent.qq.com/c/wbbl', page_limit=True, total_page_count=6) )
    worker_list.append( QQWork('http://ent.qq.com/c/mxzx', page_limit=True, total_page_count=6) )
    worker_list.append( QQWork('http://ent.qq.com/c/dlxw', page_limit=True, total_page_count=6) )
    worker_list.append( QQWork('http://ent.qq.com/c/omxwn', page_limit=True, total_page_count=6) )
    worker_list.append( QQWork('http://ent.qq.com/c/txdj', page_limit=True, total_page_count=6) )
    
    worker_list.append( SinaWork(lid=1244,pageid=107, total_page_count=10) )
    worker_list.append( SinaWork(lid=1245,pageid=107, total_page_count=10) )
    worker_list.append( SinaWork(lid=1246,pageid=107, total_page_count=10) )
    worker_list.append( SinaWork(lid=1247,pageid=107, total_page_count=10) )
    worker_list.append( SinaWork(lid=1248,pageid=107, total_page_count=10) )
    worker_list.append( SinaWork(lid=1249,pageid=107, total_page_count=10) )
    
    worker_list.append( SinaWork(lid=54  ,pageid=108, total_page_count=10) )
    worker_list.append( SinaWork(lid=1251,pageid=108, total_page_count=10) )
    worker_list.append( SinaWork(lid=1252,pageid=108, total_page_count=10) )
    worker_list.append( SinaWork(lid=1253,pageid=108, total_page_count=10) )
    worker_list.append( SinaWork(lid=1254,pageid=108, total_page_count=10) )
    worker_list.append( SinaWork(lid=1255,pageid=108, total_page_count=10) )
    
    worker_list.append( BaiduWork(cmd=4, channel_name='star' ) )
    worker_list.append( BaiduWork(cmd=4, channel_name='star_chuanwen' ) )
    worker_list.append( BaiduWork(cmd=4, channel_name='star_gangtai' ) )
    worker_list.append( BaiduWork(cmd=4, channel_name='star_neidi' ) )
    worker_list.append( BaiduWork(cmd=4, channel_name='star_oumei' ) )
    worker_list.append( BaiduWork(cmd=4, channel_name='star_rihan' ) )
    worker_list.append( PeopleWork() )
    worker_list.append( MXHWork(total_page_count=10) )
    worker_list.append( QHTVWork(total_page_count=5) )
    worker_list.append( SZHKWork() )
    worker_list.append( ChinaNewsWork(total_page_count=5) )
    worker_list.append( HuabianWork(total_page_count=5) )
    worker_list.append( CNTVWork() )
    worker_list.append( CNTVStarImageWork() )
    for worker in worker_list:
        p = Process(target=worker)
        p.start()
        #p.join()
        print 'all is done'