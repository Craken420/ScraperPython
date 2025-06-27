from fastapi import FastAPI
from scraper import scrap_books

app = FastAPI()

@app.get("/scrape-books")
async def scrape_books():
    books = await scrap_books()
    return books
