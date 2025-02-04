# SpaceX Launch Records Dashboard

This project is a dashboard developed to visualize SpaceX launch records. The dashboard provides various interactive visualizations to help users analyze the launch data effectively.

## Project Overview

The goal of this project is to create a dashboard that visualizes SpaceX launch data using Plotly and Dash. The dashboard includes:
- A dropdown menu to select the launch site, which updates the pie chart.
- A pie chart showing the success rate of launches for the selected site or all sites.
- A range slider to select the payload mass range, which updates the scatter plot.
- A scatter plot showing the relationship between payload mass and launch success for the selected site and payload mass range.

## Features

- **Launch Site Selection:** Users can select a specific launch site or view data for all sites.
- **Success Rate Visualization:** A pie chart displays the success rate of launches for the selected site.
- **Payload Range Filtering:** A range slider allows users to filter launches by payload mass.
- **Payload vs. Success Visualization:** A scatter plot shows the relationship between payload mass and launch success.

## Libraries and Tools Used

- **Pandas:** For data manipulation and analysis.
- **Dash:** For building the web application and creating interactive components.
- **Dash HTML Components:** For HTML components in the Dash application.
- **Plotly Express:** For creating interactive plots and visualizations.
- **Matplotlib and Seaborn:** For additional data visualization capabilities.

## Skills Upgraded and Learned

- **Data Analysis:** Improved skills in data manipulation and analysis using Pandas.
- **Web Development:** Gained experience in building interactive web applications using Dash.
- **Data Visualization:** Enhanced ability to create interactive and informative visualizations using Plotly Express.
- **Problem Solving:** Developed problem-solving skills by handling real-world data and creating meaningful visualizations.

## How the Dashboard was Developed

1. **Data Preparation:** The dataset `spacex_launch_dash.csv` was read using Pandas, and necessary preprocessing was done, including creating new columns for better visualization.
2. **Dash Application:** A Dash application was created with a layout consisting of various Dash components like dropdowns, sliders, and graphs.
3. **Interactive Components:** Callback functions were implemented to update the visualizations based on user interactions with the dropdown menu and range slider.
4. **Visualization:** Pie charts and scatter plots were created using Plotly Express to visualize the success rate and the relationship between payload mass and launch success.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/PedroRgz/CareerAcademy-IBM-DS-RocketLaunchesDashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CareerAcademy-IBM-DS-RocketLaunchesDashboard
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Dash application:
   ```bash
   python app.py
   ```

## Conclusion

This project showcases the ability to analyze and visualize data effectively using modern data science tools and libraries. It demonstrates skills that are crucial for a data science junior role, including data analysis, web development, and data visualization.
