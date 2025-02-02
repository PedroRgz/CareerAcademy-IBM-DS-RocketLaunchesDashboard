# Import required libraries
import pandas as pd
import dash
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

#Read the dataset stored in the csv file called 'spacex_launch_dash.csv'
spacex_df = pd.read_csv("spacex_launch_dash.csv")
#Set a variable for the max payload
max_payload = spacex_df['Payload Mass (kg)'].max()
#Set a variable for the min payload
min_payload = spacex_df['Payload Mass (kg)'].min()

#Create a new column class_verb -> Success or Failure based on the value of the 'class' column
spacex_df['class_verb'] = spacex_df['class'].apply(lambda x: 'Success' if x == 1 else 'Failure')

#Create the dash application
app = dash.Dash(__name__)

#Create the layout of the application
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={'text-align': 'center', 'color': '#503D36',
                                                    'font-size': 40}),
    #Add a dropdown list to allow the user to select the site for the launch
    dcc.Dropdown(id='site-dropdown',
                options=[
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                ],
                value='ALL',
                placeholder="Select a Launch Site here",
                searchable=True
                ),
    #Add a pie chart to show the total successful launches count for all sites given a specific launch site
    html.Div([
        html.Br(),
        html.Div(dcc.Graph(id='success-pie-chart'))
    ]),
    #Add a scatter plot to show the relationship between payload and launch success
    html.Div([
        html.Br(),
        html.Div([
            html.Div('Payload range (Kg):'),
            dcc.RangeSlider(id='payload-slider',
                            min=0,
                            max=10000,
                            step=1000,
                            marks={0: '0',
                                2500: '2500',
                                5000: '5000',
                                7500: '7500',
                                10000: '10000'},
                            value=[min_payload, max_payload]
                            )
        ], style={'width': '80%', 'margin': 'auto'})
    ]),
    html.Div([
        html.Br(),
        html.Div(dcc.Graph(id='success-payload-scatter-chart'))
    ])
])

#Add a callback function for `site-dropdown` as input, `success-pie-chart` as output to create the pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', names='Launch Site', title='Total Success Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class_verb', title=f'Total Success Launches for site {entered_site}')
    return fig

#Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output to create the scatter plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
    Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    if entered_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class_verb', color='Booster Version Category',
                        title='Payload Success Rate for All Sites')
    else:
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high) & (spacex_df['Launch Site'] == entered_site)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class_verb', color='Booster Version Category',
                        title=f'Payload Success Rate for site {entered_site}')
    return fig

#Run the application
if __name__ == '__main__':
    app.run_server()