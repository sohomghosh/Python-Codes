#Pandas basics
import pandas as pd
data=pd.read_csv('<url:>/<location><filename.csv>')
data.head()
data.tail()
data.shape()


#Read bad lines
data_natun=pd.read_csv("file.csv",sep='\x01', dtype={'id': np.int32, 'name': object, 'projct_id':np.int32,'address':object,'age':np.float64}, error_bad_lines=False,index_col=None,low_memory=False)

#Read data giving _csv.Error: line contains NULL byte
from io import StringIO
data=pd.concat(pd.read_csv(StringIO(''.join(l.replace('\x00', '') for l in open("data.csv"))),sep=',',error_bad_lines=False,header=0,engine='python',chunksize=16*1024,quoting=csv.QUOTE_NONE, encoding='utf-8'))

#Read data where string is enclosed in "" and string has within itself
import csv
data = pd.read_csv("/data.csv",sep=r',(?=\S)',quoting=csv.QUOTE_ALL, encoding = 'utf-8')
data = pd.read_csv("/data.csv",sep=r',(?=\S)',quoting=csv.QUOTE_ALL, error_bad_lines=False, dtype={'name_string_field':np.object_,'Id':np.int32,'distinct_num':np.int32,'total_num':np.int32}, encoding = 'utf-8')


#pandas.errors.ParserError: ',' expected after '"'
pd.read_csv(StringIO(''.join(l.replace('"', '') for l in open("day_data.csv"))))

#change number display format in pandas
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#change text display format in pandas
pd.set_option('display.max_colwidth', -1)

**AFTER JOINING ALWAYS CHECK NUMBER OF RECORDS**

#Join no result:
If after joining two pandas dataframes you are getting no results then check the datatype of the parameter used for joining the two dataframes

#Join extra results:
USE 
df.drop_duplicates() before join



#Column rearrange
final_data = final_data[['col4','col2','col1']]


#Combine 2 dataframes side by side
new_df=pd.concat([df1,df2],axis=1)
#It is important to mention axis=1 else nan values may come

#Combine 2 columns : concat cpntents of 2 columns : example -> name in col1 CONCAT with surname in col2
df['name_surname'] = df['name'].map(str) + df['surname'].map(str)

#add certain number of days to a date ##Reference: https://stackoverflow.com/questions/20480897/pandas-add-one-day-to-column
df['new_date_one_advanced'] = pd.DatetimeIndex(pd.to_datetime(df['date'])) + pd.DateOffset(1)

#Drop dupicates / duplicate rows
data=data.drop_duplicates()

#Drop duplicate columns
df = df.loc[:,~df.columns.duplicated()]

#Apply on more than one columns [condition apply to a column based on another]
#tweet_text_df has 2 columns: 'tweet_text', 'language_detected'
def func(x):
    if x['language_detected']!='en':
        return str(TextBlob('u'+str(x['language_detected'])).translate(to='en'))
    return x['tweet_text']

tweet_text_df['language_translated'] = tweet_text_df.apply(func, axis=1)



#Flat Map
[item for sublist in main_list for item in sublist]
flatten = lambda main_list: [item for sublist in main_list for item in sublist]

#remove / drop a column
df.drop(['column1_to_remove','column2_to_remove'],axis=1)

#remove / drop rows with index 'Coce' and 'Puma' 
df.drop(['Coce', 'Puma'])

#Find out the index of the maximum value from each row in a dataframe df
df.idxmax(axis = 1)


#Find out top 5 key words per document
#Refernce: https://stackoverflow.com/questions/38955182/find-names-of-top-n-highest-value-columns-in-each-pandas-dataframe-row
nlargest = 5
order = np.argsort(-tfidf_df.values, axis=1)[:,:nlargest]
result = pd.DataFrame(tfidf_df.columns[order], 
                      columns=['top{}'.format(i) for i in range(1, nlargest+1)],
                      index=tfidf_df.index)
result.head()



#Group by then join
#Every man should have min five distinct cars
c=pd.DataFrame({'is_car_cnt_more5':cleaned_data.groupby(['man_id'])['car_id'].nunique()>=5}).reset_index()
c=c[c['is_car_cnt_more5']==True]
del c['is_car_cnt_more5']
cleaned_data=pd.merge(cleaned_data,c,on=['man_id'])
cleaned_data=cleaned_data.dropna()

df1.join(df2,left_on='col_for_joining_of_df1',right_on='col_for_joining_of_df2').drop('col_for_joining_of_df2',axis=1)

#groupby then count and rename the count as new_cc
gf.groupby(['id'], as_index=False).size().reset_index().rename(columns={0:'new_cc'}).head()


#Group by with multiple list unmap
#For a given animal find frequency of all the attributes
#DATA
#class_id animal_id    attributes
#1        21           walk, talk, sleep
#1        22           eat, sleep
#1        21           cry,laugh, sleep
#1        21           dance, cook, walk
cluster_attribites=pd.DataFrame({'attribute_frequency' : data_use.groupby('animal_id').apply(lambda x: str(Counter([item for sublist in [i.split(',') for i in list(x['attributes'])] for item in sublist])))}).reset_index()


#Group Concat
df.groupby('team').apply(lambda x: ','.join(x.user))
df.groupby('team').apply(lambda x: [i for i in x.user])

#Group concat with concat /aggregate on multiple columns
di = {'Start Date': lambda g:  ','.join([str(i) for i in list(df.loc[g.index]['Start Date'])]) , 
     'End Date': lambda g:  ','.join([str(i) for i in list(df.loc[g.index]['End Date'])])}
df_use =  df.groupby(['id', 'product_id', 'validity in months']).agg(di).reset_index()


#If the column which is to be concatenated after grouping has null values then typecaste into string first
df.groupby('userid').apply(lambda x : len(set([str(i) for i in x.gender]))).reset_index().rename(columns = {0 : 'gender_list'})


#Group concat with aggregate
df_new = final_df.groupby('type').agg({'eve_name':np.size, 'is_positive':np.sum, 'g_id': lambda x: ','.join(x)}).reset_index()


useful_data.groupby('single_kv', as_index=False).agg(lambda x : str(Counter(x.cleaned_single_sv).most_common(50)))
#single_kv, cleaned_single_sv are columns
#If the above gives error like Series does not have the column cleaned_single_sv, then instead of using multiple columns in groupby, first concat these columns create a single column out of them and then groupby 

#Source: https://stackoverflow.com/questions/23794082/pandas-groupby-and-join-lists
In [63]: df
Out[63]: 
   a          b    c
0  1  [1, 2, 3]  foo
1  1     [2, 5]  bar
2  2     [5, 6]  baz


In [64]: df.groupby('a').agg({'b': 'sum', 'c': lambda x: ' '.join(x)})
Out[64]: 
         c                b
a                          
1  foo bar  [1, 2, 3, 2, 5]
2      baz           [5, 6]

#groupby with agg and size within agg dictionary [then use np.size instead of size()]
final_df.groupby('source').agg({'col_name':np.size, 'col2_name':np.sum}).reset_index()


#group by with sorting
df.groupby('team').apply(lambda x: ','.join(sorted(x.user)))
OR

df.groupby('team').agg({'user' : lambda x: ', '.join(x)})


#Read hive exported files in pandas
The default separator is "^A". In python language, it is "\x01"
import pandas as pd
data=pd.DataFrame.from_csv("000000_0",sep='\x01',index_col=None)
data.columns=['colname1', 'colname2', 'colname3', 'colname4', 'colname5', 'colname6', 'colname7', 'colname8', 'colname9']
data.head


#Index of elements after sorting
s = [2, 3, 1, 4, 5]
print(sorted(range(len(s)), key=lambda k: s[k]))
#Output: [2, 0, 1, 3, 4] #Means after sorting "1" comes in front whose postion is 2nd in the original list, "2" comes second whose postion is 0th in the original list and so on


#Read files with multi-char seperator
import pandas as pd
import numpy as np
from io import StringIO

data=pd.read_csv(StringIO(''.join(l.replace('||', '$') for l in open("data.csv"))),sep='$')


#Order by
final_data=final_data.sort_values(['person_id','role_id'])

#Group by then order by
test_data.groupby(['col1','col2'], as_index = False).size().reset_index().sort_values(['col1','col2']).to_csv("/index/ans.csv",index=False)

#order by indescending order
final_data.sort_values(['count'], ascending = False)

#Column transformation
#Converting to months
final_data['company_rating']=[int(i) for i in final_data['company_rating']/30]


#Count distinct
In [2]: table
Out[2]: 
   CLIENTCODE  YEARMONTH
0           1     201301
1           1     201301
2           2     201301
3           1     201302
4           2     201302
5           2     201302
6           3     201302

In [3]: table.groupby('YEARMONTH').CLIENTCODE.nunique()
Out[3]: 
YEARMONTH
201301       2
201302       3


#################################DATA FRAME OPERATIONS##############################################################
#Create empty dataframe and keep appending / adding dataframes to it
import os
df = pd.DataFrame({})
for fil in os.listdir('folder_name_with_csv_files/):
    df1 = pd.read_csv(fil)
    df = df.append(df1)


#Creating empty dataframe
df = pd.DataFrame({c: np.repeat(0, [nrow]) for c in data['PAGENO'].unique()})

#Assigning values to a cell of a dataframe
#Populating the dataframe
for row in data.iterrows():
	if list(list(row)[1])[1] in data['PAGENO'].unique():
		df.set_value(index=di[list(list(row)[1])[0]], col=list(list(row)[1])[1], value=list(list(row)[1])[2])

#Extracting one by one rows
for i in range(0,nrow):
	row_df=list(df.iloc[i,0:ncol])#iloc for extracting by index, loc for extracting by names

#Extracting rows by names
df.loc[['row_name_1', 'row_name_2'],:]

#Extracting rows by index
df.iloc[[0, 1],:]

#Extracting columns by names
df.loc[:,['column_name_1', 'column_name_2']]

#Extracting columns by index
df.iloc[:,[0, 1]]

#Setting values by names
df.set_value('row_name','column_name',value=10,takeable=False)

#Setting values by index
df.set_value(0,1,value=10,takeable=True)#Referring to the 0th row and 1st column

#Select as in sql
selected_data1_erp=data[data['Profession'] == 'Data Analyst']
selected_data2_erp=selected_data1_erp.groupby(['WorkExp'],as_index = False)['Salary'].mean()

#################################################################################################################

#Sort a dataframe by one column after the other
final_data=final_data.sort_values(['org_id','class_id','subclass_id_consider'])


#Drop na : Remove all data with na missing values
final_data=final_data.dropna()

#extract only numeric columns
train_only_numeric = train._get_numeric_data()

#extract only numeric columns
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
newdf = df.select_dtypes(include=numerics)

#se;ect only categorical columns
cat_data = X.select_dtypes(include='object')
num_data = X.select_dtypes(exclude='object')
cat_cols = cat_data.columns.values
num_cols = num_data.columns.values
print('Categorical Columns : ',cat_cols)
print('Numerical Columns : ',num_cols)		      
		      
#Filter by list
In [5]: df = DataFrame({'A' : [5,6,3,4], 'B' : [1,2,3, 5]})

In [6]: df
Out[6]:
   A  B
0  5  1
1  6  2
2  3  3
3  4  5

In [7]: df[df['A'].isin([3, 6])]
Out[7]:
   A  B
1  6  2
2  3  3


#Import error remove
import csv
import pandas as pd
data=pd.read_csv("file.csv", header = None, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8') #read a file without header
data.head()

#target encoding
#conda install -c conda-forge category_encoders
from category_encoders import *
X = train[['gender','ever_married']]
y = train['stroke']
enc = BinaryEncoder(cols=['gender','ever_married']).fit(X, y)
numeric_dataset = enc.transform(X)

#######################################PANDAS SQL############################################################
#From link http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
import pandas as pd
import numpy as np

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'
tips = pd.read_csv(url)
tips.head()

##SQL => SELECT
#SELECT total_bill, tip, smoker, time
#FROM tips
#LIMIT 5;

tips[['total_bill', 'tip', 'smoker', 'time']].head(5)



##SQL => WHERE
#SELECT *
#FROM tips
#WHERE time = 'Dinner'
#LIMIT 5;

tips[tips['time'] == 'Dinner'].head(5)
#OR
#is_dinner = tips['time'] == 'Dinner'
#tips[is_dinner].head(5)


#SELECT *
#FROM tips
#WHERE time = 'Dinner' AND tip > 5.00;

tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
#############################################################################################################


#Percentile calculation
#Keep only those people whose age is between 65 and 95 percentle
import numpy as np
data=data[(data['age']>=np.nanpercentile(data['age'],65))&(data['age']<=np.nanpercentile(data['age'],95))]


#Read big file in chunks
data=pd.concat(pd.read_csv("file_name_downloaded_from_hive",sep='\x01',error_bad_lines=False,header=0,low_memory=False,chunksize=16*1024))


#Store count after groupby
df1=pd.DataFrame({'count' : df1.groupby( [ "Name", "City"] ).size()}).reset_index()


#Convert string column to numeric
pre_final_data['appln_id']=pd.to_numeric(pd.Series(pre_final_data['appln_id']),errors='coerce')


#Transform column by comparing with a list (intersection)
#See if anything is common between a list 'similar_pos' and column 'pos_spec' of a dataframe data
similar_pos=['123','322']
#data['pos_spec']=['123|452','987|321']
dt_pos=data['pos_spec'].apply(lambda x : len(set(str(x).split('|')).intersection(set(similar_pos)))>0)

#Combine lists of different length to a dataframe; First need to convert lists to a dataframe
#Combine dataframes of different number of rows to a single dataframe
pd.concat([df,df1], ignore_index=True, axis=1) #df and df2 are dataframes created from lists of different length


#Apply on multiple pandas columns
def quater(mn,yr):
	if mn in [1,2,3]:
		return "Q1-"+str(yr)
	elif mn in [4,5,6]:
		return "Q2-"+str(yr)
	elif mn in [7,8,9]:
		return "Q3-"+str(yr)
	elif mn in [10,11,12]:
		return "Q4-"+str(yr)
	else:
		return np.nan()

#Transforming multiple columns on df_all
df_all['quater']=df_all[['month','year']].apply(lambda x: quater(*x), axis=1)


#Apply on the whole row
cat = search_by_category(text)
def score_increase(row):
    new_score = int(row['score'])
    #print(row['l2_category'])
    if row['l2_category'].lower() in cat:
        new_score = new_score + 10
    return new_score

dtf.apply(score_increase, axis=1)

def score_increase(row):
    new_score = int(row['score'])
    if row[param].lower() in li:
        new_score = new_score + 10
    return new_score

#Apply on function taking mulitiple parameters as input on the whole row 
def score_increase(row, li, param):
    new_score = int(row['score'])
    if row[param].lower() in li:
        new_score = new_score + 10
    return new_score

cat = search_by_category(text)
    if len(cat) != 0:
      dtf['score'] = dtf.apply(lambda x:score_increase(x,cat,'l2_category'), axis=1) 
    


###DO NOT USE THIS### PRODUCES ERRONEOUS RESULTS####
pd.DatetimeIndex(data['Given Date'],ambiguous ='NaT').month#######DO NOT USE THIS### PRODUCES ERRONEOUS RESULTS####
###DO NOT USE THIS### PRODUCES ERRONEOUS RESULTS####

### Find out columns having null  ###
pd.isnull(df).sum() > 0

### Find out number of null values in each column
pd.isnull(df).sum()

### Pivot ### [Row to Column]
df_new=df.pivot(index='id', columns='column_to_be_transformed_to_multiple_columns', values='column_whose_values_are_to_be_shown_in_each_cell').reset_index()

### Pivot table ### [Row to Column]
df_new=df.pivot_table(index=['id1','id2'], columns=['1st_column_to_be_transformed_to_multiple_columns','2nd_column_to_be_transformed_to_multiple_columns'], values=['1st_column_whose_values_are_to_be_shown_in_each_cell','2nd_column_whose_values_are_to_be_shown_in_each_cell']).reset_index()

### Fatten-a-hierarchical-index-in-columns after using pivot_table ###
[' '.join(col).strip() for col in df.columns.values]

### See more text each column in pandas
 pd.options.display.max_colwidth = 100
	

### Source: https://medium.com/towards-data-science/pandas-tips-and-tricks-33bcc8a40bb9
#Name: "Sohom Ghosh" to "Sohom" "Ghosh" each in seperate column; Spliting a string into multiple strings by space
df[‘name’] = df.name.str.split(" ", expand=True)

#Fill one column by another
df['Cat1'].fillna(df['Cat2'])

### Row to Column ###
#Different types entries mentioned in "activity" column as seperate columns. The entries of these cells will be number of occurrences
df.groupby('name')['activity'].value_counts().unstack().fillna(0)

#Suppose target has 0,1. Check which variable is capturing more variablity of target variable. Use unstack to get variable,count_0,count_1 side by side
data.groupby(['column_against_whom_we_want_to_see_distribution', 'target']).size().unstack().reset_index()

df.columns
#[id,'type','time']


df.head(2)
'''
id,type,time
1,full,12:02
2,not_full,13:09
'''


#OUTPUT REQUIRED
'''
id,full,not_full
1,12:02,NaN
2,NaN,13:09
'''

df.groupby(['id','type'])['time'].agg(np.min).unstack().reset_index()

OR

p = df.pivot(index='id', columns='type', values='time')
#####################################################################

#Time Difference between timestamps of activities of a person
df = df.sort_values(by=['name','timestamp'])
df['time_diff'] = df.groupby('name')['timestamp'].diff()

#Move each row one up in the dataframe
df[‘new_shifted_column’] = df.time_diff.shift(-1)
# -1 means one row up

#Convert Time Difference to total seconds betweeen them
df['time_diff'] = df.time_diff.dt.total_seconds()

#cumuative sum
df['money_spent_so_far'] = df.groupby(‘name’)['money_spent'].cumsum()

#Cumulative count
df2 = df[df.groupby(‘name’).cumcount()==1]


#See dtype of all columns
[(f,train[f].dtype) for f in train.columns]

from sklearn.preprocessing import LabelEncoder

#LabelEncoder
for f in ['Destination_Type']:#Add all categorical features in the list
    lbl = LabelEncoder()
    lbl.fit(list(train_test[f].values))
    train_test[f] = lbl.transform(list(train_test[f].values))

#Convert all categorical features to numeric
for f in features:
    if df_final_train[f].dtype=='object':
    	lbl = LabelEncoder()
    	lbl.fit(list(df_final_train[f].values)+list(df_final_test[f].values))
    	df_final_train[f] = lbl.transform(list(df_final_train[f].values))
    	df_final_test[f]= lbl.transform(list(df_final_test[f].values))

# Equivalent to summary in python #Gives Max, Min, count, detailed description
train_clean.describe()

# Spelling correction in pandas dataframe
data['col']=data['col'].replace(to_replace=['wrong_spelling_1','wrong_spelling_2'],value='correct_spelling')

#replace all values except a few by 'others' :: here : replace all states other than UP, MH by 'others
ff_new['cleaned_state'] =ff_new['state']
ff_new = ff_new.set_value(index=ff_new[~ff_new['cleaned_state'].isin(['UP','MH'])].index,col='cleaned_state',value='others')



#Apply user defined function taking multiple columns of a pandas dataframe input simultaneously
df.apply(lambda row: my_test(row['a'], row['c']), axis=1)
#Source: https://stackoverflow.com/questions/16353729/pandas-how-to-use-apply-function-to-multiple-columns

#Pandas - R dataframe comparison link
http://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html

#Pandas - categorical features
http://pandas.pydata.org/pandas-docs/stable/categorical.html#categorical
http://pandas.pydata.org/pandas-docs/stable/api.html#api-categorical

#Reading excel file
data6 = pd.read_excel('mar_data.xls',header=0,sheetname=1)

#JOIN using pandas
pd.merge(df1,df2,on='key_column_to_merge',how='inner')

#JOIN using pandas on multiple columns
pd.merge(df1,df2,on=['1st_key_column_to_merge','2nd_key_column_to_merge'],how='inner')


#Encoding
train_test['Gender'] = train_test['Gender'].replace(to_replace = {'Male': 0, 'Female': 1})

#Train Valid divide
from sklearn.model_selection import train_test_split
X_train,X_valid=train_test_split(train,test_size=0.33, random_state=42)

#Check if a column is null in pandas
train_data_clean = pd.notnull(train_data_clean['label'])


#pandas dataframe to dictonary convert
df.set_index('ID').T.to_dict('list')

#df is a dataframe and is like follows:
'''
id    name
1     abc
2     pqr
'''
dictionary_use = df.set_index('id').T.to_dict('records')[0]


#drop suplicates
df.drop_duplicates(subset=['id','aadhar_no'])

# Type casting to date time
pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')
# Type casting from mongoDB exported date time [like:Tue Nov 28 2017 05:29:59 GMT+0530 (IST)] to python date time format
data ['createTime_formatted'] =  pd.to_datetime(data['createTime'], format='%a %b %d %Y %H:%M:%S GMT+0530 (IST)',errors='coerce')

#Age calculation : : Date of birth : dob_format : 1980-10-22
from datetime import datetime
days_diff = datetime.today() - pd.to_datetime(data['dob'], errors = 'coerce')
data['age'] = days_diff.astype('timedelta64[D]')/365

#Add n days to a date
df['dt_time'] + datetime.timedelta(+6)
df['yesterday'] = df['today'] + datetime.timedelta(-1)

train_test['DateTime'] =  pd.to_datetime(train_test['DateTime'], format='%Y-%m-%d %H:%M:%S',errors='coerce')

train_test['weekday'] = train_test['DateTime'].dt.weekday
train_test['day_of_month'] = train_test['DateTime'].dt.day
train_test['month'] = train_test['DateTime'].dt.month
train_test['hour'] = train_test['DateTime'].dt.hour
train_test['year'] = train_test['DateTime'].dt.year
train_test['minutes'] = train_test['DateTime'].dt.minute
train_test['seconds'] = train_test['DateTime'].dt.second

#Extract date from datetime object pandas
train_test['DateTime'].dt.date

#Consecutive rows difference in a pandas dataframe
df['dA'] = df['A'] - df['A'].shift(-1)

#epoch to datetime
import time		      
data['new_date_time_human_readable_col'] = data['epoch_unix_times_time'].apply(lambda x:time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(x))))


#Creating random numbers (as labels)
np.random.choice([0, 1], size = (10,), p = [1./3, 2./3])#[numbers to randomly choose from], size = number of numbers to generate, p = [proportions of the numbers chosen in same order as mentioned in the first argument as list]
np.random.randint(0, 2, 10)#lower_number, higher_number, number_of_numbers

import random
train_ids = random.sample(list(data.index),int(.8*len(data.index)))
train = data[data.index.isin(train_ids)]
valid = data[~data.index.isin(train_ids)]

#Cross-tabulation #For generally for categorical_variables
pd.crosstab(df.col_1, [df.col_2, df.col_3], rownames=['col_1'], colnames=['col_2', 'col_3'])

#Source: https://stackoverflow.com/questions/19960077/how-to-implement-in-and-not-in-for-pandas-dataframe
For "IN" use: something.isin(somewhere)
Or for "NOT IN": ~something.isin(somewhere)
df[df.countries.isin(countries)]
df[~df.countries.isin(countries)]

####One Hot Encoding

one_hot_encoded_train_test = pd.get_dummies(train_test[['Gender','City_Category','Employer_Category1','Employer_Category2','Customer_Existing_Primary_Bank_Code','Primary_Bank_Type', 'Contacted', 'Source', 'Source_Category', 'Var1']])
train_test_use = pd.concat([train_test[['Monthly_Income','Existing_EMI','Loan_Amount','Loan_Period','Interest_Rate','EMI','city_encoded','employer_encoded','age','lead_age','loan_emi_ratio','loan_income_ratio','savings','is_new_emi_more','is_emi_available','Approved']],one_hot_encoded_train_test], axis=1)


#Source: https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

label_encoder = LabelEncoder()
onehot_encoder = OneHotEncoder(sparse=False)

def one_hot_encode_fns(col_to_encode,train):
	integer_encoded = label_encoder.fit_transform(train[col_to_encode].values).reshape(train.shape[0], 1)
	onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
	onehot_encoded_df = pd.DataFrame(onehot_encoded)
	onehot_encoded_df.index = train.index
	onehot_encoded_df.columns = [col_to_encode + "one_hot" + str(i) for i in range(onehot_encoded_df.shape[1])]
	return onehot_encoded_df


col_to_encode = "C6"
#train[col_to_encode] has values like True, False, True
onehot_df = one_hot_encode_fns(col_to_encode,train)
train = pd.concat([train, onehot_df], axis = 1)
del train[col_to_encode]

#Ensembled multiple dataframes
df_all=pd.read_csv("sub6.csv")
for i in [18,36]:
	df_all=df_all.append(pd.read_csv("sub"+str(i)+".csv"))

ensembled_ans=df_all.groupby('roadId',as_index=False)['noOfLanes'].agg(lambda x: x.value_counts().index[0])
ensembled_ans.to_csv("sub39.csv",index=False)

#Replace unreadable characters
given_str.replace(u"\u001A", "").strip()

#https://stackoverflow.com/questions/32796651/extract-dictionary-from-counter-object
>>> from collections import Counter
>>> a = Counter({'menu': 20, 'good': 15, 'happy': 10, 'bar': 5})
>>> b = Counter({'menu': 1, 'good': 1, 'bar': 3})
>>> a + b
Counter({'menu': 21, 'good': 16, 'happy': 10, 'bar': 8})


from collections import Counter, OrderedDict
locations = list(data['city'].apply(lambda x : str(x).lower().strip()))
ordered_dict = OrderedDict(Counter(locations).most_common())

location_distribution = pd.DataFrame({'count' :list(ordered_dict.values()), 'city' :list(ordered_dict.keys())})


#Parallelizing pandas
#Source: http://www.racketracer.com/2016/07/06/pandas-in-parallel/
import pandas as pd
import numpy as np
import seaborn as sns
from multiprocessing import Pool
num_partitions = 10 #number of partitions to split dataframe
num_cores = 4 #number of cores on your machine
iris = pd.DataFrame(sns.load_dataset('iris'))
def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

def multiply_columns(data):
    data['length_of_word'] = data['species'].apply(lambda x: len(x))
    return data
    
iris = parallelize_dataframe(iris, multiply_columns)

#Distributed processing using pandas
#Source: http://gouthamanbalaraman.com/blog/distributed-processing-pandas.html
import pandas as pd
import multiprocessing as mp
LARGE_FILE = "D:\\my_large_file.txt"
CHUNKSIZE = 100000 # processing 100,000 rows at a time
def process_frame(df):
        # process data frame
        return len(df)

if __name__ == '__main__':
        reader = pd.read_table(LARGE_FILE, chunksize=CHUNKSIZE)
        pool = mp.Pool(4) # use 4 processes

        funclist = []
        for df in reader:
                # process each data frame
                f = pool.apply_async(process_frame,[df])
                funclist.append(f)
        result = 0
        for f in funclist:
                result += f.get(timeout=10) # timeout in 10 seconds
        print "There are %d rows of data"%(result)


#Transpose a pyspark dataframe	
df.T

#all but one column [except one column select]
df4.iloc[:,df4.columns != 'col_name']

#columnwise sum
df.sum(axis=0)

#rowwise sum
df.sum(axis=1)


#reorder columns of a dataframe
df.reindex(columns=['col1', 'col2'])

#Removing upper triangular matrix
df.mask(np.triu(np.ones(df.shape, dtype=np.bool_)))

#Removing lower triangular matrix
df.mask(np.tril(np.ones(df.shape, dtype=np.bool_)))

#Set a column as an index of a dataframe
df4.set_index(df4.col_name, inplace=True)

#dealing data with dask
#https://dask.pydata.org/en/latest/dataframe-overview.html
import dask.dataframe as dd
df = dd.read_csv("cat0_click_data.csv", error_bad_lines = False)
$split -d -l 100 cat0_click_data.csv cat0_parts_
$for f in cat0_parts_*; do mv $f $f.csv; done
ddata = dd.read_csv('data/iata_2000_*.csv', nrows=MAX_ROWS, header=0, names=cols, dtype=dtypes)

#http://dask-ml.readthedocs.io/en/latest/modules/api.html#module-dask_ml.xgboost
	

#error-in-reading-a-csv-file-in-pandascparsererror-error-tokenizing-data-c-err
#Source: https://stackoverflow.com/questions/33998740/error-in-reading-a-csv-file-in-pandascparsererror-error-tokenizing-data-c-err
df_clean = pd.read_csv('test_error.csv', lineterminator='\n')

#Adding plots / coloured cells / to excel
http://xlsxwriter.readthedocs.io/working_with_pandas.html
http://pbpython.com/excel-pandas-comp-2.html

#### Connecting to mysql databases
import pymysql
conn= pymysql.connect(host='<host_ip_without_port_like 172.11.11.123>',user='user_name',password='password',db='name_of_db')
df = pd.read_sql_query("select * from table_name", con = conn)

#### Connecting to databases : aws
import psycopg2
import pandas as pd
import time
from datetime import datetime

conn_string = "dbname='name_of_database' port='port_number' user='user_name' password='password' host='host_name_or_ip'";

conn = psycopg2.connect(conn_string);
df = pd.read_sql_query("select * from table_name", con = conn)

#see all table names using read_sql
pd.read_sql("SELECT * FROM information_schema.tables", con = conn).head()

#OR

#INSERT INTO MYSQL
conn= pymysql.connect(host='<host_ip_without_port_like 172.11.11.123>',user='user_name',password='password',db='name_of_db')
cursor = conn.cursor();
sql = "INSERT INTO TABLE (FIELD_ONE_STRING, FIELD_TWO_INTEGER, REQ_DATE_TIME) VALUES ('string_value_of_field1',123,'2018-07-19 15:25:39')"
cursor.execute(sql)
conn.commit()

result = cursor.execute("select * from table_name")
#NOT WORKING IN PYTHON3# df1 = pd.DataFrame(result.fetchall())
#NOT WORING IN PYTHON3# df1.columns = result.keys()

#Fetch result in batches
#Reference: https://stackoverflow.com/questions/32625593/retrieving-data-from-mysql-in-batches-via-python

cursor.execute("SELECT count(*) FROM mytable")
count = cursor.fetchone()[0]
batch_size = 42 # whatever

for offset in xrange(0, count, batch_size):
    cursor.execute(
        "SELECT * FROM mytable LIMIT %s OFFSET %s", 
        (batch_size, offset))
   for row in cursor:
       do_something_with(row)

# Sort a pandas dataframe based on index of other pandas dataframe
df2.reindex(df.index)

#Adding values of 2 dataframes element wise
df_add = df1.add(df2, fill_value=0)

#Finding correlation between 2 columns of a dataframe
df['A'].corr(df['B'])


#Finding cosine similarity between all pairs of elements of a matrix : #Reference: https://stackoverflow.com/questions/17627219/whats-the-fastest-way-in-python-to-calculate-cosine-similarity-given-sparse-mat
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
A =  np.array([[0, 1, 0, 0, 1], [0, 0, 1, 1, 1],[1, 1, 0, 1, 0]])
A_sparse = sparse.csr_matrix(A)
similarities = cosine_similarity(A_sparse)
similarities

#Styling and coloring cells, conditional formating of pandas dataframe
http://pandas.pydata.org/pandas-docs/stable/style.html

#Save dataframe as html
df.to_html('filename.html')

#Save styled data frame as excel #Reference: https://stackoverflow.com/questions/47398937/saving-pandas-styler-object-in-anyway
df.style.background_gradient(cmap='RdYlGn',low=.09,high=.18,axis=1).to_excel('d:/temp/a.xlsx', engine='openpyxl')

#Save pandas dataframe as excel, xlsx file
writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
writer.save()

#Save dataframe as image png #Reference: https://stackoverflow.com/questions/35634238/how-to-save-a-pandas-dataframe-table-as-a-png
import matplotlib.pyplot as plt
from pandas.tools.plotting import table
ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
#df is the required pandas dataframe
table(ax, df)  # where df is your data frame
plt.savefig('mytable.png')

#text to columns : transform a column having many fileds sepearted by , to different columns
df = data['col_name'].str.split(',', expand=True)
#whenever there will be no data corresponding to a filed, it will be None

#write without header and index
df.to_csv("data.csv", header=False, index = False)

# Remove .0 from int columns while writing
#Even after using astype sometimes .0 doesnot get replaced. This is because column has a nan value which it treats as float. In such cases, first fillna then typecast
df['ab_id'].fillna(0, inplace = True)
df['ab_id'] = df['ab_id'].astype(int,errors='ignore')


#columns to rows : use melt function #Reference: https://stackoverflow.com/questions/28654047/pandas-convert-some-columns-into-rows
data_melted = pd.melt(data, id_vars=["col1_not_to_be_made_row", "col2_not_to_be_made_row"], var_name="name_of_the_new_column_which_will_have_all_previous_column_names", value_name="name_of_the_new_column_which_will_have_values_corresponding_to_previous_columns")
df
'''
location  name  Jan-2010  Feb-2010  March-2010
0        A  test        12        20          30
1        B   foo        18        20          25
'''

df2 = pd.melt(df, id_vars=["location", "name"], var_name="Date", value_name="Value")
df2

'''
  location  name        Date  Value
0        A  test    Jan-2010     12
1        B   foo    Jan-2010     18
2        A  test    Feb-2010     20
3        B   foo    Feb-2010     20
4        A  test  March-2010     30
5        B   foo  March-2010     25
'''


#Rank events based on their time occurrence, when multiple occurrence of the same event occurs

#data
id,event,time
1,install,18/05/18 13:17
2,install,19/05/18 13:17
2,play,19/05/18 13:19
1,uninstall,21/05/18 13:17
4,install,22/05/18 13:17
4,play,23/05/18 13:17
4,uninstall,24/05/18 13:17
4,install,25/05/18 13:17
3,install,26/05/18 13:17
3,uninstall,27/05/18 13:17
2,uninstall,28/05/18 13:17
2,install,28/05/18 13:17
1,install,21/05/18 14:17
2,play,28/05/18 13:19


data['date_time']=pd.to_datetime(data['time'],errors='coerce')
data['rank'] = data.groupby(['id','event'])['date_time'].rank(method="dense", ascending=True)
data['event_ranked'] = data['event'].str.cat(data['rank'].astype(int).astype(str))
data.sort_values(['id','event','date_time'])

#OUTPUT
    id      event            time           date_time  rank event_ranked
0    1    install  18/05/18 13:17 2018-05-18 13:17:00   1.0     install1
12   1    install  21/05/18 14:17 2018-05-21 14:17:00   2.0     install2
3    1  uninstall  21/05/18 13:17 2018-05-21 13:17:00   1.0   uninstall1
1    2    install  19/05/18 13:17 2018-05-19 13:17:00   1.0     install1
11   2    install  28/05/18 13:17 2018-05-28 13:17:00   2.0     install2
2    2       play  19/05/18 13:19 2018-05-19 13:19:00   1.0        play1
13   2       play  28/05/18 13:19 2018-05-28 13:19:00   2.0        play2
10   2  uninstall  28/05/18 13:17 2018-05-28 13:17:00   1.0   uninstall1
8    3    install  26/05/18 13:17 2018-05-26 13:17:00   1.0     install1
9    3  uninstall  27/05/18 13:17 2018-05-27 13:17:00   1.0   uninstall1
4    4    install  22/05/18 13:17 2018-05-22 13:17:00   1.0     install1
7    4    install  25/05/18 13:17 2018-05-25 13:17:00   2.0     install2
5    4       play  23/05/18 13:17 2018-05-23 13:17:00   1.0        play1
6    4  uninstall  24/05/18 13:17 2018-05-24 13:17:00   1.0   uninstall1



			
##statmodels VIF
#variance_inflation_factor(exog, exog_idx)
#One recommendation is that if VIF is greater than 5, then the explanatory variable given by exog_idx is highly collinear with the other explanatory variables, and the parameter estimates will have large standard errors because of this
from statsmodels.stats.outliers_influence import variance_inflation_factor
df = train[['age','avg_glucose_level','bmi']].dropna()
pd.Series([variance_inflation_factor(df.values, i) for i in range(df.shape[1])], index=df.columns)


## transform date of different forms into one form
new_data = pd.DataFrame({'date':['12/4/2018 23:59','12/4/2018 23:59','12/4/2018 23:59','12/4/2018 23:59','13-04-2018 00:00:23','13-04-2018 00:00:23','13-04-2018 00:00:53','13-04-2018 00:01:17','13-04-2018 00:01:17','13-04-2018 00:01:33']})
pd.to_datetime(new_data['response_date'])

#rolling mean
df.rolling(window=3, min_periods=1).mean()

#strings encode as numeric
df['y'] = pd.factorize(df['sex'])[0]

#pandas explode
df['ref_list_new'] = df['ref_list'].apply(lambda x : eval(x)) #covert column of string "[1, 4, 5]" to list [1, 4, 5]
df['ref_list_new'].apply(pd.Series).stack().rename('ref_list_new') .to_frame().reset_index(1, drop=True).join(df[list(set(train_info.columns) - set(['ref_list', 'ref_list_new']))]).reset_index(drop=True)
df['<name_of_col_having_list>'].apply(pd.Series).stack().rename('<name_of_col_having_list>') .to_frame().reset_index(1, drop=True).join(df[<list_of_columns_expect_the_one_having_list>]).reset_index(drop=True)
#References: https://stackoverflow.com/questions/38428796/how-to-do-lateral-view-explode-in-pandas
#df1 = df.A.apply(pd.Series).stack().rename('A')
#df2 = df1.to_frame().reset_index(1, drop=True)
#df2.join(df.B).reset_index(drop=True)


#pandas explode : convert a row which consists of list to seperate rows #Reference: https://stackoverflow.com/questions/38428796/how-to-do-lateral-view-explode-in-pandas
#remeber column A may be stored as a string of list like "[1,2]" . In this case we need to use eval to extract the list from the string
# df['A'] = df['A'].apply(lambda x : eval(str(x)))
pd.DataFrame([[item]+list(df.loc[line,'B':]) for line in df.index for item in df.loc[line,'A']], columns=df.columns)
#Here A is the column which has list, B is a sperate column
# input:
        A   B
0  [1, 2]  10
1  [5, 6] -20
# output:
   A   B
0  1  10
1  2  10
2  5 -20
3  6 -20



#univariate analysis
train.describe().T.to_csv('univariate_analysis_train.csv')

#Using pandas to read a text file with the headers in multiple rows : Reference: https://stackoverflow.com/questions/46436419/using-pandas-to-read-a-text-file-with-the-headers-in-multiple-rows
g = lambda x: '' if x.startswith('Unnamed') else x

pd.read_fwf(
    'file.txt',
    sep='\s{2,}',
    header=[0, 1, 2],
    skiprows=[3]
).rename(columns=g)

#Deciles cut for Lift Chart
df = pd.DataFrame({'actual_label' : validation_df['label'], 'predicted' : valid_preds}).sort_values('predicted', ascending = False)
df['deciles'] = pd.qcut(df['predicted'].values,10)
df.reset_index().groupby('deciles').agg({'index':np.size,'actual_label':np.sum,'predicted':np.sum})
df.reset_index().groupby('deciles').agg({'actual_label':np.mean}) #The mean of actual_label should increase from 0th deciles to 10th deciles
################################LEARNINGS################################
1) If 2 dataframe does not join or produces no/nan values on joining, check if the datatype of their common columns are same
2) df.replace ({'a':'aa'}) is not efficient when number of rows and columns are more, better read row by row and replace elementwise
3) Whenever there is nan or na, astype(int) does not convert into int, so .0 comes with the column when the dataframe is written. Remove nan by fill na first, then do astype(int, errors = 'ignore')
4) Whenever joining : Make sure there is no nan and duplicate values in dataframes to be merged. After mergeing count verify
5) After value_counts() if not get one kind of values : means the other is nan
6) Groupby removes records of pandas dataframes with null values. If we need the count corresponding to null/na/nan values too, then remove them first using 
new_final_df = final_df.fillna('no vaues')
Then groupby
7) if length does not match like length of train and train_test_use : then while assigning, it may restart assigning remaining elements of train_test_use from begining may be: 
		train_test_use['stroke'] = train['stroke'] # THIS MAY RESULT IN BUGS
8)		

#########################################################################

