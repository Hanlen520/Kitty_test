# -*- coding:utf-8 -*-
import  requests
import  json
import unittest
from Login_check.Login_test import Login
class  TestHot():
    def getHot(cls):
        print "获取Hot页数据"
        params = {'page': 1, 'size': 20}
        get_url="http://testapi.kitty.live/v1/recommand/hot"
        cookles_session = Login.post()
        print "登录后获取的cookles", cookles_session
        headers={'Conten-Type':'application/json;charset=UTF-8','cookie':'session='+cookles_session}
        response=requests.get(url=get_url,params=params,headers=headers)
        print response
        back_json=json.loads(response.content)
        print  back_json
        cls.assertEqual(response.status_code, 200)
        cls.assertIsInstance(back_json, dict)
        print  (back_json.keys())
        ##返回数据中期望的key值
        exceptkeys=[u'show_pos',u'message',u'code',u'recommand_list']



if __name__ == '__main__':
    unittest.main
  # unittest.main