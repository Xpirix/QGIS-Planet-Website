#!/usr/bin/env python3

import feedparser
import os
import json
from urllib.parse import urlparse
import string
import random
import requests
import shutil
from datetime import datetime
from scripts.resize_image import resize_image, convert_to_webp, is_valid_image, is_valid_svg
from dateutil.parser import parse as date_parse
from bs4 import BeautifulSoup

# Path to the subscribers.json file
SUBSCRIBERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data', 'subscribers.json')
ALL_POSTS_FOLDER = os.path.join("content", "posts")

DEFAULT_AVAILABLE_LANG = ["en_GB"]
DEFAULT_MAIN_LANG = "en_GB"
DEFAULT_CATEGORIES = ["QGIS"]

class FeedProcessor:
    def __init__(
            self,
            subscriber_name: str,
            shortname: str,
            feed_url: str,
            available_lang: list,
            main_lang: str,
            filter_categories: list):

        """
        Initializes a new instance of the class.

        Args:
            subscriber_name (str): The name of the subscriber.
            shortname (str): A short name or identifier for the subscriber.
            feed_url (str): The URL of the feed to be fetched.
            available_lang (list): A list of languages available for the feed.
            main_lang (str): The default language for the feed.
            filter_categories (list): A list of categories to filter the feed by.

        Description:
            This class is responsible for initializing the subscriber's details 
            including their name, a short identifier, and the URL of the feed 
            they are subscribed to.
        """
        self.subscriber_name = subscriber_name
        self.shortname = shortname
        self.feed_url = feed_url
        self.available_lang = available_lang
        self.main_lang = main_lang
        self.filter_categories = filter_categories

    def fetch_and_create_post(self):
        try:
            feed = feedparser.parse(self.feed_url)
            for entry in feed.entries:
                self.process_entry(entry)
        except Exception as e:
            print(f"Failed to process feed for {self.subscriber_name}: {e}")

    def fetch_all_images(self, content, subscriber_shortname, post_name):
        img_folder = os.path.join("img", "subscribers", subscriber_shortname, post_name)
        soup = BeautifulSoup(content, 'html.parser')
        unknown_img_folder = os.path.join("static", img_folder, "unknown")

        if os.path.exists(unknown_img_folder):
            shutil.rmtree(unknown_img_folder)
        os.makedirs(unknown_img_folder, exist_ok=True)

        for img in soup.find_all('img'):
            img_url = img['src']
            file_name = self.get_image_name(img_url.split('?')[0])
            try:
                downloaded_img = self.download_and_process_image(img_url, file_name, img_folder, unknown_img_folder)
                img['src'] = downloaded_img
            except Exception as e:
                img['src'] = ""
                print(f"Failed to process image: {e}")

        for video in soup.find_all('video'):
            video_url = video.find('source')['src']
            video.replace_with(soup.new_tag('a', href=video_url, target="_blank", string="Watch Video"))

        return str(soup)

    def download_and_process_image(self, img_url, file_name, img_folder, unknown_img_folder):
        no_param_url = img_url.split('?')[0]  # Remove query parameters
        if no_param_url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
            downloaded_img = self.download_image(no_param_url, file_name, os.path.join("static", img_folder))
            if not is_valid_image(downloaded_img):
                os.remove(downloaded_img)
                raise Exception(f"Invalid image: {downloaded_img}")
            resize_image(downloaded_img, max_height=600)
            webp_img_path = convert_to_webp(downloaded_img, replace=True)
            return os.path.join("/", img_folder, os.path.basename(webp_img_path))
        elif no_param_url.lower().endswith('.svg'):
            downloaded_img = self.download_image(no_param_url, file_name, os.path.join("static", img_folder))
            if not is_valid_svg(downloaded_img):
                os.remove(downloaded_img)
                raise Exception(f"Invalid image: {downloaded_img}")
            return os.path.join("/", img_folder, file_name)
        else:
            downloaded_img = self.handle_unknown_image_format(img_url, unknown_img_folder)
            return os.path.join("/", img_folder, "unknown", os.path.basename(downloaded_img))

    def handle_unknown_image_format(self, img_url, dest_folder):
        """
        Handle unknown image formats by downloading the image and converting it to webp format.
        """
        prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        file_name = f"image_{prefix}.png"

        downloaded_img = self.download_image(
            img_url,
            file_name,
            dest_folder,
            is_unknown=True
        )
        if not is_valid_image(downloaded_img):
            os.remove(downloaded_img)
            raise Exception(f"Invalid image: {downloaded_img}")
        resize_image(downloaded_img, max_height=600)
        return convert_to_webp(downloaded_img, replace=True)


    def process_entry(self, entry):
        try:
            dest_folder = self.get_dest_folder()
            title = entry.title

            post_url = entry.link

            base_url = post_url.split('?')[0]
            file_name = os.path.basename(os.path.normpath(base_url))
            entry_date = self.get_entry_date(entry)
            content = self.get_content(entry)
            if not content:
                content = self.get_summary(entry)
            tags = self.get_tags(entry)

            are_tags_present = any(str(category).lower() in tags for category in self.filter_categories)
            if are_tags_present:
                content = self.fetch_all_images(content, self.shortname, file_name)
                content = self.generate_markdown_content(title, entry_date, post_url, content, tags)
                
                # Copy the markdown file to the posts folder
                markdown_filename = os.path.join(dest_folder, f"{file_name}.md")
                self.write_to_file(markdown_filename, content)

        except Exception as e:
            print(f"Failed to process entry for {self.subscriber_name}: {e}")
    
    def get_dest_folder(self):
        """
        Get the destination folder
        """
        dest_folder = ALL_POSTS_FOLDER
        os.makedirs(dest_folder, exist_ok=True)
        return dest_folder

    def get_image_name(self, image_url):
        name = os.path.basename(os.path.normpath(image_url))
        image_name = name.replace("..", ".")
        return image_name

    def get_entry_date(self, entry):
        date_formats = [
            "%a, %d %b %Y %H:%M:%S %z",  # Example: Wed, 14 Dec 2022 00:00:00 +0000
            "%a, %d %b %Y %H:%M:%S %Z",  # Example: Wed, 14 Dec 2022 00:00:00 GMT
            "%Y-%m-%dT%H:%M:%SZ",        # Example: 2024-09-04T04:52:11Z
            "%Y-%m-%dT%H:%M:%S%z",       # Example: 2017-09-01T12:09:27+02:00
            "%Y-%m-%d"                   # Example: 2025-01-17
        ]
        
        date_to_parse = entry.get('updated', entry.get('published', None))
        if date_to_parse:
            for date_format in date_formats:
                try:
                    parsed_date = datetime.strptime(date_to_parse, date_format)
                    return parsed_date.strftime("%Y-%m-%dT%H:%M:%S%z")
                except (AttributeError, ValueError):
                    continue
        
        print(f"Date format error: Unable to parse date {date_to_parse}")
        # with open("unprocessed_dates.txt", "a") as f
        # :
        #     f.write(f"Failed to parse date for entry: {entry.get('updated', entry.get('published', None))} \n\n")
        return ""

    def get_summary(self, entry):
        try:
            return entry.summary
        except AttributeError:
            return ""
        
    def get_content(self, entry):
        try:
            return entry.content[0].value
        except AttributeError:
            return None

    def get_tags(self, entry):
        try:
            return [tag.term.lower() for tag in entry.tags]
        except AttributeError:
            return []

    def generate_markdown_content(self, title, entry_date, image_url, summary, tags):
        tags_str = ", ".join([f'"{tag}"' for tag in tags])
        available_lang_str = ", ".join(f'"{str(lang).lower()}"' for lang in self.available_lang)
        return f"""---
source: "blog"
title: "{title}"
date: "{entry_date}"
link: "{image_url}"
draft: "false"
showcase: "planet"
subscribers: ["{self.shortname}"]
author: "{self.subscriber_name}"
tags: [{tags_str}]
languages: ["{self.main_lang.lower()}"]
available_languages: [{available_lang_str}]
---

{summary}
"""

    def write_to_file(self, filename, content):
        with open(filename, "w", encoding="utf=8") as f:
            f.write(content)

    def download_image(self, image_url, image_name, dest_folder, is_unknown=False):
        os.makedirs(dest_folder, exist_ok=True)
        image_filename = os.path.join(dest_folder, image_name)
        if is_unknown:
            response = requests.get(image_url, stream=True)
            with open(image_filename, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
        else:
            response = requests.get(image_url, stream=True)
            content = response.raw
            with open(image_filename, 'wb') as out_file:
                shutil.copyfileobj(content, out_file)
        return image_filename


class FunderProcessor:
    """
    A class to process and fetch funder information from a remote JSON feed.

    This class provides methods to fetch funder data from a specified URL, process each funder entry,
    and generate corresponding markdown files and images for each funder.

    Methods:
        fetch_funders(): Fetches the funder data from the remote JSON feed.
        process_funder(item): Processes a single funder entry and generates the markdown file and image.
    """

    @staticmethod
    def fetch_funders():
        response = requests.get("https://changelog.qgis.org/en/qgis/members/json/")
        data = json.loads(response.text)
        items = data["rss"]["channel"]["item"]
        for item in items:
            FunderProcessor.process_funder(item)

    @staticmethod
    def process_funder(item):
        link = item["member_url"]
        image_url = item["image_url"]
        title = item["title"]
        level = item["member_level"]
        country = item["member_country"]
        start_date = item["start_date"]
        end_date = item["end_date"]

        start_date = date_parse(start_date, fuzzy_with_tokens=True)[0]
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = date_parse(end_date, fuzzy_with_tokens=True)[0]
        end_date = end_date.strftime("%Y-%m-%d")

        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(link))
        image_name = "%s.%s" % (name, image_ext)
        image_name = image_name.replace("..", ".")

        content = f"""---
level: "{level}"
title: "{title}"
logo: "{image_name}"
startDate: "{start_date}"
endDate: "{end_date}"
link: "{link}"
country: "{country}"
---
"""
        markdown_filename = f"content/funders/{name}.md"
        with open(markdown_filename, "w", encoding="utf=8") as f:
            f.write(content)
            print(f"Writing: {markdown_filename}")

        response = requests.get(image_url, stream=True)
        image_filename = f"content/funders/{image_name}"
        with open(image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"Writing: {image_filename}")
        del response
        try:
            if level.lower() in ["flagship", "large"]:
                resize_image(image_filename, max_height=150)
            else:
                resize_image(image_filename)
        except Exception as e:
            print(f"Error resizing image: {e}")


if __name__ == "__main__":
    # Load the subscribers from the JSON file
    with open(SUBSCRIBERS_JSON_PATH, 'r') as f:
        subscribers = json.load(f)

    # Remove all files inside the content/posts folder
    for filename in os.listdir(ALL_POSTS_FOLDER):
        file_path = os.path.join(ALL_POSTS_FOLDER, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    # Iterate over the subscribers and fetch posts for active ones
    i = 1
    for subscriber in subscribers:
        if not subscriber.get('is_active'):
            continue
        print(f"{i}/{len(subscribers)}: Processing feed for {subscriber['name']}")
        languages = subscriber.get('languages', {})
        available_lang = languages.get('available', DEFAULT_AVAILABLE_LANG)
        main_lang = languages.get('main', DEFAULT_MAIN_LANG)
        filter_categories = subscriber.get('filter_categories', DEFAULT_CATEGORIES)
        
        processor = FeedProcessor(
            subscriber['name'],
            subscriber['shortname'],
            subscriber['feed'],
            available_lang,
            main_lang,
            filter_categories
        )
        processor.fetch_and_create_post()
        i += 1
    
    FunderProcessor.fetch_funders()
