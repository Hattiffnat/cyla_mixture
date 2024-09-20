import dearpygui.dearpygui as dpg
from pathlib import Path

from .backend import Engine
from .dpg_cyrillic_support import CyrillicSupport


class GUI:
    def __init__(self, engine: Engine, app_path: Path):
        self._engine = engine
        self.app_path = app_path

        self.gold_f = 1.6180339887

        self._cyrillic_support = CyrillicSupport(app_path)

    def _setup_gui(self):
        self._cyrillic_support.registry_font()
        self._main_window = dpg.add_window()

        self._input_text = dpg.add_input_text(
            label="Input",
            parent=self._main_window,
            multiline=True,
        )

        self._generate_button = dpg.add_button(
            parent=self._main_window,
            label="Generate",
            callback=self._generate_button_cb,
        )

        self._output_text = dpg.add_input_text(
            parent=self._main_window,
            label="Output",
            enabled=False,
            multiline=True,
        )

    def _generate_button_cb(self):
        dpg.configure_item(
            self._output_text,
            default_value=self._engine.generate_mixture(
                self._cyrillic_support.decode_string(dpg.get_value(self._input_text))
            ),
        )

    def run(self):
        dpg.create_context()

        Ы = self.app_path / 'resources/Ы.ico'
        dpg.create_viewport(
            title="CyLa Mixture",
            width=int(600 * self.gold_f),
            height=600,
            small_icon=Ы.as_posix(),
            large_icon=Ы.as_posix(),
        )

        self._setup_gui()

        dpg.set_primary_window(self._main_window, True)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
