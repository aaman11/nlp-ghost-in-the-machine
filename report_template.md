# Ghost in the Machine
## Stylometric Detection of Human vs AI Generated Literary Text

PRECOG Recruitment Tasks 2026  
Theme: NLP

---

# Author

Name: <Aaman Raees> 
Email: <aamanraees022@gmail.com>  


---

# Declaration

This project was completed independently for the PRECOG Recruitment Tasks 2026.

External libraries, APIs, papers, and online resources used during development have been cited appropriately.

---

# Task Completion Summary

| Task | Status | Notes |
|---|---|---|
| Corpus Construction | Completed | Project Gutenberg literary corpus collected |
| Stylometric Analysis | Completed | Lexical, syntactic, readability, punctuation features |
| Classical ML Models | Completed | Random Forest + XGBoost |
| Transformer Fine-Tuning | Completed | DistilBERT + LoRA |
| Explainability | Completed | Captum + SHAP |
| Genetic Algorithm Attack | Completed | Adversarial text evolution |
| Error Analysis | Completed | Misclassification inspection |
| Extended Experiments | Partial | Limited by compute resources |

---

# Abstract

This project investigates whether AI-generated literary prose can be distinguished from human-authored prose using stylometric analysis, machine learning, transformer-based classifiers, explainability methods, and adversarial attacks.

The work focuses on controlled-topic literary generation using:
- human-authored literature,
- neutral AI-generated prose,
- style-mimic AI generations.

The project studies:
- lexical richness,
- syntactic complexity,
- punctuation rhythm,
- readability,
- transformer interpretability,
- adversarial detector bypass strategies.

Importantly, the work emphasizes:
- research methodology,
- analysis,
- reproducibility,
- limitations,
- negative findings.

---

# 1. Introduction

Recent advances in Large Language Models (LLMs) have made AI-generated text increasingly difficult to distinguish from human-authored writing.

Traditional AI detection systems often rely on:
- lexical repetition,
- perplexity,
- shallow stylistic markers.

However, modern LLMs increasingly reproduce:
- authorial rhythm,
- syntactic structure,
- punctuation style,
- semantic coherence.

This project investigates whether stylometric analysis remains effective under:
- controlled topic settings,
- literary prose,
- deliberate style imitation.

---

# 2. Research Questions

The project investigates the following questions:

1. Are human and AI literary texts statistically separable?
2. Which stylometric features contribute most strongly to separability?
3. Can transformer models capture higher-order stylistic rhythm?
4. Does style mimicry reduce stylometric distinguishability?
5. Can adversarial rewriting bypass AI detectors?

---

# 3. Dataset Construction

# 3.1 Human Corpus

Human-authored literary texts were collected from Project Gutenberg.

## Authors Used
- Jane Austen
- Charles Dickens

## Books Used
- Pride and Prejudice
- Great Expectations
- Emma
- Oliver Twist

The raw texts were:
- cleaned,
- normalized,
- stripped of Gutenberg metadata,
- segmented into paragraph-level samples.

Paragraphs shorter than a threshold were removed.

---

# 3.2 AI Corpus

Two AI-generated datasets were created using Gemini API.

## Class 1 — Neutral AI
AI-generated literary paragraphs on controlled topics without style imitation.

## Class 2 — Style-Mimic AI
AI-generated literary paragraphs explicitly prompted to imitate:
- Austen,
- Dickens.

---

# 3.3 Topic Control

Topics included:
- inheritance,
- morality,
- loneliness,
- industrialization,
- ambition,
- emotional restraint,
- social hierarchy,
- class conflict.

Topic control ensured that authorship/style remained the dominant signal.

---

# 4. Methodology

# 4.1 Stylometric Feature Extraction

The following features were extracted.

## Lexical Richness
- Type Token Ratio (TTR)
- Hapax Legomena

## Syntactic Complexity
- Adjective-to-Noun ratio
- Average sentence length
- Dependency tree depth

## Punctuation Rhythm
- semicolon density,
- em-dash density,
- comma frequency,
- exclamation frequency.

## Readability
- Flesch-Kincaid Grade Level

Feature extraction was implemented using:
- SpaCy,
- NLTK,
- textstat.

---

# 4.2 Classical Machine Learning

Two classical classifiers were trained.

## Models
- Random Forest
- XGBoost

Input:
- handcrafted stylometric features.

Evaluation:
- accuracy,
- F1 score,
- confusion matrix,
- feature importance.

---

# 4.3 Transformer-Based Detection

Transformer classifiers were fine-tuned using:
- DistilBERT,
- LoRA adapters,
- HuggingFace PEFT.

## Training Details

| Parameter | Value |
|---|---|
| Batch Size | 16 |
| Epochs | 3 |
| Learning Rate | 2e-5 |
| Max Length | 384 |
| Optimizer | AdamW |

LoRA was used to reduce parameter count and computational cost.

---

# 4.4 Explainability

Explainability methods:
- SHAP,
- Captum Integrated Gradients.

These methods were used to identify:
- token-level importance,
- stylistic markers,
- punctuation effects,
- rhythmic indicators.

---

# 4.5 Adversarial Attack

A Genetic Algorithm (GA) pipeline was implemented to evolve AI-generated paragraphs toward higher “human” confidence.

## Mutation Strategies
- sentence rhythm modification,
- punctuation variation,
- grammatical inconsistencies,
- archaic vocabulary injection.

The objective was to maximize:
- classifier human probability.

---

# 5. Experimental Setup

# Hardware
- Google Colab GPU

# Libraries
- HuggingFace Transformers
- PEFT
- SpaCy
- Scikit-learn
- XGBoost
- Captum
- SHAP

---

# 6. Results

# 6.1 Classical ML Results

| Model | Accuracy | F1 Score |
|---|---|---|
| Random Forest | 
| XGBoost |
---

# 6.2 Transformer Results

| Model | Accuracy | F1 Score |
|---|---|---|
| DistilBERT + LoRA | 

---

# 6.3 Observations

Key findings:
- stylometric features separated neutral AI prose effectively,
- style-mimic generations reduced separability,
- punctuation rhythm was highly informative,
- transformer models captured higher-order stylistic structure.

---

# 7. Visualizations

The project includes:
- confusion matrices,
- SHAP summaries,
- feature importance plots,
- punctuation heatmaps,
- PCA projections,
- UMAP projections,
- GA optimization curves.

(Insert figures here)

---

# 8. Explainability Findings

Integrated Gradients and SHAP revealed that the classifier relied heavily on:
- punctuation rhythm,
- sentence structure,
- stylistic repetition.

Certain AI-associated patterns emerged repeatedly:
- highly regular sentence rhythm,
- balanced punctuation,
- excessive semantic smoothness.

Interestingly, vocabulary alone was often insufficient for reliable classification.

---

# 9. Error Analysis

Several interesting failure cases were observed.

## Human Misclassified as AI
In some cases:
- highly polished literary prose,
- repetitive rhetorical structures,
- unusually formal rhythm

caused human text to be flagged as AI-generated.

## AI Misclassified as Human
Style-mimic generations occasionally reproduced:
- punctuation cadence,
- irregular sentence flow,
- lexical diversity

sufficiently well to bypass the detector.

These findings suggest that modern LLMs partially reproduce higher-order stylistic structure.

---

# 10. Adversarial Attack Results

The Genetic Algorithm successfully increased classifier human confidence over multiple generations.

Observed mutation effects:
- punctuation irregularity improved human confidence,
- sentence-length variation reduced AI detectability,
- slight grammatical inconsistency improved robustness against detection.

This suggests that many AI detectors rely heavily on stylistic regularity.

---

# 11. Limitations

Several limitations remain.

- limited author diversity,
- relatively small literary corpus,
- possible topic leakage,
- Gemini generation quality dependence,
- limited computational resources,
- inability to perform large-scale hyperparameter sweeps.

---

# 12. Future Work

Potential extensions include:
- multilingual stylometry,
- rhythm-aware transformers,
- larger author pools,
- adversarially robust detectors,
- stylometric transfer learning,
- semantic-rhythm disentanglement.

---

# 13. Conclusion

This project explored stylometric AI detection through:
- handcrafted features,
- transformer fine-tuning,
- explainability,
- adversarial optimization.

The findings suggest that:
- modern LLMs increasingly reproduce human stylistic structure,
- punctuation rhythm and sentence cadence remain valuable signals,
- style mimicry substantially reduces separability.

Most importantly, the project demonstrates that:
- negative results,
- failure analysis,
- adversarial robustness

are essential components of trustworthy AI detection research.

---

# References

1. Project Gutenberg  
2. HuggingFace Transformers Documentation  
3. PEFT / LoRA Documentation  
4. SHAP Documentation  
5. Captum Documentation  
6. SpaCy Documentation  
7. Scikit-learn Documentation  
8. XGBoost Documentation

---


