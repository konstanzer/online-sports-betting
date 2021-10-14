import pandas as pd

'''
Run the following link in a browser to download .xlsx file of greenhouse gas concentrations:
https://greenhousegases.science.unimelb.edu.au/img/SUPPLEMENT_DataTables_Meinshausen_6May2020.xlsx
'''

def save_tables(f):

	#read historical data and predictions from spreadsheet
	#runtime - 3 minutes
	hist = pd.read_excel(f, sheet_name=1, index_col=0, header=8)
	hist2 = pd.read_excel(f, sheet_name=2, index_col=0, header=8)
	s119 = pd.read_excel(f, sheet_name=3, index_col=0, header=8)
	s126 = pd.read_excel(f, sheet_name=4, index_col=0, header=8)
	s245 = pd.read_excel(f, sheet_name=5, index_col=0, header=8)
	s370 = pd.read_excel(f, sheet_name=6, index_col=0, header=8)
	s370l = pd.read_excel(f, sheet_name=7, index_col=0, header=8)
	s434 = pd.read_excel(f, sheet_name=8, index_col=0, header=8)
	s460 = pd.read_excel(f, sheet_name=9, index_col=0, header=8)
	s534 = pd.read_excel(f, sheet_name=10, index_col=0, header=8)
	s585 = pd.read_excel(f, sheet_name=11, index_col=0, header=8)
	
	#skip hemisphere columns for this project
	world_cols = range(0, hist.shape[1], 3)
	
	#save units in a series
	units = hist.iloc[0, world_cols]
	units.to_csv('units.csv')

	#delete headers and hemisphere columns
	hist = hist.iloc[3:, world_cols]
	hist2 = hist2.iloc[3:, world_cols]
	s119 = s119.iloc[3:, world_cols]
	s126 = s126.iloc[3:, world_cols]
	s245 = s245.iloc[3:, world_cols]
	s370 = s370.iloc[3:, world_cols]
	s370l = s370l.iloc[3:, world_cols]
	s434 = s434.iloc[3:, world_cols]
	s460 = s460.iloc[3:, world_cols]
	s534 = s534.iloc[3:, world_cols]
	s585 = s585.iloc[3:, world_cols]

	#relabel index
	hist.index.name = 'year'
	hist2.index.name = 'year'
	s119.index.name = 'year'
	s126.index.name = 'year'
	s245.index.name = 'year'
	s370.index.name = 'year'
	s370l.index.name = 'year'
	s434.index.name = 'year'
	s460.index.name = 'year'
	s534.index.name = 'year'
	s585.index.name = 'year'

	#save tables in .csv files
	hist.to_csv('hist.csv')
	hist2.to_csv('hist2.csv')
	s119.to_csv('s119.csv')
	s126.to_csv('s126.csv')
	s245.to_csv('s245.csv')
	s370.to_csv('s370.csv')
	s370l.to_csv('s370l.csv')
	s434.to_csv('s434.csv')
	s460.to_csv('s460.csv')
	s534.to_csv('s534.csv')
	s585.to_csv('s585.csv')
	

if __name__ == '__main__':

	#change to local file location
	f = '~/Documents/GitHub/school/greenhouse_gases/data/greenhouse_explore.xlsx'
	save_tables(f)
