from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage


class MyWindow:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assests_ui1")

    def __init__(self):
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

        self.images = self.load_images()

        for image in self.images:
            self.canvas.create_image(image["x"], image["y"], image=image["image"])

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
        return MyWindow.ASSETS_PATH / Path(path)

    def load_images(self):
        images = []
        image_positions = [
            (182.0, 57.0),
            (1139.0, 647.0),
            (1214.597900390625, 643.0),
            (631.0, 360.0),
            (1048.0, 644.0),
            (409.0, 233.0),
            (968.0, 233.0),
            (409.0, 445.0),
            (968.0, 446.0),
        ]
        for i in range(1, 10):
            image = PhotoImage(file=self.relative_to_assets(f"image_{i}.png"))
            images.append(
                {
                    "image": image,
                    "x": image_positions[i - 1][0],
                    "y": image_positions[i - 1][1],
                }
            )
        return images

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    MyWindow().run()
