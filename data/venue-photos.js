(() => {
  'use strict';

  const key = window.NP_GOOGLE_MAPS_API_KEY;
  if (!key) return;

  const normalize = text => String(text || '')
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLocaleLowerCase('hu').replace(/[^a-z0-9]+/g, ' ').trim();
  const ignore = new Set(['pizza', 'pizzeria', 'napolyi', 'napoletana', 'di', 'the', 'etterem']);
  const tokens = text => normalize(text).split(' ').filter(t => t.length > 2 && !ignore.has(t));
  const results = new Map();
  const pending = [];
  let active = 0;
  let Place;
  const ID_CACHE_DAYS = 30;
  const idCacheKey = id => `np:place-id:v1:${id}`;

  function savedPlaceId(id) {
    try {
      const saved = JSON.parse(localStorage.getItem(idCacheKey(id)) || 'null');
      if (saved?.placeId && saved.expires > Date.now()) return saved.placeId;
      localStorage.removeItem(idCacheKey(id));
    } catch { /* Browsers can disable local storage. */ }
    return null;
  }

  function savePlaceId(id, placeId) {
    try {
      localStorage.setItem(idCacheKey(id), JSON.stringify({
        placeId, expires: Date.now() + ID_CACHE_DAYS * 24 * 60 * 60 * 1000
      }));
    } catch { /* Continue without local storage. */ }
  }

  function forgetPlaceId(id) {
    try { localStorage.removeItem(idCacheKey(id)); } catch { /* Ignore. */ }
  }

  function matches(candidate, name, city, address) {
    const foundName = normalize(candidate.displayName);
    const foundAddress = normalize(candidate.formattedAddress);
    const nameTokens = tokens(name);
    if (!nameTokens.length || !foundName.includes(nameTokens[0])) return false;
    if (!foundAddress.includes(normalize(city))) return false;

    if (address) {
      const street = tokens(address).find(t => !/^\d/.test(t));
      const house = normalize(address).match(/\b\d+[a-z]?\b/);
      if (street && !foundAddress.includes(street)) return false;
      if (house && !foundAddress.includes(house[0])) return false;
    } else if (nameTokens.length > 1 &&
               !nameTokens.slice(1).some(t => foundName.includes(t))) {
      return false;
    }
    return true;
  }

  async function fetchPlace(el) {
    const { placeName: name, placeCity: city, placeAddress: address } = el.dataset;
    const id = [name, city, address].join('|');
    if (!results.has(id)) {
      results.set(id, (async () => {
        const cachedId = savedPlaceId(id);
        if (cachedId) {
          try {
            // Place IDs may be saved; photos and their temporary URLs may not.
            const cachedPlace = new Place({ id: cachedId });
            await cachedPlace.fetchFields({ fields: ['photos'] });
            if (cachedPlace.photos?.length) return cachedPlace;
          } catch { /* A removed or changed place needs a fresh search. */ }
          forgetPlaceId(id);
        }
        const query = [name, address, city, 'Magyarország'].filter(Boolean).join(', ');
        const { places = [] } = await Place.searchByText({
          textQuery: query,
          fields: ['id', 'displayName', 'formattedAddress', 'photos', 'googleMapsURI'],
          maxResultCount: 5,
          language: 'hu',
          region: 'hu'
        });
        const match = places.find(p => matches(p, name, city, address) && p.photos?.length) || null;
        if (match?.id) savePlaceId(id, match.id);
        return match;
      })().catch(() => null));
    }
    return results.get(id);
  }

  async function load(el) {
    if (!el.isConnected) return;
    const place = await fetchPlace(el);
    if (!place || !el.isConnected) return;
    const photo = place.photos.find(p => p.widthPx >= 400) || place.photos[0];
    if (!photo) return;

    const img = document.createElement('img');
    img.className = 'venue-image';
    img.loading = 'lazy';
    img.alt = `${el.dataset.placeName} – fotó a Google Mapsen`;
    img.src = photo.getURI({ maxWidth: 840 });
    img.onerror = () => { if (el.isConnected) el.replaceChildren(...el._fallback); };

    const credit = document.createElement('div');
    credit.className = 'photo-credit';
    const source = document.createElement('a');
    source.href = photo.googleMapsURI || place.googleMapsURI ||
      `https://www.google.com/maps/place/?q=place_id:${encodeURIComponent(place.id)}`;
    source.target = '_blank';
    source.rel = 'noopener noreferrer';
    source.textContent = 'Google Maps';
    source.setAttribute('translate', 'no');
    credit.append(source);
    for (const author of photo.authorAttributions || []) {
      const label = document.createElement('span');
      label.append(' · Fotó: ');
      if (author.uri) {
        const link = document.createElement('a');
        link.href = author.uri;
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        link.textContent = author.displayName || 'Fotós';
        label.append(link);
      } else {
        label.append(author.displayName || 'Fotós');
      }
      credit.append(label);
    }
    el._fallback = [...el.childNodes];
    el.replaceChildren(img, credit);
    el.setAttribute('aria-label', `${el.dataset.placeName}: fotó és forrásmegjelölés`);
  }

  function pump() {
    while (active < 2 && pending.length) {
      const el = pending.shift();
      active++;
      load(el).finally(() => { active--; pump(); });
    }
  }

  window.initGuidePhotos = async () => {
    try {
      ({ Place } = await google.maps.importLibrary('places'));
      const observer = new IntersectionObserver(entries => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          observer.unobserve(entry.target);
          pending.push(entry.target);
        }
        pump();
      }, { rootMargin: '250px' });

      const scan = (event) => {
        document.querySelectorAll('.venue-photo:not([data-observed])').forEach(el => {
          // Automatic carousel changes must not generate a stream of paid searches.
          if (el.closest('#picks') && event?.detail?.loadCarousel !== true) return;
          if (el.closest('#list article[hidden]')) return;
          el.dataset.observed = '1';
          observer.observe(el);
        });
      };
      document.addEventListener('venuephotos:refresh', scan);
      scan({ detail: { loadCarousel: true } });
    } catch (error) {
      console.warn('Az étteremfotók most nem tölthetők be.', error);
    }
  };

  // Do not even load the Google library on pages without visible photo cards.
  const start = () => {
    const script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=' +
      encodeURIComponent(key) + '&v=weekly&loading=async&callback=initGuidePhotos';
    script.async = true;
    script.onerror = () => console.warn('A fotószolgáltatás nem érhető el.');
    document.head.append(script);
  };
  const bootstrap = new IntersectionObserver((entries, observer) => {
    if (entries.some(entry => entry.isIntersecting)) {
      observer.disconnect();
      start();
    }
  }, { rootMargin: '150px' });
  document.querySelectorAll('.venue-photo, #picks').forEach(el => {
    if (!el.closest('#list article[hidden]')) bootstrap.observe(el);
  });
})();
