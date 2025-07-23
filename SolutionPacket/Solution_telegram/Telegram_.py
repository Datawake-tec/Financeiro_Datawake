import telegram
import asyncio
import requests


class TelegramSend:

    def __init__(self, name):
        self.name = name

    def telegram_bot(self, message, itoken, chat_id):
        """Telegram Bot
        :param message: Mensagem a ser enviada pelo telegram;
        :param itoken: Itoken do father no telegram;
        :param chat_id: id da conversa ou do grupo a qual as mensagens vao ser direcionadas;
        :return: Retorna um json dom todos os paramentros e status da mensagem.
        """
        url = "https://api.telegram.org/bot" + itoken + "/sendMessage?chat_id=" + chat_id + "&text=" + self.name + ' ' + message
        resposta = requests.get(url)
        return resposta.json()


    def telegram_bot_image(self, message, itoken, chat_id, path_image):
        """Telegram Bot
        :param message: Mensagem a ser enviada pelo telegram;
        :param itoken: Itoken do father no telegram;
        :param chat_id: id da conversa ou do grupo a qual as mensagens vao ser direcionadas;
        :param path_image: caminho da imagem que vai ser enviada;
        :return: Retorna um json com todos os parâmetros e status da mensagem.
        """
        bot = telegram.Bot(token=itoken)

        async def send_image():
            await bot.send_photo(chat_id=chat_id, photo=open(path_image, 'rb'))

        # Verifica se um loop de eventos já está em execução
        try:
            loop = asyncio.get_running_loop()
            task = loop.create_task(send_image())  # Agendar a execução da tarefa
        except RuntimeError:  # Não há nenhum loop rodando
            asyncio.run(send_image())

        # Enviar a mensagem de texto após enviar a imagem
        url = f"https://api.telegram.org/bot{itoken}/sendMessage?chat_id={chat_id}&text={self.name} {message}"
        resposta = requests.get(url)
        return resposta.json()


if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()

    token = os.getenv('TOKEN')
    chat_id = os.getenv('CHAT_ID')
    chat_id_rpa = os.getenv('CHAT_ID_RPA')
    tele = TelegramSend('teste')

    cam = r'C:\Users\tom\PycharmProjects\Qualidade_Indicadores\Marelli'
    path_erro_find_element = os.path.join(cam, 'erro_find_element_marelli.png')
    tele.telegram_bot_image(f'Erro ao encontrar o elemento ', token, chat_id_rpa,
                            path_erro_find_element)