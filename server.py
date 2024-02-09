from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging

import uvicorn
from util import utility
import cohere_ai_model
from util.models import SocialMediaPostRequest

app = FastAPI()

logging.basicConfig(
    # filemode="w",
    # filename=os.path.join(os.path.curdir, "runlog.log"),
    level=logging.INFO,
    format="%(levelname)s %(module)s %(message)s",
)
logger = logging.getLogger(__name__)

@app.get("/")
def index() -> HTMLResponse:
    index_html = utility.read_file("./index.html")
    return HTMLResponse(content=index_html, status_code=200)


@app.post("/create_post")
async def create_post(request: SocialMediaPostRequest):
    try:
        response = cohere_ai_model.create_post(
            topic=request.product,
            social_media_company=request.platform,
        )
        return response
    except Exception as err:
        return {
        "text": str(err),
        "images": [],
        "link": "#",
        "title": f"Error:{err}",
        "hashtags": [],
        "refs": [],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
