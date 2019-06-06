# Django Image Cropper

## Start Application

1. Start virtual environment and install requirements.txt
    ```bash
    pip install -r requirements.txt
    ```
2. Install cropper and jquery dependencies
    ```bash
    npm install
    ```
3. Apply all migrations
    ```bash
    python manage.py migrate
    ```
4. Collect staticfiles
    ```bash
    python manage.py collectstatic
    ```
    If you want to change path of static folders change path in [settings](src/django_image_cropper/settings.py#L127).
5. Run application
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
    Browse [image cropper](http://127.0.0.1:8000)