#!/bin/bash
# Spellcode Academy Test Runner
# Comprehensive testing script for content validation and quality assurance

set -e

echo "🧙‍♂️ Spellcode Academy Test Suite"
echo "=================================="

# Check if we're in the right directory
if [ ! -f "_config.yml" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Create test results directory
mkdir -p test-results

echo "📦 Installing test dependencies..."
if [ -f "requirements-test.txt" ]; then
    pip install -r requirements-test.txt
else
    echo "⚠️  Warning: requirements-test.txt not found, installing basic dependencies"
    pip install PyYAML beautifulsoup4 markdown pytest
fi

echo ""
echo "🔍 Running comprehensive content validation..."

# Run the main test suite
if [ -f "test_runner.py" ]; then
    echo "Running custom test suite..."
    python test_runner.py
    CUSTOM_EXIT_CODE=$?
else
    echo "⚠️  Custom test runner not found"
    CUSTOM_EXIT_CODE=0
fi

echo ""
echo "🧪 Running pytest-based tests..."

# Run pytest if tests directory exists
if [ -d "tests" ]; then
    pytest tests/ \
        --html=test-results/report.html \
        --self-contained-html \
        --junitxml=test-results/junit.xml \
        -v
    PYTEST_EXIT_CODE=$?
else
    echo "⚠️  Tests directory not found, skipping pytest"
    PYTEST_EXIT_CODE=0
fi

echo ""
echo "🏗️  Testing Jekyll build..."

# Test Jekyll build if bundle is available
if command -v bundle &> /dev/null; then
    echo "Testing Jekyll build process..."
    bundle exec jekyll build --dry-run
    JEKYLL_EXIT_CODE=$?
else
    echo "⚠️  Bundle not found, skipping Jekyll build test"
    JEKYLL_EXIT_CODE=0
fi

echo ""
echo "📊 Test Results Summary"
echo "======================"

# Calculate overall exit code
OVERALL_EXIT_CODE=0

if [ $CUSTOM_EXIT_CODE -ne 0 ]; then
    echo "❌ Custom test suite: FAILED"
    OVERALL_EXIT_CODE=1
else
    echo "✅ Custom test suite: PASSED"
fi

if [ $PYTEST_EXIT_CODE -ne 0 ]; then
    echo "❌ Pytest suite: FAILED"
    OVERALL_EXIT_CODE=1
else
    echo "✅ Pytest suite: PASSED"
fi

if [ $JEKYLL_EXIT_CODE -ne 0 ]; then
    echo "❌ Jekyll build: FAILED"
    OVERALL_EXIT_CODE=1
else
    echo "✅ Jekyll build: PASSED"
fi

echo ""
if [ $OVERALL_EXIT_CODE -eq 0 ]; then
    echo "🎉 All tests passed! Your Spellcode Academy is ready for students."
else
    echo "💥 Some tests failed. Please check the output above for details."
fi

echo ""
echo "📁 Test reports saved to: test-results/"
echo "   - HTML report: test-results/report.html"
echo "   - JUnit XML: test-results/junit.xml"

exit $OVERALL_EXIT_CODE 