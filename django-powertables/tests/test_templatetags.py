from django.test import TestCase
from powertables.templatetags.powertable_tags import with_sorting_prefix


class PowertableTemplatetagsTest(TestCase):
    def test_that_with_sorting_prefix_returns_correct_value(self):
        sorting_foo = with_sorting_prefix("foo")
        self.assertEqual(sorting_foo, "sorting_foo")
