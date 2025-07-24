from PIL import Image, ImageDraw
import numpy as np
import random

# Configuration
SILHOUETTE_PATH = "platypus.png"  # Replace with your transparent PNG
OUTPUT_PATH = "canada_mmiwg_dots.png"
NUM_RED_DOTS = 582  # Exact number of dots to represent MMIWG

def create_mmiwg_silhouette():
    try:
        # Load silhouette image (must have transparent background)
        silhouette = Image.open(SILHOUETTE_PATH).convert("RGBA")
        width, height = silhouette.size

        # Create white background image
        output_img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(output_img)

        # Get all non-transparent pixel coordinates
        data = np.array(silhouette)
        opaque_pixels = np.where(data[:, :, 3] > 50)  # Alpha channel threshold
        coords = list(zip(opaque_pixels[1], opaque_pixels[0]))  # (x,y) pairs

        # Draw exactly 582 red dots randomly within the silhouette
        dot_size = 3  # Adjust based on image size
        for x, y in random.sample(coords, min(NUM_RED_DOTS, len(coords))):
            draw.ellipse(
                [x-dot_size, y-dot_size, x+dot_size, y+dot_size],
                fill="red",
                outline="darkred"
            )

        # Add respectful caption
        draw.text(
            (10, height - 10),
            "582 red dots = Missing and Murdered Indigenous Women and Girls (Canada). Source: https://www.mmiwg-ffada.ca/wp-content/uploads/2019/06/Final_Report_Vol_1a-1.pdf Page 60",
            fill="black"
        )

        output_img.save(OUTPUT_PATH)
        print(f"Silhouette with {NUM_RED_DOTS} red dots saved to {OUTPUT_PATH}")

    except FileNotFoundError:
        print(f"Error: Silhouette image not found at {SILHOUETTE_PATH}")

if __name__ == "__main__":
    create_mmiwg_silhouette()
