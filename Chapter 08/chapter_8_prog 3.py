import ipywidgets as widgets
import matplotlib.pyplot as plt

# Define data
x_data = ['City A', 'City B', 'City C','City D','City E']
y_data = [2, 3, 2.5,1,3.25] #initial value

# Define a slider widget
slider_wid = widgets.IntSlider(min=0, 
                               max=10, 
                               step=1, 
                               value=0,
                               description='Slider:', 
                               disabled=False, 
                               continuous_update=False, 
                               orientation='horizontal', 
                               readout=True, 
                               readout_format='d')

# Define a function to update the graph when slider value changes
def update_graph(x):
    # x is of type: <class 'traitlets.utils.bunch.Bunch'>
    val = x['new']
    plt.clf()
    plt.bar(x_data , [element * val for element in y_data])
    plt.xlabel('Cities name')
    plt.ylabel('Rupees (Crores)') 
    plt.title('Municipal Tax Collection (Rs Crores)')
    plt.show()

# Call the function when the slider value changes
slider_wid.observe(update_graph, 'value')

# Display the slider
display(slider_wid)