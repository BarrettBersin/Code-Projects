from instabot import Bot
import os

# Set up the bot
bot = Bot()

# Login credentials
username = "your_username"
password = "your_password"

# Login to Instagram
bot.login(username=username, password=password)

# Path to the image you want to upload
image_path = "path/to/your/image.jpg"

# Caption for the post
caption = "Your caption here"

# Upload the image with the caption
bot.upload_photo(image_path, caption=caption)

# Logout
bot.logout()