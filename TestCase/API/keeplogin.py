from utils.HTTPRequest.RequestBase import RequestBase
from multiprocessing import Pool
from bs4 import BeautifulSoup
class TestMultiProcessGET(object):

    def __init__(self):
        self.request_base = RequestBase(pattern='z_workflow')
        self.request_base.keep_login_alive()
        print("当前cookies 为  %s" % self.request_base.cookies)

    def request_case_center(self, time):
        print("开启第 %s 次进程" % time)
        request_method = "GET"
        request_data = {"hh": 'ss'}
        api_url = "/HandlerCaseCenter/index"
        req = self.request_base.begin_request(request_data= request_data, request_method=request_method,api_url=api_url, cookies=self.request_base.cookies)
        assert req[0] == 200
        if req :
            print("状态码为%s "  % req[0])
            bs = BeautifulSoup(req[1], 'html.parser')
            all_element = bs.find_all(['li'])
            case_handler = ['<li class="on" data-status="1" z-tabindex="0" z-trigger="1"><a>待办<span lang="NORMAL">0</span></a></li>',
                            '<li data-status="90" z-tabindex="1"><a>已完成<span lang="FINISH">0</span></a></li>',
                            '<li data-status="40" z-tabindex="2"><a>已退回<span lang="CALLBACK">0</span></a></li>',
                            '<li data-status="20" z-tabindex="3"><a>挂起<span lang="HANG_UP">0</span></a></li>',
                            '<li data-status="160" z-tabindex="4"><a>作废<span lang="OBSOLETE">0</span></a></li>',
                            '<li data-status="190" z-tabindex="5"><a>关注<span lang="ATTENTION">0</span></a></li>',
                            '<li data-status="210" z-tabindex="6"><a>抄送<span lang="CC">0</span></a></li>',
                            '<li data-status="260" z-tabindex="7"><a>已督办<span lang="SUPERVISE">0</span></a></li>']
            for i in all_element:
                # case_center必须有的标签如果没有，则表示失败
                assert str(i) in case_handler

    def start_multiprocessing(self, times):
        processing_pool = Pool(times)
        for i in range(times):
            processing_pool.apply(func=self.request_case_center,args=(i,))
        processing_pool.close()
        processing_pool.join()

if __name__ == "__main__":
    test_1 = TestMultiProcessGET()
    test_1.start_multiprocessing(times=20)


