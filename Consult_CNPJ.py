# Automação de consultas empresariais a partir do CNPJ

from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome()
navegador.get("https://www.consultacnpj.com/cnpj/")
navegador.maximize_window()
t.sleep(5)
cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

for cnpj in cnpjs:
    input = navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div/div/div[2]/div/div/input')
    input.clear()
    input.send_keys(cnpj)
    # input.send_keys(Keys.ENTER) caso fosse necessário, em nosso site não o é.
    t.sleep(3)
    texto = navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div/div[2]')
    with open(f'{str(cnpj)}.csv', 'w', encoding="UTF-8") as csv:
        csv.write(texto.text)
    t.sleep(4)

navegador.quit()
