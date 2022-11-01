
class Response:
    def __init__(self, resp):
        r = resp.json()
        self.code = resp.status_code
        self.msg = r.get('msg', '')
        self.flag = r.get('flag', False)
        self.data = r.get('data', '')


def assert_success_response(resp):
    response = Response(resp)
    assert response.msg == '操作成功'
    assert response.flag == True
    assert response.code == 200
