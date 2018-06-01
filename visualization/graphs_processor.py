import dash_core_components as dcc
import dash_html_components as html
from data import data_cleaner as dc
from . import color_picker

def processComparisonGraph(main_database):
    return dcc.Graph(
        id='attribute_comparison_likes_retweets',
        figure={
            'data': [
                {'x': dc.getListOfLikes(main_database), 'y': dc.getListOfRetweets(main_database), 'type': 'bar',
                 'name': 'Likes vs. Retweets'}
            ],
            'layout': {
                'title': 'Likes vs. Retweets',
                'color': 'blue',
                'xaxis': {'title': 'Likes', 'color': ['twitter_blue']},
                'yaxis': {'title': 'Retweets', 'color': color_picker.getColor('twitter_blue')}
            }
        }
    )

def processSentimentGraph(score):
    if score > 0:
        return html.P(
            children='Your tweets are mostly positive.',
            style={'font-family': 'Roboto', 'fontSize': 40, 'textAlign': 'left', 'color': color_picker.getColor('green')})
    elif score < 0:
        return html.P(
            children='Your tweets tend to be negative. You should boost up the sentiment in your engagements.',
            style={'font-family': 'Roboto', 'fontSize':40,  'textAlign': 'left', 'color': color_picker.getColor('red')})
    else:
        return html.P(children = 'Your tweets are neutral. Maybe you should try to engage more emotion in your audience.',
            style = {'font-family' : 'Roboto', 'fontSize': 40,  'textAlign' : 'left', 'color': color_picker.getColor('twitter_blue')})
