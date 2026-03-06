import argparse
import multiprocessing as mp
import os
from PIL import Image
from tqdm import tqdm

def arg_parser():
    parser = argparse.ArgumentParser(description="Parallel Image Resizer")
    parser.add_argument("-i", "--input", required=True, help="Input image directory or single image path")
    parser.add_argument("-o", "--output", required=True, help="Output directory")
    parser.add_argument("-W", "--width", type=int, required=True, help="Resize width")
    parser.add_argument("-H", "--height", type=int, required=True, help="Resize height")
    parser.add_argument("-f", "--format", default=None, help="Output format (JPEG, PNG), defaults to original format")
    parser.add_argument("-p", "--workers", type=int, default=mp.cpu_count(), help="Number of parallel workers, defaults to number of CPU cores")
    return parser.parse_args()

def resize_image(args):
    image_path, output_dir, width, height, format_ = args

    try:
        with Image.open(image_path) as img:
            img_resized = img.resize((width, height))

        name = os.path.splitext(os.path.basename(image_path))[0]
        if format_ is None:
            format_ = img.format # If format isnt specified by user
        output_path = os.path.join(output_dir, f"{name}.{format_.lower()}")
        img_resized.save(output_path, format_)

        return f"Processed {image_path}"

    except Exception as e:
        return f"Error processing {image_path}: {e}"

def get_images(input_dir):
    if os.path.isfile(input_dir):
        return [input_dir]

    valid_ext = (".png", ".jpg", ".jpeg")
    return [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if f.lower().endswith(valid_ext)
    ]

def main():
    args = arg_parser()
    os.makedirs(args.output, exist_ok=True)
    image_files = get_images(args.input)
    tasks = [(img, args.output, args.width, args.height, args.format) for img in image_files]

    with mp.Pool(args.workers) as pool:
        for r in tqdm(pool.imap_unordered(resize_image, tasks), total=len(tasks)): # Progress bar to track progress
            print(r)

if __name__ == "__main__":
    main()