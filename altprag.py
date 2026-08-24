#dataset taken from https://huggingface.co/datasets/Huangtubaye233/AltPrag
print("started")
from datasets import load_dataset

ds = load_dataset("Huangtubaye233/AltPrag")

ds = ds.shuffle(seed=42)

data = ds['test'].to_pandas()

ft_data = data[:649]
eval_data = data[649:]

print("Done running!")