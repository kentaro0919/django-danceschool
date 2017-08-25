from django.forms import ModelForm
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import DiscountCombo, DiscountComboComponent, PointGroup, PricingTierGroup, RegistrationDiscount, TemporaryRegistrationDiscount
from danceschool.core.models import Registration, TemporaryRegistration, PricingTier


class DiscountComboComponentInline(admin.StackedInline):
    model = DiscountComboComponent
    extra = 1
    fields = (('pointGroup','quantity',),'allWithinPointGroup',('level','weekday'),)


class DiscountComboAdminForm(ModelForm):

    class Meta:
        model = DiscountCombo
        exclude = []

    class Media:
        js = ('js/discountcombo_collapsetypes.js',)


class DiscountComboAdmin(admin.ModelAdmin):
    inlines = [DiscountComboComponentInline,]
    form = DiscountComboAdminForm

    list_display = ('name','discountType','active','expirationDate','restrictions')
    list_filter = ('discountType','active','newCustomersOnly','expirationDate')
    ordering = ('name',)
    actions = ['enableDiscount','disableDiscount']

    fieldsets = (
        (None, {
            'fields': ('name',('active','expirationDate'),'newCustomersOnly','daysInAdvanceRequired','discountType',)
        }),
        (_('Flat-Price Discount (in default currency)'), {
            'classes': ('type_flatPrice',),
            'fields': ('onlineStudentPrice','doorStudentPrice','onlineGeneralPrice','doorGeneralPrice'),
        }),
        (_('Dollar Discount (in default currency)'), {
            'classes': ('type_dollarDiscount',),
            'fields': ('dollarDiscount',),
        }),
        (_('Percentage Discount'), {
            'classes': ('type_percentageDiscount',),
            'fields': ('percentDiscount','percentUniversallyApplied'),
        }),
    )

    def restrictions(self,obj):
        text = []
        if obj.newCustomersOnly:
            text.append(_('First-time customer'))
        if obj.daysInAdvanceRequired:
            text.append(_('%s day advance registration' % obj.daysInAdvanceRequired))
        return ', '.join([str(x) for x in text])
    restrictions.short_description = _('Restrictions')

    def disableDiscount(self, request, queryset):
        rows_updated = queryset.update(active=False)
        if rows_updated == 1:
            message_bit = "1 discount was"
        else:
            message_bit = "%s discounts were" % rows_updated
        self.message_user(request, "%s successfully disabled." % message_bit)
    disableDiscount.short_description = _('Disable selected Discounts')

    def enableDiscount(self, request, queryset):
        rows_updated = queryset.update(active=True)
        if rows_updated == 1:
            message_bit = "1 discount was"
        else:
            message_bit = "%s discounts were" % rows_updated
        self.message_user(request, "%s successfully enabled." % message_bit)
    enableDiscount.short_description = _('Enable selected Discounts')


class RegistrationDiscountInline(admin.TabularInline):
    model = RegistrationDiscount
    readonly_fields = ('discount', 'discountAmount')
    extra = 0

    # Prevents adding new discounts without going through
    # the standard registration process
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TemporaryRegistrationDiscountInline(admin.TabularInline):
    model = TemporaryRegistrationDiscount
    readonly_fields = ('discount', 'discountAmount')
    extra = 0

    # Prevents adding new discounts without going through
    # the standard registration process
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PricingTierGroupInline(admin.TabularInline):
    model = PricingTierGroup
    extra = 0
    verbose_name = _('pricing tier discount group')
    verbose_name_plural = _('pricing tier discount groups')


class PointGroupAdmin(admin.ModelAdmin):
    inlines = (PricingTierGroupInline,)

    list_display = ('name',)
    ordering = ('name',)


# This adds the inlines to Registration and TemporyRegistration without subclassing
admin.site._registry[Registration].inlines.insert(0,RegistrationDiscountInline)
admin.site._registry[TemporaryRegistration].inlines.insert(0,TemporaryRegistrationDiscountInline)
admin.site._registry[PricingTier].inlines.insert(0,PricingTierGroupInline)

admin.site.register(DiscountCombo,DiscountComboAdmin)
admin.site.register(PointGroup,PointGroupAdmin)