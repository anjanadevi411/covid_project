class DataTable():
    def __init__(self,data):
        self.data=None

    def read_csv(self,path):
        list_data=[]
        row_count=0      #variable for getting how many rows in the given dataset(csv file)
        with open(path) as fileobject:
            row_data = fileobject.readline().strip().split(',') # reading the first row data from csv file as list
            no_of_columns = len(row_data)-1 #number of columns in the dataset excluding the index
            print('number of columns in the given csv file excluding index '+ str(no_of_columns))
            for next_line_data in fileobject:
                lines = next_line_data.strip().split(',') # reading the rest of the data from from csv file as list
                dict1 = dict(zip(row_data, lines))        # converting the two lists into dictionary
                list_data.append(dict1)                    #appending the dictionary to list
                row_count += 1                              #for getting the row data count from dataset(csv file)
            print('number of rows in the the given csv file '+ str(row_count))
            self.data=list_data                            #keeping the list data into global variable
            print(self.data)


    def locate_column(self,column_name): #getting the column name as 'index','date','country',.......
        list_column_data = []
        #value = '0'
        for info in self.data:
            data = info[column_name]        #getting and storing the column name data
            list_column_data.append(data)   # appending one by one column data into list
            #if info['confirmed'] >= '1' and value == '0':
             #   print('First country which has a confirmed case ' + info['country'])
              #  value = '1'
        return list_column_data
        #print(list_column_data)

    def locate_index(self,index_no):        # getting the row number from user
        value = 0
        for index_name_no in self.data:
            if(index_name_no['index'] == index_no): # checking for the row number from user
                return index_name_no
                #print(index_name_no)
                break


    def filter_values(self,column_name='country',value ='Denmark'):
        confirmed_value = 0
        sum_recovered = 0.0
        sum_confirmed_cases = 0.0
        sum_of_confirmed = 0
        data_value = []

        for info_column in self.data:
            if info_column[column_name] == value and info_column['recovered'] != 'N/A' and info_column[
                'confirmed'] != 'Not defined':
                sum_confirmed_cases += float(info_column['confirmed'])
                if sum_confirmed_cases >= 1000 and sum_of_confirmed == 0:
                    print('Number of confirmed cases reached 1000 on date ' + info_column['date'])
                    sum_of_confirmed = 1

        for info_column in self.data:
            if info_column[column_name] == value:
                data_value.append(info_column)
        return data_value


        '''for info_column in self.data:
            if info_column[column_name] == value and info_column['recovered'] != 'N/A' and info_column['confirmed'] != 'Not defined':
                sum_recovered = float(info_column['recovered'])
                sum_recovered += float(info_column['recovered']) # getting the total recovered count from perticular country
                sum_confirmed_cases += float(info_column['confirmed'])
                if sum_confirmed_cases >= 1000 and sum_of_confirmed == 0:
                    print('Number of confirmed cases reached 1000 on date ' + info_column['date'])
                    sum_of_confirmed = 1'''
            #else:
             #   print('N/A')

            #if info_column['confirmed'] == '1.0' and confirmed_value == 0 and info_column[column_name] == value:
             #   print('First country which has a confirmed case ' + info_column['country'])
              #  confirmed_value = 1'''
        #print(f'number of recovered in the country {value} is {sum_recovered}')


    def value_counts(self,column_name):
        list_column_data = []
        list_count = []
        new_dict = {}
        for info_col in self.data:
            data = info_col[column_name]        # we are collecting/storing data from column name Ex: column name- country data will be country name
            #print(data)
            list_column_data.append(data)
            # print(data)
            count_value = list_column_data.count(data)
            list_count.append(count_value)
            #print(count_value)
            new_dict = dict(zip(list_column_data, list_count))
        return new_dict
        #print(list_column_data)
        #print(list_count)


    def max_death_country(self, column_name):
            list_column_country=[]
            list_column_deaths = []
            sum_of_deaths = 0.0
            new_dict = {}
            list_set = []
            list_set1 = []
            for info_col in self.data:
                data_country = info_col[column_name]  # we are collecting/storing data from column name Ex: column name- country data will be country name
                list_column_country.append(data_country)
            list_set = set(list_column_country)
            list_set1 = list(list_set)
            for value in range (len(list_set1)):
                for info_column in self.data:
                    if info_column[column_name] == list_set1[value]:
                        sum_of_deaths += float(info_column['deaths'])
                list_column_deaths.append(sum_of_deaths)
                sum_of_deaths = 0
            new_dict = dict(zip(list_column_deaths,list_set1))
            max_deaths = max(new_dict)
            return new_dict[max_deaths],max_deaths
            #print( f'{new_dict[max_deaths]} country with maximum deaths {max_deaths}')

    def scandic_country(self, column_name,value):
            list_scandic_country=['Denmark','Sweden','Norway','Finland']
            confirmed = 0.0
            for info_column in self.data:
                if info_column[column_name] == value and info_column['country'] in list_scandic_country:
                    confirmed += float(info_column['confirmed'])
                    #print(confirmed)
            return str(confirmed)
            #print('Total number of cases confirmed in a day in scandinavia ' + str(confirmed))


data_table = DataTable(data=None)
data_table.read_csv('covid_data.csv')


#column_name=input('Enter the column name: ')
#list_column_data = data_table.locate_column(column_name)
#print(list_column_data)

#index_no = input('Enter the index number to get info: ')
#row_data = data_table.locate_index(index_no)
#print(row_data)

column_name = input('Enter the column name: ')
value = input('Enter the value corresponding to column name: ')
dk_data = data_table.filter_values(column_name,value)
print(dk_data)

#column_name = input('Enter the column name as country or date: ')
#country_count = data_table.value_counts(column_name)
#print(country_count)

#column_name = input('Enter the column name as country for knowing the maximum deaths: ')
#country_name,max_deaths = data_table.max_death_country(column_name)
#print(f'{country_name} country with maximum deaths {max_deaths}')

#column_name = input('Enter the column name as date: ')
#value = input('Enter the date to see the confirmed cases in Scandinavia : ')
#confirmed_cases = data_table.scandic_country(column_name,value)
#print('Total number of cases confirmed in a day in scandinavia ' + confirmed_cases)


