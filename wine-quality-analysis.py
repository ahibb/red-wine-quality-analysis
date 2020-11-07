import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Displays a simple table describing the summary of the given attribute columns.
params
 dataset: Pandas DataFrame that contains the dataset
 attribute: String containing the name of the attribute
'''
def display_attribute_summary(dataset,attribute):
    print(attribute, "summary")
    print("----------------------")
    print(dataset[attribute].describe())
    print()

'''
Gets number of wines with each quality value and returns a series with quality value and counts.
No params
'''
def get_wine_count_by_quality(wine_data):
    num_wines_by_quality = {}

    # choose range 3 to 8 for the qualities in the wine
    for i in range(3,9):
        # check if the row has the current quality value
        qual_series_obj = wine_data.apply(lambda x: True if x['quality'] == i else False, axis=1)
    
        # get the number of rows with quality value = i
        num_of_rows = len(wine_data[qual_series_obj == True].index)
        num_wines_by_quality[i] = num_of_rows

    num_wines_by_quality_series = pd.Series(num_wines_by_quality)
    return num_wines_by_quality_series

'''
Plots the number of wines with a particular value rating. 
No params
'''
def plot_wine_count_by_quality(wine_data):
    wine_count_by_quality_ser = get_wine_count_by_quality(wine_data)
    ax = wine_count_by_quality_ser.plot.bar(rot=0)
    plt.title("Fig 1: Wine Count by Quality Value")
    plt.xlabel("Wine Quality Value")
    plt.ylabel("Wine Count")
    #plt.close()

'''
Plots a histogram for a given dataset.
params
 num_bins: integer number of bins for the histogram chart
 dataset: pandas DataFrame containing the dataset
 x_label: string for the label that should go on the x-axis
 y_label: string for the label on the y-axis
 title: string describing the title of the plot
'''
def plot_histogram(num_bins,dataset,x_label,y_label,title):
    # the histogram of the data
    n, bins, patches = plt.hist(dataset, num_bins, facecolor='blue', alpha=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def draw_box_whisker_plot(df,column_prop,group_by_prop,showfliers):
    bp = df.boxplot(column=column_prop,by=group_by_prop, patch_artist=True,return_type='dict',showfliers=showfliers)

    # hide the grouped by title
    plt.suptitle("Spread of residual sugar values grouped by quality")
    for key in bp.keys():
        # change outline color
        [box.set(color='#66447a',linewidth=2) for box in bp[key]['boxes']]
        # change fill color
        [box.set(facecolor='#176836') for box in bp[key]['boxes']]
        # change whisker color
        [whisker.set(color='#66447a', linewidth=2) for whisker in bp[key]['whiskers']]
        # change cap color
        [cap.set(color='#66447a', linewidth=2) for cap in bp[key]['caps']]
        # change median line color
        [median.set(color='#b2df8a', linewidth=2) for median in bp[key]['medians']]
        
        # set outlier flier color
        [flier.set(marker='o', markerfacecolor='#f596b5', alpha=0.5) for flier in bp[key]['fliers']]

def main():
    # load in the data
    wine_data = pd.read_csv('winequality-red.csv',sep=';')

    num_rows = len(wine_data.index)
    print("Number of instances: ", num_rows)  

    display_attribute_summary(wine_data,"quality")
    display_attribute_summary(wine_data,"fixed acidity")
    display_attribute_summary(wine_data,"volatile acidity")
    display_attribute_summary(wine_data,"citric acid")
    display_attribute_summary(wine_data,"pH")
    display_attribute_summary(wine_data,"free sulfur dioxide")

    plot_wine_count_by_quality(wine_data)

    plot_histogram(20,wine_data["fixed acidity"],"Fixed Acidity","Frequency","Figure 2: Histogram of Fixed Acidity Values")
    plot_histogram(20,wine_data["volatile acidity"],"Volatile Acidity","Frequency","Figure 3: Histogram of Volatile Acidity Values")
    plot_histogram(20,wine_data["citric acid"],"Citric Acid","Frequency","Figure 4: Histogram of Citric Acid Values")
    plot_histogram(20,wine_data["residual sugar"], "Residual Sugar", "Frequency", "Figure 5: Histogram of Residual Sugar")
    plot_histogram(15,wine_data["chlorides"], "Chlorides", "Frequency", "Figure 6: Histogram of Chlorides")
    plot_histogram(20,wine_data["free sulfur dioxide"],"Free Sulfur Dioxide", "Frequency", "Figure 7: Frequency of Free Sulfur Dioxide Concentrations")
    plot_histogram(20,wine_data["total sulfur dioxide"],"Total Sulfur Dioxide","Frequency","Figure 8: Frequency of Total Sulfur Dioxide Concentrations")
    plot_histogram(20,wine_data["density"],"Density","Frequency","Figure 9: Frequency of Density")
    plot_histogram(20,wine_data["pH"],"pH","Frequency","Figure 10: Frequency of wine samples with a measure pH")
    plot_histogram(20,wine_data["sulphates"],"sulphates","Frequency","Figure 11: Frequency of wine samples with a specific sulphate concentration")
    plot_histogram(20,wine_data["alcohol"],"alcohol","Frequency","Figure 12: Frequency of wine samples with a measured alcohol content")

    draw_box_whisker_plot(wine_data,['residual sugar'],'quality',False)
    draw_box_whisker_plot(wine_data,['residual sugar'],'quality',True)
if __name__ == "__main__":
    main()