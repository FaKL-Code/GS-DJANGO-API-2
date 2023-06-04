from django.urls import include, path
from rest_framework import routers

from backend.doacoes import views as v
from backend.doacoes.api.viewsets import DoacoesViewSet

app_name = 'doacoes'

router = routers.DefaultRouter()

router.register(r'doacoes', DoacoesViewSet)

doacoes_urlpatterns = [
    path('', v.DoacoesListView.as_view(), name='doacoes_list'),
    path('<int:pk>/', v.DoacoesDetailView.as_view(), name='doacoes_detail'),
    path('create/', v.DoacoesCreateView.as_view(), name='doacoes_create'),
    path('<int:pk>/update/', v.DoacoesUpdateView.as_view(), name='doacoes_update'),
    path('<int:pk>/delete/', v.DoacoesDeleteView.as_view(), name='doacoes_delete'),
]

urlpatterns = [
    path('doacoes/', include(doacoes_urlpatterns)),
    path('api/v1/', include(router.urls)),
]
