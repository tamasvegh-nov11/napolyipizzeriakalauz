# Nápolyi Pizzéria Kalauz

Magyarországi nápolyi pizzériák statikus, kereshető kalauza.

## Közzététel GitHub Pages-en

A `docs/` mappa a kész weboldal. A repository **Settings → Pages → Build and deployment** részében válaszd a `Deploy from a branch` lehetőséget, a `main` ágat és a `/docs` mappát. A GitHub Free csomagban ehhez nyilvános repository szükséges.

Egyéni domain: `https://napolyipizzeriakalauz.com/`. A GitHub Pages a `main` ág `/docs` mappájából szolgálja ki az oldalt. A `docs/CNAME` fájl a GitHub Pages domainbeállításának része.

Másik domain használatakor a hivatkozások és kanonikus URL-ek újragenerálása:

```bash
SITE_BASE_URL=https://uj-domain.example/ python3 build.py
```

Másik domainhez a `docs/CNAME` fájl tartalmát és a GitHub Pages, valamint a DNS-beállításokat is módosítani kell.

## Keresőeszközök

A ténylegesen elérhető, végleges domain tulajdonjogát ellenőrizd a Google Search Console-ban és a Bing Webmaster Toolsban. Küldd be a `<domain>/sitemap.xml` címet mindkettőben. A sitemap elküldése nem garantál megjelenést a találatok között.

## Tartalomfrissítés

A `data/places.json` csak a nyilvános telephelyadatokat tartalmazza, belső részpontokat nem. Módosítás után futtasd a `python3 build.py` parancsot, és commitold az új `docs/` állományt. A kiemelt helyek, az összes pizzéria oldala, a módszertan és a külön adatlapok statikus HTML-ben is megjelennek. A `blog/` és `kapcsolat/` oldalak addig `noindex` jelzést kapnak, amíg valós tartalom és kapcsolati adat nem kerül rájuk.

A `docs/pizza.jpg` általános illusztráció; a kártyákon az éttermi fotó helyét mockup jelzi. A tényleges fotókhoz az adott helyhez kötött, jogszerű forrás és szükség esetén fotós attribúció szükséges. A generátor a `data/site.css` és `data/pizza.jpg` forrásfájlokat használja.

## Éttermi fotók

A `data/venue-photos.js` a Google Maps JavaScript Places könyvtárával a kártyákon látható éttermet keresi meg név, település és — ha ismert — utca és házszám alapján. Csak egyező hely fotóját jeleníti meg a fotó és a Google Maps forrásmegjelölésével; az egyezés nélkül maradt kártyák képhelye megmarad. A lekérések a látható kártyákra korlátozódnak. A Google-fotók URL-jét és tartalmát a projekt nem menti el.

Az integráció a `data/photo-config.js` fájlban alapértelmezetten ki van kapcsolva. A bekapcsoláshoz külön, a `napolyipizzeriakalauz.com` domainre HTTP referrerrel korlátozott böngészős Google Maps JavaScript API-kulcs szükséges; a szerveroldali Food Atlas kulcsot nem szabad nyilvánosan megjeleníteni. A kulcs projektjében a Maps JavaScript API és Places API (New) hozzáférést engedélyezni kell. Ez a megoldás Google Maps Platform díjköteles lekéréseket indíthat.
