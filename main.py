# make sure install instaloader
#by using pip install instaloader



import instaloader
import re
import os

def get_instagram_info(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download profile picture
        loader.download_profilepic(profile)

        # Gather the required information
        user_info = {
            "Name": profile.full_name,
            "Username": profile.username,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
            "Is Private": profile.is_private
        }

        return user_info
    except instaloader.exceptions.ProfileNotExistsException:
        return None

def save_user_info(username, user_info):
    # Save user info to a text file
    with open(f"{username}.txt", "w", encoding="utf-8") as file:
        for key, value in user_info.items():
            file.write(f"{key}: {value}\n")

def main():
    # Ask the user for input
    input_username = input("Enter the Instagram username (with or without '@'): ")

    # Remove '@' if present
    username = re.sub(r'^@', '', input_username)

    # Get user info
    user_info = get_instagram_info(username)

    if user_info:
        save_user_info(username, user_info)
        print(f"User information saved in {username}.txt")
        print(f"Profile picture saved as {username}.png")
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
