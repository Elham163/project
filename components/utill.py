#get 10 Top countries by market cap
import pandas as pd


def Share_of_consumption():
    df = pd.read_csv('C:/Users/mi5194/Desktop/Elli/Nobel_desk/project/components/Solar_Power_Energy_by_Country.csv')
    new_column_name = "Countries"
    df.columns.values[1] = new_column_name
    df['Share_consumption'] = df['Share of totalconsumption'].apply(lambda x: float(x.split("%")[0]) if isinstance(x, str) and "%" in x else None)
    df.dropna(subset=['Share_consumption'], inplace=True)
    return df








# def Share_of_consumption():
#     df = pd.read_csv('C:/Users/mi5194/Desktop/Elli/Nobel_desk/project/components/Solar_Power_Energy_by_Country.csv')
#     new_column_name = "Countries"
#     df.columns.values[1] = new_column_name
#     Share_of_consumption= df['Share of totalconsumption']
#     Share_of_consumption1=df['Share_consumption'] = df['Share of totalconsumption'].apply(lambda x: float(x.split("%")[0]) if isinstance(x, str) and "%" in x else None)
#     Share_of_consumption2=df.dropna(subset=['Share_consumption'], inplace=True)
#     return Share_of_consumption2


    # Total_sumation = df.groupby('country')[['Name']].count()
    # countries['total_marketcap'] = df.groupby('country')['marketcap'].sum()
    # countries.rename(columns = {'Name': 'num_companies'}, inplace = True)
    # globalMarketCap = countries['total_marketcap'].sum()
    # countries['%_global_cap'] = countries['total_marketcap']/globalMarketCap
    # countries.sort_values('total_marketcap', ascending = False, inplace=True)
    # countries['trillions']  = round(countries["total_marketcap"]/1000000000000,2)
    # countries.reset_index(inplace=True)
    # top10 = countries.iloc[:10]
    # return top10