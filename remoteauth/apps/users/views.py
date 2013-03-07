from django.views.generic import TemplateView
from .models import User


class UserView(TemplateView):
    model = User
    template_name = "users/view.html"

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)

        import time
        time.sleep(5)

        username = self.kwargs['user']

        try:
            context['rank'] = User.objects.get(
                username=username
            ).rank
        except:
            context['rank'] = None

        return context
