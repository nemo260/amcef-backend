# Amcef testovacie zadanie

## Inštalacia
Pre testovanie je potrebne mať vytvorenú lokálnu PostgreSQL databázu a v settings.py v DATABASE vyplniť údaje alebo vytvoriť .env súbor

Následne nainštalovať:

```bash
pip install django-environ
```
```bash
pip install requests
```
Po uspešnom nainštalovaní stačí zapnúť server:
```bash
py manage.py runserver 127.0.0.1:7000
```
## API Dokumentácia
Na testovanie endpointov som využil Postman, v ktorom som vygeneroval dokumentáciu: [API Documentation](https://documenter.getpostman.com/view/20139116/Uz5GnbAg)
