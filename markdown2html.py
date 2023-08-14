#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)
    
    # The actual conversion from Markdown to HTML can be added here
    
    sys.exit(0)

if __name__ == "__main__":
    main()
    