# Spellcode Academy - Python Game Tutorial for Kids

A magical and interactive tutorial to teach Python programming to children through game development, culminating in a 2D RPG game.

## About This Project

This tutorial is designed for children around 10 years old who want to learn programming in a fun and engaging way. The lessons build upon each other, starting with basic Python concepts and gradually introducing game development topics until the student can create their own 2D RPG game.

## Features

- Step-by-step lessons with clear explanations
- Fun, interactive examples with a magical theme
- Challenges to reinforce learning
- **Direct URL multilingual support** with clean, SEO-friendly URLs (English and German)
- **Smart language switching** that preserves current page context
- **Browser language detection** with automatic redirection on first visit
- Child-friendly design and magical theme

## Project Structure

- `_config.yml`: Jekyll configuration file with site settings and multilingual configuration
- `index.md`: Main landing page with language selector
- `en/index.md`: English homepage
- `de/index.md`: German homepage
- `_layouts/`: HTML templates for the site
  - `default.html`: Main layout template with header, footer, and language selector
  - `lesson.html`: Template for lesson pages with language-aware navigation
- `_data/`: Data files for the site
  - `translations.yml`: Translations for UI elements in different languages
- `assets/`: CSS, images, and other static files
  - `css/main.css`: Main stylesheet for the site
- `_lessons/`: Individual lesson files organized by language
  - `en/`: English lessons (outline.md, lesson1.md, lesson2.md, etc.)
  - `de/`: German lessons (outline.md, lesson1.md, lesson2.md, etc.)

## Setup for Local Development

You can set up this project locally using either Docker or by installing the dependencies directly.

### Option 1: Using Docker (Recommended)

#### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)

#### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Spellcode.git
   cd Spellcode
   ```

2. Build and start the Docker container:
   ```
   docker compose up
   ```

3. Open your browser and go to `http://localhost:4000/Spellcode/`

> **Note for Linux users:** You might encounter permission issues with the mounted volumes. If this happens, you can fix it by running the Docker container with your user ID: `docker-compose up -d --user "$(id -u):$(id -g)"` or by adjusting the permissions of the generated files after running the container.

### Option 2: Direct Installation

#### Prerequisites

- [Ruby](https://www.ruby-lang.org/en/downloads/) (version 2.5.0 or higher)
- [Bundler](https://bundler.io/)
- [Jekyll](https://jekyllrb.com/docs/installation/)

#### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Spellcode.git
   cd Spellcode
   ```

2. Install dependencies:
   ```
   bundle install
   ```

3. Run the site locally:
   ```
   bundle exec jekyll serve
   ```

4. Open your browser and go to `http://localhost:4000/Spellcode/`

## Multilingual System

This site features a **direct URL multilingual system** that provides clean, SEO-friendly URLs and excellent user experience.

### URL Structure

The site uses a clean, direct URL approach:

- **Main page:** `/` (language selector)
- **English content:** `/en/` and `/en/lessons/lesson1/`
- **German content:** `/de/` and `/de/lessons/lesson1/`

### How It Works

1. **Direct URLs:** Each language has its own URL path (`/en/` or `/de/`)
2. **Language switching:** Dropdown preserves current page context when switching languages
3. **Browser detection:** Automatically redirects to user's preferred language on first visit
4. **Local storage:** Remembers user's language preference for future visits
5. **Bookmarkable:** All URLs are directly accessible and shareable

### Writing Content

When creating content, always use language-specific links with Jekyll's `relative_url` filter:

```markdown
✅ Good (Language-Specific Links):
[Quest Map]({{ '/en/lessons/outline/' | relative_url }})
[Lesson 1]({{ '/en/lessons/lesson1/' | relative_url }})

For German content:
[Questkarte]({{ '/de/lessons/outline/' | relative_url }})
[Lektion 1]({{ '/de/lessons/lesson1/' | relative_url }})
```

### Adding New Languages

To add a new language (e.g., Spanish):

1. **Create directory structure:**
   ```
   es/index.md
   _lessons/es/outline.md
   _lessons/es/lesson1.md
   ```

2. **Update `_config.yml`:**
   ```yaml
   languages:
     - code: en
       name: English
       flag: 🇬🇧
       default: true
     - code: de
       name: Deutsch
       flag: 🇩🇪
     - code: es
       name: Español
       flag: 🇪🇸
   ```

3. **Update `_data/translations.yml`:**
   ```yaml
   nav:
     lessons:
       en: "Lessons"
       de: "Quests"
       es: "Lecciones"
   ```

4. **Create content files with proper permalinks:**
   ```yaml
   ---
   layout: lesson
   title: "Lección 1"
   lang: es
   permalink: /es/lessons/lesson1/
   ---
   ```

### File Organization

- **English:** `en/index.md`, `_lessons/en/lesson1.md`
- **German:** `de/index.md`, `_lessons/de/lesson1.md`
- **Spanish:** `es/index.md`, `_lessons/es/lesson1.md`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and translators
- Special thanks to the Python and Pygame communities for their excellent documentation
