# Nápolyi Pizzéria Kalauz

Magyarországi nápolyi pizzériák statikus, kereshető kalauza.

## Közzététel GitHub Pages-en

A `docs/` mappa a kész weboldal. A repository **Settings → Pages → Build and deployment** részében válaszd a `Deploy from a branch` lehetőséget, a `main` ágat és a `/docs` mappát. A GitHub Free csomagban ehhez nyilvános repository szükséges.

Alapértelmezett cím: `https://tamasvegh-nov11.github.io/napolyipizzeriakalauz/`.

Miután az új domaint megvetted és beállítottad GitHub Pages-ben, a hivatkozások és kanonikus URL-ek újragenerálása:

```bash
SITE_BASE_URL=https://napolyipizzeriakalauz.hu/ python3 build.py
```

Ezt követően a `docs/CNAME` fájlba csak a domainnév kerül (`napolyipizzeriakalauz.hu`), és a DNS-t a GitHub Pages hivatalos útmutatója szerint kell beállítani. A domain beállítása előtt ne hozz létre CNAME fájlt. A korábbi github.io címről az új domainre történő átálláskor ellenőrizd a canonical és sitemap URL-eket.

## Keresőeszközök

A ténylegesen elérhető, végleges domain tulajdonjogát ellenőrizd a Google Search Console-ban és a Bing Webmaster Toolsban. Küldd be a `<domain>/sitemap.xml` címet mindkettőben. A sitemap elküldése nem garantál megjelenést a találatok között.

## Tartalomfrissítés

A `data/places.json` csak a nyilvános telephelyadatokat tartalmazza, belső részpontokat nem. Módosítás után futtasd a `python3 build.py` parancsot, és commitold az új `docs/` állományt. A kiemelt helyek, az összes pizzéria oldala, a módszertan és a külön adatlapok statikus HTML-ben is megjelennek. A `blog/` és `kapcsolat/` oldalak addig `noindex` jelzést kapnak, amíg valós tartalom és kapcsolati adat nem kerül rájuk.

A `docs/pizza.jpg` általános illusztráció; a kártyákon az éttermi fotó helyét mockup jelzi. A tényleges fotókhoz az adott helyhez kötött, jogszerű forrás és szükség esetén fotós attribúció szükséges. A generátor a `data/site.css` és `data/pizza.jpg` forrásfájlokat használja.
