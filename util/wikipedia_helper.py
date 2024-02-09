import wikipedia
import logging

logging.basicConfig(
    # filemode="w",
    # filename=os.path.join(os.path.curdir, "runlog.log"),
    level=logging.INFO,
    format="%(levelname)s %(module)s %(message)s",
)
logger = logging.getLogger(__name__)

wikipedia.set_lang("en")


def get_wikipedia_data(term: str):
    items = wikipedia.search(term)
    logger.info(f"wikipedia search {term}; items {len(items)=}")
    if not items:
        raise ValueError(f"{term} is not found, try another value")
    for item in items:
        try:
            page = wikipedia.page(item)
            return page
        except Exception as ex:
            pass
    else:
        raise ValueError(f"{term} is not found, try another value")
