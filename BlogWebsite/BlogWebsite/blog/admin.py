from django.contrib import admin
from .models import Post
from .models import myUsers
from .models import Comment
from .models import category


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "Title", "Content", "Category", "Date_Published",)


class commentAdmin(admin.ModelAdmin):
    list_display = ("id","PostID", "UserID", "Content", "DatePosted",)


class userAdmin(admin.ModelAdmin):
    list_display = ("id","Username", "Email", "Password",)
class categoryAdmin(admin.ModelAdmin):
    list_display = ("id","Name",)


admin.site.register(Post, PostAdmin)
admin.site.register(myUsers,userAdmin)
admin.site.register(Comment, commentAdmin)
admin.site.register(category,categoryAdmin)
