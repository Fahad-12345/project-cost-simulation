import plotly.express as px
import pandas as pd

# Step 1: Define your tasks and timeline
data = [
    {"Task": "Define Problem Statement", "Start": "2025-01-01", "Finish": "2025-01-10", "Status": "Completed"},
    {"Task": "Data Collection", "Start": "2025-01-11", "Finish": "2025-01-20", "Status": "Completed"},
    {"Task": "Exploring Components & Parameters", "Start": "2025-01-21", "Finish": "2025-02-05", "Status": "Completed"},
    {"Task": "Preparing Python Script", "Start": "2025-02-06", "Finish": "2025-02-20", "Status": "In Progress"},
    {"Task": "Creating Histogram & CDFs", "Start": "2025-02-21", "Finish": "2025-03-05", "Status": "Pending"},
    {"Task": "Preparing Presentation", "Start": "2025-03-06", "Finish": "2025-03-20", "Status": "Pending"},
    {"Task": "Report Writing", "Start": "2025-03-21", "Finish": "2025-04-15", "Status": "Pending"},
]

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Create the Gantt chart using Plotly
fig = px.timeline(
    df, 
    x_start="Start", 
    x_end="Finish", 
    y="Task", 
    color="Status",
    title="Monte Carlo Simulation Project Timeline (Jan – Apr 2025)",
    color_discrete_map={
        "Completed": "green",
        "In Progress": "orange",
        "Pending": "red"
    }
)

# Step 4: Adjust layout
fig.update_yaxes(autorange="reversed")  # To show first task at the top
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Project Tasks",
    font=dict(size=14)
)

# Step 5: Show the chart
fig.show()
