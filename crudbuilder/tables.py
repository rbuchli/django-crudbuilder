import django_tables2 as tables
from django_tables2.utils import A

from .abstract import BaseBuilder
from .helpers import model_class_form, plural, custom_postfix_url


class TableBuilder(BaseBuilder):
    """
    Table builder which returns django_tables2 instance
    app : app name
    model : model name for which table will be generated
    table_fields : display fields for tables2 class
    css_table : css class for generated tables2 class
    """

    def generate_table(self):
        model_class = self.get_model_class()

        detail_url_name = '{}-{}-detail'.format(
            self.app, custom_postfix_url(self.crud(), self.model)
        )

        main_attrs = dict(
            pk=tables.LinkColumn(detail_url_name, args=[A('pk')])
        )

        # separator = ', '

        meta_attrs = dict(
            model=self.get_model_class,
            # There may be only one field. That's why we have to check first and create a tuple later
            # changed by Reto Buchli, 04.06.2021, removed, wrong column order
            # fields=('pk',) + tuple(self.tables2_fields) if isinstance(self.tables2_fields, str) else (
            #    self.tables2_fields) if self.tables2_fields else ('pk',),
            fields=('pk',) + self.tables2_fields if self.tables2_fields else ('pk',),
            attrs={
                "class": self.tables2_css_class,
                "empty_text": "No {} exist".format(plural(self.model, ''))
            })

        main_attrs['Meta'] = type('Meta', (), meta_attrs)
        klass = type(
            model_class_form(self.model + 'Table'),
            (tables.Table,),
            main_attrs
        )
        return klass
