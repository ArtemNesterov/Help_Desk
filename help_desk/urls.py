from django.urls import path

from help_desk import views

urlpatterns = [
    path('', views.ClaimListView.as_view(), name='claims_list_page'),
    path('help_desk/<int:pk>', views.ClaimDetailView.as_view(), name='claim_detail'),
    path('help_desk/new', views.NewClaimView.as_view(), name='new_claim'),
    path('help_desk/edit/<int:pk>', views.EditClaimView.as_view(), name='edit_claim'),
    path('help_desk/delete/<int:pk>', views.ClaimDetailView.as_view(), name='claim_delete'),
    path('comment/<int:pk>/new', views.NewCommentView.as_view(), name='new_comment'),
]
