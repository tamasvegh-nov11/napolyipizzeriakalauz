// Keep each venue card in the document when the carousel advances. A photo
// lookup may finish after its card stops being visible, and can be reused later.
let offset = 0;
const box = document.getElementById('picks');
const cards = picks.map(p => {
  const article = document.createElement('article');
  article.className = 'pick';
  article.hidden = true;

  const mock = document.createElement('div');
  mock.className = 'photo-mock venue-photo';
  mock.dataset.placeName = p.name;
  mock.dataset.placeCity = p.city;
  mock.dataset.placeAddress = p.address;
  mock.setAttribute('role', 'img');
  mock.setAttribute('aria-label', p.name + ': az éttermi fotó helye');
  mock.innerHTML = '<div class="photo-mark">NP</div><span>ÉTTERMI FOTÓ HELYE</span>';

  const content = document.createElement('div');
  content.className = 'pick-content';
  const badge = document.createElement('span');
  badge.className = 'pill';
  badge.textContent = 'ARANY MINŐSÍTÉS';
  const heading = document.createElement('h3');
  if (p.href) {
    const link = document.createElement('a');
    link.href = p.href;
    link.textContent = p.name;
    heading.append(link);
  } else {
    heading.textContent = p.name;
  }
  const city = document.createElement('p');
  city.textContent = p.city;
  content.append(badge, heading, city);
  article.append(mock, content);
  return article;
});
box.replaceChildren(...cards);

function draw(loadCarousel = false) {
  const count = innerWidth < 700 ? 1 : innerWidth < 1000 ? 2 : 3;
  const visible = new Set();
  const names = new Set();
  for (let k = 0; k < picks.length && visible.size < count; k++) {
    const index = (offset + k) % picks.length;
    if (names.has(picks[index].name)) continue;
    names.add(picks[index].name);
    visible.add(index);
  }
  cards.forEach((card, index) => { card.hidden = !visible.has(index); });
  document.dispatchEvent(new CustomEvent('venuephotos:refresh', {
    detail: { loadCarousel }
  }));
}

function step(amount, manual = false) {
  offset = (offset + amount + picks.length) % picks.length;
  draw(manual);
}
document.getElementById('pick-prev').onclick = () => step(-1, true);
document.getElementById('pick-next').onclick = () => step(1, true);
addEventListener('resize', () => draw());
setInterval(() => {
  if (!document.hidden && !box.matches(':hover')) step(1);
}, 11000);
draw(true);
