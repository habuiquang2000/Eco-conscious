# https://django-ckeditor.readthedocs.io/en/latest/#toc-entry-5
# CKEDITOR_UPLOAD_PATH setting. This setting specifies an
# relative path to your ckeditor media upload directory. Make
# sure you have write permissions for the path, i.e.:
#     CKEDITOR_UPLOAD_PATH = 'content/ckeditor/' which
#     will be added to SITE_MEDIA/MEDIA_ROOT where needed by storage engine.

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'full',
    },
    'default': {
        'toolbar': 'full',
        # 'height': 456,
        # 'width': 656,
    },
    # 'versionCheck': False,
}
