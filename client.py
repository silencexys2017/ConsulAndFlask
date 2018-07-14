# -*- coding: utf-8 -*-
from consulclient import ConsulClient
import requests
#请求rest api 实例
class HttpClient():
    #指定consul 服务的主机，端口，以及所要请求的应用民
    def __init__(self,consulhost,consulport,appname):
        self.consulhost=consulhost
        self.consulport=consulport
        self.appname=appname
        self.consulclient=ConsulClient(host=self.consulhost,port=self.consulport)
    def request(self):
        serviceList = self.consulclient.getService(self.appname)
        serviceList1 = self.consulclient.getServices()
        #scrapyMessage=requests.get('http://'+host+':'+str(port)+'/'+self.appname).text
        print serviceList 
        print serviceList1
        
if __name__=='__main__':
    client=HttpClient('10.63.15.47','8500','xiaoyongsheng2')
    client.request()

