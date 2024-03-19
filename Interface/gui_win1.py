from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    Entry,
    Button,
    PhotoImage,
    Text,
    DISABLED,
    END,
    Scrollbar,
    filedialog,
    messagebox,
)
from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk

import speech_recognition as sr
import OCR as OCR

# import Chatbot.chat as chat


class SecondWindow:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assests_ui1")

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

        self.image_1 = self.load_image("image_1.png", 182.0, 57.0)

        def recognize_speech():
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            try:
                recognized_text = recognizer.recognize_google(audio)
                # Update GUI with recognized text
                self.entry_1.delete(0, tk.END)
                self.entry_1.insert(tk.END, recognized_text)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Speech Recognition service; {0}".format(
                        e
                    )
                )

        self.image_2 = self.load_image("image_2.png", 1128.0, 648.0)
        self.button_2 = Button(
            self.window,
            image=self.image_2,
            command=recognize_speech,
            bg="#141416",  # Same as the background
            bd=0,  # No border
            highlightthickness=0,  # No highlight when focus is in this widget
            relief="flat",  # No 3d button look
        )
        self.button_2.place(x=1110.0, y=620.0)

        self.image_3 = self.load_image("image_3.png", 1214.597900390625, 643.0)
        self.image_4 = self.load_image("image_4.png", 631.0, 360.0)
        self.image_5 = self.load_image("image_5.png", 1048.0, 644.0)
        self.image_6 = self.load_image("image_6.png", 409.0, 233.0)
        self.image_7 = self.load_image("image_7.png", 968.0, 233.0)
        self.image_8 = self.load_image("image_8.png", 409.0, 445.0)
        self.image_9 = self.load_image("image_9.png", 968.0, 446.0)

        self.canvas.create_text(
            233.0,
            31.0,
            anchor="nw",
            text="medAI",
            fill="#FFFFFF",
            font=("Humanist521BT Bold", 36 * -1),
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            564.0, 643.0, image=self.entry_image_1
        )
        self.entry_1 = Entry(bd=0, bg="#1A1A1F", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=186.0, y=593.0, width=756.0, height=98.0)

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return SecondWindow.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def some_method(self):
        data = self.shared_data["key"]

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    SecondWindow().run()
