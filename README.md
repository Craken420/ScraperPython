# 📚 Python Book Scraper Service

Este repositorio contiene un servicio simple en Python que realiza *web scraping* de libros desde un sitio web de ejemplo usando `requests` y `BeautifulSoup`.

## 🚀 Funcionalidad

- Extrae información de libros (título y precio) desde páginas como [Books to Scrape](http://books.toscrape.com/).
- Organizado como servicio, fácilmente adaptable a otros dominios o ampliable como una API REST.
- Código limpio y comentado, ideal como punto de partida para proyectos de scraping más grandes.

## 🧠 Tecnologías utilizadas

- [Python 3](w)
- [requests](w)
- [BeautifulSoup](w) (bs4)

## 🧩 Estructura del proyecto

```
book_scraper_service/
├── scraper/
│   ├── __init__.py
│   └── book_scraper.py
├── main.py
├── requirements.txt
└── README.md
```

## 📄 Ejemplo de uso

```python
from scraper.book_scraper import scrape_books_from_url

url = "http://books.toscrape.com/"
books = scrape_books_from_url(url)

for book in books:
    print(f"{book['title']} - {book['price']}")
```

## 🔧 Instalación

```bash
git clone https://github.com/tu-usuario/book-scraper-service.git
cd book-scraper-service
pip install -r requirements.txt
python main.py
```

## 📚 Fuente de prueba

Este scraper está diseñado para funcionar con el sitio de prueba [Books to Scrape](http://books.toscrape.com/), una plataforma pública para prácticas de scraping.

## 📝 Licencia

Este proyecto está licenciado bajo la MIT License.
