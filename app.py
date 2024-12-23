import vpn
import send_wpp
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

send_wpp.start_process()
vpn.vpn_process()
send_wpp.msg_connect_vpn()

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

wd = webdriver.Chrome(options=chrome_options)
wd.get('http://ponto.intranet.***.com.br/ForpontoWeb/')
sleep(5)

wait = WebDriverWait(wd, 10)


select_funcionario = wd.find_element(By.ID, 'cmbTipo')
select = Select(select_funcionario)
select.select_by_visible_text("Funcionario")
sleep(1)

user_fpt = wd.find_element(By.ID, 'txtMatricula')
user_fpt.send_keys('1234')
sleep(1)

pass_fpt = wd.find_element(By.ID, 'txtCodConsulta')
pass_fpt.send_keys('1234')
pass_fpt.send_keys(Keys.ENTER)
sleep(5)


button_side_menu = wd.find_element(
    By.XPATH, "//button[@class='navbar-toggle btn-menunav']")
button_side_menu.click()
sleep(1)

efetua_marcacao = wd.find_element(By.XPATH, "//a[@id='mnuMarcacaoWeb']")
efetua_marcacao.click()

sleep (2)

iframe = wd.find_element(By.XPATH, '//*[@id="frmEdicao"]')

wd.switch_to.frame(iframe)

sleep(2)

# cancel_button = wd.find_element(By.XPATH, "//div[@class='pnl-botoes']/a[2]")
# cancel_button.click()

ok_button = wd.find_element(By.ID, "btnOk")
ok_button.click()
sleep(10)

send_wpp.msg_ponto()
vpn.vpn_process()
send_wpp.msg_disconnect_vpn()
send_wpp.end_process()

