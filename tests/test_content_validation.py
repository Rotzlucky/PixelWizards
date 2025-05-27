"""
Pytest-based content validation tests for Spellcode Academy.
These tests provide more granular testing and better integration with CI/CD.
"""

import pytest
import yaml
import re
import ast
from pathlib import Path
from typing import List, Dict


class TestContentValidation:
    """Test suite for validating educational content quality."""
    
    @pytest.fixture(scope="class")
    def project_root(self):
        """Get the project root directory."""
        return Path(__file__).parent.parent
    
    @pytest.fixture(scope="class")
    def languages(self):
        """Supported languages."""
        return ["en", "de"]
    
    def test_language_directories_exist(self, project_root, languages):
        """Test that all language directories exist."""
        for lang in languages:
            lang_dir = project_root / lang
            assert lang_dir.exists(), f"Language directory '{lang}' missing"
            assert lang_dir.is_dir(), f"'{lang}' is not a directory"
    
    def test_required_files_exist(self, project_root, languages):
        """Test that required files exist in each language directory."""
        required_files = ["index.md", "outline.md", "preparation.md"]
        
        for lang in languages:
            lang_dir = project_root / lang
            if not lang_dir.exists():
                pytest.skip(f"Language directory '{lang}' does not exist")
            
            for file_name in required_files:
                file_path = lang_dir / file_name
                assert file_path.exists(), f"Required file '{file_name}' missing in {lang}"
    
    def test_lessons_directory_structure(self, project_root, languages):
        """Test that lessons directory structure is correct."""
        for lang in languages:
            lessons_dir = project_root / lang / "lessons"
            assert lessons_dir.exists(), f"Lessons directory missing in {lang}"
            
            lesson_files = list(lessons_dir.glob("lesson*.md"))
            assert len(lesson_files) > 0, f"No lesson files found in {lang}/lessons"
    
    def test_multilingual_lesson_parity(self, project_root, languages):
        """Test that all languages have the same lessons."""
        lang_lessons = {}
        
        for lang in languages:
            lessons_dir = project_root / lang / "lessons"
            if lessons_dir.exists():
                lang_lessons[lang] = {f.stem for f in lessons_dir.glob("lesson*.md")}
        
        if len(lang_lessons) < 2:
            pytest.skip("Need at least 2 languages to test parity")
        
        base_lang = languages[0]
        base_lessons = lang_lessons[base_lang]
        
        for lang in languages[1:]:
            current_lessons = lang_lessons.get(lang, set())
            missing = base_lessons - current_lessons
            extra = current_lessons - base_lessons
            
            assert not missing, f"Missing lessons in {lang}: {missing}"
            assert not extra, f"Extra lessons in {lang}: {extra}"
    
    def test_front_matter_validity(self, project_root, languages):
        """Test that all markdown files have valid front matter."""
        for lang in languages:
            lang_dir = project_root / lang
            if not lang_dir.exists():
                continue
            
            md_files = list(lang_dir.rglob("*.md"))
            
            for md_file in md_files:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                assert content.startswith('---'), f"Missing front matter in {md_file}"
                
                end_marker = content.find('---', 3)
                assert end_marker != -1, f"Incomplete front matter in {md_file}"
                
                front_matter_text = content[3:end_marker]
                try:
                    front_matter = yaml.safe_load(front_matter_text)
                    assert isinstance(front_matter, dict), f"Invalid front matter format in {md_file}"
                except yaml.YAMLError as e:
                    pytest.fail(f"YAML error in {md_file}: {e}")
    
    def test_lesson_order_sequence(self, project_root, languages):
        """Test that lesson order is sequential."""
        for lang in languages:
            lessons_dir = project_root / lang / "lessons"
            if not lessons_dir.exists():
                continue
            
            lessons = []
            for lesson_file in lessons_dir.glob("lesson*.md"):
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if content.startswith('---'):
                    end_marker = content.find('---', 3)
                    if end_marker != -1:
                        front_matter = yaml.safe_load(content[3:end_marker])
                        order = front_matter.get('order', 0)
                        lessons.append((lesson_file.name, order))
            
            lessons.sort(key=lambda x: x[1])
            
            for i, (filename, order) in enumerate(lessons, 1):
                assert order == i, f"Order gap in {lang}: expected {i}, got {order} in {filename}"
    
    def test_python_code_syntax(self, project_root, languages):
        """Test that all Python code examples are syntactically correct."""
        for lang in languages:
            lang_dir = project_root / lang
            if not lang_dir.exists():
                continue
            
            md_files = list(lang_dir.rglob("*.md"))
            
            for md_file in md_files:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract Python code blocks
                python_blocks = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)
                
                for i, code_block in enumerate(python_blocks):
                    # Skip incomplete examples
                    if any(placeholder in code_block for placeholder in ['...', 'TODO', 'FIXME']):
                        continue
                    
                    try:
                        ast.parse(code_block)
                    except SyntaxError as e:
                        pytest.fail(f"Syntax error in {md_file.name}, block {i+1}: {e}")
    
    def test_internal_links_validity(self, project_root, languages):
        """Test that internal links point to existing files."""
        for lang in languages:
            lang_dir = project_root / lang
            if not lang_dir.exists():
                continue
            
            md_files = list(lang_dir.rglob("*.md"))
            
            for md_file in md_files:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find markdown links
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                
                for link_text, link_url in links:
                    # Skip external links and anchors
                    if link_url.startswith(('http', '#', 'mailto:')):
                        continue
                    
                    # Handle Jekyll relative_url filter
                    if 'relative_url' in link_url:
                        path_match = re.search(r"'([^']+)'", link_url)
                        if path_match:
                            link_url = path_match.group(1)
                    
                    # Convert to file path
                    if link_url.startswith('/'):
                        target_path = project_root / link_url.lstrip('/')
                    else:
                        target_path = md_file.parent / link_url
                    
                    # Check if target exists
                    if not target_path.exists():
                        md_target = target_path.with_suffix('.md')
                        index_target = target_path / 'index.md'
                        
                        assert (md_target.exists() or index_target.exists()), \
                            f"Broken link in {md_file.name}: '{link_text}' -> {link_url}"


class TestEducationalProgression:
    """Test suite for validating educational progression and content quality."""
    
    @pytest.fixture(scope="class")
    def project_root(self):
        return Path(__file__).parent.parent
    
    def test_difficulty_progression(self, project_root):
        """Test that lesson difficulty increases appropriately."""
        for lang in ["en", "de"]:
            lessons_dir = project_root / lang / "lessons"
            if not lessons_dir.exists():
                continue
            
            lessons = []
            for lesson_file in lessons_dir.glob("lesson*.md"):
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if content.startswith('---'):
                    end_marker = content.find('---', 3)
                    if end_marker != -1:
                        front_matter = yaml.safe_load(content[3:end_marker])
                        order = front_matter.get('order', 0)
                        difficulty = front_matter.get('difficulty')
                        if difficulty is not None:
                            lessons.append((order, difficulty))
            
            lessons.sort()
            
            for i in range(1, len(lessons)):
                prev_difficulty = lessons[i-1][1]
                curr_difficulty = lessons[i][1]
                assert curr_difficulty >= prev_difficulty, \
                    f"Difficulty regression in {lang}: lesson {lessons[i][0]} is easier than previous"
    
    def test_objectives_exist(self, project_root):
        """Test that lessons have learning objectives."""
        for lang in ["en", "de"]:
            lessons_dir = project_root / lang / "lessons"
            if not lessons_dir.exists():
                continue
            
            for lesson_file in lessons_dir.glob("lesson*.md"):
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if content.startswith('---'):
                    end_marker = content.find('---', 3)
                    if end_marker != -1:
                        front_matter = yaml.safe_load(content[3:end_marker])
                        objectives = front_matter.get('objectives')
                        
                        assert objectives is not None, f"Missing objectives in {lesson_file.name}"
                        assert isinstance(objectives, list), f"Objectives should be a list in {lesson_file.name}"
                        assert len(objectives) > 0, f"Empty objectives list in {lesson_file.name}" 