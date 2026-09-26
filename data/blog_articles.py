"""Original editorial articles for the public blog."""

from textwrap import dedent

ARTICLES = [
    {
        "slug": "elso-latogatas-napolyi-pizzeriaban",
        "title": "Először jársz egy nápolyi pizzériában? Ezzel a pizzával kezdd",
        "description": "Marinara vagy Margherita? Gyakorlati útmutató ahhoz, mit érdemes megfigyelni egy új nápolyi pizzériában a tésztától a feltétekig.",
        "teaser": "Miért érdemes elsőre Marinarát vagy Margheritát rendelni, és mit figyelj a tésztán, a sütésen és az ízek egyensúlyán?",
        "date": "2026-09-26",
        "reading": "5 perc olvasás",
        "body": dedent("""\
            <p class="lead">Új pizzériában könnyű rögtön a legizgalmasabb feltétekkel kezdeni. Ha azonban arra vagy kíváncsi, milyen az alap, rendelj először egy Marinarát vagy egy Margheritát. Ezeken a pizzákon kevesebb íz mögé lehet elbújni: jobban érezni a tésztát, a paradicsomot és a sütést.</p>

            <h2>Marinara, ha tényleg az alapokat kóstolnád</h2>
            <p>A Marinara a paradicsom, a fokhagyma, az oregánó és az olaj találkozása a tésztán. Nincs rajta sajt, ezért tisztán érezhető, hogy a paradicsom frissnek vagy tompának hat-e, a fokhagyma jól illeszkedik-e hozzá, és a tészta önmagában is ízletes-e. Ez jó választás akkor is, ha a sajtot nem szeretnéd az első benyomásba bevonni.</p>
            <p>Nem kell laboratóriumi vizsgálatot végezni a tányér fölött. Egyél meg néhány falatot a közepéből, majd a pereméből is. Ha minden falatban jól működik a paradicsom és a tészta, már van mihez viszonyítanod a hely többi pizzáját.</p>

            <h2>Margherita, ha a teljesebb képet keresed</h2>
            <p>A Margheritán a paradicsom mellé sajt, bazsalikom és olaj kerül. Itt azt is megfigyelheted, hogy a feltétek mennyisége mennyire illik a tésztához. Jó, ha a sajt és a paradicsom egyszerre érvényesül, és a közepe a feltéttől sem válik nyers, nehéz masszává.</p>
            <p>A két alapváltozat közül válaszd azt, amelyiket szívesebben ennéd meg. A lényeg nem egy kötelező vizsga, hanem hogy az első rendelésnél is legyen esélyed megismerni a pizzéria saját stílusát.</p>

            <h2>Nézd meg a peremet, és emeld fel egy pillanatra</h2>
            <p>A nápolyi pizzára jellemző a levegős, megemelkedett perem és a vékonyabb, puhább közép. Harapj bele a perembe: az állaga legyen kellemes és megsült, ne ragacsos nyers tészta. Az alját is érdemes egy pillanatra megnézni. A szépen sült felület és néhány sötétebb pont más, mint a nagy felületen keserűre égett alj.</p>
            <p>A frissen érkező pizzát kóstold meg előbb úgy, ahogy felszolgálták. Az olajjal, csípőssel vagy más kiegészítőkkel később is kísérletezhetsz. Ha az első néhány falat tetszik, legközelebb bátran jöhet egy összetettebb feltétű pizza.</p>

            <h2>Egy látogatás jó kezdet, nem végső ítélet</h2>
            <p>Az élményt a saját ízlésed, a választott pizza és az adott napi sütés is befolyásolja. Ne várd, hogy minden nápolyi pizzéria pontosan ugyanazt adja. Ha egy hely felkeltette az érdeklődésedet, nézz vissza egy másik alkalommal, és próbálj ki még egy pizzát. A <a href="https://napolyipizzeriakalauz.com/pizzeriak/">kereshető pizzérialistában</a> város és minősítés szerint is böngészhetsz.</p>

            <p class="article-source">Szakmai háttér: az <a href="https://www.pizzanapoletana.org/it/decalogo" target="_blank" rel="noopener noreferrer">AVPN tízpontos útmutatója</a> a klasszikus feltéteket, a puha állagot, a peremet és a sütés jellemzőit is leírja. A fenti kóstolási tippek szerkesztői javaslatok, nem minősítési feltételek.</p>
        """),
    },
    {
        "slug": "miert-puha-a-napolyi-pizza",
        "title": "Miért puha a nápolyi pizza közepe? Amit az első falat előtt érdemes tudni",
        "description": "A nápolyi pizza puha közepéről, levegős pereméről és sütéséről közérthetően. Mi számít a stílus részének, és mi az, amire valóban figyelj?",
        "teaser": "A nápolyi pizza másképp hajlik és másképp sül, mint a ropogós szeletpizza. Megmutatjuk, miért nem hiba önmagában a puha közép.",
        "date": "2026-09-26",
        "reading": "4 perc olvasás",
        "body": dedent("""\
            <p class="lead">Ha a pizzáról a ropogós, merev szelet jut eszedbe, a nápolyi változat meglephet. A közepe vékonyabb és puhább, a széle magasabb és levegősebb. A szelet hajlítható; ezt a stílust nem érdemes ugyanazzal a mércével nézni, mint egy egészen más pizzát.</p>

            <h2>A közép és a perem kétféle élményt ad</h2>
            <p>A tésztát kézzel nyújtják, a levegőt pedig a széle felé terelik. Sütéskor a perem megemelkedik, míg a közép vékony marad, hogy a feltéteknek legyen helye. Emiatt a pizzát tányérról, késsel és villával is kényelmes enni, de összehajtott szeletként is megkóstolhatod.</p>
            <p>A puha közép önmagában nem azt jelenti, hogy a pizza nyers. Az számít, hogy a tészta megsült-e, az íze kellemes-e, és a feltét nem áztatja-e el annyira, hogy az egész szétessen. A stílusra jellemző hajlékonyság és a kellemetlenül ragacsos állag között van különbség.</p>

            <h2>Mi történik a sütőben?</h2>
            <p>A nápolyi stílus egyik sajátossága a magas hőfokon, rövid ideig tartó sütés. Az AVPN hagyományos, fatüzelésű eljárást leíró útmutatója 60–90 másodperces sütési időt ad meg. Ez segít megérteni, miért nem olyan a végeredmény, mint a hosszabban sütött, egyenletesen ropogós pizzáké. A pizzériák gyakorlata és felszerelése eltérhet; egy jó pizzát nem lehet pusztán egyetlen sütési adatból megítélni.</p>
            <p>A peremen megjelenhetnek sötétebb foltok. Figyeld inkább az összhatást: érezhető-e kellemesen a megsült tészta, vagy az égett, keserű íz uralja? A saját ízlésed is számít. Ha a nagyon puha pizza nem a te világod, attól még nem rendeltél „rosszul”, egyszerűen lehet, hogy más stílust kedvelsz.</p>

            <h2>Hogyan kóstold meg először?</h2>
            <p>Frissen, helyben fogyasztva a legkönnyebb megérteni, milyen állagra törekedett a pizzéria. Kóstold meg a közepét és a peremét külön is, majd nézd meg, hogy a paradicsom, a sajt és a tészta együtt működik-e. Ha most próbálod először, az <a href="https://napolyipizzeriakalauz.com/blog/elso-latogatas-napolyi-pizzeriaban/">első látogatáshoz írt útmutatónkban</a> segítünk választani a Marinara és a Margherita között.</p>

            <p class="article-source">Szakmai háttér: az <a href="https://www.pizzanapoletana.org/it/ricetta_pizza_napoletana" target="_blank" rel="noopener noreferrer">AVPN nápolyi pizza leírása</a> és a <a href="https://www.pizzanapoletana.org/it/decalogo" target="_blank" rel="noopener noreferrer">tízpontos útmutató</a>. A cikk a stílus jellemzőit magyarázza, nem egy étterem AVPN-tanúsítványát állítja.</p>
        """),
    },
    {
        "slug": "hogyan-ertekelj-ettermet-igazsagosan",
        "title": "Hogyan értékelj igazságosan egy éttermet?",
        "description": "Hogyan írj pontos és hasznos éttermi értékelést? Hibák, csillagok, kiszállítás, személyes ízlés és jó visszajelzés közérthetően.",
        "teaser": "Egy rossz élmény után is lehet pontosan és hasznosan értékelni. Így különítheted el a hibát, a személyes ízlést és az egész éttermi élményt.",
        "date": "2026-09-26",
        "reading": "6 perc olvasás",
        "body": dedent("""\
            <p class="lead">Egy csillag, két dühös mondat, küldés. Neked ez fél perc; egy étterem online megítélésében jóval tovább látszódhat. A rossz tapasztalatot természetesen megírhatod. Az igazán hasznos értékelés azonban megmutatja, pontosan mi történt, és segít a következő vendégnek dönteni.</p>

            <h2>Mit jelent az egy csillag?</h2>
            <p>Az ötcsillagos rendszerekben az egy csillag a legalacsonyabb érték. Nem feltétlenül azt fejezi ki, hogy valami apróság nem sikerült, hanem azt, hogy az élményed egészét nagyon rossznak ítéled. Ez nem tiltott pontszám: ha a tapasztalatod valóban elfogadhatatlan volt, teljesen helyénvaló lehet.</p>
            <p>Mielőtt rányomsz, gondold végig, hogy az egész vacsora ilyen volt-e. Az étel, a kiszolgálás, az ár és a probléma kezelése közül mi működött, és mi nem? Az egyes részletek megnevezése többet mond, mint egy önmagában álló csillag.</p>

            <h2>Ha hiba történt, a reakció is számít</h2>
            <p>Hiányozhat egy feltét, érkezhet másik köret, vagy egy forgalmas estén tovább tarthat az étel elkészítése. Egy hiba kellemetlen, de abból is sokat megtudhatsz a helyről, hogy mit tesznek, amikor szólsz. Kijavítják? Kicserélik az ételt? Bocsánatot kérnek, vagy felajánlanak ésszerű megoldást?</p>
            <p>Ha van rá lehetőség, jelezd a problémát még ott, vagy vedd fel a kapcsolatot az ügyfélszolgálattal. A megoldásra adott esély nem kötelez arra, hogy később jó értékelést adj. Arra viszont lehetőséget ad, hogy a visszajelzésed a teljes történetet mutassa be.</p>

            <h2>Kiszállításnál kihez tartozott a hiba?</h2>
            <p>Kiszállításkor több szereplő vesz részt abban, hogy az étel megérkezzen. Az étterem készíti és csomagolja, a futár vagy a platform pedig továbbítja. Ha rossz fogást készítettek, az az étterem hibája lehet. Ha a csomag útközben sérült meg, sokat késett vagy kihűlt, előbb érdemes megtudni, hol akadt el a folyamat.</p>
            <p>Képzeld el, hogy a pizza forrón kerül a futárhoz, de hosszú út után hidegen érkezik meg. A csalódottságod teljesen érthető, ugyanakkor az étterem felelőssége az átadás körülményeitől függ. Előfordulhat az ellenkezője is: az étel már az étteremben sokáig állt. Ha ezt nem tudod biztosan, írd le a megfigyelhető tényt, és jelezd a problémát a platformnak is.</p>

            <h2>Írd le, amit valóban tapasztaltál</h2>
            <p>A „Finom volt a pizza, de negyven percet vártunk rá” sokkal többet segít a következő vendégnek, mint a „Szörnyű! Egy csillag!”. Írhatsz az ételről, a kiszolgálásról, a hangulatról és arról is, hogy az ár megfelelt-e az élményednek. Ha valami rosszul sikerült, különösen hasznos leírni, miként reagált rá a hely.</p>
            <p>A személyes ízlésedet is érdemes elválasztani az elkészítéstől. A nápolyi pizza például puhább és hajlíthatóbb lehet, mint amit egy ropogós pizzától várnál. Teljesen rendben van, ha ez neked nem ízlik; az olvasónak viszont többet segít, ha leírod, hogy ez a stílus nem a kedvenced, és azt is, ha konkrét elkészítési hibát tapasztaltál.</p>

            <h2>Csillagok és szavak együtt</h2>
            <p>Nincs minden platformon és minden embernél érvényes csillagszótár. Támpontként az öt csillag kiemelkedő, a négy jó, a három vegyes, a kettő jelentős hibákkal terhelt, az egy pedig nagyon rossz vagy elfogadhatatlan élményt jelenthet. A szöveges magyarázat azért fontos, mert ugyanaz a csillagszám két teljesen különböző estét takarhat.</p>
            <p>Beküldés előtt kérdezd meg magadtól: valóban az étterem okozta a problémát? Jeleztem, ha lehetett? Hogyan reagáltak? Az egész élményem megfelel a választott pontszámnak? Ha ezek után is egy csillagot tartasz pontosnak, írd meg nyugodtan, miért.</p>

            <p class="article-pull"><strong>A jó értékelés a következő vendégnek segít dönteni.</strong> Légy őszinte: írd le a rosszat és a jót is. A hibák előfordulnak; az, ahogyan egy étterem kezeli őket, az élmény része.</p>
            <p>A pizzéria kiválasztásához az <a href="https://napolyipizzeriakalauz.com/pizzeriak/">országos keresőben</a> böngészhetsz. A kalauz minősítéseinek külön módszertanát <a href="https://napolyipizzeriakalauz.com/modszertan/">itt olvashatod el</a>; ez a cikk vendégeknek szóló tanács, nem a kalauz pontozási szabályzata.</p>
        """),
    },
]
