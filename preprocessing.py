import re
from pathlib import Path

def read_txt(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8", errors="ignore")

def clean_gutenberg(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    start = re.search(r"\*\*\* START OF.*?\*\*\*", text, re.I | re.S)
    end = re.search(r"\*\*\* END OF.*?\*\*\*", text, re.I | re.S)
    if start and end and start.end() < end.start():
        text = text[start.end():end.start()]
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()

def split_paragraphs(text, min_words=80):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.split()) >= min_words]
    if not paras:
        paras = [p.strip() for p in re.split(r"(?<=[.!?])\s+", text) if len(p.split()) >= min_words]
    return paras
