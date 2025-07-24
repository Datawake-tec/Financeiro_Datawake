from playwright.sync_api import sync_playwright
from time import sleep


class LoginPlaywright:

    def __init__(self, name):
        self.name = name

    def login_prothues(self, login, senha, page):
        try:
            page.goto("http://192.168.0.31:16000/webapp/")
            sleep(5)
            page.frame_locator("iframe").get_by_placeholder("Ex. sp01\\nome.sobrenome").click()
            page.frame_locator("iframe").get_by_placeholder("Ex. sp01\\nome.sobrenome").fill(login)

            page.frame_locator("iframe").get_by_label("Insira sua senha").click()
            page.frame_locator("iframe").get_by_label("Insira sua senha").fill(senha)
            sleep(2)
            page.frame_locator("iframe").get_by_role("button", name="Entrar").click()
            sleep(8)
            page.locator("iframe").content_frame.get_by_role("textbox", name="Grupo").fill("17")
            sleep(2)
            page.locator("iframe").content_frame.get_by_role("button", name="Entrar").click()
            sleep(1)

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
        teste_login = teste.login_prothues('gmelo', 'DW.2025', page_)
        print(teste_login)
