from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList

kv = """
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    # padding: "8dp"
    # spacing: "8dp"

    # AnchorLayout:
    #     anchor_x: "left"
    #     size_hint_y: None
    #     height: avatar.height
    # 
    #     Image:
    #         id: avatar
    #         size_hint: None, None
    #         size: "56dp", "56dp"
    #         source: "data/logo/kivy-icon-256.png"

    # MDLabel:
    #     text: "Main"
    #     font_style: "Button"
    #     adaptive_height: True
    # 
    # MDLabel:
    #     text: "kivydevelopment@gmail.com"
    #     font_style: "Caption"
    #     adaptive_height: True

    ScrollView:

        DrawerList:
            id: md_list
            ItemDrawer:
                icon: 'star'
                text: 'Main'
                on_press:
                    app.root.ids.nav_drawer.set_state("close")
                    app.root.ids.sm.current = "main_screen"

            ItemDrawer:
                icon: 'youtube'
                text: 'Video Player Configuration'
                on_press:
                    app.root.ids.nav_drawer.set_state("close")
                    app.root.ids.sm.current = "video_config_screen"

            ItemDrawer:
                icon: 'midi-port'
                text: 'MIDI Configuration'
            ItemDrawer:
                icon: 'midi-port'
                text: 'Midi Monitor'
            



BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: "MIDI Video Controller"
        elevation: 10
        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        
        ScreenManager:
            id: sm
            MDScreen:
                name: 'main_screen'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Main Screen'
            MDScreen:
                name: 'video_config_screen'
                MDLabel:
                    text: 'Video Config Screen' 
                    


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
"""


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MidiVideoControllerApp(MDApp):
    def build(self):
        self.title = 'MIDI Video Controller V0.0'
        return Builder.load_string(kv)

    # def on_start(self):
    #     icons_item = {
    #         "folder": "My files",
    #         "account-multiple": "Shared with me",
    #         "star": "Starred",
    #         "history": "Recent",
    #         "checkbox-marked": "Shared with me",
    #         "upload": "Upload",
    #     }
    #     for icon_name in icons_item.keys():
    #         self.root.ids.content_drawer.ids.md_list.add_widget(
    #             ItemDrawer(icon=icon_name, text=icons_item[icon_name])
    #         )


MidiVideoControllerApp().run()