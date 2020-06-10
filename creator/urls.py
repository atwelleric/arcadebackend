from django.urls import path
from .views import CreatorListView, CreatorView, TopCreatorView

urlpatterns = [
    path('', CreatorListView.as_view()),
    path('topcreator', TopCreatorView.as_view()),
    path('<pk>', CreatorView.as_view())

]
