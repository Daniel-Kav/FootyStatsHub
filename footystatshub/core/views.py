from django.shortcuts import render

from core.services.understat_service import get_player_stats, get_team_stats

def player_stats_view(request, player_id):
    """
    A view to display player stats by calling the Understat API.
    """
    stats = get_player_stats(player_id)
    context = {
        'player_stats': stats
    }
    return render(request, 'core/player_stats.html', context)

def team_stats_view(request, team_id):
    """
    A view to display team stats by calling the Understat API.
    """
    stats = get_team_stats(team_id)
    context = {
        'team_stats': stats
    }
    return render(request, 'core/team_stats.html', context)

