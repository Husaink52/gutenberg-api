# Gutenberg‑API 📚

A RESTful web service to expose [Project Gutenberg](https://www.gutenberg.org/) metadata — built with **Django**, **Django REST Framework**, and a **MySQL** database.

This API provides structured, queryable access to metadata for over 60,000 free eBooks from Project Gutenberg. Developers can retrieve book titles, authors, formats, subjects, languages, and more — perfect for digital libraries, cataloguing tools, educational apps, or search interfaces.

---

## 🎯 Project Overview

### Features

- ✅ Parses RDF metadata from Project Gutenberg’s official nightly RDF dump
- ✅ Extracts structured information on books, authors, formats, languages, and subjects
- ✅ Loads data into a relational database for efficient querying
- ✅ Offers a clean, well-documented REST API using Django REST Framework
- ✅ Supports pagination, filtering, search, and sorting
- ✅ Deployable to the cloud with Railway (MySQL) and Render (App server)

### Key Endpoints

- `GET /books/` — paginated list of books with filtering options
- `GET /books/<id>/` — detailed info for a single book
- `GET /authors/` — author details and their works
- `GET /subjects/` — explore books by subject
- `GET /languages/` — available books by language
- `GET /formats/` — see downloadable file formats

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **Django 4.x**
- **Django REST Framework**
- **MySQL**
- **Gunicorn** for production WSGI
- **Render** for deployment
- **Railway** for database hosting

---

## 🚀 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Husaink52/gutenberg-api.git
cd gutenberg-api
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
