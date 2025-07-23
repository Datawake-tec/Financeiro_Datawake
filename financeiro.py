from time import sleep
from SolutionPacket.Solution_login import LoginPlaywright
from playwright.sync_api import sync_playwright


nome_robo = 'Conta a Pagar - '
login = LoginPlaywright(nome_robo)


def run_protheus(page_):
    sleep(3)
    page_.get_by_text("Consultas (3)").click()
    sleep(2)
    page_.get_by_text("• Posição de Títulos a Pagar").click()
    sleep(1)
    page_.get_by_role("button", name="Confirmar").click()
    sleep(3)

if __name__ == '__main__':
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)  # Coloque True se não quiser abrir o navegador
        page = navegador.new_page()
        # navegador.close()
        teste = login.login_prothues('gmelo', 'DW.2025', page)
        if teste:
            run_protheus(page)

