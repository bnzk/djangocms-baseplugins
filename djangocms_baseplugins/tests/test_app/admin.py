from django.contrib import admin

from djangocms_baseplugins.admin import FormFieldStashMixin
from .models import TestModelSingle, TestModelAdvanced, TestModelInInlineModel, TestInlineModelSingle, \
    TestInlineModel


class TestModelAdmin(FormFieldStashMixin, admin.ModelAdmin):
    single_formfield_stash = ('selection', )

admin.site.register(TestModelSingle, TestModelAdmin)


class TestInlineModelInline(admin.StackedInline):
    model = TestInlineModel


ADVANCED_STASH = {
    'set': {
        'set1': ('set1_1', '#testinlinemodel_set-group', ),
        'set2': ('set2_1', 'set2_2', 'set2_3', ),
        'set3': ('set3_1', 'set2_1', ),
    },
}


class TestModelAdvancedAdmin(FormFieldStashMixin, admin.ModelAdmin):
    inlines = [TestInlineModelInline, ]
    formfield_stash = ADVANCED_STASH

admin.site.register(TestModelAdvanced, TestModelAdvancedAdmin)


class TestInlineModelSingleInline(FormFieldStashMixin, admin.StackedInline):
    model = TestInlineModelSingle
    single_formfield_stash = ('selection', )


class TestModelInInlineModelAdmin(FormFieldStashMixin, admin.ModelAdmin):
    inlines = [TestInlineModelSingleInline, ]

admin.site.register(TestModelInInlineModel, TestModelInInlineModelAdmin)
