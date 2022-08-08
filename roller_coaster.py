# Import internal library
import codecademylib3

# 1 
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load rankings data
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_df['material'] = 'wood'
steel_df['material'] = 'steel'
print(wood_df.head())
print(steel_df.head())
# load rankings data

# 2

# 3
# Create a plot of El Toro ranking over time
# Create a function to plot rankings over time for 1 roller coaster
def ranking_over_time(roller_coaster, df, park):
  
  # 1st we find the rankings of the roller coaster in the dataframe if weren't there we send a menssage
  
  ranking = df[(df.Name == roller_coaster) & (df.Park == park)].sort_values(by=['Year of Rank'], ascending=True)[['Rank', 'Year of Rank']]
  if (len(ranking)==0):
    print("\nRoller coaster '{roller_coaster}' not found.".format(roller_coaster=roller_coaster))
  else:
    #we plot de line plot
    plt.clf()
    ax = plt.subplot()
    #plt.bar(range(len(ranking)), ranking.Rank)
    plt.plot(ranking['Year of Rank'], ranking.Rank)
    plt.title("Ranking for '{roller_coaster}' at the '{park}' park.".format(park=park, roller_coaster=roller_coaster))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend(['Rank'])
    #ax.set_xticks(range(len(ranking)))
    #ax.set_xticklabels(ranking['Year of Rank'])
    plt.show()
#Testing the function ranking_over_time
ranking_over_time('Phoenix', wood_df, 'Knoebels Amusement Resort')


# 3 Create a plot of El Toro and Boulder dash hurricanes
def ranking_over_time_2(roller_coaster, df, park):
  
  
  # 1st we find the rankings of the roller coaster in the dataframe if weren't there we send a menssage
  
  ranking_1 = df[(df.Name == roller_coaster[0]) & (df.Park == park)].sort_values(by=['Year of Rank'], ascending=True)[['Rank', 'Year of Rank']]
  if (len(ranking_1)==0):
    print("\nRoller coaster '{roller_coaster}' not found.".format(roller_coaster=roller_coaster[0]))
  else:


    #we plot de line plot 1
    
    ax = plt.subplot()
    #plt.bar(range(len(ranking)), ranking.Rank)
    plt.plot(ranking_1['Year of Rank'], ranking_1.Rank)
    plt.title("Two roller coasters")
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend(roller_coaster)
    #ax.set_xticks(range(len(ranking)))
    #ax.set_xticklabels(ranking['Year of Rank'])
    plt.show()

# find ranks for the second roller coaster
  ranking_2 = df[(df.Name == roller_coaster[1]) & (df.Park == park)].sort_values(by=['Year of Rank'], ascending=True)[['Rank', 'Year of Rank']]

  if (len(ranking_2)==0):
    print("\nRoller coaster '{roller_coaster}' not found.".format(roller_coaster=roller_coaster[1]))
  else:
    plt.plot(ranking_2['Year of Rank'], ranking_2.Rank)
    plt.legend(roller_coaster)
    plt.title("Two Roller Coasters")
    plt.show()

#testing the function ranking_over_time_2(roller_coaster, df, park):
ranking_over_time_2(['El Toro', 'Boulder Dash' ], wood_df, 'Lake Compounce')

# 4
# Create a function to plot top n rankings over time
def top_n(n, df, year):
  #find the top n
  #top_n = df.sort_values(by=['Year of Rank']).sort_values(by=['Rank'], ascending=True)
  #top_n = df[(df['Year of Rank'] == year) & (df.Rank <= n)]
  top_n = df[(df.Rank <= n)]

  #print(top_n.head(100))
  plt.clf()
  ax = plt.subplot()
  for coaster in set(top_n['Name']):
    coaster_rankings = top_n[top_n['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
  plt.legend(loc='upper right')  
  material = top_n.material[0]
  plt.title("Top {n} {material} roller coaster".format(n=n, material=material))
  plt.show()
  
#we test the top_n function
top_n(5, steel_df, 2013)


# 5
# load roller coaster data
roller_statics = pd.read_csv('roller_coasters.csv')
print(roller_statics.info())
print(roller_statics.head(10))

# 6
# Create a function to plot histogram of column values

def any_column_histogram(df, column_name):
  plt.clf()
  ax=plt.subplot()
  plt.hist(df[column_name].dropna())
  plt.title('{column_name} histogram'.format(column_name=column_name.capitalize()))
  plt.show()





# Create histogram of roller coaster speed
any_column_histogram(roller_statics, 'speed')
# Create histogram of roller coaster length
any_column_histogram(roller_statics, 'length')
# Create histogram of roller coaster number of inversions
any_column_histogram(roller_statics, 'num_inversions')
# Create a function to plot histogram of height values
any_column_histogram(roller_statics, 'height')
# Create a histogram of roller coaster height

# 7
# Create a function to plot inversions by coaster at park
def plt_bar_inversions(df, park):
  result = df[df.park == park][['name', 'num_inversions']]
  plt.clf()
  ax=plt.subplot()
  plt.bar(range(len(result)), result.num_inversions)
  plt.title('Inversions for {park}'.format(park=park))
  plt.legend(['Num Inversions'])
  plt.xlabel('Roller coaster')
  plt.ylabel('Num Inversions')
  ax.set_xticks(range(len(result.num_inversions)))
  ax.set_xticklabels(result.name)
  plt.xticks(rotation=10,  fontsize='6', horizontalalignment='right')
  plt.show()
# Create barplot of inversions by roller coasters
plt_bar_inversions(roller_statics, 'Parque Warner Madrid')

# 8
# Create a function to plot a pie chart of status.operating
def plt_pie(df):
  plt.clf()
  #we obtain the operating RC and the closed RC
  rc_statuses = df[(df.status == 'status.operating') | (df.status == 'status.closed.definitely')].status.value_counts()
  #plt.pie(rc_statuses.values())
  #plt.pie(rc_statuses.values, rc_statuses.index, autopct = '%0.1f%%')
  plt.pie(rc_statuses.values, autopct = '%0.1f%%')
  plt.axis('equal')
  plt.legend(rc_statuses.index)
  plt.show()

# Create pie chart of roller coasters
plt_pie(roller_statics)

# 9
# Create a function to plot scatter of any two columns
def scatter_plot(df, column_1, column_2):
  plt.clf()
  x = df[column_1]
  y = df[column_2]
  #colors = np.random.rand(N)
  #area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
  plt.scatter(x, y, alpha=0.5)
  plt.xlabel(column_1)
  plt.ylabel(column_2)
  plt.show()
# Create a function to plot scatter of speed vs height

# Create a scatter plot of roller coaster height by speed
scatter_plot(roller_statics, 'speed', 'length')


