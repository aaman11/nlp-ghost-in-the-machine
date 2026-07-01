import pickle

config = {
    "model_name": "distilbert-base-uncased",
    "max_length": 256,
    "batch_size": 16,
    "epochs": 3,
    "lora_r": 8,
    "lora_alpha": 16,
    "seed": 42
}

with open("transformer_pipeline.p", "wb") as f:
    pickle.dump(config, f)
