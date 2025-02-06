from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("bigscience-data/roots_fr_wikipedia")

# Print the first few entries to verify the dataset
print(ds['train'][0])