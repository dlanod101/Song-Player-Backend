import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from cloudinary.api import delete_resources

load_dotenv()

# Configuration       
cloudinary.config( 
    cloud_name = "dxbotxymj", 
    api_key = os.getenv("API_KEY"),
    api_secret = os.getenv("API_SECRET"), # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
def upload_item(path, name:str):
    upload_result = cloudinary.uploader.upload(path, public_id=name, folder="Song Backend/image")
    return upload_result["secure_url"]

def delete_image(public_ids):
    public_ids = [f"{public_ids}"]
    delete_resources(public_ids, resource_type="image", type="upload")

def upload_audio(path, name:str):
    result = cloudinary.uploader.upload(
    path,
    resource_type="video",
    public_id=name,
    folder="Song Backend/audio")
    return result["secure_url"]
