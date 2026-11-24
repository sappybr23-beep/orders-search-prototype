# Поиск заказов и операций — кликабельный прототип

Прототип секции «Поиск заказов и операций» из Figma: точка входа с онбордингом, открытие и закрытие поиска, выбор «Искать по», мультипоиск чипами, валидация, «Ничего не найдено», брейкпоинты 375 / 576 / 1024 / 1440 / 1920.

**Открыть:** https://sappybr23-beep.github.io/orders-search-prototype/

## Структура
- `index.html` — исходник (ссылается на `assets/*.svg`)
- `assets/` — иконки из Figma
- `build.py` — встраивает SVG и собирает `docs/index.html` (сайт) и `dist/`
- `docs/` — то, что публикует GitHub Pages

## Обновить сайт
```bash
python3 build.py && git add -A && git commit -m "Update prototype" && git push
```
