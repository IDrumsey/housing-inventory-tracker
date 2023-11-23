import requests


def print_progress_bar(progress: int, total_length=50):
    """
    Prints a progress bar indicating progress like the following

    ====
    ============
    ===================
    """

    percentage = min(max(0, round(progress, 2)), 100)

    filled_length = int(total_length * percentage // 100)
    bar = "=" * filled_length + "-" * (total_length - filled_length)

    print(f"Progress: |{bar}| {percentage}%", end="\r")


def download_latest(source_url: str, destination_uri: str):
    """
    Downloads the latest data from the url
    """

    with requests.get(source_url, stream=True) as response:
        print(f"{response.status_code}: {response.url}")

        # keep track of the progress
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        progress = 0

        # save content
        with open(destination_uri, "wb") as file:
            for chunk in response.iter_content(chunk_size=block_size):
                file.write(chunk)
                progress += len(chunk)
                percentage_downloaded = 100 * (progress / total_size)

                print_progress_bar(percentage_downloaded)

            print()
