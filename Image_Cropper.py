import streamlit as st
from PIL import Image

# Function to crop the image based on ratio
def crop_image(image, x_ratio, y_ratio):
    try:
        width, height = image.size
        ratio = x_ratio / y_ratio
        if width > height:
            new_width = int(height * ratio)
            left = (width - new_width) // 2
            top = 0
            right = left + new_width
            bottom = height
        else:
            new_height = int(width / ratio)
            left = 0
            top = (height - new_height) // 2
            right = width
            bottom = top + new_height

        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image
    except Exception as e:
        st.error("Error: " + str(e))
        return None

# Function to resize the image
def resize_image(image, width, height):
    try:
        resized_image = image.resize((width, height))
        return resized_image
    except Exception as e:
        st.error("Error: " + str(e))
        return None

# Calculate estimated file size in kilobytes
def calculate_file_size(image):
    try:
        width, height = image.size
        channels = len(image.getbands())
        file_size = (width * height * channels) / 1024
        return file_size
    except Exception as e:
        st.error("Error calculating file size: " + str(e))
        return None

# Main function to run the Streamlit app
def main():
    st.title("Image Editor")

    # File upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Sidebar for input parameters
        st.sidebar.title("Edit Options")
        edit_option = st.sidebar.selectbox("Choose edit option:", ["Crop", "Resize"])

        if edit_option == "Crop":
            # Get cropping ratio from the user
            x_ratio = st.sidebar.number_input("X ratio", min_value=0.1, max_value=10.0, step=0.1, value=1.0)
            y_ratio = st.sidebar.number_input("Y ratio", min_value=0.1, max_value=10.0, step=0.1, value=1.0)

            if st.button("Crop Image"):
                # Crop the image
                cropped_image = crop_image(image, x_ratio, y_ratio)

                if cropped_image is not None:
                    st.image(cropped_image, caption="Cropped Image", use_column_width=True)

                    # Display dimensions
                    st.write(f"Dimensions: {cropped_image.size[0]} x {cropped_image.size[1]} pixels")

                    # Calculate and display estimated file size
                    file_size = calculate_file_size(cropped_image)
                    if file_size is not None:
                        st.write(f"Estimated File Size: {file_size:.2f} KB")

                    # Download button for cropped image
                    if st.button("Download Cropped Image"):
                        with st.spinner("Downloading..."):
                            cropped_image.save("cropped_image.png")
                            st.success("Cropped image downloaded successfully!")

        elif edit_option == "Resize":
            # Get resizing parameters from the user
            width = st.sidebar.number_input("Width", 1, image.width, image.width)
            height = st.sidebar.number_input("Height", 1, image.height, image.height)

            if st.button("Resize Image"):
                # Resize the image
                resized_image = resize_image(image, width, height)

                if resized_image is not None:
                    st.image(resized_image, caption="Resized Image", use_column_width=True)

                    # Display dimensions
                    st.write(f"Dimensions: {resized_image.size[0]} x {resized_image.size[1]} pixels")

                    # Calculate and display estimated file size
                    file_size = calculate_file_size(resized_image)
                    if file_size is not None:
                        st.write(f"Estimated File Size: {file_size:.2f} KB")

                    # Download button for resized image
                    if st.button("Download Resized Image"):
                        with st.spinner("Downloading..."):
                            resized_image.save("resized_image.png")
                            st.success("Resized image downloaded successfully!")

# Run the main function to start the Streamlit app
if __name__ == "__main__":
    main()
