{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "613ce1cc-a024-4b9e-81f6-af6cf9927a39",
   "metadata": {},
   "source": [
    "Building an interactive web app for technical analysis\r\n",
    "using Streamlit"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07141901-8dd5-4652-888d-112231a962d9",
   "metadata": {},
   "source": [
    "Streamlit is an open source framework (and a company\n",
    "under the same name, similarly to Plotly) that allows us to build interactive web apps using only Python, all within minutes. Below you can find the highlights of Streamlit:\n",
    "\n",
    "• It is easy to learn and can generate results very quickly\n",
    "\n",
    "• It is Python only; no frontend experience is required\n",
    "\n",
    "• It allows us to focus purely on the data/ML sides of the app\n",
    "\n",
    "• We can use Streamlit’s hosting services for our apps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c77d4c6c-a702-479a-b6e0-15ef606d8f74",
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports\n",
    "import yfinance as yf\n",
    "import streamlit as st\n",
    "import datetime \n",
    "import pandas as pd\n",
    "import cufflinks as cf\n",
    "from plotly.offline import iplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a78b588e-144d-4e45-a875-8eacc44fc541",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-2.12.1.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## set offline mode for cufflinks\n",
    "cf.go_offline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7b93d72a-8379-429e-94e9-c0e6a1302d32",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:36:15.183 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "#Define a function for downloading a list of IBEX 35 constituents from Wikipedia:\n",
    "# Define the custom hash function\n",
    "def my_hash_func(obj):\n",
    "    return hash(str(obj))\n",
    "\n",
    "# Define your function with caching and the custom hash function\n",
    "@st.cache_data(hash_funcs={type(lambda: None): my_hash_func})\n",
    "def get_IBEX35_components():\n",
    "    df = pd.read_html(\"https://www.dividendmax.com/market-index-constituents/ibex-35\")\n",
    "    df = df[0]\n",
    "    print(df.columns)  # Print the column names to identify the correct ones\n",
    "    print(df.head())   # Print the first few rows to inspect the DataFrame structure\n",
    "    tickers = df[\"Ticker\"].to_list()\n",
    "    tickers_companies_dict = dict(\n",
    "        zip(df[\"Ticker\"], df[\"Company\"])\n",
    "    )\n",
    "    return tickers, tickers_companies_dict\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7c97790a-8a9e-4e37-91bb-342235ba8499",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:36:19.348 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "@st.cache_data\n",
    "def load_data(symbol, start, end):\n",
    "    return yf.download(symbol, start, end)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "aef4e68b-9cb4-4558-af53-c3f9ee966080",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:36:24.981 No runtime found, using MemoryCacheStorageManager\n"
     ]
    }
   ],
   "source": [
    "\n",
    "@st.cache_data\n",
    "def convert_df_to_csv(df):\n",
    "    return df.to_csv().encode(\"utf-8\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "930ed9a6-9309-4e4d-a9a0-8e9ec11a8247",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:36:26.666 No runtime found, using MemoryCacheStorageManager\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Company', 'Ticker', 'Unnamed: 2', 'Exchange', 'Sector', 'Market Cap'], dtype='object')\n",
      "                                             Company Ticker Unnamed: 2  \\\n",
      "0                                            Acciona    ANA         🇪🇸   \n",
      "1                                           Acerinox    ACX         🇪🇸   \n",
      "2  ACS, Actividades de Construccion Y Servicios, ...    ACS         🇪🇸   \n",
      "3                                   Aena S.M.E. S.A.   AENA         🇪🇸   \n",
      "4                              Amadeus IT Group S.A.    AMS         🇪🇸   \n",
      "\n",
      "                Exchange                        Sector Market Cap  \n",
      "0  Madrid Stock Exchange     Commercial Transportation     €6.6bn  \n",
      "1  Madrid Stock Exchange             Industrial Metals     €2.5bn  \n",
      "2  Madrid Stock Exchange      Construction & Materials    €11.2bn  \n",
      "3  Madrid Stock Exchange              Travel & Leisure    €26.8bn  \n",
      "4  Madrid Stock Exchange  Software & Computer Services    €28.8bn  \n"
     ]
    }
   ],
   "source": [
    "## inputs for downloading data\n",
    "st.sidebar.header(\"Stock Parameters\")\n",
    "\n",
    "available_tickers, tickers_companies_dict = get_IBEX35_components()\n",
    "ticker = st.sidebar.selectbox(\n",
    "    \"Ticker\", \n",
    "    available_tickers, \n",
    "    format_func=tickers_companies_dict.get\n",
    ")\n",
    "start_date = st.sidebar.date_input(\n",
    "    \"Start date\", \n",
    "    datetime.date(2019, 1, 1)\n",
    ")\n",
    "end_date = st.sidebar.date_input(\n",
    "    \"End date\", \n",
    "    datetime.date.today()\n",
    ")\n",
    "\n",
    "if start_date > end_date:\n",
    "    st.sidebar.error(\"The end date must fall after the start date\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "53dc7056-f0dd-4ecd-9fa4-9eae677d20d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "## inputs for technical analysis\n",
    "st.sidebar.header(\"Technical Analysis Parameters\")\n",
    "\n",
    "volume_flag = st.sidebar.checkbox(label=\"Add volume\")\n",
    "\n",
    "exp_sma = st.sidebar.expander(\"SMA\")\n",
    "sma_flag = exp_sma.checkbox(label=\"Add SMA\")\n",
    "sma_periods= exp_sma.number_input(\n",
    "    label=\"SMA Periods\", \n",
    "    min_value=1, \n",
    "    max_value=50, \n",
    "    value=20, \n",
    "    step=1\n",
    ")\n",
    "\n",
    "exp_bb = st.sidebar.expander(\"Bollinger Bands\")\n",
    "bb_flag = exp_bb.checkbox(label=\"Add Bollinger Bands\")\n",
    "bb_periods= exp_bb.number_input(label=\"BB Periods\", \n",
    "                                min_value=1, max_value=50, \n",
    "                                value=20, step=1)\n",
    "bb_std= exp_bb.number_input(label=\"# of standard deviations\", \n",
    "                            min_value=1, max_value=4, \n",
    "                            value=2, step=1)\n",
    "\n",
    "exp_rsi = st.sidebar.expander(\"Relative Strength Index\")\n",
    "rsi_flag = exp_rsi.checkbox(label=\"Add RSI\")\n",
    "rsi_periods= exp_rsi.number_input(\n",
    "    label=\"RSI Periods\", \n",
    "    min_value=1, \n",
    "    max_value=50, \n",
    "    value=20, \n",
    "    step=1\n",
    ")\n",
    "rsi_upper= exp_rsi.number_input(label=\"RSI Upper\", \n",
    "                                min_value=50, \n",
    "                                max_value=90, value=70, \n",
    "                                step=1)\n",
    "rsi_lower= exp_rsi.number_input(label=\"RSI Lower\", \n",
    "                                min_value=10, \n",
    "                                max_value=50, value=30, \n",
    "                                step=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "989bae63-4658-4506-b9db-8225bd282bcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:36:30.732 No runtime found, using MemoryCacheStorageManager\n",
      "[*********************100%%**********************]  1 of 1 completed\n"
     ]
    }
   ],
   "source": [
    "# main body\n",
    "\n",
    "st.title(\"A simple web app for technical analysis\")\n",
    "st.write(\"\"\"\n",
    "### User manual\n",
    "* you can select any of the companies that is a component of the S&P index\n",
    "* you can select the time period of your interest\n",
    "* you can download the selected data as a CSV file\n",
    "* you can add the following Technical Indicators to the plot: Simple Moving \n",
    "Average, Bollinger Bands, Relative Strength Index\n",
    "* you can experiment with different parameters of the indicators\n",
    "\"\"\")\n",
    "\n",
    "df = load_data(ticker, start_date, end_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8ed0c34d-e4b5-4fce-a51c-1e3a5ea956a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-02</th>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0036</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>285007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-03</th>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-04</th>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-07</th>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0036</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>1714985</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-08</th>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0.0038</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-02-24</th>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-02-25</th>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-02-28</th>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-01</th>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-02</th>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0.8250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>793 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              Open    High     Low   Close  Adj Close   Volume\n",
       "Date                                                          \n",
       "2019-01-02  0.0038  0.0038  0.0036  0.0038     0.0038   285007\n",
       "2019-01-03  0.0038  0.0038  0.0038  0.0038     0.0038        0\n",
       "2019-01-04  0.0038  0.0038  0.0038  0.0038     0.0038        0\n",
       "2019-01-07  0.0038  0.0038  0.0036  0.0038     0.0038  1714985\n",
       "2019-01-08  0.0038  0.0038  0.0038  0.0038     0.0038        0\n",
       "...            ...     ...     ...     ...        ...      ...\n",
       "2022-02-24  0.8250  0.8250  0.8250  0.8250     0.8250        0\n",
       "2022-02-25  0.8250  0.8250  0.8250  0.8250     0.8250        0\n",
       "2022-02-28  0.8250  0.8250  0.8250  0.8250     0.8250        0\n",
       "2022-03-01  0.8250  0.8250  0.8250  0.8250     0.8250        0\n",
       "2022-03-02  0.8250  0.8250  0.8250  0.8250     0.8250        0\n",
       "\n",
       "[793 rows x 6 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a99232b7-c642-4af5-8791-f98cae5d5fd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-29 12:37:28.480 No runtime found, using MemoryCacheStorageManager\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## data preview part\n",
    "data_exp = st.expander(\"Preview data\")\n",
    "available_cols = df.columns.tolist()\n",
    "columns_to_show = data_exp.multiselect(\n",
    "    \"Columns\", \n",
    "    available_cols, \n",
    "    default=available_cols\n",
    ")\n",
    "data_exp.dataframe(df[columns_to_show])\n",
    "\n",
    "csv_file = convert_df_to_csv(df[columns_to_show])\n",
    "data_exp.download_button(\n",
    "    label=\"Download selected as CSV\",\n",
    "    data=csv_file,\n",
    "    file_name=f\"{ticker}_stock_prices.csv\",\n",
    "    mime=\"text/csv\",\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "68e7885d-0c0f-4265-ad3e-6219e5278da1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## technical analysis plot\n",
    "title_str = f\"{tickers_companies_dict[ticker]}'s stock price\"\n",
    "qf = cf.QuantFig(df, title=title_str)\n",
    "if volume_flag:\n",
    "    qf.add_volume()\n",
    "if sma_flag:\n",
    "    qf.add_sma(periods=sma_periods)\n",
    "if bb_flag:\n",
    "    qf.add_bollinger_bands(periods=bb_periods,\n",
    "                           boll_std=bb_std)\n",
    "if rsi_flag:\n",
    "    qf.add_rsi(periods=rsi_periods,\n",
    "               rsi_upper=rsi_upper,\n",
    "               rsi_lower=rsi_lower,\n",
    "               showbands=True)\n",
    "\n",
    "fig = qf.iplot(asFigure=True)\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4a18305-c347-4163-a7cc-f9774781fff5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
