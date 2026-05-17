import os
import shutil
from pathlib import Path

# Define the correct folder structure
folders = {
    'pizza': ['margherita-pizza.jpg', 'pepperoni-pizza.jpg', 'farmhouse-pizza.jpg'],
    'burgers': ['veg-burger.jpg', 'chicken-burger.jpg', 'double-cheese-burger.jpg'],
    'drinks': ['coca-cola.jpg', 'fresh-lime-soda.jpg', 'buttermilk.jpg'],
    'south-indian': ['masala-dosa.jpg', 'idli-sambhar.jpg', 'vada.jpg'],
    'desserts': ['gulab-jamun.jpg', 'ice-cream.jpg', 'brownie.jpg'],
    'combos': ['pizza-combo.jpg', 'burger-combo.jpg', 'south-indian-combo.jpg']
}

# Create all folders
for folder_name in folders.keys():
    Path(f'static/images/{folder_name}').mkdir(parents=True, exist_ok=True)
    print(f"✓ Created folder: static/images/{folder_name}")

# Move images to correct folders
for folder_name, files in folders.items():
    for file_name in files:
        source = f'static/images/{file_name}'
        destination = f'static/images/{folder_name}/{file_name}'
        
        if os.path.exists(source):
            shutil.move(source, destination)
            print(f"✓ Moved: {file_name} -> {folder_name}/")
        else:
            print(f"⚠ File not found: {file_name}")

print("\n" + "="*50)
print("✅ Images organized successfully!")
print("="*50)

# List all images in their correct locations
print("\n📁 Current image locations:")
for folder_name, files in folders.items():
    print(f"\n  {folder_name}/")
    for file_name in files:
        path = f'static/images/{folder_name}/{file_name}'
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"    ✓ {file_name} ({size} bytes)")
        else:
            print(f"    ✗ {file_name} (missing)")
