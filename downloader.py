from openimages.download import download_images

download_images(dest_dir="dir", class_labels=[
                "Hammer", "Scissors"],  exclusions_path="./exclude.txt", csv_dir="./csv", limit=100)
