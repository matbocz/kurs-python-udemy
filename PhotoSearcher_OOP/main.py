import requests
import wikipedia
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        user_query = self.manager.current_screen.ids.user_query.text

        # Get wikipedia page and list of image urls
        page = wikipedia.page(user_query)
        image_links = page.images

        # Get first image link
        first_image_link = image_links[0]

        return first_image_link

    def download_image(self):
        # Download the image
        req = requests.get(self.get_image_link())
        image_path = 'files/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(req.content)

        return image_path

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
