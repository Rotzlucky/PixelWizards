#!/usr/bin/env python3
"""
Spellcode Academy Test Suite
Comprehensive testing framework for content quality, multilingual consistency,
and educational progression.
"""

import sys
import re
from pathlib import Path
from typing import List, Optional, Dict, Any


class TestResult:
    def __init__(self, test_name: str, passed: bool, message: str, 
                 details: str = None):
        self.test_name = test_name
        self.passed = passed
        self.message = message
        self.details = details


class LessonMetadata:
    def __init__(self, file_path: str, title: str, lang: str, 
                 permalink: str, order: int, difficulty: Optional[int] = None,
                 objectives: Optional[List[str]] = None):
        self.file_path = file_path
        self.title = title
        self.lang = lang
        self.permalink = permalink
        self.order = order
        self.difficulty = difficulty
        self.objectives = objectives


class SpellcodeTestSuite:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.results: List[TestResult] = []
        self.languages = ["en", "de"]
        
    def run_all_tests(self) -> bool:
        """Run all test suites and return overall success status."""
        print("🧙‍♂️ Starting Spellcode Academy Test Suite...")
        print("=" * 60)
        
        # Content structure tests
        self.test_content_structure()
        
        # Multilingual consistency tests
        self.test_multilingual_consistency()
        
        # Educational progression tests
        self.test_educational_progression()
        
        # Python code validation tests
        self.test_python_code_examples()
        
        # Link integrity tests
        self.test_link_integrity()
        
        # Front matter validation
        self.test_front_matter_consistency()
        
        return self.print_results()
    
    def add_result(self, test_name: str, passed: bool, message: str, 
                   details: str = None):
        """Add a test result to the collection."""
        self.results.append(TestResult(test_name, passed, message, details))
    
    def test_content_structure(self):
        """Test that content structure is consistent across languages."""
        print("\n📁 Testing Content Structure...")
        
        for lang in self.languages:
            lang_dir = self.project_root / lang
            
            # Check if language directory exists
            if not lang_dir.exists():
                self.add_result(
                    f"Content Structure - {lang.upper()}",
                    False,
                    f"Language directory '{lang}' does not exist"
                )
                continue
            
            # Check required files
            required_files = ["index.md", "outline.md", "preparation.md"]
            for file_name in required_files:
                file_path = lang_dir / file_name
                if not file_path.exists():
                    self.add_result(
                        f"Content Structure - {lang.upper()}",
                        False,
                        f"Required file '{file_name}' missing in {lang}"
                    )
                else:
                    self.add_result(
                        f"Content Structure - {lang.upper()}",
                        True,
                        f"Required file '{file_name}' exists"
                    )
            
            # Check lessons directory
            lessons_dir = lang_dir / "lessons"
            if not lessons_dir.exists():
                self.add_result(
                    f"Content Structure - {lang.upper()}",
                    False,
                    f"Lessons directory missing in {lang}"
                )
            else:
                lesson_files = list(lessons_dir.glob("lesson*.md"))
                self.add_result(
                    f"Content Structure - {lang.upper()}",
                    len(lesson_files) > 0,
                    f"Found {len(lesson_files)} lesson files"
                )
    
    def test_multilingual_consistency(self):
        """Test that content is consistent across languages."""
        print("\n🌍 Testing Multilingual Consistency...")
        
        # Get lesson files for each language
        lang_lessons = {}
        for lang in self.languages:
            lessons_dir = self.project_root / lang / "lessons"
            if lessons_dir.exists():
                lang_lessons[lang] = {
                    f.stem for f in lessons_dir.glob("lesson*.md")
                }
        
        # Check if all languages have the same lessons
        if len(lang_lessons) >= 2:
            base_lang = self.languages[0]
            base_lessons = lang_lessons.get(base_lang, set())
            
            for lang in self.languages[1:]:
                current_lessons = lang_lessons.get(lang, set())
                missing_lessons = base_lessons - current_lessons
                extra_lessons = current_lessons - base_lessons
                
                if missing_lessons:
                    self.add_result(
                        f"Multilingual Consistency - {lang.upper()}",
                        False,
                        f"Missing lessons: {', '.join(missing_lessons)}",
                        f"These lessons exist in {base_lang} but not in {lang}"
                    )
                
                if extra_lessons:
                    self.add_result(
                        f"Multilingual Consistency - {lang.upper()}",
                        False,
                        f"Extra lessons: {', '.join(extra_lessons)}",
                        f"These lessons exist in {lang} but not in {base_lang}"
                    )
                
                if not missing_lessons and not extra_lessons:
                    self.add_result(
                        f"Multilingual Consistency - {lang.upper()}",
                        True,
                        f"All lessons synchronized with {base_lang}"
                    )
    
    def test_educational_progression(self):
        """Test that lessons follow proper educational progression."""
        print("\n📚 Testing Educational Progression...")
        
        for lang in self.languages:
            lessons = self.get_lesson_metadata(lang)
            if not lessons:
                self.add_result(
                    f"Educational Progression - {lang.upper()}",
                    False,
                    "No lessons found for progression analysis"
                )
                continue
            
            # Sort lessons by order
            sorted_lessons = sorted(lessons, key=lambda x: x.order)
            
            # Check order sequence
            expected_order = 1
            order_issues = []
            for lesson in sorted_lessons:
                if lesson.order != expected_order:
                    order_issues.append(
                        f"Expected {expected_order}, found {lesson.order}"
                    )
                expected_order += 1
            
            if order_issues:
                self.add_result(
                    f"Educational Progression - {lang.upper()}",
                    False,
                    f"Lesson order gaps found: {len(order_issues)} issues",
                    "; ".join(order_issues[:3])
                )
            else:
                self.add_result(
                    f"Educational Progression - {lang.upper()}",
                    True,
                    f"Lesson order is sequential ({len(sorted_lessons)} lessons)"
                )
            
            # Check difficulty progression
            difficulties = [
                lesson.difficulty for lesson in sorted_lessons 
                if lesson.difficulty is not None
            ]
            if len(difficulties) > 1:
                regression_found = False
                for i in range(1, len(difficulties)):
                    if difficulties[i] < difficulties[i-1]:
                        self.add_result(
                            f"Educational Progression - {lang.upper()}",
                            False,
                            f"Difficulty regression at lesson {i+1}",
                            f"Difficulty: {difficulties[i-1]} -> {difficulties[i]}"
                        )
                        regression_found = True
                        break
                
                if not regression_found:
                    self.add_result(
                        f"Educational Progression - {lang.upper()}",
                        True,
                        f"Difficulty progression consistent "
                        f"({len(difficulties)} lessons)"
                    )
            
            # Check learning objectives
            lessons_with_objectives = [
                lesson for lesson in sorted_lessons if lesson.objectives
            ]
            if len(lessons_with_objectives) < len(sorted_lessons) * 0.8:
                self.add_result(
                    f"Educational Progression - {lang.upper()}",
                    False,
                    f"Only {len(lessons_with_objectives)}/"
                    f"{len(sorted_lessons)} lessons have learning objectives"
                )
            else:
                self.add_result(
                    f"Educational Progression - {lang.upper()}",
                    True,
                    f"Learning objectives present in "
                    f"{len(lessons_with_objectives)}/{len(sorted_lessons)} lessons"
                )
    
    def test_python_code_examples(self):
        """Test that Python code examples exist and look reasonable."""
        print("\n🐍 Testing Python Code Examples...")
        
        for lang in self.languages:
            lang_dir = self.project_root / lang
            if not lang_dir.exists():
                continue
            
            # Find all markdown files
            md_files = list(lang_dir.rglob("*.md"))
            total_code_blocks = 0
            valid_code_blocks = 0
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract Python code blocks
                    python_blocks = re.findall(r'```python\n(.*?)\n```', 
                                             content, re.DOTALL)
                    
                    for code_block in python_blocks:
                        total_code_blocks += 1
                        
                        # Skip incomplete examples
                        if any(placeholder in code_block 
                               for placeholder in ['...', 'TODO', 'FIXME']):
                            continue
                        
                        # Basic validation - check for Python keywords
                        if any(keyword in code_block for keyword in 
                               ['print', 'def', 'if', 'for', 'while', 'import',
                                'class', 'return', '=']):
                            valid_code_blocks += 1
                
                except Exception as e:
                    self.add_result(
                        f"Python Code - {lang.upper()}",
                        False,
                        f"Error reading file {md_file.name}",
                        str(e)
                    )
            
            if total_code_blocks > 0:
                success_rate = (valid_code_blocks / total_code_blocks) * 100
                self.add_result(
                    f"Python Code - {lang.upper()}",
                    success_rate >= 80,
                    f"Code validation: {valid_code_blocks}/"
                    f"{total_code_blocks} blocks valid ({success_rate:.1f}%)"
                )
            else:
                self.add_result(
                    f"Python Code - {lang.upper()}",
                    False,
                    "No Python code blocks found"
                )
    
    def test_link_integrity(self):
        """Test that internal links are valid."""
        print("\n🔗 Testing Link Integrity...")
        
        for lang in self.languages:
            lang_dir = self.project_root / lang
            if not lang_dir.exists():
                continue
            
            md_files = list(lang_dir.rglob("*.md"))
            broken_links = []
            total_internal_links = 0
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Find markdown links
                    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                    
                    for link_text, link_url in links:
                        # Skip external links and anchors
                        if link_url.startswith(('http', '#', 'mailto:')):
                            continue
                        
                        total_internal_links += 1
                        
                        # Handle Jekyll relative_url filter
                        if 'relative_url' in link_url:
                            # Extract path from Jekyll liquid syntax
                            path_match = re.search(r"'([^']+)'", link_url)
                            if path_match:
                                link_url = path_match.group(1)
                        
                        # Convert to file path
                        if link_url.startswith('/'):
                            # Absolute path from site root
                            target_path = self.project_root / link_url.lstrip('/')
                        else:
                            # Relative path
                            target_path = md_file.parent / link_url
                        
                        # Check if target exists
                        if not target_path.exists():
                            # Try with .md extension
                            md_target = target_path.with_suffix('.md')
                            index_target = target_path / 'index.md'
                            
                            if not (md_target.exists() or 
                                   index_target.exists()):
                                broken_links.append(
                                    f"{md_file.name}: '{link_text}' -> {link_url}"
                                )
                
                except Exception as e:
                    self.add_result(
                        f"Link Integrity - {lang.upper()}",
                        False,
                        f"Error checking links in {md_file.name}",
                        str(e)
                    )
            
            if broken_links:
                self.add_result(
                    f"Link Integrity - {lang.upper()}",
                    False,
                    f"Found {len(broken_links)} broken internal links",
                    "\n".join(broken_links[:5])  # Show first 5
                )
            elif total_internal_links > 0:
                self.add_result(
                    f"Link Integrity - {lang.upper()}",
                    True,
                    f"All {total_internal_links} internal links are valid"
                )
            else:
                self.add_result(
                    f"Link Integrity - {lang.upper()}",
                    True,
                    "No internal links found to validate"
                )
    
    def test_front_matter_consistency(self):
        """Test that front matter is consistent and complete."""
        print("\n📋 Testing Front Matter Consistency...")
        
        required_fields = ['layout', 'title', 'lang', 'permalink']
        lesson_required_fields = required_fields + ['order']
        
        for lang in self.languages:
            lang_dir = self.project_root / lang
            if not lang_dir.exists():
                continue
            
            md_files = list(lang_dir.rglob("*.md"))
            issues = []
            
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract front matter
                    if content.startswith('---'):
                        end_marker = content.find('---', 3)
                        if end_marker != -1:
                            front_matter_text = content[3:end_marker]
                            try:
                                # Simple YAML-like parsing
                                front_matter = self.parse_simple_yaml(
                                    front_matter_text
                                )
                                
                                # Determine required fields
                                is_lesson = 'lesson' in md_file.name
                                required = (lesson_required_fields if is_lesson 
                                          else required_fields)
                                
                                # Check required fields
                                missing_fields = [field for field in required 
                                                if field not in front_matter]
                                if missing_fields:
                                    issues.append(
                                        f"{md_file.name}: missing "
                                        f"{', '.join(missing_fields)}"
                                    )
                                
                                # Check language consistency
                                if ('lang' in front_matter and 
                                    front_matter['lang'] != lang):
                                    issues.append(
                                        f"{md_file.name}: lang mismatch "
                                        f"(expected {lang}, got "
                                        f"{front_matter['lang']})"
                                    )
                                
                            except Exception as e:
                                issues.append(
                                    f"{md_file.name}: invalid front matter - "
                                    f"{str(e)}"
                                )
                        else:
                            issues.append(
                                f"{md_file.name}: incomplete front matter"
                            )
                    else:
                        issues.append(f"{md_file.name}: missing front matter")
                
                except Exception as e:
                    issues.append(
                        f"{md_file.name}: error reading file - {str(e)}"
                    )
            
            if issues:
                self.add_result(
                    f"Front Matter - {lang.upper()}",
                    False,
                    f"Found {len(issues)} front matter issues",
                    "\n".join(issues[:5])  # Show first 5
                )
            else:
                self.add_result(
                    f"Front Matter - {lang.upper()}",
                    True,
                    "All front matter is valid and complete"
                )
    
    def parse_simple_yaml(self, yaml_text: str) -> Dict[str, Any]:
        """Simple YAML parser for basic key-value pairs and lists."""
        result = {}
        lines = yaml_text.strip().split('\n')
        current_key = None
        current_list = []
        
        for line in lines:
            original_line = line
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Check if this is a list item
            if line.startswith('- ') and current_key:
                # This is a list item for the current key
                item = line[2:].strip()
                # Remove quotes if present
                if item.startswith('"') and item.endswith('"'):
                    item = item[1:-1]
                elif item.startswith("'") and item.endswith("'"):
                    item = item[1:-1]
                current_list.append(item)
                continue
            
            # If we were building a list and hit a non-list line, save the list
            if current_key and current_list:
                result[current_key] = current_list
                current_list = []
                current_key = None
            
            # Check for key-value pairs
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # If value is empty, this might be the start of a list
                if not value:
                    current_key = key
                    current_list = []
                    continue
                
                # Remove quotes
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                
                # Convert numbers
                if value.isdigit():
                    value = int(value)
                elif value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                
                result[key] = value
        
        # Don't forget to save the last list if we were building one
        if current_key and current_list:
            result[current_key] = current_list
        
        return result
    
    def get_lesson_metadata(self, lang: str) -> List[LessonMetadata]:
        """Extract metadata from lesson files."""
        lessons = []
        lessons_dir = self.project_root / lang / "lessons"
        
        if not lessons_dir.exists():
            return lessons
        
        for lesson_file in lessons_dir.glob("lesson*.md"):
            try:
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if content.startswith('---'):
                    end_marker = content.find('---', 3)
                    if end_marker != -1:
                        front_matter_text = content[3:end_marker]
                        front_matter = self.parse_simple_yaml(front_matter_text)
                        
                        # Extract objectives from parsed YAML
                        objectives = front_matter.get('objectives')
                        if objectives and not isinstance(objectives, list):
                            # Convert to list if it's a string
                            objectives = [str(objectives)]
                        
                        lessons.append(LessonMetadata(
                            file_path=str(lesson_file),
                            title=front_matter.get('title', ''),
                            lang=front_matter.get('lang', lang),
                            permalink=front_matter.get('permalink', ''),
                            order=front_matter.get('order', 0),
                            difficulty=front_matter.get('difficulty'),
                            objectives=objectives
                        ))
            
            except Exception as e:
                print(f"Warning: Could not parse {lesson_file}: {e}")
        
        return lessons
    
    def print_results(self) -> bool:
        """Print test results and return overall success status."""
        print("\n" + "=" * 60)
        print("🧙‍♂️ Test Results Summary")
        print("=" * 60)
        
        passed = sum(1 for r in self.results if r.passed)
        failed = len(self.results) - passed
        
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"📊 Total:  {len(self.results)}")
        
        if failed > 0:
            print("\n❌ Failed Tests:")
            for result in self.results:
                if not result.passed:
                    print(f"  • {result.test_name}: {result.message}")
                    if result.details:
                        print(f"    Details: {result.details[:200]}...")
        
        print(f"\n🎯 Overall Status: "
              f"{'✅ PASS' if failed == 0 else '❌ FAIL'}")
        
        if failed == 0:
            print("\n🎉 Congratulations! Your Spellcode Academy content is "
                  "well-structured")
            print("   and ready for students to begin their magical coding "
                  "journey!")
        else:
            print(f"\n💡 Found {failed} issues that should be addressed to "
                  "improve")
            print("   the quality and consistency of your educational content.")
        
        return failed == 0


def main():
    """Main entry point for the test suite."""
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    test_suite = SpellcodeTestSuite(project_root)
    success = test_suite.run_all_tests()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main() 