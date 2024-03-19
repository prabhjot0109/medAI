from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage


class MyWindow:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assests_baseui")

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

        self.image_1 = self.load_image("image_1.png", 633.0, 379.0)
        self.image_2 = self.load_image("image_2.png", 52.0, 331.0)
        self.image_3 = self.load_image("image_3.png", 52.0, 250.0)
        self.image_4 = self.load_image("image_4.png", 640.0, 50.0)

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return MyWindow.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    MyWindow().run()
