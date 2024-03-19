from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    NORMAL,
    END,
    Button,
    PhotoImage,
    Text,
    Scrollbar,
    filedialog,
)
from PIL import Image, ImageTk
from _tkinter import *
from prediction_script import XRayPrediction


class ThirdWindow:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assests_ui2")

    def __init__(self, shared_data=None):
        self.shared_data = shared_data
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)

        self.canvas = Canvas(
            self.window,
            bg="#141416",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.image_1 = self.load_image("image_1.png", 50.0, 360.0)
        self.image_2 = self.load_image("image_2.png", 688.0, 85.0)
        self.image_3 = self.load_image("image_3.png", 1125.0, 44.0)
        self.button_3 = Button(
            self.window,
            image=self.image_3,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_3_click,
        )
        self.button_3.place(x=1090.0, y=5.0)

        self.text_widget = Text(
            self.window,
            width=0,
            height=0,
            bg="#141416",
            fg="#FFFFFF",
            font=("Helvetica", 16),
            bd=0,
            highlightthickness=0,
        )

        self.text_widget.place(height=520, width=1110, rely=0.08, x=150, y=120)
        self.text_widget.configure(
            cursor="arrow", state=NORMAL
        )  # Normal state to allow editing.

        # # Insert image into text widget
        # self.text_widget.image_create("end", image=self.image_3)
        self.text_widget.image = []

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        def open_file_dialog():
            filepath = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.png")]
            )
            print(filepath)

            if filepath:
                # Check if a file was selected
                image = Image.open(filepath)
                photo = ImageTk.PhotoImage(image)

                self.text_widget.image_create("end", image=photo)
                self.text_widget.insert("end", "\n")
                self.text_widget.image.append(photo)

                xray_predictor = XRayPrediction()
                label = xray_predictor.predict(filepath)
                # print(label)
                print(f"Label: {label}")

                self.text_widget.tag_configure(
                    "bold_underline", font=("Arial", 30, "bold underline")
                )

                # Inserts the label into the text widget
                self.text_widget.insert(
                    "end", " \nPrediction: " + label + "\n\n\n", "bold_underline"
                )

        self.image_4 = self.load_image("image_4.png", 674.0, 362.0)
        self.button_4 = Button(
            self.window,
            image=self.image_4,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=open_file_dialog,
        )
        # Embed the button in the text widget
        self.text_widget.window_create("end", window=self.button_4)
        self.text_widget.insert("end", "\n\n\n")  # Add a newline after the button

    def on_button_3_click(self):
        self.window.destroy()
        from gui_win1 import SecondWindow

        second_window = SecondWindow(self.shared_data)
        second_window.run()

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ThirdWindow.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    ThirdWindow().run()
