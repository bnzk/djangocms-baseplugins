import django
from django.contrib import admin
from django import forms
from django.urls import path
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from form_designer.admin import FormAdmin as FormAdminBase
from form_designer.admin import FormFieldAdmin as FormFieldAdminBase
from form_designer.admin import FormSubmissionAdmin as FormSubmissionAdminBase
from form_designer.models import Form, FormField, FormSubmission
# from rangefilter.filter import DateRangeFilter
from xlsxdocument import XLSXDocument
from admin_sort.admin.inlines import DragAndDropSortableInlineMixin


admin.site.unregister(Form)
admin.site.unregister(FormSubmission)


class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        exclude = ('', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['is_required'].initial = False


class FormFieldInline(DragAndDropSortableInlineMixin, FormFieldAdminBase):
    form = FormFieldForm
    position_field = 'ordering'


@admin.register(Form)
class FormAdmin(FormAdminBase):
    inlines = [FormFieldInline]


@admin.register(FormSubmission)
class FormSubmissionAdmin(FormSubmissionAdminBase):

    # list_filter = [('submitted', DateRangeFilter), ] + list(FormSubmissionAdminBase.list_filter)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export/',
                self.admin_site.admin_view(self.export_admin_button),
                name='form_designer_formsubmission_export_change_list'),
        ]
        return my_urls + urls

    def export_admin_action(self, request, queryset):
        """
        Exports the selected rows using file_format.
        """
        return self.export_from_queryset(queryset)

    export_admin_action.short_description = _(
        'Export selected %(verbose_name_plural)s')
    actions = admin.ModelAdmin.actions + [export_admin_action]

    def export_admin_button(self, request, *args, **kwargs):
        """
        exports whats currently filtered in admin
        :return:
        """
        queryset = self.get_export_queryset(request)
        return self.export_from_queryset(queryset)

    def export_from_queryset(self, queryset):
        rows = []
        keys = []
        meta_keys = ['form', 'path', 'date', 'time']
        for submission in queryset:
            data = submission.sorted_data()
            for item in data.items():
                if not item[0] in keys:
                    keys.append(item[0])
        title_row = meta_keys + [key for key in keys]
        rows.append(title_row)
        for submission in queryset:
            data = submission.sorted_data()
            meta_data = [
                submission.form,
                submission.path,
                submission.submitted.date(),
                submission.submitted.time(),
            ]
            data_row = meta_data + [data.get(key, '-') for key in keys]
            rows.append(data_row)

        xlsx = XLSXDocument()
        title = 'forms-{}'.format(timezone.now().strftime('%Y-%m-%d_%H-%M_%Z'))
        xlsx.add_sheet(title)
        xlsx.table([], rows)
        return xlsx.to_response("%s.xlsx" % slugify(title))

    def get_export_queryset(self, request):
        """
        Returns export queryset.
        Default implementation respects applied search and filters.
        """
        list_display = self.get_list_display(request)
        list_display_links = self.get_list_display_links(request, list_display)
        list_filter = self.get_list_filter(request)
        search_fields = self.get_search_fields(request)
        if self.get_actions(request):
            list_display = ['action_checkbox'] + list(list_display)

        ChangeList = self.get_changelist(request)
        changelist_kwargs = {
            'request': request,
            'model': self.model,
            'list_display': list_display,
            'list_display_links': list_display_links,
            'list_filter': list_filter,
            'date_hierarchy': self.date_hierarchy,
            'search_fields': search_fields,
            'list_select_related': self.list_select_related,
            'list_per_page': self.list_per_page,
            'list_max_show_all': self.list_max_show_all,
            'list_editable': self.list_editable,
            'model_admin': self,
        }
        if django.VERSION >= (2, 1):
            changelist_kwargs['sortable_by'] = self.sortable_by
        cl = ChangeList(**changelist_kwargs)

        return cl.get_queryset(request)
