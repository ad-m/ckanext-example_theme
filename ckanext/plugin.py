# encoding: utf-8

import ckan.plugins as plugins

import ckan.plugins.toolkit as toolkit


class ExampleThemePlugin(plugins.SingletonPlugin):
    '''Sample resource override plugin.

    An exemplary plugin, the purpose of which is to demonstrate the
    overwriting of selected JS files of the embedded CKAN module without
    copying / forcing it entirely.

    '''
    plugins.implements(plugins.IConfigurer, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_resource('resource', 'ckanext-reclineview')
