#!/usr/bin/env python3
import argparse
import os
import sys

from wand.image import Image


def main():
    parser = argparse.ArgumentParser(description="Add new image(s) to static folder")
    parser.add_argument("slug")
    parser.add_argument("files", metavar='file', type=str, nargs='*',
                            help='file to convert')
    parser.add_argument("--size", default=1920, type=int,
                            help='size to resize')
    parser.add_argument("--quality", default=80, type=int,
                            help='compression quality')

    args = parser.parse_args()
    dir_path = os.path.join("static", "images", "models", args.slug)
    try:
        os.mkdir(dir_path)
        print(f"created new dir {dir_path}")
    except FileExistsError:
        pass
    except Exception as e:
        print(f"Failed to create img dir: {str(e)}")
        sys.exit(1)
    for filename in args.files:
        with Image(filename=filename) as img:
            old_name = os.path.basename(filename)
            base_name, ext = os.path.splitext(old_name)
            new_name = f"{base_name}_{args.size}{ext}"
            new_path = os.path.join(dir_path, new_name)
            with img.clone() as i:
                i.compression_quality = args.quality
                i.transform("", str(args.size))
                i.strip()
                i.save(filename=new_path)
                print(f"Saved {new_path}")

if __name__ == "__main__":
    main()
