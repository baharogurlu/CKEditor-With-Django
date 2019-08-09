# CKEditor-With-Django
CKEditor Rich Text Editor With Django

Contents
Required for using widget with file upload	2
Optional - customizing CKEditor editor	2
Optional for file upload	2
Kullanımı	3
Field	3
Widget	3
Outside of django admin	3
Dosya Yükleme İçin;	4
Using S3	4
If you want to use allowedContent	5
Plugins:	5
CKEditor Configuration Örneği (settings.py)	5
Troubleshooting	7

 

1.	RichTextField, RichTextUploadingField, CKEditorWidget and CKEditorUploadingWidget özelliklerini sağlar.
2.	pip install django-ckeditor yada python path’ine ekle (C:\Users\tr1o5213\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\)
3.	INSTALLED_APPS  içerisine ‘ckeditor’ ekle
4.	Python manage.py collectstatic komutunu çalıştırınız. Projenin ana dizininde yani manage.py olan dizinde static dosyası olmalıdır ve setting py içerisinde STATIC_ROOT path tanıtımı olmalıdır.  Bu komut ckeditor için gerekli olan dosyaları static dosyası altına kopyalar.
Required for using widget with file upload
5.	INSTALLED_APPS  içerisine ‘ckeditor_uploader ekle(file upload işlevini kullanmak için) ve CKEDITOR_UPLOAD_PATH=”uploads/” ekle ancak bunun için MEDIA_ROOT,MEDIA_URL pathleri ekli olmalıdır.
6.	Dosya yüklerken eğer dosya adının otomatik üretilmesini istiyorsak utils.py altına dosya generator metodu yazmalıyız. CKEDITOR_FILENAME_GENERATOR = 'app_name.utils.get_filename' ifadesi settings.py içerisine eklenmelidir.
7.	url(r'^ckeditor/', include('ckeditor_uploader.urls')), urls.py dosyasına ekle
Optional - customizing CKEditor editor
8.	CKEDITOR_CONFIGS settings.py İçerisinde customize edilebilir. Örn: 
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': Full,
    },
}
content = RichTextField(config_name='awesome_ckeditor')
widget = CKEditorWidget(config_name='awesome_ckeditor')
şeklinde kullanılabilir.Default tanımlarsak adını
 CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
} ,
text = RichTextField(config_name='forum-post') şeklinde kullanılır.
 Optional for file upload

9.	CKEDITOR_UPLOAD_SLUGIFY_FILENAME to False setting.py içerisinde 
10.	CKEDITOR_RESTRICT_BY_USER setting to True  Bu özellik örneğin her kullanıcının kendi yüklediği dosyaları görmesini sağlar. Bu özellik sadece CKEditor için getirilmiştir.
11.	CKEDITOR_BROWSE_SHOW_DIRS = True  Browse Server
12.	CKEDITOR_RESTRICT_BY_DATE = True dosyaları tarihe göre ayarlar.
Kullanımı
Field
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()
(Dosya yükleme için : RichTextUploadingField , ckeditor_uploader.fields.)
Widget
Forms.py
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from post.models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)

(Dosya yükleme için : CKEditorUploadingWidget , ckeditor_uploader.widgets.)
Outside of django admin
<form>
    {{ myform.media }}
    {{ myform.as_p }}
    <input type="submit"/>
</form>
or you can load the media manually as it is done in the demo app:
{% load static %}
<script type="text/javascript" src="{% static "ckeditor/ckeditor-init.js" %}"></script>
<script type="text/javascript" src="{% static "ckeditor/ckeditor/ckeditor.js" %}"></script

•	Objeleri listelerken html taglarinin gözükmemesi için safe template tagi kullanılmalıdır. Örneğin; {{name|safe}}
Dosya Yükleme İçin;
•	CKEDITOR_FILE_NAME_GENERATOR nesnesi settings içerisinde appname.utils.get_filename fonsiyonu settings.py içerisinde tanımı yapılır. Appname verilmezse aşağıdaki örnekteki gibi hata oluşur. utils.py dosyasını görmesi gerekir. Utils.py içerisinde get_filename fonskiyonu olmalıdır.
•	Projenin ana dizininde(manage.py ile aynı dizinde) media klasörü ve içerisine uploads klasörü açılmalıdır. Çünkü CKEditor tarafından yüklenen dosyalar uploads altında yer alır. CKEDITOR_UPLOAD_PATH=”uploads/”.
•	Dosyaların upload edilmesi için urls.py içerisine urls_pattern’e  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  eklenmelidir. Örnek kod:
•	urlpatterns = [
    path('admin/', admin.site.urls),
    path('ck_editor/', include('ck_editor.urls', namespace='ck_editor')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
•	Javascript+html tarafında da gözükmesi için aşağıdaki şekilde konfigurasyonu yapılmalıdır. 
•	CKEDITOR.replace( element_id,{
   filebrowserBrowseUrl: '/ckeditor/browse/browse.php',
   filebrowserImageBrowseUrl: '/ckeditor/browse/browse.php?type=Images',
   filebrowserUploadUrl: '/ckeditor/upload/upload.php',
   filebrowserImageUploadUrl: '/ckeditor/upload/upload.php?type=Images'
});
•	Element_id div/textarea vs id değeridir. 
•	Yüklenen dosyaları media/uploads/user_name/YYYY/MM/DD klasör düzeninde yer alır. 
Bootstrap classlarını kullanmak için;
Örneğin buton eklerken bootstrap butonlarını kullanmak istiyorsanız;
1.	Kullanılmak istenen plugin indirilir(https://ckeditor.com/cke4/addon/floatpanel)
2.	İndirilen plugin ckeditor/plugins klasörü altına yapıştırılır.
3.	Ckeditor/config.js içerisinde konfigurasyon içerisine plugin adı aşağıdaki gibi yazılır. (emoji örnektir.)
config.extraPlugins = 'emoji';

Using S3
 Django-editor AWS_QUERYSTRING_AUTH = False komutu olmadan S3 ile çalışmayacaktır. Settings.py içerisine eklenir.

If you want to use allowedContent
allowedContent özelliğini kullanmak için stylesheetparser  devre dışı bırakılır(settings.py).
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
    }

Plugins:
django-ckeditor aşağıdaki pluginlerin hepsini içerir ancak default olarak aktif değildir.
a11yhelp, about, adobeair, ajax, autoembed, autogrow, autolink, bbcode, clipboard, codesnippet,
codesnippetgeshi, colordialog, devtools, dialog, div, divarea, docprops, embed, embedbase,
embedsemantic, filetools, find, flash, forms, iframe, iframedialog, image, image2, language,
lineutils, link, liststyle, magicline, mathjax, menubutton, notification, notificationaggregator,
pagebreak, pastefromword, placeholder, preview, scayt, sharedspace, showblocks, smiley,
sourcedialog, specialchar, stylesheetparser, table, tableresize, tabletools, templates, uicolor,
uploadimage, uploadwidget, widget, wsc, xml
(The image/file upload feature is done by the uploadimage plugin.)

CKEditor Configuration Örneği (settings.py)
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

Troubleshooting
If your browser has problems displaying uploaded images in the image upload window you may need to change Django settings: X_FRAME_OPTIONS = 'SAMEORIGIN'. More on https://docs.djangoproject.com/en/1.11/ref/clickjacking/#setting-x-frame-options-for-all-responses






