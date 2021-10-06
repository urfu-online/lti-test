from django.views.generic.base import TemplateView
from lti_provider.mixins import LTIAuthMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
# from django.views.decorators.clickjacking import xframe_options_exempt

from django.shortcuts import redirect, reverse, render
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
# xframe_options_exempt_m = method_decorator(xframe_options_exempt, name='get')


# @xframe_options_exempt_m
class IndexView(TemplateView):
    template_name = 'lti/index.html'

    def get(self, request, *args, **kwargs):
        for key, value in request.session.items():
            test = '{} => {}'.format(key, value)
            logger.warning(test)
        return render(request, 'lti/index.html')
    # def post(self, request):
    #     return redirect('http://10.16.208.139:8009/lti/')


# @xframe_options_exempt_m
class EmbedView(TemplateView):
    template_name = 'lti/embed.html'

    # def post(self, request):
    #     return redirect('http://10.16.208.139:8009/lti/')


class LTIAssignment1View(LTIAuthMixin, LoginRequiredMixin, TemplateView):
    template_name = 'lti/assignment.html'

    def get_context_data(self, **kwargs):
        return {
            'lis_outcome_service_url': self.lti.lis_outcome_service_url(self.request),
            'is_student': self.lti.lis_result_sourcedid(self.request),
            'course_title': self.lti.course_context(self.request),
            'number': 1
        }
