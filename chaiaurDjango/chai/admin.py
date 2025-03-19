from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiCertificate, ChaiStore

# Register your models here.


class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2


class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added", "price")
    inlines = [ChaiReviewInline]


class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ["chai_varieties"]


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number", "issue_date", "valid_until")


admin.site.register(ChaiVarity, ChaiVarietyAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
admin.site.register(ChaiStore, ChaiStoreAdmin)
