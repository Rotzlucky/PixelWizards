# Python Game Tutorial for Kids

A fun and interactive tutorial to teach Python programming to children through game development, culminating in a 2D RPG game.

## About This Project

This tutorial is designed for children around 10 years old who want to learn programming in a fun and engaging way. The lessons build upon each other, starting with basic Python concepts and gradually introducing game development topics until the student can create their own 2D RPG game.

## Features

- Step-by-step lessons with clear explanations
- Fun, interactive examples
- Challenges to reinforce learning
- Multilingual support (currently English and German)
- Child-friendly design and language

## Project Structure

- `_config.yml`: Jekyll configuration file with site settings and multilingual configuration
- `index.md`: Main landing page (English)
- `index.de.md`: Main landing page (German)
- `_layouts/`: HTML templates for the site
  - `default.html`: Main layout template with header, footer, and language selector
  - `lesson.html`: Template for lesson pages with navigation and objectives
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
   git clone https://github.com/yourusername/PixelWizards.git
   cd PixelWizards
   ```

2. Build and start the Docker container:
   ```
   docker-compose up
   ```

3. Open your browser and go to `http://localhost:4000/PixelWizards/`

> **Note for Linux users:** You might encounter permission issues with the mounted volumes. If this happens, you can fix it by running the Docker container with your user ID: `docker-compose up -d --user "$(id -u):$(id -g)"` or by adjusting the permissions of the generated files after running the container.

### Option 2: Direct Installation

#### Prerequisites

- [Ruby](https://www.ruby-lang.org/en/downloads/) (version 2.5.0 or higher)
- [Bundler](https://bundler.io/)
- [Jekyll](https://jekyllrb.com/docs/installation/)

#### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/PixelWizards.git
   cd PixelWizards
   ```

2. Install dependencies:
   ```
   bundle install
   ```

3. Run the site locally:
   ```
   bundle exec jekyll serve
   ```

4. Open your browser and go to `http://localhost:4000/PixelWizards/`

## Deploying to GitHub Pages

1. Create a new repository on GitHub
2. Push this code to your repository
3. Go to Settings > Pages
4. Select the main branch as the source
5. Your site will be published at `https://yourusername.github.io/PixelWizards/`

## Contributing

Contributions are welcome! Here are some ways you can help improve this project:

### Types of Contributions Needed

- **New Lessons**: Create additional lessons following the outline in `_lessons/outline.md`
- **Translations**: Translate existing content to other languages
- **Bug Fixes**: Fix issues with the site functionality or content
- **Enhancements**: Improve the UI, add new features, or optimize performance
- **Documentation**: Improve or expand the documentation

### How to Contribute

1. **Fork the repository**: Click the Fork button at the top right of this page
2. **Clone your fork**: `git clone https://github.com/yourusername/PixelWizards.git`
3. **Create a new branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes**: Follow the guidelines below for specific types of contributions
5. **Test your changes**: See the Testing section below
6. **Commit your changes**: `git commit -m 'Add some feature'`
7. **Push to your branch**: `git push origin feature/your-feature-name`
8. **Open a Pull Request**: Go to the original repository and click "New Pull Request"

### Guidelines for Specific Contributions

#### Adding New Lessons

- Follow the format of existing lesson files in `_lessons/`
- Include YAML front matter with appropriate metadata
- Ensure content is child-friendly and age-appropriate
- Include code examples, explanations, and challenges

#### Adding Translations

- Create a new file with the language code suffix (e.g., `lesson2.fr.md` for French)
- Update `_data/translations.yml` if adding UI elements in a new language
- Add the new language to `_config.yml` if it's not already there
- Ensure translations are accurate and maintain the original tone

## Testing

### Testing Links

To ensure all links in the website work correctly, you can use the provided test script:

1. Start the Jekyll server using Docker:
   ```
   ./scripts/docker-serve.sh
   ```

2. In a new terminal window, run the link test script:
   ```
   ./scripts/test-links.sh
   ```

This script will check that all important links in the site are working correctly, including:
- Language switching between English and German
- Links to lessons from the main pages
- Links within the lesson outline page

If any links are broken, the script will report the errors.

## Adding New Languages

To add a new language:

1. Add the language to the `languages` section in `_config.yml`
2. Create translated versions of pages with the language code (e.g., `index.fr.md` for French)
3. Create a directory for lesson translations if needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and translators
- Special thanks to the Python and Pygame communities for their excellent documentation
