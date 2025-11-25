import cloudinary
import cloudinary.uploader
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def upload_photo(file):
    
    #Uploads a photo file to Cloudinary and returns the secure URL.
   
    result = cloudinary.uploader.upload(file)
    return result.get("secure_url")
