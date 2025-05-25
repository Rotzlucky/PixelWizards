# Python Game Tutorial for Kids

A fun and interactive tutorial to teach Python programming to children through game development, culminating in a 2D RPG game.

## About This Project

This tutorial is designed for children around 10 years old who want to learn programming in a fun and engaging way. The lessons build upon each other, starting with basic Python concepts and gradually introducing game development topics until the student can create their own 2D RPG game.

## Features

- Step-by-step lessons with clear explanations
- Fun, interactive examples
- Challenges to reinforce learning
- **Automated multilingual support** with cookie-based language persistence (English and German)
- **Smart navigation** that maintains language consistency throughout the site
- Child-friendly design and language

## Project Structure

- `_config.yml`: Jekyll configuration file with site settings and multilingual configuration
- `index.md`: Main landing page (English)
- `index.de.md`: Main landing page (German)
- `_layouts/`: HTML templates for the site
  - `default.html`: Main layout template with header, footer, and language selector
  - `lesson.html`: Template for lesson pages with automated language-aware navigation
- `_includes/`: Reusable components
  - `language-handler.html`: JavaScript for automatic link conversion and language detection
  - `link-helper.html`: Helper functions for multilingual link generation
- `_data/`: Data files for the site
  - `translations.yml`: Translations for UI elements in different languages
- `assets/`: CSS, images, and other static files
  - `css/main.css`: Main stylesheet for the site
- `_lessons/`: Individual lesson files (both English and German versions)
  - `outline.md` & `outline.de.md`: Lesson outline in English and German
  - `lesson1.md` & `lesson1.de.md`: First lesson in English and German

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
   docker-compose up
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

#### Adding Translations

- Create a new file with the language code suffix (e.g., `lesson2.fr.md` for French)
- **Use neutral links** - write all internal links using neutral English paths like `{{ 'lessons/lesson1/' | relative_url }}` (the system will automatically convert them)
- Update `_data/translations.yml` to add UI elements in the new language
- Add the new language to `_config.yml` languages section
- Update `_includes/language-handler.html` to add language detection rules for the new language
- Ensure translations are accurate and maintain the original tone

## Multilingual System

This site features an **automated multilingual system** that requires minimal maintenance while providing an excellent user experience.

### How It Works

1. **Content authors write neutral links** using Jekyll's `relative_url` filter
2. **JavaScript automatically detects** the current page language
3. **Links are converted** to the appropriate language version on page load
4. **Cookie stores** user language preference for future visits
5. **Users stay in their language** when navigating throughout the site

### Writing Content with Neutral Links

When creating content, always use neutral English links that will be automatically converted:

```markdown
✅ Good (Neutral Links):
[Quest Map]({{ 'lessons/outline/' | relative_url }})
[Lesson 1]({{ 'lessons/lesson1/' | relative_url }})

❌ Avoid (Language-Specific Links):
[Quest Map]({{ 'lessons/outline-de/' | relative_url }})
[Lesson 1]({{ 'lessons/lesson1-de/' | relative_url }})
```

### Adding New Languages

To add a new language (e.g., Spanish):

1. **Update `_config.yml`:**
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

2. **Update `_data/translations.yml`:**
   ```yaml
   nav:
     lessons:
       en: "Lessons"
       de: "Quests"
       es: "Lecciones"
   ```

3. **Update `_includes/language-handler.html`:**
   Add language detection and conversion rules for Spanish files (`.es` suffix)

4. **Create content files:**
   - `index.es.md`
   - `lesson1.es.md`
   - etc.

### File Naming Convention

- **English:** `lesson1.md`, `outline.md`, `index.md`
- **German:** `lesson1.de.md`, `outline.de.md`, `index.de.md`
- **Spanish:** `lesson1.es.md`, `outline.es.md`, `index.es.md`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and translators
- Special thanks to the Python and Pygame communities for their excellent documentation
