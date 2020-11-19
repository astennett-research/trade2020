import dash

import dash_bootstrap_components as dbc

import dash_core_components as dcc

import dash_html_components as html

from dash.dependencies import Input, Output

import Trade_2020

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# allows callback that induce further callbacks
app.config.suppress_callback_exceptions = True

layout_dict = {}
overall_fig_dict = {}

def layout_generator( strand_dict, strand_name):
    layout = html.Div([
        # creates dropdown menu based on keys or names of figures from the given strand_dict
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': key, 'value': key} for key in strand_dict.keys()],
            # this fixes the first value
            value=list(strand_dict.keys())[0],
        ),
        html.Div(id='graphs')

    ])
    # places layout in layout_dict
    layout_dict[strand_name] = layout
    # maps strand_name to strand dictionary
    overall_fig_dict[strand_name] = strand_dict

# organise data from dashboard_data
layout_generator(Trade_2020.Export_dict, "/exports_2013_to_2020")
layout_generator(Trade_2020.Import_dict, "/imports_2013_to_2020")


# creates navbar using https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(

    children=[

        dbc.NavLink("Home", href="/home", id="page-1-link"),

        dbc.NavLink("Exports", href="/exports_2013_to_2020", id="page-2-link"),

        dbc.NavLink("Imports", href="/imports_2013_to_2020", id="page-3-link"),


    ],

    # controls title
    brand="Northern Ireland Trade 2020",


    color="primary",

    dark=True,

)

# this is the layout for the home screen

home_body=dbc.Container(

    # made up of various components from dash html components https://dash.plot.ly/dash-html-components
    [
        dbc.Row(
            [
                # H2 and H1 components can be used for titles
                html.H2('Northern Ireland Trade')
            ]),
        dbc.Row([
            # P is used for writing paragraphs
            # if need to include links or linebreaks give list of components
            # if just continuous text can just use a string, no list
            # dcc.Link is used to make links dcc.Link('How link appears', href='url')
            # html.Br() produces linebreak
                        html.P(['This dashboard presents HMRC data on NI quarterly trade in good from 2013 to 2020.'
                                'Its purpose is to illustrate the impact of COVID-19 on NI trade during the first'
                                'two quarters of 2020, relative to previous quarters'
                                'The dashboard examines both export and import date:', html.Br(), html.Br(),
                                      dcc.Link('Exports', href='exports_2013_to_2020'), html.Br(),
                                      dcc.Link('Imports', href='imports_2013_to_2020'), html.Br(),html.Br(),
                                'Within each area users may use the dropdown menus to navigate the data.']),

            ])
    ],

    className='mt-4,'
)


app.layout = html.Div(

    # dbc has a Row/Col structure

    [
        #this allows multipages in app to be naviagted
        dcc.Location(id="url"),

        # add the navigation bar to the top of page
        navbar,

        # Container for page layout
        dbc.Row([dbc.Container(id="page-content", className="pt-4")]),
        dbc.Row(
            [
                # footer with assembly logo. Local files and images can be used
                # need to use app.get_asset_url to get image file. image should be stored in folder named assets
                dbc.Col(dbc.ModalFooter(children = html.Img(src=app.get_asset_url("niassembly-logo.png")))),
            ],
            align='end')

    ]

)


# this callback uses the current pathname to set the active state of the

# corresponding nav link to true, allowing users to tell see page they are on


# this changes the appearance of links in the the NavBar so that when clicker the label becomes 'active'
@app.callback(

    [Output(f"page-{i}-link", "active") for i in range(1,3)],

    [Input("url", "pathname")],

)
def toggle_active_links(pathname):
    if pathname == "/home":
        # Treat page 1 as the homepage / index

        return True, False, False,



    return [False]+[pathname == f"/strand-{i}" for i in range(1,3)]


# when the url changes either by the user clicking on links or manually typing out the address
# the relevant layout is loaded into the page content. Error page used with incorrect url is given
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:

        return home_body

    elif pathname in layout_dict.keys():

        return layout_dict[pathname]


    # If the user tries to reach a different page, return a 404 message

    return dbc.Jumbotron(

        [

            html.H1("404: Not found", className="text-danger"),

            html.Hr(),

            html.P(f"The pathname {pathname} was not recognised..."),

        ]

    )

# This loads the correct graph based the value from the drop down and uses the url
# to select the right path/strand from the overall fig dict
@app.callback(
    Output('graphs', 'children'),
    [Input('dropdown', 'value'), Input("url", "pathname") ])
def update_output(selected_value, path):
    graph = html.Div('Home text')
    if not selected_value == 'Home':
        graph = dcc.Graph(figure=overall_fig_dict[path][selected_value])
    return graph


if __name__ == "__main__":
    app.run_server(port=8887)



