"""
TextInputDialog library based on PySide6-Fluent-Widgets.
Usage: text, success = QInputDialog.getText(self, mode=...)
mode: TextInputDialog.Mode.LINEEDIT (Default) / TextInputDialog.Mode.TEXTEDIT
Set language: TextInputDialog.setLanguage(TextInputDialog.Language.YOURLANGUAGE) (default is CHINESE).
"""
__version__ = "0.0.1"

from .text_input_dialog import TextInputDialog