"""Unit tests for SemanticChunkCutter."""
import unittest
from semantic_chunk_cutter.cutter import SemanticChunkCutter

class TestSemanticChunkCutter(unittest.TestCase):
    def test_paragraph_preservation(self):
        doc = "Para 1.\n\nPara 2.\n\nPara 3."
        chunks = SemanticChunkCutter.chunk(doc, max_chars=20)
        self.assertGreater(len(chunks), 1)
        self.assertIn("Para 1.", chunks[0])

if __name__ == "__main__":
    unittest.main()
