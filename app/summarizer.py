import asyncio

import nltk
from app.models.tortoise import TextSummary
from newspaper import Article


async def generate_summary(summary_id: int, url: str) -> None:
    """Generate summary."""
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    finally:
        article.nlp()

    summary = article.summary
    await asyncio.sleep(10)

    await TextSummary.filter(id=summary_id).update(summary=summary)
