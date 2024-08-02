import pandas as pd
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import CSVFile
from django.conf import settings
import os
import seaborn as sns


# Set the matplotlib backend before importing pyplot
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for rendering PNGs
import matplotlib.pyplot as plt

def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('analysis:analysis')
    else:
        form = CSVUploadForm()
    return render(request, 'analysis/upload.html', {'form': form})

def analyze_file(request):
    last_file = CSVFile.objects.last()
    file_path = os.path.join(settings.MEDIA_ROOT, last_file.file.name)
    df = pd.read_csv(file_path)

    # Basic Data Analysis
    head = df.head().to_html()
    description = df.describe().to_html()

    # Handling missing values
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ['Column', 'Missing Values']
    missing_values_html = missing_values.to_html(index=False)

    # Visualization
    plots = []

    # Histogram
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plot = df[column].plot(kind='hist').get_figure()
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_hist.png')
        plot.savefig(plot_path)
        plots.append(f'/media/{os.path.basename(plot_path)}')
        plot.clf()

    # Line Plot
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.lineplot(data=df, x=df.index, y=column)
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_line.png')
        plt.savefig(plot_path)
        plots.append(f'/media/{os.path.basename(plot_path)}')
        plt.close()

    # Scatter Plot
    if len(df.columns) > 1:
        plt.figure()
        sns.scatterplot(data=df, x=df.columns[0], y=df.columns[1])
        plot_path = os.path.join(settings.MEDIA_ROOT, 'scatter.png')
        plt.savefig(plot_path)
        plots.append(f'/media/{os.path.basename(plot_path)}')
        plt.close()

    # Box Plot
    plt.figure()
    sns.boxplot(data=df)
    plot_path = os.path.join(settings.MEDIA_ROOT, 'boxplot.png')
    plt.savefig(plot_path)
    plots.append(f'/media/{os.path.basename(plot_path)}')
    plt.close()

    # Bar Plot (if categorical data is present)
    for column in df.select_dtypes(include=['object']).columns:
        plt.figure()
        sns.countplot(data=df, x=column)
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_bar.png')
        plt.savefig(plot_path)
        plots.append(f'/media/{os.path.basename(plot_path)}')
        plt.close()# Close the plot to free up memory

    return render(request, 'analysis/analysis.html', {
        'head': head,
        'description': description,
        'missing_values': missing_values_html,
        'plots': plots,
    })
