from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('level', views.answer, name="situation"),
    path('leaderboard', views.leaderboard, name="leaderboard"),
    path('rules', views.rules, name="rules"),
    path('logout', views.logout_view, name="logout"),
    path('rule', views.rule, name="rules_pre"),
    path('privacypolicy', views.privacy_policy_fb, name="privacypolicy"),
    path('adj', views.graph_and_player_path, name="adj"),
    path('graph', views.graph, name="graph"),
    path('graphy', views.graphy, name="graphy"),
]
