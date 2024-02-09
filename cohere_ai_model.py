import cohere
import os
from dotenv import load_dotenv
import logging
from util import wikipedia_helper
from datetime import datetime

from util.utility import hashtagify

load_dotenv()
co = cohere.Client(os.environ.get("CO_KEY"))

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(asctime)s %(message)s at %(lineno)s",
    # filename=logfile_path,
    # filemode="a",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info(f"Program started at {datetime.now()}")


def search(message: str, documents: list[dict[str, str]] = []):
    response = co.chat(
        model="command",
        message=message,
        return_chat_history=True,
        documents=documents,
        prompt_truncation="AUTO",
    )
    return response


def create_post(
    topic: str,
    social_media_company: str,
):
    query_for_cohere = f"Generate a {social_media_company} Marketing post for {topic}"

    wiki_content = wikipedia_helper.get_wikipedia_data(term=topic)

    response = search(
        message=query_for_cohere,
        documents=[{"title": wiki_content.title, "snippet": wiki_content.content}],
    )
    return {
        "text": response.text,
        "images": wiki_content.images,
        "link": wiki_content.url,
        "title": wiki_content.original_title,
        "hashtags": hashtagify(wiki_content.categories),
        "refs": wiki_content.references[:5],
    }


if __name__ == "__main__":
    logger.debug("main function started")
    topic = "Apple Vision Pro"
    social_media_company = "LinkedIn"
    response = create_post(topic, social_media_company)
    cohere_response = response.text
    print(cohere_response)
