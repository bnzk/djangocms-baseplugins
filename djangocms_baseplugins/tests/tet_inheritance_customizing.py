# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

from djangocms_baseplugins.tests.utils.django_utils import create_superuser
from djangocms_baseplugins.tests.utils.selenium_utils import SeleniumTestCase, CustomWebDriver, \
    invisibility_of
from djangocms_baseplugins.tests.test_app.models import TestModelSingle, TestModelAdvanced


class FormFieldStashAdminTests(SeleniumTestCase):
    def setUp(self):
        self.single_empty = TestModelSingle()
        self.single_empty.save()
        self.single = TestModelSingle(**{'selection': 'octopus', })
        self.single.save()
        self.advanced_empty = TestModelAdvanced()
        self.advanced_empty.save()
        self.advanced = TestModelAdvanced(**{'set': 'set1', })
        self.advanced.save()
        self.superuser = create_superuser()
        # Instantiating the WebDriver will load your browser
        self.wd = CustomWebDriver()

    def tearDown(self):
        self.wd.quit()

    def test_app_index_get(self):
        self.login()
        self.open(reverse('admin:index'))
        self.wd.find_css(".app-test_app")

    def test_single_stash_empty(self):
        self.login()
        self.open(reverse('admin:test_app_testmodelsingle_change', args=[self.single_empty.id]))
        horse = self.wd.find_css("div.field-horse")
        # why wait? widget init delays initialization for 20ms, for other widgets to initialize.
        wait = WebDriverWait(self.wd, 1)
        wait.until(invisibility_of(horse))
        # self.assertFalse(horse.is_displayed())
        bear = self.wd.find_css("div.field-bear")
        wait.until(invisibility_of(bear))
        # self.assertFalse(bear.is_displayed())
        octo = self.wd.find_css("div.field-octopus")
        wait.until(invisibility_of(octo))
        # self.assertFalse(octo.is_displayed())

    def test_single_stash(self):
        self.login()
        self.open(reverse('admin:test_app_testmodelsingle_change', args=[self.single.id]))
        horse = self.wd.find_css("div.field-horse")
        wait = WebDriverWait(self.wd, 1)
        wait.until(invisibility_of(horse))
        # self.assertFalse(horse.is_displayed())
        bear = self.wd.find_css("div.field-bear")
        wait.until(invisibility_of(bear))
        # self.assertFalse(bear.is_displayed())
        octo = self.wd.find_css("div.field-octopus")
        wait.until(visibility_of(octo))
        # self.assertTrue(octo.is_displayed())
        # change select value
        self.wd.find_css("div.field-selection select > option[value=horse]").click()
        horse = self.wd.find_css("div.field-horse")
        self.assertTrue(horse.is_displayed())
        octo = self.wd.find_css("div.field-octopus")
        self.assertFalse(octo.is_displayed())

    def test_multi_stash_empty(self):
        self.login()
        self.open(reverse('admin:test_app_testmodeladvanced_change', args=[self.advanced_empty.id]))
        inline = self.wd.find_css("#testinlinemodel_set-group")
        wait = WebDriverWait(self.wd, 1)
        wait.until(invisibility_of(inline))
        # self.assertFalse(inline.is_displayed())
        f11 = self.wd.find_css("div.field-set1_1")
        wait.until(invisibility_of(f11))
        # self.assertFalse(f11.is_displayed())
        f31 = self.wd.find_css("div.field-set3_1")
        wait.until(invisibility_of(f31))
        # self.assertFalse(f31.is_displayed())

    def test_multi_stash(self):
        self.login()
        self.open(reverse('admin:test_app_testmodeladvanced_change', args=[self.advanced.id]))
        inline = self.wd.find_css("#testinlinemodel_set-group")
        wait = WebDriverWait(self.wd, 1)
        wait.until(visibility_of(inline))
        # self.assertTrue(inline.is_displayed())
        f11 = self.wd.find_css("div.field-set1_1")
        wait.until(visibility_of(f11))
        # self.assertTrue(f11.is_displayed())
        f31 = self.wd.find_css("div.field-set3_1")
        wait.until(invisibility_of(f31))
        # self.assertFalse(f31.is_displayed())

