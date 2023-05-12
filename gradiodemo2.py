import gradio as gr
import matplotlib.pyplot as plt

def plot_function(x):
    y = x
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of x=y')
    return plt


interface = gr.Interface(plot_function,
                         inputs=gr.inputs.Slider(0, 10),
                         outputs=gr.Plot(),
                         live=True)

interface.launch()
