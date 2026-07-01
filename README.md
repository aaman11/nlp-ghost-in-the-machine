# Ghost in the Machine

This project studies whether human authorship can be separated from AI-generated text when topic is controlled and style is matched.

## Data input
Place your already-downloaded Project Gutenberg `.txt` files in the project root or `data/` folder.
The notebooks load only local files and do not download ebooks.

## Files
- notebooks/
- src/
- data/
- outputs/
- models/

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Workflow
1. Run `01_corpus_and_stylometry.ipynb`
2. Run `02_classical_ml.ipynb`
3. Run `03_transformer_training.ipynb`
4. Run `04_explainability_and_ga.ipynb`
