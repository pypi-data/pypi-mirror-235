from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, TextEdit
from PySide6.QtWidgets import QWidget

class TextInputDialog(MessageBoxBase):
    """
    Usage: text, success = TextInputDialog.getText(self, mode=...)
    """
    language = 0
    class Language:
        """
        ENGLISH = 0,
        CHINESE = 1
        """
        ENGLISH = 0
        CHINESE = 1
    class Mode:
        """
        LINEEDIT = 0,
        TEXTEDIT = 1
        """
        LINEEDIT = 0
        TEXTEDIT = 1

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.widget.setFixedSize(300, 200)
        if self.language == self.Language.CHINESE:
            self.title = SubtitleLabel("请输入")
            self.yesButton.setText("确认")
            self.cancelButton.setText("取消")
        else:
            self.title = SubtitleLabel("Please enter")
            self.yesButton.setText("Confirm")
            self.cancelButton.setText("Cancel")
        self.viewLayout.addWidget(self.title)
        self.input = LineEdit()
        self.viewLayout.addWidget(self.input)

    @classmethod
    def setLanguage(clz, language: Language):
        """Set your language

        Args:
            language (Language): ENGLISH = 0, CHINESE = 1
        """
        clz.language = language


    @staticmethod
    def getText(parent: QWidget, title: str = ..., placeholder: str = ..., yesButton: str = ..., noButton: str = ..., mode: Mode =...) -> (str, bool):
        """Get the text of TextInputDialog

        Args:
            parent: The parent widget.
            title: The title of the dialog (optional, default is "Please enter").
            placeholder: The placeholder text for the input field (optional).
            yesButton: The text for the confirm button (optional, default is "Confirm").
            noButton: The text for the cancel button (optional, default is "Cancel").
            mode: The input mode (optional, default is LINEEDIT, can be LINEEDIT or TEXTEDIT).

        Returns:
            (str, bool): text, success status
        """
        inputDialog = MessageBoxBase(parent)
        inputDialog.widget.setFixedSize(300, 300 if mode == TextInputDialog.Mode.TEXTEDIT else 200)
        isChinese = TextInputDialog.language == TextInputDialog.Language.CHINESE
        if title == ...:
            title = "请输入" if isChinese else "Please enter"
        if isLineEdit := (mode != TextInputDialog.Mode.TEXTEDIT):
            inputDialog.input = LineEdit()
        else:
            inputDialog.input = TextEdit()
        if placeholder != ...:
            inputDialog.input.setPlaceholderText(placeholder)
        if yesButton == ...:
            yesButton = "确认" if isChinese else "Confirm"
        if noButton == ...:
            noButton = "取消" if isChinese else "Cancel"
        inputDialog.title = SubtitleLabel(title)
        inputDialog.yesButton.setText(yesButton)
        inputDialog.cancelButton.setText(noButton)
        inputDialog.viewLayout.addWidget(inputDialog.title)
        inputDialog.viewLayout.addWidget(inputDialog.input)
        success = inputDialog.exec() == 1
        if isLineEdit:
            return (inputDialog.input.text() if inputDialog.input.text() != "" else "", success)
        else:
            return (inputDialog.input.toPlainText() if inputDialog.input.toPlainText() != "" else "", success)
