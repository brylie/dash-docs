# -*- coding: utf-8 -*-
from textwrap import dedent as s
import dash_core_components as dcc
import dash_html_components as html
from tutorial.chapter_index import chapters

from tutorial.tools import merge

styles = {
    'underline': {
        'border-bottom': 'thin lightgrey solid',
        'margin-top': '50px'
    }
}

def Chapter(name, href=None, caption=None):
    linkComponent = html.A if href.startswith('http') else dcc.Link
    return html.Div([
        html.Li(
            linkComponent(
                name,
                href=href,
                style={'paddingLeft': 0},
                id=href
            )
        ),
        html.Small(dcc.Markdown(s(caption or '')), style={
            'display': 'block',
            'marginTop': '-10px' if caption else ''
        }) if caption else None
    ])


def Section(title, links, description=None, headerStyle={}):
    return html.Div([
        html.H2(title, style=merge(styles['underline'], headerStyle)),
        (
            html.Div(description)
            if description is not None else None
        ),
        html.Ul(links)
    ])


layout = html.Div(className='toc', children=[
    html.H1('Dash User Guide'),

    Section("What's Dash?", [
        Chapter(chapters['introduction']['name'],
                chapters['introduction']['url'],
                "A quick paragraph about Dash and a link to the talk at Plotcon that started it all."),
        Chapter('Announcement Essay',
                'https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503',
                ("Our extended essay on Dash. An extended discussion of Dash's architecture "
                 "and our motivation behind the project.")),
        Chapter(chapters['gallery']['name'],
                chapters['gallery']['url'],
                "A glimpse into what's possible with Dash."),
        Chapter('Dash Club',
                'http://eepurl.com/dE7CHT',
                'A fortnightly email newsletter by chriddyp, the creator of Dash.'),
    ]),

    Section('Dash Tutorial', [
        Chapter(chapters['installation']['name'],
                chapters['installation']['url']),
        Chapter(chapters['getting-started']['name'],
                chapters['getting-started']['url'],
                chapters['getting-started']['description']),
        Chapter(chapters['getting-started-part-2']['name'],
                chapters['getting-started-part-2']['url'],
                chapters['getting-started-part-2']['description']),
        Chapter(chapters['state']['name'],
                chapters['state']['url'],
                chapters['state']['description']),
        Chapter(chapters['graphing']['name'],
                chapters['graphing']['url'],
                chapters['graphing']['description']),
        Chapter(chapters['shared-state']['name'],
                chapters['shared-state']['url'],
                chapters['shared-state']['description']),
        Chapter(chapters['faqs']['name'],
                chapters['faqs']['url'],
                chapters['faqs']['description'])
    ]),

    Section('Component Libraries', [
        Chapter(chapters['dash-core-components']['name'],
                chapters['dash-core-components']['url'],
                chapters['dash-core-components']['description']),
        Chapter(chapters['dash-html-components']['name'],
                chapters['dash-html-components']['url'],
                chapters['dash-html-components']['description']),
        Chapter(chapters['dashdaq']['name'],
                chapters['dashdaq']['url'],
                chapters['dashdaq']['description'])
    ]),

    Section('Creating Your Own Components', [
        Chapter(chapters['react-for-python-developers']['name'],
                chapters['react-for-python-developers']['url'],
                chapters['react-for-python-developers']['description']),
        Chapter(chapters['plugins']['name'],
                chapters['plugins']['url'],
                chapters['plugins']['description']),
        Chapter(chapters['d3-plugins']['name'],
                chapters['d3-plugins']['url'],
                chapters['d3-plugins']['description']),

    ]),

    Section('Beyond the Basics', [
        Chapter(chapters['performance']['name'],
                chapters['performance']['url'],
                chapters['performance']['description']),
        Chapter(chapters['live-updates']['name'],
                chapters['live-updates']['url'],
                chapters['live-updates']['description']),
        Chapter(chapters['external']['name'],
                chapters['external']['url'],
                chapters['external']['description']),
        Chapter(chapters['urls']['name'],
                chapters['urls']['url'],
                chapters['urls']['description'])
    ]),

    Section('Production', [
        Chapter(chapters['auth']['name'],
                chapters['auth']['url']),
        Chapter(chapters['deployment']['name'],
                chapters['deployment']['url']),
    ]),

    Section('Getting Help', [
        Chapter('The Dash Community Forum', 'https://community.plot.ly/c/dash'),
        Chapter(chapters['support']['name'],
                chapters['support']['url'])
    ]),

    Section('Dash Deployment Server', [
        Chapter('About Dash Deployment Server',
                'https://plot.ly/dash/pricing/'),
        Chapter(chapters['dash-deployment-server']['name'],
                chapters['dash-deployment-server']['url'])],
        description="""Dash Deployment Server is Plotly's commercial offering
                       for hosting and sharing Dash apps on-premises or in the
                       cloud.""",
        headerStyle={'color': '#0D76BF'}
    )
])
