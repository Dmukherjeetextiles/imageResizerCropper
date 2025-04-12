import streamlit as st
from PIL import Image
import math

def resize_image(image, width, height):
    return image.resize((int(width), int(height)))

def calculate_file_size(image):
    return (image.size[0] * image.size[1] * len(image.getbands())) / 1024

def resize_to_target_size(original_image, target_kb):
    original_size = calculate_file_size(original_image)
    if target_kb >= original_size:
        return original_image, original_size
    
    # Calculate scaling factor based on area reduction
    scale_factor = math.sqrt(target_kb / original_size)
    new_width = int(original_image.width * scale_factor)
    new_height = int(original_image.height * scale_factor)
    
    return resize_image(original_image, new_width, new_height), target_kb

def main():
    st.title("Image Resizer")
    
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Original Image", use_container_width=True)
        st.write(f"Original Dimensions: {img.size[0]}x{img.size[1]}")
        st.write(f"Original Size: {calculate_file_size(img):.2f} KB")
        
        st.sidebar.header("Resize Options")
        resize_method = st.sidebar.selectbox(
            "Choose resize method:",
            ["Custom Dimensions", "Maintain Aspect Ratio (Width)", "Target File Size (KB)"]
        )
        
        if resize_method == "Custom Dimensions":
            new_width = st.sidebar.number_input("Width", 1, 10000, img.width)
            new_height = st.sidebar.number_input("Height", 1, 10000, img.height)
            
            if st.button("Resize to Custom Dimensions"):
                resized = resize_image(img, new_width, new_height)
                st.image(resized, caption=f"Resized to {new_width}x{new_height}", use_container_width=True)
                st.write(f"New Size: {calculate_file_size(resized):.2f} KB")
                
                resized.save("custom_resized.png")
                with open("custom_resized.png", "rb") as file:
                    st.download_button("Download Custom Resized Image", file.read(), file_name="custom_resized.png")
        
        elif resize_method == "Maintain Aspect Ratio (Width)":
            new_width = st.sidebar.number_input("Enter Width", 1, 10000, img.width)
            aspect_ratio = img.width / img.height
            new_height = int(new_width / aspect_ratio)
            
            if st.button("Resize Maintaining Aspect Ratio"):
                resized = resize_image(img, new_width, new_height)
                st.image(resized, caption=f"Resized to {new_width}x{new_height}", use_container_width=True)
                st.write(f"New Size: {calculate_file_size(resized):.2f} KB")
                
                resized.save("aspect_resized.png")
                with open("aspect_resized.png", "rb") as file:
                    st.download_button("Download Aspect Ratio Resized Image", file.read(), file_name="aspect_resized.png")
        
        elif resize_method == "Target File Size (KB)":
            original_size_kb = calculate_file_size(img)
            target_kb = st.sidebar.number_input("Target Size (KB)", 1, int(original_size_kb * 2), int(original_size_kb))
            
            if st.button("Resize to Target Size"):
                resized, estimated_size = resize_to_target_size(img, target_kb)
                st.image(resized, caption=f"Resized to Target Size", use_container_width=True)
                st.write(f"New Dimensions: {resized.size[0]}x{resized.size[1]}")
                st.write(f"Estimated Size: {calculate_file_size(resized):.2f} KB")
                
                resized.save("size_resized.png")
                with open("size_resized.png", "rb") as file:
                    st.download_button("Download Size-Resized Image", file.read(), file_name="size_resized.png")

if __name__ == "__main__":
    main()