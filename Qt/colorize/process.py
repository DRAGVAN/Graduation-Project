import sys
import requests


class Login(object):
    def __init__(self, filename, method):
        self.filename = filename
        self.method = method
        self.id = 'GE6J32T9RFADD1G8UIHGDTKECU9OBJVY'

        # form data
        self.data = {
            'id': self.id,
            'blur': '0',
            'ref': '',
            'line': '',
        }

        self.files = {
            'line': ('file', open(self.filename, 'rb'))
        }

        self.post_url = 'https://petalica.com/v1/post'
  
        self.post_url2 = 'https://petalica.com/v1/paint/' + self.method

        self.get_url = 'https://petalica.com/images/out/'
        self.session = requests.Session()

    # def getId(self):
    #     context = execjs.compile(self.js_from_file('getId.js'))
    #     return context.call('uniqueid')

    def process(self):
        req = self.session.post(self.post_url, files=self.files, data=self.data)
        # id = eval(str(req.content, 'utf-8'))['image_id']
        params = {'id': self.id}
        self.session.post(self.post_url2, data=params)
        url = self.get_url + self.id + '_0.jpg'
        req_get = self.session.get(url)
        # print(req_get.status_code)
        # with open('processed\\' + self.filename, 'wb') as f:
        #     f.write(req_get.content)
        return req_get.content


if __name__ == '__main__':
    # login = Login('D:/Study/Code/Python/Qt/colorize/dataset/1.jpg', '5')
    # print(login.getPic())
    print("hello")

