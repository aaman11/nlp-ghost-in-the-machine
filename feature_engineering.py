import re, numpy as np, spacy, textstat
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def tokenize_words(text):
    return re.findall(r"[A-Za-z']+", text.lower())

def ttr(text):
    tok = tokenize_words(text)
    return len(set(tok)) / max(1, len(tok))

def hapax_legomena(text):
    tok = tokenize_words(text)
    cnt = Counter(tok)
    return sum(1 for _, c in cnt.items() if c == 1)

def tree_height(root):
    if not list(root.children):
        return 1
    return 1 + max(tree_height(child) for child in root.children)

def avg_dep_depth(text):
    doc = nlp(text)
    roots = [sent.root for sent in doc.sents if sent.text.strip()]
    if not roots:
        return 0.0
    return float(np.mean([tree_height(r) for r in roots]))

def pos_adj_noun_ratio(text):
    doc = nlp(text)
    nouns = sum(1 for t in doc if t.pos_ in {"NOUN", "PROPN"})
    adjs = sum(1 for t in doc if t.pos_ == "ADJ")
    return adjs / max(1, nouns)

def readability_fk(text):
    try:
        return textstat.flesch_kincaid_grade(text)
    except:
        return np.nan

def punct_features(text):
    return {
        "semicolon": text.count(";"),
        "emdash": text.count("—") + text.count("--"),
        "exclamation": text.count("!"),
        "colon": text.count(":"),
        "comma": text.count(",")
    }

def extract_features(text):
    feats = {
        "ttr": ttr(text),
        "hapax": hapax_legomena(text),
        "adj_noun_ratio": pos_adj_noun_ratio(text),
        "dep_depth": avg_dep_depth(text),
        "fkg": readability_fk(text),
        "word_count": len(tokenize_words(text)),
        "char_count": len(text),
    }
    feats.update(punct_features(text))
    return feats
