# CLI Image Resizer

A fast, parallel image resizer that can resize images in a directory or a single image.
This project was made to drastically decrease the size of a screenshots folder which only stored 4k images. 

## Features

- Parallel processing using multiprocessing
- Progress bar to track progress
- Supports both directory and single image input
- Supports both JPEG and PNG formats
- Defaults to original format if not specified

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python resizer.py -i <input> -o <output> -W <width> -H <height> [-f <format>] [-p <workers>]
```

### Options

- `-i`, `--input`: Input image directory or single image path (required)
- `-o`, `--output`: Output directory (required)
- `-W`, `--width`: Resize width (required)
- `-H`, `--height`: Resize height (required)
- `-f`, `--format`: Output format (JPEG, PNG), defaults to original format
- `-p`, `--workers`: Number of parallel workers, defaults to number of CPU cores

