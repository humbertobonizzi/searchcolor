from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_classificar_cores(self):
        #Usuário precisa classificar as cores conforme classificação sazonal
        self.browser.get('http://localhost:8000')

        #Cabeçalho que contém as cores para serem classificadas
        header_text = self.browser.find_element_by_tag_name('h1').text        
        self.assertIn('Nomes das cores', header_text)

        #Insere um tipo de coloração sazonal para a cor
        #A página é atualizada exibindo a lista classificada
        select_box = self.send_keys('Outono')
        select_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == 'Outono' for row in rows)
        )

        self.fail('Fim do teste')

if __name__ == '__main__': 
    unittest.main(warnings='ignore')

