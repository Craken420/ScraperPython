from playwright.async_api import async_playwright

URL = "http://books.toscrape.com/"

async def scrap_books():
    print("🟢 Iniciando scraping de libros...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # Extrae los títulos de los libros
        titles = await page.eval_on_selector_all(
            "article.product_pod h3 a",
            "elements => elements.map(el => el.getAttribute('title'))"
        )

        # Extrae los precios de los libros
        prices = await page.eval_on_selector_all(
            "article.product_pod .price_color",
            "elements => elements.map(el => el.textContent.trim())"
        )

        # Extrae la disponibilidad
        availability = await page.eval_on_selector_all(
            "article.product_pod .availability",
            "elements => elements.map(el => el.textContent.trim())"
        )

        await browser.close()

        books = []
        for i in range(len(titles)):
            books.append({
                "title": titles[i],
                "price": prices[i],
                "availability": availability[i],
            })

        print(f"✅ Extracción completada, libros encontrados: {len(books)}")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['title']} - {book['price']} - {book['availability']}")
        return books
