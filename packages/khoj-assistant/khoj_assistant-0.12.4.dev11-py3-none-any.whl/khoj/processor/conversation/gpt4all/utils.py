import os
import logging
import requests
import hashlib

from tqdm import tqdm

from khoj.processor.conversation.gpt4all import model_metadata

logger = logging.getLogger(__name__)

expected_checksum = {"llama-2-7b-chat.ggmlv3.q4_K_S.bin": "cfa87b15d92fb15a2d7c354b0098578b"}


def get_md5_checksum(filename: str):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def download_model(model_name: str):
    try:
        from gpt4all import GPT4All
    except ModuleNotFoundError as e:
        logger.info("There was an error importing GPT4All. Please run pip install gpt4all in order to install it.")
        raise e

    url = model_metadata.model_name_to_url.get(model_name)
    model_path = os.path.expanduser(f"~/.cache/gpt4all/")
    if not url:
        logger.debug(f"Model {model_name} not found in model metadata. Skipping download.")
        return GPT4All(model_name=model_name, model_path=model_path)

    filename = os.path.expanduser(f"~/.cache/gpt4all/{model_name}")
    if os.path.exists(filename):
        # Check if the user is connected to the internet
        try:
            requests.get("https://www.google.com/", timeout=5)
        except:
            logger.debug("User is offline. Disabling allowed download flag")
            return GPT4All(model_name=model_name, model_path=model_path, allow_download=False)
        return GPT4All(model_name=model_name, model_path=model_path)

    # Download the model to a tmp file. Once the download is completed, move the tmp file to the actual file
    tmp_filename = filename + ".tmp"

    try:
        os.makedirs(os.path.dirname(tmp_filename), exist_ok=True)
        logger.debug(f"Downloading model {model_name} from {url} to {filename}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get("content-length", 0))
            with open(tmp_filename, "wb") as f, tqdm(
                unit="B",  # unit string to be displayed.
                unit_scale=True,  # let tqdm to determine the scale in kilo, mega..etc.
                unit_divisor=1024,  # is used when unit_scale is true
                total=total_size,  # the total iteration.
                desc=model_name,  # prefix to be displayed on progress bar.
            ) as progress_bar:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    progress_bar.update(len(chunk))

        # Verify the checksum
        if expected_checksum.get(model_name) != get_md5_checksum(tmp_filename):
            logger.error(
                f"Checksum verification failed for {filename}. Removing the tmp file. Offline model will not be available."
            )
            os.remove(tmp_filename)
            raise ValueError(f"Checksum verification failed for downloading {model_name} from {url}.")

        # Move the tmp file to the actual file
        os.rename(tmp_filename, filename)
        logger.debug(f"Successfully downloaded model {model_name} from {url} to {filename}")
        return GPT4All(model_name)
    except Exception as e:
        logger.error(f"Failed to download model {model_name} from {url} to {filename}. Error: {e}", exc_info=True)
        # Remove the tmp file if it exists
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
        return None
