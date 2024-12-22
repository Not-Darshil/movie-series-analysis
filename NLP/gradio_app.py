import gradio as gr
import matplotlib.pyplot as plt
import pandas as pd
from theme_classifier import ThemeClassifier

def get_themes(themes_list, subtitles_path, save_path):
    themes_list = themes_list.split(",")
    theme_classifier = ThemeClassifier(themes_list)
    
    # Get the dataframe of the theme scores
    output_df = theme_classifier.get_themes(subtitles_path, save_path)
    
    # Filter out 'dialogue' theme if it exists
    themes_list = [theme for theme in themes_list if theme != 'dialogue']
    
    # Select only the columns corresponding to the themes
    output_df = output_df[themes_list]
    
    # Sum the values for each theme and reset index
    output_df = output_df.sum().reset_index()
    output_df.columns = ['Theme', 'Score']
    
    # Plot the data using matplotlib
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(output_df['Theme'], output_df['Score'], color='skyblue')
    ax.set_xlabel('Score')
    ax.set_title('Series Theme')
    
    # Return the plot
    return fig

def main():
    with gr.Blocks() as iface:
        with gr.Row():
            with gr.Column():
                gr.HTML("<h1>Theme Classification (Zero Shot Classifiers)</h1>")
                with gr.Row():
                    with gr.Column():
                        # Use gr.Plot to display matplotlib figure
                        plot = gr.Plot()
                    with gr.Column():
                        theme_list = gr.Textbox(label='Themes')
                        subtitles_path = gr.Textbox(label='Subtitles or Script Path ')
                        save_path = gr.Textbox(label='Save Path')
                        get_themes_button = gr.Button("Get Themes")
                        get_themes_button.click(get_themes, inputs=[theme_list, subtitles_path, save_path], outputs=[plot])

    iface.launch(share=True)

if __name__ == "__main__":
    main()
