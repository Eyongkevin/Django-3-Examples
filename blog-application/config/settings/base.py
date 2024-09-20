# Application definition
from pathlib import Path

SITE_ID = 1

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_APPS = [
    # add default apps here
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.postgres",
]
CREATED_APPS = [
    # add created apps here
    "blogs.blog.apps.BlogConfig",
    "blogs.comment.apps.CommentConfig",
]

THIRD_PARTY_APPS = [
    # add third-party apps here
    "taggit",
    "admin_honeypot",
    "ckeditor",
]

INSTALLED_APPS = [*DEFAULT_APPS, *CREATED_APPS, *THIRD_PARTY_APPS]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        "OPTIONS": {"max_similarity": 0.5},
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        # "OPTIONS": {"max_length": 12},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))
# STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
# STATIC_ROOT = "/usr/local/var/www/blog/staticfiles"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CSP(Content Security Policy) Configs
# CSP_DEFAULT_SRC = [
#     "'self'",
#     "http://fonts.googleapis.com/css?family=Muli",
# ]
# CSP_SCRIPT_SRC = [
#     "'self'",
#     "http://fonts.googleapis.com/",
# ]
# CSP_FONT_SRC = [
#     "'self'",
#     "http://fonts.gstatic.com/s/muli/v28/7Aulp_0qiz-aVz7u3PJLcUMYOFnOkEk40e6fwniDtzNAAw.woff",
#     "http://fonts.gstatic.com/s/muli/v28/7Aulp_0qiz-aVz7u3PJLcUMYOFnOkEk50e6fwniDtzNAAw.woff",
#     "http://fonts.gstatic.com/s/muli/v28/7Aulp_0qiz-aVz7u3PJLcUMYOFnOkEk30e6fwniDtzM.woff",
# ]

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "width": "auto",
        "extraPlugins": ",".join(
            [
                "codesnippet",
                "bbcode",
            ]
        ),
        "codeSnippet_languages": {
            "bash": "Bash",
            "css": "CSS",
            "django": "Django",
            "html": "HTML",
            "javascript": "JavaScript",
            "sql": "Sql",
            "python": "Python",
        },
    },
}
# CKEDITOR_CONFIGS = {
#     "default": {
#         "skin": "moono",
#         # 'skin': 'office2013',
#         "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
#         "toolbar_YourCustomToolbarConfig": [
#             {
#                 "name": "document",
#                 "items": [
#                     "Source",
#                     "-",
#                     "Save",
#                     "NewPage",
#                     "Preview",
#                     "Print",
#                     "-",
#                     "Templates",
#                 ],
#             },
#             {
#                 "name": "clipboard",
#                 "items": [
#                     "Cut",
#                     "Copy",
#                     "Paste",
#                     "PasteText",
#                     "PasteFromWord",
#                     "-",
#                     "Undo",
#                     "Redo",
#                 ],
#             },
#             {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
#             {
#                 "name": "forms",
#                 "items": [
#                     "Form",
#                     "Checkbox",
#                     "Radio",
#                     "TextField",
#                     "Textarea",
#                     "Select",
#                     "Button",
#                     "ImageButton",
#                     "HiddenField",
#                 ],
#             },
#             "/",
#             {
#                 "name": "basicstyles",
#                 "items": [
#                     "Bold",
#                     "Italic",
#                     "Underline",
#                     "Strike",
#                     "Subscript",
#                     "Superscript",
#                     "-",
#                     "RemoveFormat",
#                 ],
#             },
#             {
#                 "name": "paragraph",
#                 "items": [
#                     "NumberedList",
#                     "BulletedList",
#                     "-",
#                     "Outdent",
#                     "Indent",
#                     "-",
#                     "Blockquote",
#                     "CreateDiv",
#                     "-",
#                     "JustifyLeft",
#                     "JustifyCenter",
#                     "JustifyRight",
#                     "JustifyBlock",
#                     "-",
#                     "BidiLtr",
#                     "BidiRtl",
#                     "Language",
#                 ],
#             },
#             {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
#             {
#                 "name": "insert",
#                 "items": [
#                     "Image",
#                     "Flash",
#                     "Table",
#                     "HorizontalRule",
#                     "Smiley",
#                     "SpecialChar",
#                     "PageBreak",
#                     "Iframe",
#                 ],
#             },
#             "/",
#             {"name": "styles", "items": ["Styles", "Format", "Font", "FontSize"]},
#             {"name": "colors", "items": ["TextColor", "BGColor"]},
#             {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
#             {"name": "about", "items": ["About"]},
#             "/",  # put this to force next toolbar on new line
#             {
#                 "name": "yourcustomtools",
#                 "items": [
#                     # put the name of your editor.ui.addButton here
#                     "Preview",
#                     "Maximize",
#                 ],
#             },
#         ],
#         "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
#         # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # 'height': 291,
#         # 'width': '100%',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 940,
#         # 'toolbarCanCollapse': True,
#         # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         "tabSpaces": 4,
#         "extraPlugins": ",".join(
#             [
#                 "uploadimage",  # the upload image feature
#                 # your extra plugins here
#                 "codesnippet",
#                 # "div",
#                 # "autolink",
#                 # "autoembed",
#                 # "embedsemantic",
#                 # "autogrow",
#                 # # 'devtools',
#                 # "widget",
#                 # "lineutils",
#                 # "clipboard",
#                 # "dialog",
#                 # "dialogui",
#                 # "elementspath",
#             ]
#         ),
#         "codeSnippet_languages": {
#             "bash": "Bash",
#             "css": "CSS",
#             "django": "Django",
#             "html": "HTML",
#             "javascript": "JavaScript",
#             "sql": "Sql",
#             "python": "Python",
#         },
#     }
# }

# def get_env_variables(
#     var_name: str,
#     default: Optional[Union[str, bool]] = None,
# ):
#     """Get the environment variable or return default if given or exception

#     Args:
#         var_name (str): the variable to look for
#         default (Union[str,bool]): the default value
#     """
#     try:
#         return (
#             os.environ.get(var_name, default)
#             if default is not None
#             else os.environ[var_name]
#         )
#     except KeyError as err:
#         error_msg = f"set the {var_name} variable"
#         raise ImproperlyConfigured(error_msg) from err
