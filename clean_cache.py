import os
import shutil

cache_dir = "cache/"

def clean_or_create_cache():
    # Check if cache directory exists
    if os.path.exists(cache_dir):
        # If it exists, delete its contents
        for filename in os.listdir(cache_dir):
            file_path = os.path.join(cache_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        # If cache directory doesn't exist, create it
        os.makedirs(cache_dir)
        print(f"Created {cache_dir} directory.")

if __name__ == "__main__":
    clean_or_create_cache()
    print("Cache cleaned!")
