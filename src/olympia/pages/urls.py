from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponsePermanentRedirect as perma_redirect
from django.views.generic.base import TemplateView

from olympia.amo.urlresolvers import reverse


urlpatterns = [
    url(
        '^about$',
        TemplateView.as_view(template_name='pages/about.lhtml'),
        name='pages.about',
    ),
    url(
        '^google1f3e37b7351799a5\.html$',
        TemplateView.as_view(
            template_name='pages/google_webmaster_verification.html'
        ),
    ),
    url(
        '^google231a41e803e464e9\.html$',
        TemplateView.as_view(template_name='pages/google_search_console.html'),
    ),
    url(
        '^review_guide$',
        TemplateView.as_view(template_name='pages/review_guide.html'),
        name='pages.review_guide',
    ),
    url(
        '^shield-study-2/',
        TemplateView.as_view(template_name='pages/shield_study_2.html'),
        name='pages.shield_study_2',
    ),
    url(
        '^shield_study_3$',
        TemplateView.as_view(template_name='pages/shield_study_3.html'),
        name='pages.shield_study_3',
    ),
    url(
        '^shield_study_4$',
        TemplateView.as_view(template_name='pages/shield_study_4.html'),
        name='pages.shield_study_4',
    ),
    url(
        '^shield_study_5$',
        TemplateView.as_view(template_name='pages/shield_study_5.html'),
        name='pages.shield_study_5',
    ),
    url(
        '^shield_study_6$',
        TemplateView.as_view(template_name='pages/shield_study_6.html'),
        name='pages.shield_study_6',
    ),
    url(
        '^shield_study_7$',
        TemplateView.as_view(template_name='pages/shield_study_7.html'),
        name='pages.shield_study_7',
    ),
    url(
        '^shield_study_8$',
        TemplateView.as_view(template_name='pages/shield_study_8.html'),
        name='pages.shield_study_8',
    ),
    url(
        '^shield_study_9$',
        TemplateView.as_view(template_name='pages/shield_study_9.html'),
        name='pages.shield_study_9',
    ),
    url(
        '^shield_study_10$',
        TemplateView.as_view(template_name='pages/shield_study_10.html'),
        name='pages.shield_study_10',
    ),
    url(
        '^shield_study_11$',
        TemplateView.as_view(template_name='pages/shield_study_11.html'),
        name='pages.shield_study_11',
    ),
    url(
        '^shield_study_12$',
        TemplateView.as_view(template_name='pages/shield_study_12.html'),
        name='pages.shield_study_12',
    ),
    url(
        '^shield_study_13$',
        TemplateView.as_view(template_name='pages/shield_study_13.html'),
        name='pages.shield_study_13',
    ),
    url(
        '^shield_study_14$',
        TemplateView.as_view(template_name='pages/shield_study_14.html'),
        name='pages.shield_study_14',
    ),
    url(
        '^shield_study_15$',
        TemplateView.as_view(template_name='pages/shield_study_15.html'),
        name='pages.shield_study_15',
    ),
    url(
        '^shield_study_16$',
        TemplateView.as_view(template_name='pages/shield_study_16.html'),
        name='pages.shield_study_16',
    ),
    url(
        '^pages/review_guide$',
        lambda r: perma_redirect(reverse('pages.review_guide')),
    ),
    url(
        '^pages/developer_agreement$',
        lambda r: perma_redirect(
            reverse('devhub.docs', args=['policies/agreement'])
        ),
    ),
    url(
        '^pages/validation$',
        lambda r: perma_redirect(settings.VALIDATION_FAQ_URL),
    ),
    url(
        '^pioneer$',
        TemplateView.as_view(template_name='pages/pioneer.html'),
        name='pages.pioneer',
    ),
]
