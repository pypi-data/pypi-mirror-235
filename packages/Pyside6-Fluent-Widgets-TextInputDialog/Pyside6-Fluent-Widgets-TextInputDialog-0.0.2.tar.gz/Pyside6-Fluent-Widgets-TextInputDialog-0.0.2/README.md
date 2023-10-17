## PySide6-Fluent-Widgets-TextInputDialog

TextInputDialog is a library for creating text input dialogs based on PySide6-Fluent-Widgets. It provides a simple way to create text input dialogs.


### Usage

```python
from qfluentwidgets_textinputdialog import TextInputDialog

# Create a text input dialog
dialog = TextInputDialog(parent)

# Set the language (default is English)
TextInputDialog.setLanguage(TextInputDialog.Language.ENGLISH)

# Get the text input
text, success = TextInputDialog.getText(parent, title=..., placeholder=..., yesButton=..., noButton=..., mode=...)
```

### Parameters

- `parent`: The parent widget.
- `title`: The title of the dialog (optional, default is "Please enter").
- `placeholder`: The placeholder text for the input field (optional).
- `yesButton`: The text for the confirm button (optional, default is "Confirm").
- `noButton`: The text for the cancel button (optional, default is "Cancel").
- `mode`: The input mode (optional, default is LINEEDIT, can be LINEEDIT or TEXTEDIT).

### Example

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from qfluentwidgets_textinputdialog import TextInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TextInputDialog Example")
        self.setGeometry(100, 100, 500, 500)

        button = QPushButton("Open Dialog", self)
        button.setGeometry(100, 100, 200, 50)
        button.clicked.connect(self.open_dialog)

    def open_dialog(self):
        text, success = TextInputDialog.getText(self, title="Please enter your name", placeholder="Enter your name", yesButton="OK", noButton="Cancel")
        if success:
            print("Your name is:", text)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

### Version

Current version: 0.0.2
