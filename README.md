# Moonripple Lake — Русский перевод / Russian Translation

Неофициальный фанатский перевод визуальной новеллы **Moonripple Lake** на русский язык.

> **Steam:** https://store.steampowered.com/app/2857910/Moonripple_Lake/

## Установка / Installation

### Windows
1. Скачайте этот репозиторий (кнопка **Code → Download ZIP**)
2. Распакуйте архив
3. Скопируйте папку `game` в корневую папку игры, например:
   ```
   C:\Program Files (x86)\Steam\steamapps\common\Moonripple Lake\
   ```
4. При копировании выберите **"Объединить папки"** / **"Merge folders"**
5. Запустите игру — она автоматически будет на русском

### macOS
1. Скачайте этот репозиторий (кнопка **Code → Download ZIP**)
2. Распакуйте архив
3. Найдите игру в Steam: ПКМ → Управление → Просмотреть локальные файлы
4. ПКМ на `Moonripple_Lake.app` → Показать содержимое пакета
5. Скопируйте папку `game` в `Contents/Resources/autorun/`:
   ```
   Moonripple_Lake.app/Contents/Resources/autorun/
   ```
6. При копировании выберите **"Объединить"** / **"Merge"**
7. Запустите игру

### Linux
1. Скачайте и распакуйте
2. Скопируйте папку `game` в корень игры:
   ```
   ~/.local/share/Steam/steamapps/common/Moonripple Lake/
   ```
3. Запустите игру

## Что в переводе

- Все эпизоды (Pilot, Making Friends, Making Friends II, Episode 5, Episode 6, Revelations, Halloween Special)
- Все локации и диалоги
- Интерфейс (меню, настройки, экраны)
- Галерея (подписи к фото, сцены)
- Разговор с Сайласом

## Статистика

| Файл | Покрытие |
|------|----------|
| Pilot Episode | 96% |
| Making Friends | 94% |
| Making Friends II | 95% |
| Episode 5 | 94% |
| Episode 6 | 94% |
| Revelations | 95% |
| Halloween Special | 96% |
| Silas Convo | 100% |
| Locations | 97% |
| UI / Screens | 100% |
| Gallery | 96-98% |

Оставшиеся ~5% — это строки без текста (переменные с именами персонажей, эмодзи, звуковые эффекты), перевод которых не требуется.

**Эффективное покрытие перевода: ~100%**

## Примечания

- Перевод выполнен с помощью AI (Claude) и проверен вручную
- Файл `force_russian.rpy` автоматически переключает язык на русский
- Если хотите вернуть английский — удалите файл `game/force_russian.rpy`
- Совместимость проверена на текущей версии игры в Steam

## Нашли ошибку?

Создайте Issue в этом репозитории с указанием:
- Эпизод / сцена
- Скриншот (если возможно)
- Правильный вариант перевода
