import requests
import unittest


def checkReq():
  r = requests.get('http://localhost:5000/')
  return r


class TestHelloWorld(unittest.TestCase) :

  def test_retcode(self):
    req = checkReq()
    self.assertEqual(req.status_code,200)

  def test_helloworld(self):
    req = checkReq()
    self.assertEqual(req.text,'Hello World!')


if __name__ == '__main__':
  unittest.main()
