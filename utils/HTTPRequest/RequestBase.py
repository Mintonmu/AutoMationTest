from config.globalVars import G
import requests
from .RequestDataSource import RequestDataSource
from logFile.logger import Logger

RequestDataSource = RequestDataSource()


class RequestBase(object):
    def __init__(self, *args, **kwargs):
        self.ip = kwargs.get("ip") if kwargs.get("ip") else G.Server_IP
        self.port = kwargs.get("port") if kwargs.get("port") else G.Server_Port
        self.body_type = kwargs.get("body_type") if kwargs.get("body_type") else "form"
        self.pattern = kwargs.get("pattern")
        self.auth = None
        self.logger = Logger()
        self.cookies = kwargs.get("cookies") if kwargs.get("cookies") else RequestDataSource.DataSource_Cookies()
        self.session = None

    @staticmethod
    def remake_form(data):
        """

        :param data: 请求数据 字典形式
        :return: 重组为form表单的请求body
        """
        assert type(data) is dict
        remake_data = dict()
        for i in data:
            remake_data[i] = (None, data[i])
        return remake_data

    def auth_check(self, data):
        if self.auth:
            """
            目前平台API均未加密，暂时不定义
            """
            pass
        else:
            ticket = G.Server_Checking_ticket
            for i in ticket:
                data[i] = ticket[i]
        return data

    def remake_url(self, api_url):
        return "http://" + self.ip + ":"+ str(self.port) + "/" + self.pattern + api_url

    def begin_request(self, *args, **kwargs):
        request_data = kwargs.get("request_data")
        request_method = kwargs.get("request_method")
        request_header = kwargs.get("request_header")
        api_url = kwargs.get("api_url")
        request_url = self.remake_url(api_url)
        cookies = kwargs.get("cookies") if kwargs.get("cookies") else None
        self.auth = kwargs.get("auth") if kwargs.get("auth") else None
        if request_data:
            request_data = self.remake_form(data=request_data)
            request_data = self.auth_check(request_data)
        self.logger.info("本地请求HEADER为 %s " % request_header )
        self.logger.info("本次请求URL为%s " % request_url)
        self.logger.info("本次请求方式为%s " % request_method)
        req = requests.request(method=request_method.upper(), url=request_url, files=request_data, headers= request_header, cookies=cookies)
        if req:
            print(requests.utils.dict_from_cookiejar(req.cookies))
            return req.status_code, req.text, req.headers

    def keep_login_alive(self):

        # 需要登录请求的API的需要先调用本方法，后续请求参数中加入cookies = self.cookies
        request_data = {"username" :"Admin",
                        "password": "zjugis1402!"}

        url = "http://" + self.ip + ":" + str(self.port)+"/z_user_org_right/Login/index"
        request_method = "POST"
        self.session = requests.Session()
        self.begin_request(request_method=request_method, request_data=request_data, api_url=url)




class ZUserOrgRight(RequestBase):
    """
    各模块区分，继承至RequestBase
    一个接口一个方法，同一个接口不同的方式也分开定义
    函数定义方式为url中的/替换为_,最后_加上请求方式
    """

    def Login_Api_Get_Token_GET(self, *args, **kwargs):
        request_header = kwargs.get("request_header") if kwargs.get(
            "request_header") else RequestDataSource.RequestHeader()

        request_method = "GET"

        request_data = kwargs.get("request_data") if kwargs.get("request_data") else RequestDataSource.DataSource_Login_Api_Get_Token_GET()

        request_api = "/LoginApi/getToken"

        auth = kwargs.get("auth") if kwargs.get("auth") else None

        cookie = kwargs.get("cookie") if kwargs.get("cookie") else None

        return self.begin_request(request_method=request_method,request_data=request_data, request_header=request_header, api_url= request_api,
                            auth=auth)

