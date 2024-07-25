import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import numpy as np

class PDFCoordinateFinder:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.coordinates = []

    def on_click(self, event):
        # Capture the coordinates of the click
        ix, iy = event.xdata, event.ydata
        if ix is not None and iy is not None:
            self.coordinates.append((ix, iy))
            print(f"Coordinates: ({ix}, {iy})")

    def find_coordinates(self):
        doc = fitz.open(self.pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

            # Display the page image
            fig, ax = plt.subplots()
            ax.imshow(img, cmap='gray' if pix.n == 1 else None)

            # Connect the click event to the handler
            cid = fig.canvas.mpl_connect('button_press_event', self.on_click)

            plt.title(f"Page {page_num + 1} - Click to get coordinates")
            plt.show()

            # Disconnect the click event after the page is displayed
            fig.canvas.mpl_disconnect(cid)

        return self.coordinates

if __name__ == "__main__":
    pdf_path = r"./proccess_pdf/Sum24 PMMM Grad Clearance Forms REV.pdf"
    coordinate_finder = PDFCoordinateFinder(pdf_path)
    coordinates = coordinate_finder.find_coordinates()
    print("All collected coordinates:", coordinates)


