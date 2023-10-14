import numpy as np
import utils
def daily_average(data:np.ndarray, monitoring_station:str, pollutant:str):
    day_average_dict = {}
    hour_value = 1
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    for i in range (1, 366):
        day_list = []
        for j in range (0, 24):
            if data[hour_value, pollutant_position] != "No data":
                day_list.append(float(data[hour_value, pollutant_position]))
            hour_value += 1
        day_average_dict[data[i*24, 0]] = utils.meannvalues(day_list)
    return day_average_dict

def daily_median(data:np.ndarray, monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    day_median_dict = {}
    hour_value = 1
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    for i in range (1, 366):
        day_array = np.array([])
        for j in range (0, 24):
            if data[hour_value, pollutant_position] != "No data":
                day_array = np.append(day_array, float(data[hour_value, pollutant_position])) 
            hour_value += 1
        day_array.sort()
        if len(day_array) != 0: 
            if len(day_array) %2 == 0:
                day_median_dict[data[i*24, 0]] = (day_array[int(len(day_array) / 2)] + day_array[int(len(day_array) / 2 - 1)]) / 2
            elif len(day_array) %2 == 1:
                if len(day_array) > 1:
                    day_median_dict[data[i*24, 0]] = day_array[int(len(day_array) // 2 + 1)]
                else:
                    day_median_dict[data[i*24, 0]] = day_array[0]
    return day_median_dict

def hourly_average(data:np.ndarray, monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    
    hour_average_dict = {}
    day_value = 1
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    for j in range (1, 25):
        hour_list = []
        for k in range (0, 365):
            if data[day_value, pollutant_position] != "No data":
                hour_list.append(float(data[day_value, pollutant_position]))
            day_value += 24
        hour_average_dict[data[j, 1]] = utils.meannvalues(hour_list)
        day_value -= 8759
    hour_average_dict[data[24, 1]] = utils.meannvalues(hour_list)
    return hour_average_dict

def monthly_average(data:np.ndarray, monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    month_list = []
    month_average_dict = {}
    hour_value = 1
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    if data[hour_value, pollutant_position] != "No data":
        month_list.append((float(data[hour_value, pollutant_position])))
        hour_value += 1
    for i in range (2, 8761):
        if data[i, 0][:7] != data[i-1, 0][:7]:
            month_average_dict[data[i-1, 0][:7]] = utils.meannvalues(month_list)
            month_list.clear()
        if data[hour_value, pollutant_position] != "No data":
            month_list.append((float(data[hour_value, pollutant_position])))
        hour_value += 1
    month_average_dict[data[i-1, 0][:7]] = utils.meannvalues(month_list)  
    return month_average_dict

def peak_hour_date(data:np.ndarray, date:str, monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    
    hour_dict = {}
    hour_value = 1
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    while data[hour_value, 0] != date:
        hour_value += 24    
    day_list = []
    for j in range (hour_value, hour_value + 24):
        if data[j, pollutant_position] != "No data":
            day_list.append(float(data[j, pollutant_position]))
    return (data[hour_value + day_list.index(utils.maxvalues(day_list)), 1] +":\t"+ str(utils.maxvalues(day_list)))

def count_missing_data(data:np.ndarray, monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    
    missing_data_count = 0
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    for j in range (8760):
        if data[j, pollutant_position] == "No data":
            missing_data_count += 1
    return missing_data_count

def fill_missing_data(data:np.ndarray, new_value:str,  monitoring_station:str, pollutant:str):
    """Your documentation goes here"""
    
    for i in range (1, data.shape[1]):
        if data[0, i] == pollutant:
            pollutant_position = i
    for j in range (8760):
        if data[j, pollutant_position] == "No data":
            data[j, pollutant_position] = new_value
    return data
