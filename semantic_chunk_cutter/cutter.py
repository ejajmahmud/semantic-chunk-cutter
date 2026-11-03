"""Boundary-aware semantic text and code chunker."""
import re
from typing import List


class SemanticChunkCutter:
    @staticmethod
    def chunk(text: str, max_chars: int = 1000) -> List[str]:
        # Split by markdown headers and paragraphs first
        paragraphs = re.split(r"(\n{2,}|(?=^#{1,3} ))", text, flags=re.MULTILINE)
        chunks: List[str] = []
        current_chunk = []
        current_len = 0

        for p in paragraphs:
            p_clean = p.strip()
            if not p_clean:
                continue

            if current_len + len(p_clean) > max_chars and current_chunk:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = [p_clean]
                current_len = len(p_clean)
            else:
                current_chunk.append(p_clean)
                current_len += len(p_clean)

        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks
