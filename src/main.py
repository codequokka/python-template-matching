import sys

from lib.pattern_match2 import pattern_match

# from lib.pattern_match import pattern_match

if __name__ == "__main__":
    image_path = sys.argv[1]
    template_path = sys.argv[2]
    pattern_match(image_path, template_path)
