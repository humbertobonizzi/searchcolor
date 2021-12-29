from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_classificar_cores(self):
    #Usuário precisa classificar as cores conforme classificação sazonal
        self.browser.get('http://localhost:8000')

    # O título da página e o cabeçalho mencionam o formulário de classificação
        self.assertIn('Classificação de cores', self.browser.title)
        self.fail('Fim do teste')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

