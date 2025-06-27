from playwright.async_api import async_playwright

URL = "http://books.toscrape.com/"

async def scrap_books(max_pages=None):
    print("🟢 Iniciando scraping con control de páginas...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        all_books = []
        current_page = 1

        while True:
            print(f"Scrapeando página {current_page}...")

            titles = await page.eval_on_selector_all(
                "article.product_pod h3 a",
                "elements => elements.map(el => el.getAttribute('title'))"
            )
            prices = await page.eval_on_selector_all(
                "article.product_pod .price_color",
                "elements => elements.map(el => el.textContent.trim())"
            )
            availability = await page.eval_on_selector_all(
                "article.product_pod .availability",
                "elements => elements.map(el => el.textContent.trim())"
            )

            for t, p, a in zip(titles, prices, availability):
                all_books.append({
                    "title": t,
                    "price": p,
                    "availability": a
                })

            # Revisamos si hay botón 'next' y si queremos seguir scrapeando
            next_button = await page.query_selector("li.next a")
            if not next_button:
                print("No hay más páginas. Terminando scraping.")
                break

            if max_pages is not None and current_page >= max_pages:
                print(f"Se alcanzó el límite de {max_pages} páginas. Terminando scraping.")
                break

            # Hacemos click en next y esperamos que cargue la siguiente página
            await next_button.click()
            await page.wait_for_load_state("domcontentloaded")
            await page.wait_for_timeout(2000)
            current_page += 1

        await browser.close()
        print(f"✅ Scraping completado. Total libros: {len(all_books)}")
        return all_books
