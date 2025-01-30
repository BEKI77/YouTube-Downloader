# YouTube Video Downloader (YTD)

This is a Django-based web application that allows users to download YouTube videos by providing a link. The application lists available formats for the video and allows the user to select and download the desired format.

## Features

- Paste a YouTube link to get available download formats.
- Select a format and download the video.
- Responsive design using custom CSS.

## Project Structure
![First page](/public/Img1.png)

![Search Result](/public/Img2.png)


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/BEKI77/YouTube-Downloader.git
    cd YouTube-Downloader
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

5. Open your web browser and navigate to `http://127.0.0.1:8000/youtube`.

## Usage

1. Paste the YouTube link in the input field and click "Search".
2. Select the desired format from the list of available formats.
3. Click "Download" to download the video in the selected format.

## Files

- [manage.py](http://_vscodecontentref_/11): Django's command-line utility for administrative tasks.
- [settings.py](http://_vscodecontentref_/12): Django settings for the project.
- [urls.py](http://_vscodecontentref_/13): URL configuration for the project.
- [views.py](http://_vscodecontentref_/14): Contains the view functions for handling requests.
- [youtube.html](http://_vscodecontentref_/15): HTML template for the YouTube downloader page.
- [styles.css](http://_vscodecontentref_/16): CSS styles for the application.

## Dependencies

- Django
- yt-dlp

## License

This project is licensed under the MIT License.