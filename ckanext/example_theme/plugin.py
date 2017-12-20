from ckan.exceptions import CkanConfigurationException

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Example_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)

    def update_config(self, config):
        plugins = config['ckan.plugins'].split(' ')
        if 'recline_view' not in plugins:
            raise CkanConfigurationException(
                'You provided an invalid value for ckan.plugins. '
                'The "example_theme" plugin requires the "recline_view" plugin. '
                'Add "recline_view" to ckan.plugins.'
            )
        if plugins.index('example_theme') > plugins.index('recline_view'):
            raise CkanConfigurationException(
                'You provided an invalid value for ckan.plugins. '
                'The "example_theme" plugin must be before "recline_view". Change the order of the plugins.'
                'Move "recline_view" after "example_theme" in ckan.plugins.'
            )
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_resource('public', 'example_theme')
