import flood_tool
postcode_file = 'flood_tool/resources/postcodes.csv'
risk_file = 'flood_tool/resources/flood_probability.csv'
values_file = 'flood_tool/resources/property_value.csv'

def question1(postcodes):
    data = flood_tool.tool.Tool(postcode_file, risk_file, values_file)
    ans1 = data.get_sorted_flood_probability(postcodes)
    return ans1 

def question2(postcodes):
    data = flood_tool.tool.Tool(postcode_file, risk_file, values_file)
    ans2 = data.get_sorted_annual_flood_risk(postcodes)
    return ans2

def question3(postcodes):
	flood_tool.flood_alert.alert_graph(postcodes)
	return flood_tool.flood_alert.get_alert_data(postcodes)

def question4(date):
	print(flood_tool.api.get_date_readings(date))
	return flood_tool.analyze_date.wheres_wettest(date)
