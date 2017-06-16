# -*- coding:utf-8 -*-
import  requests
import  json
import  unittest
##app登陸的接口自動化   Writer  wuxiaopeng
class Login(unittest.TestCase):

    def test_post(self):  ##post请求
        print "post请求"
        get_data = {'country_code': '86', 'phone': '13716556242', 'password': '111111',
                    'signature': ''}  ##这个get_data是请求接口是时，发送的参数
        data = json.dumps(get_data)  ##将请求参数转换为json格式文件
        login_url = "http://testapi.kitty.live/v1/account/login"  ##定义请求的接口url
        reponse = requests.post(url=login_url, data=data)
        print  reponse
        cookies=requests.post(url=login_url, data=data).cookies
        session=cookies.get('session')
        back_json = json.loads(reponse.content)
        print "走到这里了"
        print  back_json
        print (reponse.status_code,type(reponse.status_code))
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(back_json, dict)
        print(back_json.keys())
        exceptkeys = [u'message',u'code',u'user']
        self.assertEqual(sorted(back_json.keys()), sorted(exceptkeys))
        for values in back_json.values():
            print(values)
            account= self.assertNotEqual(values, u"")
            if account=='':
                print "登录失败"
            else:
                print "登录成功"




##执行登陆的方法
if __name__ == '__main__':
    unittest.main()
