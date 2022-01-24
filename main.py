from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Main"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main"

            OneLineListItem:
                text: "Midi Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "midi"

            OneLineListItem:
                text: "Video Player Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "video"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MIDI Video Controller"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "main"

                MDLabel:
                    text: "Main"
                    halign: "center"

            MDScreen:
                name: "midi"

                MDLabel:
                    text: "MIDI Profile"
                    halign: "center"

            MDScreen:
                name: "video"

                MDLabel:
                    text: "Video Player Profile"
                    halign: "center"



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()