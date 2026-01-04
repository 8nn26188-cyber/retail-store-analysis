from pathlib import Path
import shutil
import kagglehub

# Creates a Path objects pointing to data/raw
raw_dir = Path("data/raw")

# Unique Kaggle dataset ID
dataset_slug = "ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning"

def download_raw_data():
    # mkdir -> create directory, parents=True -> also create data/ if missing
    # exist_ok=True -> no error if directory already exists
    raw_dir.mkdir(parents=True, exist_ok=True)

    #Downloads and extracts the dataset
    cache_path = Path(kagglehub.dataset_download(dataset_slug))
    print("KaggleHub cache path: ", cache_path)

    # Store the names of successfully copied contents
    copied = []
    # Loops over everything in the cache directory, p is a Path object
    for p in cache_path.iterdir():
        # Ensures only files are copied
        if p.is_file():
            # Combines data/raw with the file name, ex: data/raw/retail_store_sales.csv
            target = raw_dir / p.name
            # Copies the file, Preserves timestamps and metadata
            shutil.copy2(p, target)
            copied.append(target.name)

    if not copied:
        raise RuntimeError("No files copied from kagglehub cache. Check dataset contents/path.")

    print("✅ Copied to data/raw/:")
    for name in copied:
        print("  -", name)

if __name__ == "__main__":
    download_raw_data()