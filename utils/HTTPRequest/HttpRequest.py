import requests
import json
import base64
import uuid
from requests.auth import HTTPBasicAuth
from config.globalVars import G
from logFile.logger import Logger
from utils.Others.TimeOperation import datetime_strftime

log = Logger("DEBUG")


def httprequest(api_url, request_data, request_method, *args, **kwargs):
    auth = kwargs.get("auth")
    request_url = "http://" + G.Server_IP + ":" + str(G.Server_Port) + api_url
    if auth:
        Username = G.Server_Checking_Username
        Password = G.Server_Checking_password
        data = dict()
        for i in request_data:
            data[i] = (None, request_data[i])
        req = requests.request(request_method.upper(), url=request_url, files=request_data,
                               auth=HTTPBasicAuth(Username, Password))
        log.info("本次请求API为%s" % request_url)
        log.info("本次请求方式为 %s" % request_method)
        log.info("本次请求内容为%s " % request_data)
        log.info("本次请求认证方式为%s" % auth)

    else:
        if request_data:
            assert type(request_data) is dict
            data = G.Server_Checking_ticket
            for i in request_data:
                data[i] = (None, request_data[i])
            req = requests.request(request_method.upper(), url=request_url, files=data)
            log.info("本次请求API为%s" % request_url)
            log.info("本次请求方式为 %s" % request_method)
            if len(str(data)) <200:
                log.info("本次请求内容为%s " % data)
            else:
                log.info("本次请求内容为%s 内容过长不打印" % str(data)[:200])
        else:
            req = requests.request(request_method.upper(), url=request_url)
    if req:
        log.info("本次请求状态码为%d" % req.status_code)
        return req.status_code, req.text, req.headers

    else:
        return

def uploadFileToServer(filepath ):
    request_url = "http://"+G.Server_IP +":"+ str(G.Server_Port) + G.UploadFileAPI

    with open(filepath, 'rb') as f :
        base64data = base64.b64encode(f.read())
        img_uuid = ''.join(str(uuid.uuid1()).split("-"))
        fileInfo = {

        "fileName": "%s_%s.png" % (datetime_strftime(),filepath.split("/")[-1]),

        "fileInitialName": "%s_%s.png" % (datetime_strftime(),filepath.split("/")[-1]),

        "belongCatalogId": img_uuid,

        "fileChunkId": img_uuid,

        "fileSuffix":"txt",

        "fileContentStr": base64data.decode("utf-8")}

    request_data = {
        'catalogNameList': '["Testing", "AutoMation"]',
        'fileInfo': json.dumps(fileInfo),
    }
    data = G.Server_Checking_ticket
    for i in request_data:
        data[i] = (None, request_data[i])
    req = requests.request("POST", url=request_url, files=data)
    if req:
        body = json.loads(req.text)
        if req.status_code == 200 and "id" in req.text:
            log.info("文件上传状态码为%s " % req.status_code)
            log.info("文件上传Response Header为 %s " % req.headers)
            log.info("文件上传Response Body为%s " % req.text )
            imgid = body["id"]
            G.now_case_img_url = "http://"+G.Server_IP+":"+ str(G.Server_Port)+"/z_file_management/FileInfo/getFileById?id="+imgid



if __name__ == "__main__":
    uploadFileToServer(filepath='../../report/20201110-155738_test_loginPlatform.png')