import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('Golden_Ticket_Award_Winners_wood.csv')
print(steel.head())
print(wood.head())

# write function to plot rankings over time for 1 roller coaster here:
def plot_rank(rc_name, df, park):
    x = df[(df['Name'] == rc_name) & (df['Park'] == park)]['Year of Rank']
    y = df[(df['Name'] == rc_name) & (df['Park'] == park)]['Rank']
    plt.plot(x, y)
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Roller Coaster Ranking')
    ax = plt.subplot()
    ax.invert_yaxis()
    ax.set_xticks(x)
    ax.set_yticks(y)
    plt.show()
plot_rank('El Toro', wood, 'Six Flags Great Adventure')
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def plot_rank2(rc1, rc2, df, park1, park2):
    x0 = df[(df['Name'] == rc1)]['Year of Rank']
    x = x0.unique()
    y1 = df[(df['Name'] == rc1) & (df['Park'] == park1)]['Rank']
    y2 = df[(df['Name'] == rc2) & (df['Park'] == park2)]['Rank']
    plt.plot(x, y1, label=rc1)
    plt.plot(x, y2, label=rc2)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('{} vs. {}'.format(rc1, rc2))
    ax = plt.subplot()
    ax.invert_yaxis()
    ax.set_xticks(x)
    ax.set_yticks(y1)
    plt.show()
plot_rank2('El Toro', 'Boulder Dash', wood, 'Six Flags Great Adventure', 'Lake Compounce')
plt.clf()

# write function to plot top n rankings over time here:
def plot_n_rank(n, df):
    top_rc = df[(df['Rank'] <= n)]
    fig, ax = plt.subplots(figsize=(10, 10))
    for rcs in set(top_rc.Name):
        rc = top_rc[top_rc.Name == rcs]
        ax.plot(rc['Year of Rank'], rc['Rank'], label=rcs)
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Top Roller Coasters Ranking')
    plt.legend()
    ax.invert_yaxis()
    ax.set_xticks(top_rc['Year of Rank'])
    ax.set_yticks(top_rc['Rank'])
    # ax.set_xticklabels(x)
    # ax.set_yticklabels(y)
    plt.show()
plot_n_rank(5, wood)
plt.clf()

# load roller coaster data here:
captain = pd.read_csv('roller_coasters.csv')
print(captain.head())

# write function to plot histogram of column values here:
def distribution(col, df):
    if col == 'height':
        plt.hist(df[df[col]<=140][col].dropna())
    else:
        plt.hist(df[col].dropna())
    plt.show()
distribution('num_inversions', captain)
plt.clf()

# write function to plot inversions by coaster at a park here:
def inversions(park, df):
    plot_rows = df[df.park == park]
    plot_rows = plot_rows.sort_values('num_inversions', ascending=False)
    plt.bar(plot_rows['name'], plot_rows['num_inversions'])
    ax=plt.subplot()
    ax.set_xticks(range(len(plot_rows['name'])))
    ax.set_xticklabels(plot_rows['name'], rotation=30, fontsize='x-small', ha='right')
    plt.show()
inversions('Parc Asterix', captain)
plt.clf()

# write function to plot pie chart of operating status here:
def rc_status(df):
    operating = df[df['status'] == 'status.operating']['status'].count()
    closed = df[df['status'] == 'status.closed.definitely']['status'].count()
    plt.pie([operating, closed], labels=['Operating', 'Closed'], autopct='%0.1f%%', startangle=90)
    plt.axis('equal')
    plt.show()
rc_status(captain)    
plt.clf()

# write function to create scatter plot of any two numeric columns here:
def relationship(col1, col2, df):
    plt.scatter(df[col1] , df[col2])
    if col1 == 'height':
        plt.xlim(xmax=200)
    if col2 == 'height':
        plt.ylim(ymax=200)
    plt.xlabel(col1)
    plt.ylabel(col2)
    ax = plt.subplot()
    plt.show()
relationship('speed', 'length', captain)
plt.clf()
