from django.conf import settings
from django.template import Library

register = Library()
ri = register.inclusion_tag


def gtm_tag(context, google_tag_id=None, google_tag_auth=None, google_tag_preview=None):
    request = context.get("request")
    if request:
        if request.COOKIES.get(getattr(settings, "GOOGLE_TAG_BYPASS_COOKIE", None)):
            return

    if google_tag_id is None:
        google_tag_id = getattr(settings, "GOOGLE_TAG_ID", None)
    if google_tag_auth is None:
        google_tag_auth = getattr(settings, "GOOGLE_TAG_AUTH", None)
    if google_tag_preview is None:
        google_tag_preview = getattr(settings, "GOOGLE_TAG_PREVIEW", None)
    return {
        "google_tag_id": google_tag_id,
        "google_tag_auth": google_tag_auth,
        "google_tag_preview": google_tag_preview,
    }


ri("gtm/gtm.html", name="gtm", takes_context=True)(gtm_tag)
ri("gtm/gtm_head.html", name="gtm_head", takes_context=True)(gtm_tag)
ri("gtm/gtm_body.html", name="gtm_body", takes_context=True)(gtm_tag)
