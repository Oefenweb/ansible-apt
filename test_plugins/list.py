class TestModule(object):

    def tests(self):
        return {
            'list': self.is_list,
        }

    def is_list(self, value):
        """Test if a value is of type list.

        Jinja2 provides the tests `iterable` and `sequence`, but those also
        match strings and dicts and can therefore not be used to determine, if a
        value is a true list type. Therefore I wrote this test, which solves
        this shortcoming.

        Args:
            value: A value, that shall be type tested

        Returns:
            bool: True, if value is of type list, False otherwise.
        """
        return isinstance(value, list)
