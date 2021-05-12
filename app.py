import dash
from datetime import date
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
si=[1,746,1418,2161,2880,3624,4317,5050,5792,6397,7099,7818,8561]
transl={"Power_kW_H":"Power_kW", "Solarrad_H":"solarRad_W/m2", "Power-1_H":"Power-1"}
line1="The features shown has been used to create a model for the electricity consumption of the IST South Tower using the Bootstrapping algoritm."
line2="Then the model accuracy has been evaluated with the quantities shown in the table below"
labels=["Date_start","Date","Hour","Power_kW","WeekDay","temp_C","solarRad_W/m2","Holiday","Season","rain_day","Power-1","Season_name","Results_1", "Results_2"]
histo=["Power_kW_H", "Solarrad_H", "Power-1_H"]
lab=["Date_start","Season_name","Power_kW","temp_C","solarRad_W/m2","Holiday"]
labb=["MAE_BT","MSE_BT","RMSE_BT","cvRMSE_BT"]
dferr18 = pd.read_csv("err_2018.csv")
dferr17 = pd.read_csv("err_2017.csv")
dferr18["2017"]=dferr17.iloc[:,1]
dferr18.rename(columns={ dferr18.columns[1]: "2018" }, inplace = True)
dferr18.rename(columns={ dferr18.columns[1]: "2018" }, inplace = True)
dferr18.insert(1, "Value", labb)
# print(dferr18)
df18=pd.read_csv("final_2018.csv")
df17 = pd.read_csv("final_2017.csv")
dfprova18 = df18[::6]
dfprova18 = dfprova18[[labels[1], labels[2], labels[3], labels[4], labels[5], labels[6], labels[7], labels[8], labels[10]]]
dfprova17 = df17[::6]
dfprova17 = dfprova17[[labels[1], labels[2], labels[3], labels[4], labels[5], labels[6], labels[7], labels[8], labels[10]]]

app = dash.Dash(__name__)
server=app.server
tab1_content=[html.Div([
    dbc.Row(dbc.Col(html.H2("   Features"),
                    # width={"offset":1}
                    )),
    dbc.Row(dbc.Col(html.H5("Select a feature and a year to plot them on the graph, then select the starting and finishing date to zoom in the graph"),
                    # width={"offset":1}
                    )),
    dbc.Row([dbc.Col(dcc.Dropdown(id='f_dropdown', placeholder='Select a Feature...',
                                     options=[{'label': 'Power Consumption [kW]', 'value': labels[3]},
                                              {'label': 'Power Consumption [kW] - Histogram', 'value': histo[0]},
                                              {'label': 'External Temperature [°C]', 'value': labels[5]},
                                              {'label': 'Solar Radiation [W/m2]', 'value': labels[6]},
                                              {'label': 'Solar Radiation [W/m2] - Histogram', 'value': histo[1]},
                                              {'label': 'Holiday', 'value': labels[7]},
                                              {'label': 'Season', 'value': labels[11]},
                                              {'label': 'Power - 1', 'value': labels[10]},
                                              {'label': 'Power - 1 - Histogram', 'value': histo[2]}
                                              ],
                                  value=labels[3],
                                  searchable=True),
                        width={'size': 3, "offset": 2, 'order': 1}
                        ),]),
# dbc.Row([dbc.Label("Custom month"),
#         dbc.Checklist(
#             options=[
#                 {"label": "Option 1", "value": 1},
#             ],
#             value=[],
#             id="switches-input",
#             switch=True,
#         )]),
dbc.Row([
dbc.Col(dcc.Dropdown(id='sm_dropdown', placeholder='Starting month',
                                     options=[{'label': month[0], 'value': 0},
                                              {'label': month[1], 'value': 1},
                                              {'label': month[2], 'value': 2},
                                              {'label': month[3], 'value': 3},
                                              {'label': month[4], 'value': 4},
                                              {'label': month[5], 'value': 5},
                                              {'label': month[6], 'value': 6},
                                              {'label': month[7], 'value': 7},
                                              {'label': month[8], 'value': 8},
                                              {'label': month[9], 'value': 9},
                                              {'label': month[10], 'value': 10},
                                              {'label': month[11], 'value': 11},
                                              ],
                                  searchable=True),
                        width={'size': 3, "offset": 1, 'order': 2}
                        ),
# dbc.Col(dcc.Dropdown(id='sd_dropdown', placeholder='Starting month',
#                                      options=[{'label': day[0], 'value': day[0]},
#                                               {'label': day[1], 'value': day[1]},
#                                               {'label': day[2], 'value': day[2]},
#                                               {'label': day[3], 'value': day[3]},
#                                               {'label': day[4], 'value': day[4]},
#                                               {'label': day[5], 'value': day[5]},
#                                               {'label': day[6], 'value': day[6]},
#                                               {'label': day[7], 'value': day[7]},
#                                               {'label': day[8], 'value': day[8]},
#                                               {'label': day[9], 'value': day[9]},
#                                               {'label': day[10], 'value': day[10]},
#                                               {'label': day[11], 'value': day[11]},
#                                               {'label': day[12], 'value': day[12]},
#                                               {'label': day[13], 'value': day[13]},
#                                               {'label': day[14], 'value': day[14]},
#                                               {'label': day[15], 'value': day[15]},
#                                               {'label': day[16], 'value': day[16]},
#                                               {'label': day[17], 'value': day[17]},
#                                               {'label': day[18], 'value': day[18]},
#                                               {'label': day[19], 'value': day[19]},
#                                               {'label': day[20], 'value': day[20]},
#                                               {'label': day[21], 'value': day[21]},
#                                               {'label': day[22], 'value': day[22]},
#                                               {'label': day[23], 'value': day[23]},
#                                               {'label': day[24], 'value': day[24]},
#                                               {'label': day[25], 'value': day[25]},
#                                               {'label': day[26], 'value': day[26]},
#                                               {'label': day[27], 'value': day[27]},
#                                               {'label': day[28], 'value': day[28]},
#                                               {'label': day[29], 'value': day[29]},
#                                               {'label': day[30], 'value': day[30]},
#
#                                               ],
#                                   searchable=True),
#                         width={'size': 3, "offset": 2, 'order': 2}
#                         ),
dbc.Col(dcc.Dropdown(id='fm_dropdown', placeholder='Finishing month',
                                     options=[{'label': month[0], 'value': 0},
                                              {'label': month[1], 'value': 1},
                                              {'label': month[2], 'value': 2},
                                              {'label': month[3], 'value': 3},
                                              {'label': month[4], 'value': 4},
                                              {'label': month[5], 'value': 5},
                                              {'label': month[6], 'value': 6},
                                              {'label': month[7], 'value': 7},
                                              {'label': month[8], 'value': 8},
                                              {'label': month[9], 'value': 9},
                                              {'label': month[10], 'value': 10},
                                              {'label': month[11], 'value': 11},
                                              ],
                                  searchable=True),
                        width={'size': 3, "offset": 1, 'order': 3}
                        ),
            ]),
    dbc.Row(dbc.Col(
        dbc.RadioItems(
        options=[
            {'label': '2017', 'value': '2017'},
            {'label': '2018', 'value': '2018'}
        ],
    value="2017",
    inline=True,
    id="check_year"
)
    )),
    dbc.Row([dbc.Col(dcc.Graph(id='the_graph'))]),
    dbc.Row([
             dbc.Col( dbc.Card([
                # dbc.CardHeader("Select a Feature from the dropdown menu or select the results to plot them."),
                dbc.CardBody(line1),
                # dbc.CardFooter( "This page was created by Valeria Bona, ist1100833, Instituto Superior Técnico, Universidade de Lisboa"),


            ],
             # color="danger",
                 )
        )

    ]),

    ])

]
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='f_dropdown', component_property='value'),
     Input(component_id="check_year", component_property="value"),
     Input(component_id="sm_dropdown", component_property="value"),
     Input(component_id="fm_dropdown", component_property="value"),
    ]
)

def update_graph(f_dropdown, check_year, sm_dropdown,fm_dropdown):
    exc=["Power_kW","solarRad_W/m2", "Power-1"]
    # df18=pd.read_csv("final_2018.csv")
    # df17 = pd.read_csv("final_2017.csv")
    s=1
    fin=8661
    if check_year=="2018":
        df18["Date_start"] = pd.to_datetime(df18["Date_start"], format="%d-%m-%Y %H:%M:%S")
        if sm_dropdown in range(12) and fm_dropdown in range(12):
            s=si[sm_dropdown]
            fin=si[fm_dropdown+1]
        else:
            s=1
            fin=8561
        if f_dropdown in histo:
            chart=px.histogram(data_frame=df18.loc[s:fin], y=transl[f_dropdown], x=labels[0],color_discrete_sequence=['purple'])
            return(chart)
        elif f_dropdown in exc:
            chart = px.line(data_frame=df18.loc[s:fin], y=f_dropdown, x=labels[0])
            return (chart)
        else:
            chart=px.scatter(data_frame=df18.loc[s:fin], y=f_dropdown, x=labels[0])
            return (chart)
    else:
        df17["Date_start"] = pd.to_datetime(df17["Date_start"], format="%d-%m-%Y %H:%M:%S")
        if sm_dropdown in range(12) and fm_dropdown in range(12):
            s=si[sm_dropdown]
            fin=si[fm_dropdown+1]
        else:
            s=1
            fin=8561
        if f_dropdown in histo:
            chart = px.histogram(data_frame=df17.loc[s:fin], y=transl[f_dropdown], x=labels[0],color_discrete_sequence=['purple'])
            return(chart)
        elif f_dropdown in exc:
            chart = px.line(data_frame=df17.loc[s:fin], y=f_dropdown, x=labels[0])
            return (chart)
        else:
            chart = px.scatter(data_frame=df17.loc[s:fin], y=f_dropdown, x=labels[0])
            return (chart)



tab2_content= html.Div([
    dbc.Row(dbc.Col(html.H2("Results"))),
    dbc.Row(dbc.Col(html.H5("Down below the results of the year chosen are shown"))),
    dbc.Row(dbc.Col(
        dbc.RadioItems(
        options=[
            {'label': '2017', 'value': '2017'},
            {'label': '2018', 'value': '2018'}
        ],
    value="2017",
    inline=True,
    id="c_year"
)
    )),
    dbc.Row([html.H3("1) Test values and model values")]),
    dbc.Row([html.H5("Down below the test and model values are shown together to evaluate the overlapping")]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='the_graph1'))]),
    dbc.Row([html.H3("2) Test values vs model values")]),
    dbc.Row([html.H5("Down below the test values are the x while the y values are the x: the more the plot follows a straight line the better is the model")]),
    dbc.Row([dbc.Col(dcc.Graph(id="the_graph2"))]),
    dbc.Row([html.H3("3) Error table")]),
    dbc.Row(dbc.Col(dbc.Table.from_dataframe(dferr18.iloc[:, 1:], striped=True, bordered=True, responsive=True))
            ),
])
@app.callback(
    Output(component_id="the_graph1", component_property="figure"),
    # Output(component_id="the_table", component_property="figure"),
     Input(component_id="c_year", component_property="value")
     # Input(component_id="m_dropdown", component_property="value"),
)

def update_graph1(c_year):
    dfd17=pd.read_csv("dfdata_2017.csv")
    dfd18=pd.read_csv("dfdata_2018.csv")
    if c_year=="2018":
        l = ["y_test", "y_pred"]
        chart=px.line(data_frame=dfd18[1:200], y=l)
        return(chart)
    else:
        l=["y_test","y_pred"]
        chart = px.line(data_frame=dfd17[1:200], y=l)
        return (chart)

@app.callback(
    Output(component_id="the_graph2", component_property="figure"),
    # Output(component_id="the_table", component_property="figure"),
     Input(component_id="c_year", component_property="value")
     # Input(component_id="m_dropdown", component_property="value"),
)

def update_graph2(c_year):
    dfd17 = pd.read_csv("dfdata_2017.csv")
    dfd18 = pd.read_csv("dfdata_2018.csv")

    if c_year == "2018":
        chart = px.scatter(data_frame=dfd18, x="y_test", y="y_pred")
        return (chart)
    else:
        chart = px.scatter(data_frame=dfd17, x="y_test", y="y_pred")
        return (chart)
tab3_content= html.Div([
        dbc.Row(html.H2("Raw data analysis")),
        dbc.Row(html.H5("The raw data are shown down below")),
    #     dbc.Row(dbc.Col(
    #         dbc.RadioItems(
    #         options=[
    #             {'label': '2017', 'value': '2017'},
    #             {'label': '2018', 'value': '2018'}
    #         ],
    #         value="2017",
    #         inline=True,
    #         id="year_table"
    #         )
    # )),
        # dbc.Row(id="table")
        dbc.Row(html.H6("2017")),
        dbc.Row(dbc.Col(dbc.Table.from_dataframe(dfprova17,
                                             striped=True, bordered=True, responsive=True)),
            ),
        dbc.Row(html.H6("2018")),
        dbc.Row(dbc.Col(dbc.Table.from_dataframe(dfprova18,
                                                 striped=True, bordered=True, responsive=True)),
            ),

    ])
# @app.callback(
#     Output(component_id="table", component_property="data_table"),
#     Input(component_id="year_table", component_property="value")
#
# )
# def return_table(year_table):
#     if year_table=="2017":
#         return dbc.Table.from_dataframe(df17[::6], striped=True, bordered=True, responsive=True)
#     if year_table=="2018":
#         return dbc.Table.from_dataframe(df18[::6], striped=True, bordered=True, responsive=True)

app.layout=\
    tabs = html.Div([
    dbc.Row(dbc.Col(html.H1("IST Electricity consumption model"),
                    width={"offset": 3})),
    dbc.Row(dbc.Col(html.H6("Select a tab to view the steps of the analysis"))),
            dbc.Tabs(
                [
                    dbc.Tab(label="Raw data analysis", tab_id="tab-3"),
                    dbc.Tab(label="Features", tab_id="tab-1"),
                    dbc.Tab(label="Results", tab_id="tab-2"),
                ],
                id="tabs",
                active_tab="tab-3",
            ),
            html.Div(id="content"),
    dbc.Row(dbc.Card([dbc.CardBody(
    "This page was created by Valeria Bona, ist1100833, Instituto Superior Técnico, Universidade de Lisboa")]))
    ],
    style={'padding': 10},
)



@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    elif at== "tab-3":
        return tab3_content
    return html.P("This shouldn't ever be displayed...")



# def update_txt(f_dropdown, check_year):
#     hdr = "Your selection is "
#     if f_dropdown not in labels[12:13]:
#         sent=hdr + "something"
#         return('{}'.format(sent))

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    app.run_server()
