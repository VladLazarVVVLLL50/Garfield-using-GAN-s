import os
from PIL import Image


def split_and_convert_comic(input_path, output_folder):
    try:
        # Open the comic image
        comic = Image.open(input_path)
        width, height = comic.size

        # Calculate the width of each panel (assuming equal width)
        panel_width = width // 3

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Get the base filename without extension
        base_name = os.path.splitext(os.path.basename(input_path))[0]

        # Split into three panels and save as JPG
        for i in range(3):
            left = i * panel_width
            right = left + panel_width

            # Crop the panel (adding +1 to right to avoid gaps)
            panel = comic.crop((left, 0, right, height))

            # Convert to RGB if needed (JPG doesn't support alpha channel)
            if panel.mode in ('RGBA', 'P'):
                panel = panel.convert('RGB')

            # Save as JPG
            output_path = os.path.join(output_folder, f"{base_name}_panel{i + 1}.jpg")
            panel.save(output_path, 'JPEG', quality=85)

        print(f"Processed {input_path} successfully")

    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")


def process_comics_folder(input_folder, output_folder):
    # Process all PNG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            split_and_convert_comic(input_path, output_folder)


# Example usage
input_folder = "garfield_comics"
output_folder = "garfield_panels"

process_comics_folder(input_folder, output_folder)
print("All comics processed!")