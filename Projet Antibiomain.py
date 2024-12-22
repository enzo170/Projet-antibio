import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configuration des dossiers
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"
IMAGES_FOLDER = "images"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(IMAGES_FOLDER, exist_ok=True)

# Configuration de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def filter_data_for_line_graph(data):
    """Filter data for the line graph."""
    required_columns = ["sample_type", "mouse_ID", "treatment", "experimental_day", "frequency_live_bacteria"]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.warning(f"Missing columns for the line graph: {missing_columns}")
        return pd.DataFrame()
    filtered = data[data["sample_type"] == "fecal"]
    return filtered[required_columns]

def filter_data_for_violin_graph(data, sample_type):
    """Filter data for the violin graph."""
    required_columns = ["sample_type", "treatment", "experimental_day", "frequency_live_bacteria"]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        logging.warning(f"Missing columns for the violin graph: {missing_columns}")
        return pd.DataFrame()
    filtered = data[(data["sample_type"] == sample_type) & (data["experimental_day"] == 7)]
    return filtered[required_columns]

def save_filtered_data(filtered_data, filename):
    """Save filtered data to CSV."""
    if filtered_data.empty:
        logging.warning(f"No data to save for {filename}.")
        return
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    filtered_data.to_csv(output_path, index=False)
    logging.info(f"Data saved to {output_path}.")

def plot_line_graph(data):
    """Create a line graph for fecal bacteria."""
    if data.empty:
        logging.warning("No data for line graph.")
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
    plt.title("Fecal Bacteria Evolution")
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
        logging.warning(f"No data for {sample_type} violin graph.")
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
    logging.info(f"{sample_type.capitalize()} violin graph saved to {output_path}.")

def main():
    # Load CSV files
    file = "data_small.csv"  # Nom du fichier attendu
    filepath = os.path.join(INPUT_FOLDER, file)

    if not os.path.exists(filepath):
        logging.error(f"File '{file}' not found in '{INPUT_FOLDER}'.")
        return

    logging.info(f"Processing file: {file}")

    try:
        data = pd.read_csv(filepath)
    except Exception as e:
        logging.error(f"Error loading file {file}: {e}")
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
