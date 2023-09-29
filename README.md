
## Setup:

1. Run `pip install -r requirements.txt` inside the downloaded folder.
2. run this code
    ```
    pip install TikTokApi
    python -m playwright install
    ```
3. Setup the [Youtube Data Api](https://developers.google.com/youtube/v3), [Setup Credentials](https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials)


    To configure the YouTube Data API for uploading videos using Python, you will need to:

    1. **Create a Google Cloud Platform project and enable the YouTube Data API.** You can do this by going to the Google Cloud Platform Console: https://console.cloud.google.com/ and selecting your project. Then, go to the **APIs & Services** page and click **Enable API** for the **YouTube Data API v3**.
    2. **Create OAuth 2.0 credentials.** You will need to create OAuth 2.0 credentials for your application to authenticate with the YouTube Data API. You can do this by going to the **Credentials** page and clicking **Create Credentials** > **OAuth client ID**. Select the **Web application** application type and click **Create**.

    We required that `client_secrets.json` file, download it


6. Run the main.py script !

