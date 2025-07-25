import os
import shutil
from time import sleep
from SolutionPacket.Solution_login import LoginPlaywright
from playwright.sync_api import sync_playwright


nome_robo = 'Conta a Pagar - '
login = LoginPlaywright(nome_robo)

caminho_pasta_robo = os.path.join(os.getcwd(), 'Excel_proteus')
pasta_arquivo = rf'C:\temp'



def run_protheus(page_):
    try:
        sleep(5)
        page_.get_by_text("Consultas (3)").click()
        sleep(2)
        page_.get_by_text("• Posição de Títulos a Pagar").click()
        sleep(1)
        #page_.get_by_role("button", name="Confirmar").click()
        sleep(9)

        try:
            page.get_by_role("button", name="Filtrar").click()
            sleep(0.5)
            page.get_by_role("button", name="Filtrar").click()
            sleep(3)
        except Exception as e:
            print(e)
            page.get_by_role("button", name="Filtrar").click()
            sleep(0.5)
            page.get_by_role("button", name="Filtrar").click()
            sleep(3)

        try:
            page.get_by_role("button", name="Criar Filtro").click()
            sleep(3)
        except Exception as e:
            print(e)
            page.get_by_role("button", name="Criar Filtro").click()
            sleep(3)


        try:
            page.locator("#COMP7534").get_by_role("combobox").select_option("11") # Vencimento
        except Exception as e:
            print(e)
            page.locator("#COMP7534").get_by_role("combobox").select_option("11")  # Vencimento
        sleep(3)


        try:
            page.locator("#COMP7537").get_by_role("combobox").select_option("21") # Proxima data X
        except Exception as e:
            print(e)
            page.locator("#COMP7537").get_by_role("combobox").select_option("21")  # Proxima data X
        sleep(3)

        try:
            page.locator("#COMP7541").get_by_role("button").click() #
            sleep(1)
            page.get_by_role("button", name="3", exact=True).click()
            sleep(1)
            page.get_by_role("button", name="OK").click()
            sleep(3)
        except Exception as e:
            print(e)
            page.locator("#COMP7541").get_by_role("button").click() #
            sleep(1)
            page.get_by_role("button", name="3", exact=True).click()
            sleep(1)
            page.get_by_role("button", name="OK").click()
            sleep(3)


        page.get_by_role("button", name="Adicionar").click()
        sleep(1)
        page.get_by_role("button", name="Salvar").click()
        sleep(4)

        try:
            page.locator("label").filter(has_text="Vencimento Próximos 3 Dias").dblclick()
            page.get_by_role("checkbox", name="check_box_outline_blank Vencimento Próximos 3 Dias").check()
            sleep(2)
        except Exception as e:
            print(e)
            page.locator("label").filter(has_text="Vencimento Próximos 3 Dias").dblclick()
            sleep(2)

        try:
            page.get_by_role("button", name="Aplicar filtros selecionados").click()
            sleep(5)
        except Exception as e:
            print(e)
            page.get_by_role("button", name="Aplicar filtros selecionados").click()
            sleep(5)

        try:
            page.get_by_role("button", name="Outras Ações").click()
            sleep(3)
            page.get_by_text("Imprimir Browse").click()
            sleep(3)
        except Exception as e:
            print(e)
            page.get_by_role("button", name="Outras Ações").click()
            sleep(3)
            page.get_by_text("Imprimir Browse").click()
            sleep(3)

        try:
            page.get_by_role("button", name="Planilha").click()
            sleep(2)
            page.locator("#COMP6054").get_by_role("combobox").select_option("1")
            sleep(2)
            #page.locator('xpath=//*[@id="COMP6056"]//select/option[2]').click()
            sleep(2)
        except Exception as e:
            print(e)
            page.get_by_role("button", name="Planilha").click()
            sleep(2)
            page.locator("#COMP6054").get_by_role("combobox").select_option("1")
            sleep(2)
            # page.locator('xpath=//*[@id="COMP6056"]//select/option[2]').click()


        page.get_by_role("button", name="Imprimir").click()
        sleep(10)

        for arquivo in os.listdir(pasta_arquivo):
            if arquivo.lower().endswith('.xml'):  # garante que seja .xml
                origem = os.path.join(pasta_arquivo, arquivo)
                destino = os.path.join(caminho_pasta_robo, arquivo)
                shutil.move(origem, destino)
        shutil.move(pasta_arquivo, caminho_pasta_robo)
        extracao(pasta_arquivo)
        print('movi')

    except Exception as e:
        print('Erro completo', e)
        return False

def extracao(pasta_arquivo):
    ...

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)  # <- importante
        page = context.new_page()
        teste = login.login_prothues('gmelo', 'DW.2025', page)
        if teste:
            run_protheus(page)


