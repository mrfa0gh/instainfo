import instaloader
import re
import os

def get_instagram_info(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        loader.download_profilepic(profile)

        user_info = {
            "Name": profile.full_name,
            "Username": profile.username,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
            "Is Private": profile.is_private,
            "Bio": profile.biography
        }

        return user_info
    except instaloader.exceptions.ProfileNotExistsException:
        return None

def save_user_info(username, user_info):
    dir_name = username
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    info_file_path = os.path.join(dir_name, f"{username}.txt")
    with open(info_file_path, "w", encoding="utf-8") as file:
        for key, value in user_info.items():
            if key != "Bio":  
                file.write(f"{key}: {value}\n")

    bio_file_path = os.path.join(dir_name, f"bio{username}.txt")
    with open(bio_file_path, "w", encoding="utf-8") as bio_file:
        bio_file.write(user_info["Bio"])

def main():
    input_username = input("Enter the Instagram username (with or without '@'): ")

    username = re.sub(r'^@', '', input_username)

    user_info = get_instagram_info(username)

    if user_info:
        save_user_info(username, user_info)
        print(f"User information saved in {username}/{username}.txt")
        print(f"User bio saved in {username}/bio{username}.txt")
        print(f"Profile picture saved as {username}/{username}.png")
    else:
        print("User not found.")

if __name__ == "__main__":
    main()
