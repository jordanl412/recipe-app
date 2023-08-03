from recipes.models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_recipename_from_id(val):
    recipename = Recipe.objects.get(id=val)
    return recipename

def get_graph():
    # Creates a BytesIO buffer for the image
    buffer = BytesIO()

    # Create a plot with a BytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    # Set cursor to the beginning of the stream
    buffer.seek(0)

    # Retrieve the content of the file
    image_png = buffer.getvalue()

    # Encode the bytes-like object
    graph = base64.b64encode(image_png)

    # Decode to get the string as output
    graph = graph.decode('utf-8')

    # Free up the memory of the buffer
    buffer.close()

    # Return the image/graph
    return graph

def get_chart(chart_type, data, **kwargs):
    # Switch plot backend to AGG(Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    # Specify figure size
    fig = plt.figure(figsize=(6, 3))

    # Select chart_type based on user input from the form
    if chart_type == '#1':
        # Plot bar chart with recipe name as x-axis and cooking time as y-axis
        plt.title('Recipe Cooking Times')
        plt.bar(data['title'], data['cooking_time'])
        plt.xlabel('Recipes')
        plt.ylabel('Cooking Time (in minutes)')
    elif chart_type == '#2':
        # Pie chart based on cooking times
        # Cooking times are sent from the view as labels
        plt.title('Recipe Cooking Times')
        labels = kwargs.get('labels')
        plt.pie(data['cooking_time'], labels=None)
        plt.legend(
            data['title'],
            location='upper right',
        )
    elif chart_type == '#3':
        # Line chart with recipe name as x-axis and cooking time as y-axis
        plt.title('Recipe Cooking Times')
        plt.plot(data['title'], data['cooking_time'])
        plt.xlabel('Recipes')
        plt.ylabel('Cooking Time (in minutes)')
    else:
        print('Unknown chart type.')

    # Specify layout details
    plt.tight_layout()

    # Render the graph to file
    chart = get_graph()
    return chart

