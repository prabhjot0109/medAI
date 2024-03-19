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


class SecondWindow:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assests_ui1")

    def __init__(self, shared_data=None):
        self.shared_data = shared_data

        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)

        # Create a Canvas object and assign it to self.canvas
        self.canvas = Canvas(self.window, bg="#141416")
        self.canvas.pack(fill="both", expand=True)
        # Call your method to create images and buttons
        self.create_images_and_buttons()

        # Now start the mainloop
        self.window.mainloop()

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return SecondWindow.ASSETS_PATH / Path(path)

    def create_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def create_button(self, image_path, x, y, command=None):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            image=image,
            bd=0,
            highlightthickness=0,
            bg="#141416",
            command=command,  # Replace "your_command_function" with the actual command function
        )
        button.place(x=x, y=y)
        return image, button

    def create_entry(self, image_path, x, y, width, height):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        entry_bg = self.canvas.create_image(x + width / 2, y + height / 2, image=image)
        entry = Entry(
            bd=0, bg="#1a1a1f", fg="#FFFFFF", highlightthickness=0, font=("Magra", 20)
        )
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus()
        entry.bind("<Return>", self._on_enter_pressed)
        return image, entry

    def create_images_and_buttons(self):

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

        self.text_widget.place(height=490, width=1150, rely=0.08, x=130, y=40)
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.image = []

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.986)
        scrollbar.configure(command=self.text_widget.yview)

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

        self.image_1, self.entry_1 = self.create_entry(
            "entry_1.png", 250.0, 600.0, 660.0, 100.0
        )
        self.image_2, self.button_2 = self.create_button(
            "image_1.png", 1110.0, 630.0, command=recognize_speech
        )

        self.image_3 = self.create_image("image_4.png", 631.0, 360.0)

        self.image_5 = self.create_image("image_3.png", 1131.0, 59.0)

        self.image_6, self.button_3 = self.create_button(
            "image_2.png", 1165, 605.0, command=self._on_enter_pressed
        )

        self.image_9 = PhotoImage(file=self.relative_to_assets("image_6.png"))

        self.text_widget.image_create(tk.END, image=self.image_9, padx=25, pady=25)
        self.text_widget.insert(
            tk.END, "\n"
        )  # Inserts a newline character after the image

        def open_file_dialog():
            filepath = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.png")]
            )
            print(filepath)

            self.text_widget.insert("end", "\n\n")
            image = Image.open(filepath)
            photo = ImageTk.PhotoImage(image)
            self.text_widget.image_create("end", image=photo)
            self.text_widget.insert("end", "\n\n\n")
            self.text_widget.image.append(photo)

            content = OCR.ocr(filepath)

            # Format the content
            content = " ".join(content)
            formatted_content = content.replace(
                ". ", ".\n"
            )  # Add a new line after each sentence
            formatted_content = "\n".join(
                ["\n• " + line for line in formatted_content.split("\n")]
            )  # Add a new line and a bullet point before each line

            # Add a title or header
            title = "Medicine Description - \n"

            # Insert the formatted content into the Text widget
            self.text_widget.configure(state="normal")  # Enable the widget

            # Insert the title with a larger font
            self.text_widget.insert("end", title, "title")
            # Insert the content with the normal font
            self.text_widget.insert("end", formatted_content, "content")
            # Insert some newlines at the end
            self.text_widget.insert("end", "\n\n", "content")

            self.text_widget.configure(state="disabled")  # Disable the widget again

            # Configure the font styles
            self.text_widget.tag_configure(
                "title", font=("Helvetica", 20, "bold"), underline=True
            )
            self.text_widget.tag_configure("content", font=("Helvetica", 16))

        self.image_7, self.button_4 = self.create_button("image_5.png", 1020.0, 620.0)
        self.button_4.configure(command=open_file_dialog)

    def _on_enter_pressed(self, event=None):
        msg = self.entry_1.get()
        self._insert_message(msg, "You ")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.entry_1.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

        # msg2 = f"{bot_name}: {get_response(msg)}\n\n"

        self.text_widget.configure(state=NORMAL)

        # self.text_widget.insert(END, msg2)

        self.text_widget.configure(state=DISABLED)


if __name__ == "__main__":
    gui = SecondWindow()
