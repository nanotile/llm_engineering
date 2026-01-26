"""https://gemini.google.com/app/afb12daed78473b6
"""






# downloading llama3.2 model from huggingface hub
import os
from pathlib import Path
from huggingface_hub import snapshot_download

# --- CONFIGURATION ---
HF_TOKEN = os.environ.get("HF_TOKEN", "") 
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

# Your target path on the VM
target_dir = Path.home() / "OPENSOURCE_LLM" / "llama3.2"
target_dir.mkdir(parents=True, exist_ok=True)

print(f"Downloading {MODEL_ID} using your Read token...")

try:
    snapshot_download(
        repo_id=MODEL_ID,
        local_dir=str(target_dir),
        token=HF_TOKEN,            # This specifically authorizes the download
        local_dir_use_symlinks=False
    )
    print(f"✅ Download complete! Files are in {target_dir}")
except Exception as e:
    print(f"❌ Still getting an error? Check if you accepted the Meta license on the HF website. Error: {e}")


    import shutil

def check_disk_space(path="/"):
    total, used, free = shutil.disk_usage(path)

    # Convert bytes to Gigabytes
    gb = 1024**3
    print(f"Disk Space Info for: {path}")
    print(f"Total: {total / gb:.2f} GB")
    print(f"Used:  {used / gb:.2f} GB")
    print(f"Free:  {free / gb:.2f} GB")

    if (free / gb) < 15:
        print("\n⚠️ WARNING: You have less than 15GB free. Download might fail.")
    else:
        print("\n✅ You have enough space for Llama-3.2-3B.")

#check_disk_space()