# ChirieAuto - Website Static pentru Huse Auto

Un website static responsiv pentru vânzarea de huse auto premium, construit cu HTML, TailwindCSS și JavaScript vanilla.

## Structura Proiectului

```
dist/
├── index.html              # Homepage principală
├── brand.html              # Pagina de selecție model/an
├── produse.html            # Catalogul produselor
├── assets/
│   ├── app.js              # JavaScript pentru întreaga aplicație
│   ├── catalog.json        # Date despre branduri, modele și produse
│   ├── logos/              # Logo-uri SVG pentru branduri auto
│   │   ├── bmw.svg
│   │   ├── audi.svg
│   │   └── mercedes.svg
│   └── img/
│       └── product-placeholder.svg  # Placeholder pentru imagini produse
└── README.md               # Această documentație
```

## Tehnologii Utilizate

- **HTML5**: Structura semantică
- **TailwindCSS**: Styling responsiv via CDN
- **JavaScript Vanilla**: Logica aplicației
- **Inter Font**: Tipografia modernă
- **SVG**: Iconografie și logo-uri

## Funcționalități

### Homepage (index.html)
- **Hero Section**: Banner portocaliu cu CTA
- **Beneficii Produs**: Secțiune cu avantajele huselor
- **Selector Branduri**: Grid cu logo-uri branduri auto
- **Avantaje**: Trei carduri cu iconuri (livrare rapidă, durabilitate, prețuri)
- **Statistici**: Contori animate (545+ comenzi, 24h livrare, etc.)
- **Formular CTA**: Secțiune de întrebări

### Pagina Brand (brand.html)
- **Header Brand**: Logo și nume brand selectat
- **Filtre**: Dropdown-uri pentru model și an
- **Validare**: Verifică compatibilitatea model/an
- **Navigare**: Buton "Vezi produse" către catalog

### Catalog Produse (produse.html)
- **4 Categorii Produse**:
  1. Huse Eco Piele+Alcantara
  2. Huse Eco Piele
  3. Huse Eco Piele (Romb)
  4. Huse Alcantara (Romb)
- **Filtrare**: Model și an modificabile
- **Selecție Produs**: Click pentru a selecta
- **Rezumat Comandă**: Sticky bottom cu detalii
- **Acțiuni**: Comandă + linkuri WhatsApp/Telegram/Viber

## Flux de Utilizare

1. **Homepage**: Utilizatorul vede oferta și selectează un brand
2. **Brand Page**: Alege modelul și anul mașinii
3. **Products Page**: Navighează prin categorii și selectează o husă
4. **Order**: Completează telefonul și plasează comanda

## Stocare Date

### LocalStorage
```javascript
{
  "selectedBrand": {"id": "bmw", "name": "BMW"},
  "selectedModel": "Seria 5",
  "selectedYear": "2020",
  "orders": [...],
  "lastOrder": {...}
}
```

### URL Parameters
```
brand.html?brand=BMW
produse.html?brand=BMW&model=Seria%205&year=2020
```

## Schema Date (catalog.json)

```json
{
  "brands": [
    {
      "id": "bmw",
      "name": "BMW",
      "logo": "/assets/logos/bmw.svg",
      "models": [
        {
          "name": "Seria 5",
          "years": [2015, 2016, 2017, 2018, 2019, 2020]
        }
      ]
    }
  ],
  "productGroups": [
    {"id": "eco_alc", "title": "Huse Eco Piele+Alcantara"}
  ],
  "products": [
    {
      "id": "ALC-R1",
      "groupId": "alc_romb",
      "title": "Husa Alcantara (Romb)",
      "code": "ALC-R1",
      "color": "Negru + Negru",
      "price": 4300,
      "image": "/assets/img/alc-romb-negru.png"
    }
  ]
}
```

## Rulare Locală

### Opțiunea 1: Deschidere Directă
```bash
# Navighează în directorul dist/
cd dist/

# Deschide index.html în browser
open index.html
# sau pe Windows:
start index.html
# sau pe Linux:
xdg-open index.html
```

### Opțiunea 2: Server Local (Recomandat)
```bash
# Cu Python 3
cd dist/
python -m http.server 8000

# Cu Node.js (dacă ai instalat serve)
npx serve dist/

# Cu PHP
cd dist/
php -S localhost:8000
```

Apoi accesează: `http://localhost:8000`

## Customizare

### Culori
Culoarea principală (#F7941E) poate fi modificată în:
- CSS custom properties
- Clasele Tailwind `bg-[#F7941E]` și `text-[#F7941E]`

### Conținut
- **Branduri**: Editează `assets/catalog.json` - secțiunea `brands`
- **Produse**: Editează `assets/catalog.json` - secțiunea `products`
- **Texte**: Modifică direct în fișierele HTML

### Contact
- **Telefon**: Schimbă `+373 68237082` în toate fișierele
- **WhatsApp**: Actualizează numărul în `app.js` funcția `openWhatsApp`

## Responsive Design

- **Mobile**: 360px+ (grid 2 coloane produse, navbar compact)
- **Tablet**: 768px+ (grid 3-4 coloane, meniu vizibil)
- **Desktop**: 1024px+ (layout complet, max-width 1200px)

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Accessibility

- **Keyboard Navigation**: Tab index logic
- **Screen Readers**: Aria labels și text alternativ
- **Focus Management**: Ring indicators vizibile
- **Color Contrast**: Respectă standardele WCAG

## Performance

- **Lazy Loading**: Imaginile se încarcă la cerere
- **Bundle Size**: ~15KB JavaScript comprimat
- **Load Time**: <3s pe conexiuni 3G

## Contacte de Suport

Pentru modificări sau întrebări tehnice:
- Email: support@chirieauto.md
- Telefon: +373 68237082

---

**Versiune**: 1.0.0  
**Ultima actualizare**: noiembrie 2024