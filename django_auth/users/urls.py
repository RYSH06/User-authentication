from .views import CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
]
