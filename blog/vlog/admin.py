
from django.contrib import admin
from .models import AboutSection, Contact, Post, Category, Comment, Vent, VentComment
# Register your models here.
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']

class VentAdmin(admin.ModelAdmin):
    list_display = ['title', 'approved', 'created_at']
    list_filter = ['approved', 'created_at']
    search_fields = ['title', 'name', 'content']
    actions = ['approve_vents']

    def approve_vents(self, request, queryset):
        queryset.update(approved=True)
    approve_vents.short_description = "Approve selected vents"

class VentCommentAdmin(admin.ModelAdmin):
    list_display = ['commenter_name', 'created_at']  # Update with existing fields
    search_fields = ['commenter_name', 'content']



    
    







    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Vent, VentAdmin)
admin.site.register(VentComment, VentCommentAdmin)

