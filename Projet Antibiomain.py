import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Folder configuration
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
IMAGES_FOLDER = "images"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(IMAGES_FOLDER, exist_ok=True)

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of required columns for each graph
LINE_GRAPH_COLUMNS = ["sample_type", "mouse_ID", "treatment", "experimental_day", "frequency_live_bacteria"]
VIOLIN_GRAPH_COLUMNS = ["sample_type", "treatment", "frequency_live_bacteria"]

def check_missing_columns(data, required_columns):
    """Check for missing columns in the data."""
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.warning(f"Missing columns: {missing_columns}")
    return missing_columns

def filter_data_for_line_graph(data):
    """Filter data for the line graph."""
    if check_missing_columns(data, LINE_GRAPH_COLUMNS):
        return pd.DataFrame()
    return data[data["sample_type"] == "fecal"][LINE_GRAPH_COLUMNS]

def filter_data_for_violin_graph(data, sample_type):
    """Filter data for the violin graph."""
    if check_missing_columns(data, VIOLIN_GRAPH_COLUMNS):
        return pd.DataFrame()
    filtered_data = data[data["sample_type"] == sample_type][VIOLIN_GRAPH_COLUMNS]
    logging.info("Data for {}:\n{}".format(sample_type, filtered_data))
    return filtered_data

def save_filtered_data(filtered_data, filename):
    """Save filtered data to a CSV file."""
    if filtered_data.empty:
        logging.warning(f"No data to save for {filename}.")
        return
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    filtered_data.to_csv(output_path, index=False)
    logging.info(f"Data saved to {output_path}.")

def plot_line_graph(data):
    """Create a line graph for fecal bacteria."""
    if data.empty:
        logging.warning("No data for the line graph.")
        return
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=data,
        x="experimental_day",
        y="frequency_live_bacteria",
        hue="treatment",
        style="mouse_ID",
        markers=True,
        dashes=False
    )
    plt.title("Evolution of Fecal Bacteria")
    plt.xlabel("Experimental Day")
    plt.ylabel("Percentage of Live Bacteria")
    plt.legend(title="Treatment")
    plt.grid(True)
    output_path = os.path.join(IMAGES_FOLDER, "line_graph.png")
    plt.savefig(output_path)
    plt.close()
    logging.info(f"Line graph saved to {output_path}.")

def plot_violin_graph(data, sample_type):
    """Create a violin graph for cecal and ileal bacteria."""
    if data.empty:
        logging.warning(f"No data for the violin graph ({sample_type}).")
        return
    plt.figure(figsize=(10, 6))
    sns.violinplot(
        data=data,
        x="sample_type",
        y="frequency_live_bacteria",
        hue="treatment",
        split=True,
        palette="muted"
    )
    plt.title(f"Bacteria Dispersion in {sample_type.capitalize()} Samples")
    plt.xlabel("Sample Type")
    plt.ylabel("Percentage of Live Bacteria")
    plt.legend(title="Treatment")
    plt.grid(True)
    output_path = os.path.join(IMAGES_FOLDER, f"violin_graph_{sample_type}.png")
    plt.savefig(output_path)
    plt.close()
    logging.info(f"Violin graph ({sample_type}) saved to {output_path}.")

def main():
    # File path
    file = "data_small.csv" #HERE it's only for small, choose the one you want but put the csv file in the input file (small,medium,large,huge)
    filepath = os.path.join(INPUT_FOLDER, file)

    if not os.path.exists(filepath):
        logging.error(f"File '{file}' not found in '{INPUT_FOLDER}'.")
        return

    logging.info(f"Processing file: {file}")

    try:
        # Read the file with the correct separator
        data = pd.read_csv(filepath, sep=';')
    except Exception as e:
        logging.error(f"Error loading file {file}: {e}")
        return

    # Check columns
    actual_columns = data.columns.tolist()
    logging.info(f"Columns found in the file: {actual_columns}")
    missing_columns = check_missing_columns(data, LINE_GRAPH_COLUMNS + VIOLIN_GRAPH_COLUMNS)
    if missing_columns:
        logging.error(f"The following columns are missing from the CSV file: {missing_columns}")
        return

    # Filter data
    line_data = filter_data_for_line_graph(data)
    cecal_data = filter_data_for_violin_graph(data, "cecal")
    ileal_data = filter_data_for_violin_graph(data, "ileal")

    # Save filtered data
    save_filtered_data(line_data, "line_data.csv")
    save_filtered_data(cecal_data, "cecal_data.csv")
    save_filtered_data(ileal_data, "ileal_data.csv")

    # Create graphs
    plot_line_graph(line_data)
    plot_violin_graph(cecal_data, "cecal")
    plot_violin_graph(ileal_data, "ileal")

    logging.info(f"Processing complete. Outputs are in '{OUTPUT_FOLDER}' and '{IMAGES_FOLDER}'.")

if __name__ == "__main__":
    main()
