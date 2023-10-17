import re
import requests

from requests.exceptions import Timeout, ConnectionError


def save_image(link: str):
    """Function downloading photos from Instagram

    link: Link to photo from Instagram
    """
    try:
        if 'instagram.com' not in link:
            return "[!] Incorrect link"
        link = re.sub('www.instagram.com', 'ddinstagram.com', link)

        response = requests.get(link)
        if response.status_code == 200:
            image_pattern = r'<meta property="og:image" content="(.*?)"'
            link_image = re.findall(image_pattern, response.text)[0]
            link_image = f"https://ddinstagram.com{link_image}"
        else:
            return f"[!] Error: status code {response.status_code}"

        response_image = requests.get(link_image)
        if response_image.status_code == 200:
            name_pattern = r'<meta property="og:image" content="\/grid\/(.*?)"'
            image_name = re.findall(name_pattern, response.text)[0]
            with open(f"{image_name}.jpg", 'wb') as f:
                f.write(response_image.content)
        else:
            return f"[!] Error: status code {response_image.status_code}"

        return "[!] Success"

    except Timeout:
        return "[!] Timeout error."

    except ConnectionError:
        return "[!] Connection error."

    except Exception as ex:
        return f"[!] {ex}"


def save_video(link: str):
    """Function downloading video from instagram

    link: Link to video from instagram
    """
    try:
        if "instagram.com" not in link:
            return "[!] Incorrect link"
        link = re.sub('www.instagram.com', 'ddinstagram.com', link)

        response = requests.get(link)
        if response.status_code == 200:
            video_pattern = r'<meta property="og:video" content="(.*?)"'
            link_video = re.findall(video_pattern, response.text)[0]
            link_video = f"https://ddinstagram.com{link_video}"
        else:
            return f"[!] Error: status code {response.status_code}"

        response_video = requests.get(link_video)
        if response_video.status_code == 200:
            name_pattern = r'<meta property="og:video" content="\/videos\/(.*?)"'
            video_name = re.findall(name_pattern, response.text)[0]
            if '/' in video_name:
                video_name = re.sub(r'\/.*', '', video_name)
            with open(f"{video_name}.mp4", 'wb') as f:
                f.write(response_video.content)
        else:
            return f"[!] Error: status code {response_video.status_code}"

        return "[!] Success"

    except Timeout:
        return "[!] Timeout error."

    except ConnectionError:
        return "[!] Connection error."

    except Exception as ex:
        return f"[!] {ex}"
