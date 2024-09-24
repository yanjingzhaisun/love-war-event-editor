import dearpygui.dearpygui as dpg
import sys
sys.path.append('..')

class MainEditor:
    def __init__(self):
        self.window = None
        self.text = None
        self.text_buffer = None

    def run(self):
        dpg.create_context()
        with dpg.font_registry():
            with dpg.font("resources/NotoSansSC-Medium.ttf", 20) as default_font:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        dpg.bind_font(default_font)
        with dpg.window(label="Main Editor", tag="Primary Window") as self.window:
            self.draw_menu_bar()
        dpg.create_viewport(title="Main Editor", width=800, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window(self.window, True)
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
            self.update()
        dpg.destroy_context()

    def draw_menu_bar(self):
        with dpg.menu_bar():
            with dpg.menu(label="Menu"):
                dpg.add_menu_item(label="新建图", callback=self.menu_item_new_callback, tag="Menu/New")
    
    def menu_item_new_callback(self):
        pass

    def update(self):
        pass

import dearpygui.demo as demo
class DemoEditor:
    def __init__(self):
        pass
    def run(self):
        dpg.create_context()
        with dpg.font_registry():
            with dpg.font("resources/NotoSansSC-Medium.ttf", 20) as default_font:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        dpg.bind_font(default_font)
        dpg.show_font_manager()
        dpg.create_viewport(title='Custom Title', width=600, height=600)
        demo.show_demo()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

if __name__ == "__main__":
    editor = MainEditor()
    editor.run()
    # editor = DemoEditor()
    # editor.run()
    sys.exit(0)