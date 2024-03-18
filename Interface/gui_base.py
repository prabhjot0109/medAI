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

        self.images = self.load_images()

        for image in self.images:
            self.canvas.create_image(image["x"], image["y"], image=image["image"])

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return MyWindow.ASSETS_PATH / Path(path)

    def load_images(self):
        images = []
        image_positions = [
            (640.0, 50.0),
            (50.0, 360.0),
            (638.0, 53.0),
            (44.0, 155.0),
            (52.0, 244.0),
            (52.0, 331.0),
            (653.0, 437.0),
        ]
        for i in range(1, 8):
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
