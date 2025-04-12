# 📷 Streamlit Image Resizer
A web-based image resizing tool with three distinct resizing methods, built using Streamlit and Pillow. This project is just what you need to resize your images for those poor website applications that stresses you for the perfect image size or dimensions. 

## 🚀 Features

- **Three Resizing Methods:**
  - Custom Dimensions (manual width/height)
  - Maintain Aspect Ratio (width-based)
  - Target File Size (KB-based)
- Real-time image preview
- File size estimation
- Download resized images
- Responsive UI

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Dmukherjeetextiles/imageResizerCropper.git
cd imageResizerCropper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit Pillow
```

## 🖥️ Usage

Run the app:
```bash
streamlit run app.py
```

**Workflow:**
1. Upload an image (JPEG/PNG)
2. Choose resizing method:
   - **Custom Dimensions:** Set specific width/height
   - **Maintain Aspect Ratio:** Set width, auto-calculate height
   - **Target File Size:** Set desired file size in KB
3. View resized image preview
4. Download result

## 🔍 How Target File Size Works

The app uses mathematical approximation:
```python
scale_factor = sqrt(target_size / original_size)
new_width = original_width * scale_factor
new_height = original_height * scale_factor
```
Note: Actual file sizes may vary slightly due to image compression.



## 📄 License

Distributed under MIT License. See [LICENSE](LICENSE) for details.


[Demo](https://imageresizercropper.streamlit.app/)
