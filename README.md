markdown
# Interactive Visualization and Analysis Platform for Energy Sector Licensing and Permits Data

## Overview
This repository hosts the code and documentation for an interactive platform that visualizes and analyzes the 'Licenses and Permits in the Energy Sector 2025' dataset. The platform aims to enhance user engagement and transparency by providing a user-friendly interface to explore the dataset.

## Features
1. **Dynamic Visualizations**: Create bar charts, line graphs, and pie charts to visualize license distribution.
2. **Filtering Options**: Filter data based on license type, category, or other attributes.
3. **Export**: Save filtered data into new CSV files for further analysis.
4. **Custom Reports**: Generate reports tailored to user needs.

## Prerequisites
- Python 3.7+
- Pandas
- Plotly

Install required packages using:
bash
pip install pandas plotly


## Dataset
The dataset (`Licence_Category.csv`) contains information about licenses and permits in the energy sector. Ensure the file is in the same directory as the script.

### Columns in the Dataset
- **License Type**: Type of license (e.g., Electricity Generation, Water Desalination).
- **Category**: License category (e.g., Major, Instant).
- **Number of Licenses**: Total number of licenses issued.

## Running the Script
1. Place the `Licence_Category.csv` file in the script's directory.
2. Run the script using Python:
   bash
   python main.py
   
3. Follow the prompts to filter data or generate visualizations.

## Example Usage
1. **Generate Bar Chart**:
   The script generates a bar chart showing the distribution of licenses by type and category.

2. **Filter Licenses**:
   Use the `filter_licenses()` function to filter data by a specific license type:
   python
   filtered_data = filter_licenses("Electricity Generation")
   

3. **Save Filtered Data**:
   Save the filtered data to a new CSV file:
   python
   filtered_data.to_csv("Filtered_Licenses.csv", index=False)
   

## Future Improvements
- Add support for interactive web-based dashboards using frameworks such as Dash or Streamlit.
- Include APIs for real-time data updates.
- Provide multi-language support, including Arabic.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For questions or support, please contact [energy.data@abudhabi.gov.ae](mailto:energy.data@abudhabi.gov.ae).
