from xml.etree.ElementPath import xpath_tokenizer

from playwright.sync_api import sync_playwright
from time import sleep


class LoginPlaywright:

    def __init__(self, name):
        self.name = name

    def fca(self, login, senha, page):
        try:
            page.goto("https://fcagroup.esupplierconnect.com/")
            sleep(5)
            page.frame_locator('id=iFrame1').get_by_role("button", name="ACCEPT ALL").click(force=True)
            sleep(5)
            page.get_by_role("link", name="to remain on eSupplierConnect").click()
            sleep(2)
            page.get_by_text("LOGIN").click()
            sleep(3)
            page.locator('id=userNameInput').fill(login)
            sleep(1)
            page.locator('id=passwordInput').fill(senha)
            sleep(1)
            page.get_by_role("button", name="Sign in").click()
            sleep(5)
            return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False

    def volvo(self, login, senha, page):
        page.goto("https://supplier-portal.volvo.com/login/?brand=volvo")
        sleep(1)
        try:
            page.get_by_placeholder("Enter your user id").fill(login)
            sleep(1)
            page.get_by_placeholder("password").fill(senha)
            sleep(1)
            page.get_by_role("button", name="login").click()
            sleep(8)
            if page.get_by_text("We didn't recognize the username or password you entered. Please try again.").is_visible():
                return False
            else:
                return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False

    def iveco(self, login, senha, page):
        page.goto("https://supplier.ivecogroup.com/supplier/portal/home/index")
        try:
            sleep(1)
            page.get_by_role("link", name="Login").click()
            sleep(1)
            page.get_by_placeholder("UserID").fill(login)
            sleep(0.5)
            page.get_by_placeholder("Password").fill(senha)
            sleep(0.5)
            page.get_by_role("button", name="Login").click()
            sleep(2)
            if page.get_by_text("Login failed").is_visible():
                return False
            else:
                return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False

    def scania(self, page, login, senha):
        page.goto('https://supplier.Scania.com ')
        sleep(1)
        try:
            page.locator('xpath=//*[@id="cn-accept-cookie"]').click()
            sleep(1)
            page.get_by_role("button", name="Login").click()
            sleep(1)
            page.get_by_placeholder("someone@example.com").fill(login)
            sleep(1)
            page.get_by_role("button", name="Next").click()
            sleep(1)
            page.get_by_placeholder("Password").fill(senha)
            sleep(1)
            page.get_by_role("button", name="Sign in").click()
            sleep(2)

            if page.locator("xpath=//button[@name='Next']").is_visible():
                return False
            else:
                return True

        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False

    def marelli(self, login, senha, page):
        page.goto("https://suppliercollaboration.marelli.com/login")
        try:
            page.get_by_placeholder("Username").fill(login)
            sleep(1)
            page.get_by_placeholder("Password").fill(senha)
            sleep(1)
            page.get_by_role("button", name="Login").click()
            sleep(3)
            if page.get_by_role("heading", name="Wrong usename or password").is_visible():
                return False
            else:
                return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False

    def mercedes(self, login, senha, page):
        page.goto("https://supplier.daimlertruck.com/en/")
        sleep(3)
        page.get_by_test_id("uc-accept-all-button").click()

        try:
            page.locator('xpath=/html/body/header/nav/div[1]/div/div[3]/div/div/span/span[1]').click()
            sleep(1)
            page.locator('xpath=/html/body/header/nav/div[1]/div/div[3]/div/div/div/div[1]/a').click()
            sleep(4)
            page.locator('xpath=<button type="button" id="c-p-bn" class="c-bn" zn_id="15">Aceitar todos</button>')
            sleep(2)
            page.get_by_label("User ID").fill("S1QQUALI")
            sleep(1.5)
            page.get_by_role("button", name="Next").click()
            sleep(1.5)
            page.get_by_label("Password").fill("Qualpara23")
            sleep(1.5)
            page.get_by_role("button", name="Log on").click()
            sleep(5)

            if page.locator('xpath=c').is_visible():
                return False
            else:
                return True
        except Exception as erro_login:
            print(f'{self.name} - Erro login: {erro_login}')
            return False



if __name__ == '__main__':
    teste = LoginPlaywright('teste')
    with sync_playwright() as playwright_:
        browser_ = playwright_.chromium.launch(headless=False)
        context_ = browser_.new_context()
        page_ = context_.new_page()
        teste_login = teste.marelli('evsilva@paranoa.com.br', 'Paranoa.123', page_)
        print(teste_login)
