import json
import os
import unittest

from main import TodoParser


def count_issues_for_file_type(raw_issues, file_type):
    num_issues = 0
    for issue in raw_issues:
        if issue.markdown_language == file_type:
            num_issues += 1
    return num_issues


class NewIssueTests(unittest.TestCase):
    # Check for newly added TODOs across the files specified.
    def setUp(self):
        diff_file = open('tests/test_new.diff', 'r')
        parser = TodoParser()
        with open('syntax.json', 'r') as syntax_json:
            parser.syntax_dict = json.load(syntax_json)
        self.raw_issues = parser.parse(diff_file)

    def test_python_issues(self):
        # Includes 2 tests for Starlark.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 6)

    def test_yaml_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'yaml'), 2)

    def test_php_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'php'), 4)

    def test_java_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'java'), 2)

    def test_json_with_comments_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'javascript'), 2)

    def test_json5_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'javascript'), 2)

    def test_ruby_issues(self):
        # Includes 2 tests for Crystal.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'ruby'), 5)

    def test_abap_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'abap'), 2)

    def test_sql_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'sql'), 1)

    def test_tex_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'tex'), 2)

    def test_julia_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'julia'), 2)

    def test_starlark_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 6)

    def test_autohotkey_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'autohotkey'), 1)

    def test_handlebars_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'handlebars'), 2)

    def test_org_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'text'), 4)

    def test_scss_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'scss'), 2)

    def test_twig_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'twig'), 2)

    def test_md_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'markdown'), 8)

    def test_r_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'r'), 2)

    def test_haskell_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'haskell'), 2)

    def test_clojure_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'clojure'), 2)

    def test_nix_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'nix'), 2)

    def test_xaml_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'xml'), 2)

class ClosedIssueTests(unittest.TestCase):
    # Check for removed TODOs across the files specified.
    def setUp(self):
        diff_file = open('tests/test_closed.diff', 'r')
        parser = TodoParser()
        with open('syntax.json', 'r') as syntax_json:
            parser.syntax_dict = json.load(syntax_json)
        self.raw_issues = parser.parse(diff_file)

    def test_python_issues(self):
        # Includes 1 test for Starlark.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 5)

    def test_yaml_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'yaml'), 2)

    def test_php_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'php'), 4)

    def test_java_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'java'), 2)

    def test_ruby_issues(self):
        # Includes 2 tests for Crystal.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'ruby'), 5)

    def test_abap_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'abap'), 2)

    def test_sql_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'sql'), 1)

    def test_tex_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'tex'), 2)

    def test_julia_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'julia'), 4)

    def test_starlark_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 5)

    def test_json_with_comments_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'javascript'), 2)

    def test_json5_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'javascript'), 2)

    def test_autohotkey_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'autohotkey'), 1)

    def test_handlebars_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'handlebars'), 2)

    def test_org_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'text'), 4)

    def test_scss_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'scss'), 2)

    def test_twig_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'twig'), 2)

    def test_md_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'markdown'), 8)

    def test_r_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'r'), 2)

    def test_haskell_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'haskell'), 2)

    def test_clojure_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'clojure'), 2)

    def test_nix_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'nix'), 2)

    def test_xaml_issues(self):
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'xml'), 2)

class IgnorePatternTests(unittest.TestCase):

    def test_single_ignore(self):
        os.environ['IGNORE'] = '.*\\.java'
        parser = TodoParser()
        with open('syntax.json', 'r') as syntax_json:
            parser.syntax_dict = json.load(syntax_json)
        diff_file = open('tests/test_closed.diff', 'r')
        self.raw_issues = parser.parse(diff_file)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 5)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'yaml'), 2)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'php'), 4)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'java'), 0)
        # Includes 2 tests for Crystal.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'ruby'), 5)
        os.environ['IGNORE'] = ''

    def test_multiple_ignores(self):
        os.environ['IGNORE'] = '.*\\.java, tests/example-file\\.php'
        parser = TodoParser()
        with open('syntax.json', 'r') as syntax_json:
            parser.syntax_dict = json.load(syntax_json)
        diff_file = open('tests/test_closed.diff', 'r')
        self.raw_issues = parser.parse(diff_file)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'python'), 5)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'yaml'), 2)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'php'), 0)
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'java'), 0)
        # Includes 2 tests for Crystal.
        self.assertEqual(count_issues_for_file_type(self.raw_issues, 'ruby'), 5)
        os.environ['IGNORE'] = ''

class EscapeMarkdownTest(unittest.TestCase):
    def test_simple_escape(self):
        os.environ['ESCAPE'] = 'true'
        parser = TodoParser()
        with open('syntax.json', 'r') as syntax_json:
            parser.syntax_dict = json.load(syntax_json)
        diff_file = open('tests/test_escape.diff', 'r')

        # I had no other idea to make these checks dynamic.
        self.raw_issues = parser.parse(diff_file)
        self.assertEqual(len(self.raw_issues), 2)

        issue = self.raw_issues[0]
        self.assertEqual(len(issue.body), 2)
        self.assertEqual(issue.body[0], '\\# Some title')
        self.assertEqual(issue.body[1], '\\<SomeTag\\>')

        issue = self.raw_issues[1]
        self.assertEqual(len(issue.body), 2)
        self.assertEqual(issue.body[0], '\\# Another title')
        self.assertEqual(issue.body[1], '\\<AnotherTag\\>')

