from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from .models import Product, Color, Size, SizeAttribute, CategorySite, ProductPhotos, Vendor
from .admin_link import admin_link

def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)

make_featured.short_description = 'Προσθήκη στην Πρώτη Σελίδα'

def remove_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)

remove_featured.short_description = 'Αφαίρεση από τα Αγαπημένα'

class PhotoInline(admin.TabularInline):
    model = ProductPhotos


@admin.register(ProductPhotos)
class ProductPhotosAdmin(ImportExportModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    save_as = True
    list_display = ['title', 'image_tag_tiny', 'brand', 'tag_final_price', 'site_active', 'brand_link']
    list_filter = ['site_active', 'is_featured', 'category_site', 'brand']
    readonly_fields = ['tag_final_price', 'image_tag_tiny', 'image_tag']
    inlines = [PhotoInline, ]
    search_fields = ['title', ]
    list_selected_related = ['brand']
    # autocomplete_fields = ['category_site']
    filter_horizontal = ['category_site']
    list_per_page = 25
    actions = [make_featured, remove_featured]
    fieldsets = (
        ('Γενικές Πληροφορίες', {
            'fields': (('site_active', 'is_featured', 'size'),
                       ('title', ),
                       ('category_site', ),
                       ('vendor', 'brand', 'color'),
                       ('tag_final_price', 'price', 'price_discount'),
                       ('show_price', 'price_from'),
                       ('measure_unit', ),
                       'image_tag'
                    )
        }),
        ('Site data', {
            'fields': (('sku', 'site_text'),
                       ('slug', ),
                       )
        }),

    )

    def save_model(self, request, obj, form, change):
        if '_saveasnew' in request.POST:
            obj.slug = None
            return super(ProductAdmin, self).save_model(request, obj, form, change)
        return super(ProductAdmin, self).save_model(request, obj, form, change)

    @admin_link('brand', _('Brand'))
    def brand_link(self, brand):
        return brand


admin.site.register(Vendor)
