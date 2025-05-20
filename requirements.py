import importlib

packages = [
    "truecase",
    "tqdm",
    "pyhocon",
    "scipy",
    "numpy",
    "torch",
    "huggingface_hub",
    "transformers",
    "sentencepiece",
]

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"[✓] {pkg} is installed")
    except ImportError:
        print(f"[×] {pkg} is NOT installed")
