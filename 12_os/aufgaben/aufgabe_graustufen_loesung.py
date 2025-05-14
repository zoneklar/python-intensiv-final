from multiprocessing import Pool, cpu_count
from typing import TypeAlias
from PIL import Image, ImageOps
from pathlib import Path


# Bildpfad und Blockgröße
DATA_PATH = Path(__file__).resolve().parent
image_path = DATA_PATH / "testbild.jpg"
block_size = 100

# Bild laden und vorbereiten
image = Image.open(image_path)
width, height = image.size


# Ein Rechteck im Bild, definiert durch (x0, y0, x1, y1)
Box: TypeAlias = tuple[int, int, int, int]

# Ein Block besteht aus einer Box und dem ausgeschnittenen Bildbereich
Block: TypeAlias = tuple[Box, Image.Image]

# Greyscale Variante
GrayBlock: TypeAlias = tuple[Box, Image.Image]


def get_blocks(img: Image.Image, block_size: int) -> list[Block]:
    """Teilt ein Bild in Blöcke der Größe block_size × block_size."""
    blocks: list[Block] = []
    width, height = img.size  # Bildabmessungen holen

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            # Begrenzungsrechteck berechnen, abgeschnitten am Bildrand
            box: Box = (x, y, min(x + block_size, width), min(y + block_size, height))
            # Bildbereich ausschneiden
            block_img = img.crop(box)
            # Tupel aus Box und Bildblock speichern
            blocks.append((box, block_img))

    return blocks


def convert_to_grayscale(data: Block) -> GrayBlock:
    """
    Wandelt einen Bildblock in Graustufen um und gibt ihn mit Position zurück.
    """
    box, block = data  # Entpacke Position (box) und Bildbereich (block)
    gray_block = ImageOps.grayscale(block)  # Graustufenbild erzeugen
    return (box, gray_block)  # Rückgabe als (Position, Graubild)


def process_image_multiprocessing(
    image: Image.Image, block_size: int, output_path: str | Path
) -> Path:
    """
    Verarbeitet ein Bild blockweise parallel und speichert das Graustufenbild.
    """
    blocks = get_blocks(image, block_size)  # Bild in Blöcke teilen

    # Parallelverarbeitung der Blöcke in Graustufen
    with Pool(cpu_count()) as pool:
        results = pool.map(convert_to_grayscale, blocks)

    # Neues leeres Graustufenbild (L) in Originalgröße anlegen
    width, height = image.size
    new_image = Image.new("L", (width, height))

    # Jeden verarbeiteten Block an der ursprünglichen Position einfügen
    for box, gray_block in results:
        new_image.paste(gray_block, box)

    # Bild speichern
    output_path = Path(output_path)
    new_image.save(output_path)

    return output_path


if __name__ == "__main__":
    output_file = process_image_multiprocessing(
        image, block_size, DATA_PATH / "graustufen.jpg"
    )
