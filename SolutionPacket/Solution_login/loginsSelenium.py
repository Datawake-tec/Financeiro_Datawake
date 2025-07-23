from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
import pyotp

load_dotenv()


class LoginSelenium:

    def __init__(self, name):
        self.name = name

    def get_totp(self, secret):
        totp = pyotp.TOTP(secret)
        return totp.now()

    def login_volks(self, navegador, key, usuario, senha, nome_robo):
        """
        Login Volkswagen: pagina de login da volkswagen
        :param navegador:
        :param key: seguencia de numero para liberar o acesso para passar do login
        :param usuario: usurio do login
        :param senha: senha do login
        :param nome_robo: nome dado par ao robõ
        :return: caso não iniciado a aplicação sera fechada
        """
        try:
            navegador.find_element(By.XPATH, '//*[@id="contentForm:profileIdInput"]').send_keys(usuario)
            sleep(0.5)

            navegador.find_element(By.XPATH, '//*[@id="contentForm:passwordInput"]').send_keys(senha)
            sleep(0.5)

            check = navegador.find_element(By.XPATH, '//*[@id="contentForm:j_idt25"]')
            if check is None:
                navegador.find_element(By.XPATH, '//*[@id="contentForm:j_idt25"]').click()

            else:
                navegador.find_element(By.XPATH, '//*[@id="contentForm:passwordLoginAction"]').click()

            # Aqui está a correção, chamando self.get_totp
            token_ = self.get_totp(key)
            print(token_)

            # Preenche o campo do token para ter acesso ao site
            sleep(2)
            navegador.find_element(By.XPATH, '//*[@id="otp"]').send_keys(token_)
            sleep(0.5)
            navegador.find_element(By.XPATH, '//*[@id="panel-login"]/div/div[2]/form/div/button').click()
            sleep(3)
            return True
        except Exception as erro_login:
            print(nome_robo, erro_login)
            return False

    def login_mercedes(self, navegador, usuario, senha, ):

        try:

            '''sleep(0.5)
            navegador.find_element(By.XPATH,'/html/body/header/nav/div[1]/div/div[3]/div/div/span/span[1]').click()
            sleep(1)
            navegador.find_element(By.XPATH, '/html/body/header/nav/div[1]/div/div[3]/div/div/div/div[1]/a').click()
            sleep(1)'''

            navegador.find_element(By.XPATH, '//*[@id="userid"]').send_keys('S1QQUALI')
            sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="next-btn"]').click()
            sleep(1.5)
            navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys('Qualpara23')
            sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="loginSubmitButton"]').click()
            sleep(6)

            if navegador.find_element(By.ID, '//*[@id="errorLogin"]'):
                return False
            else:
                return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False


    def screenshot(self, navegador, nome_arquivo):
        path = nome_arquivo
        try:
            navegador.save_screenshot(path)
            return path
        except Exception as e:
            print(f""
                  f"{self.name} Erro ao tirar o print: {e}")
            return None
