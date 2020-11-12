
class RequestDataSource(object):

    def RequestHeader(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        return headers

    def DataSource_Login_Api_Get_Token_GET(self):
        source =  {
            "name": "Admin",
             "pwd": "zjugis1402"
                }

        return source

    def DataSource_Cookies(self):
        cookies = {'ajax_lastNext' : 'on', 'device' : 'desktop' , 'i_ca': '0' ,'keepLogin': 'on' , 'lang': 'zh-cn', 'lastBugModule' : '15', 'lastProduct': '3', 'preBranch': '0' , 'preProductID': '3', 'theme' : 'default', 'za': 'wangbaofeng', 'zjugis.ticket':'4C08401B5E408BE1D80C51F060ABE53B37A48592769BC967DF9351F8872A4CB701414C3252D18BCEF8052532F59D6070BB6F76C3633823CC8D90B3C9EBD260ADF4DABCE8B4A4AF95', 'zp': 'c373d4737f1c0750ab093dfe046602319a76d1c3'}
        return cookies