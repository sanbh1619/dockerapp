import unittest

import app


class TestDockerApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        
    def test_save_result(self):
        response = self.app.post('/', data=dict(submit='save', key=2, cache_value='two'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2', response.data)
        self.assertIn(b'two', response.data)
    
    def test_load_value(self):
        self.app.post('/', data=dict(submit='save', key=3, cache_value='three'))
        response = self.app.get('/', data=dict(submit='load', key=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3', response.data)
        self.assertIn(b'three', response.data)
    

if __name__ == '__main__':
    unittest.main()
