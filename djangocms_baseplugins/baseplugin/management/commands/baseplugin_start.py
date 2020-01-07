import logging
import os
import shutil

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    - copy plugin_template folder to new location
    - search and replace PLUGINTEMPLATE / Plugintemplate / plugintemplate in all files
    - rename template name, test file name
    """
    help = (
        "Bootstrap a new cms plugin, based on djangocms-baseplugins concepts."
        "")

    def add_arguments(self, parser):
        parser.add_argument('path', help="""
The path to copy the files to.
Will take part after last / as package name
""")
        parser.add_argument('plugin_name', help="""
Name of the new plugin. CameCase. like Teaser or ContentNav
""")

    def handle(self, *args, **options):
        # Use a stdout logger
        logger = logging.getLogger(__name__)
        stream = logging.StreamHandler(self.stdout)
        logger.addHandler(stream)
        logger.setLevel(logging.DEBUG)

        # copy
        path = options['path']
        plugin_name = options['plugin_name']
        current_path = os.path.dirname(__file__)
        source_folder = os.path.join(current_path, '..', '..', 'plugin_template')
        if not path.startswith('/'):
            target_folder = os.path.join('.', path)
        else:
            target_folder = path
        if os.path.exists(target_folder):
            logger.log(logging.INFO, 'Aborting, target folder already existing: %s' % target_folder)
            return
        shutil.copytree(source_folder, target_folder)

        # replace
        recursive_replace_template(target_folder, 'PluginTemplate', plugin_name)
        recursive_replace_template(target_folder, 'PLUGINTEMPLATE', plugin_name.upper())
        recursive_replace_template(target_folder, 'plugintemplate', plugin_name.lower())

        # rename
        template_folder = os.path.join(target_folder, 'templates', 'djangocms_baseplugins', )
        os.rename(
            os.path.join(template_folder, 'plugin_template.html'),
            os.path.join(template_folder, plugin_name.lower() + '.html'),
        )
        test_folder = os.path.join(target_folder, 'tests', )
        os.rename(
            os.path.join(test_folder, 'plugin.py'),
            os.path.join(test_folder, 'test_' + plugin_name.lower() + "plugin.py"),
        )

        logger.log(logging.INFO, 'Success, copied new plugin files to:')
        logger.log(logging.INFO,  target_folder)
        logger.log(logging.INFO, '---')
        logger.log(logging.INFO, 'Next steps')
        logger.log(logging.INFO, '- Adapt your models.py')
        logger.log(logging.INFO, '- add your app to INSTALLED_APPS')
        logger.log(logging.INFO, '- run ./manage.py makemigrations')
        logger.log(logging.INFO, '- run ./manage.py test (basic concepts like class names ')
        logger.log(logging.INFO, '  applied, admin form working, adapt to your needs)')


def recursive_replace_template(target_folder, target, replacement):
    for dname, dirs, files in os.walk(target_folder):
        for fname in files:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace(target, replacement)
            with open(fpath, "w") as f:
                f.write(s)
