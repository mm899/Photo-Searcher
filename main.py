from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # Get the user query from the text box widget
        query = self.manager.current_screen.ids.user_query.text

        if query != '':
            print('Running...')
            # Get the wikipedia page for the given query
            page = wikipedia.page(query)
            image_link = page.images[0]

            # Without the headers variable, wikipedia gives and error when attempting to download images.
            headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
            }

            # Download image
            response = requests.get(image_link, headers=headers)
            filepath = 'files/image.jpg'
            with open(filepath, 'wb') as file:
                file.write(response.content)
                file.close()

            self.manager.current_screen.ids.img.source = filepath

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
