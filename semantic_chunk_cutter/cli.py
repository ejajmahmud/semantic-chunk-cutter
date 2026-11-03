"""Command-line interface for Semantic Chunk Cutter."""
import argparse
from .cutter import SemanticChunkCutter

def main():
    parser = argparse.ArgumentParser(description="Semantic Chunk Cutter CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate semantic chunking")
    args = parser.parse_args()

    doc = """# Introduction
This is the first section of the document explaining architecture.

## Code Example
```python
def calculate(a, b):
    return a * b + 42
```

# Conclusion
Final thoughts on system implementation."""

    chunks = SemanticChunkCutter.chunk(doc, max_chars=120)
    print(f"Split document into {len(chunks)} clean semantic chunk(s):")
    for i, ch in enumerate(chunks, 1):
        print(f"--- Chunk #{i} ({len(ch)} chars) ---")
        print(ch)

if __name__ == "__main__":
    main()
