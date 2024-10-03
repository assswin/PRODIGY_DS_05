import pandas as pd

# Load the dataset
url = "https://www.kaggle.com/datasets/harshalbhamare/us-accident-eda"
# Note: For actual usage, download the dataset locally and provide the file path here
df = pd.read_csv('US_Accidents_Dec20_updated.csv')

# Display the first few rows
df.head()
# Check for missing values
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Drop rows with missing values for simplicity
df = df.dropna()

# Convert date and time to datetime object
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])
import matplotlib.pyplot as plt
import seaborn as sns

# Count accidents by weather condition
weather_counts = df['Weather_Condition'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=weather_counts.index, y=weather_counts.values)
plt.title('Accidents by Weather Condition')
plt.xticks(rotation=45)
plt.ylabel('Number of Accidents')
plt.xlabel('Weather Condition')
plt.show()
# Count accidents by road condition
road_counts = df['Road_Condition'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=road_counts.index, y=road_counts.values)
plt.title('Accidents by Road Condition')
plt.xticks(rotation=45)
plt.ylabel('Number of Accidents')
plt.xlabel('Road Condition')
plt.show()
# Extract hour from the start time
df['Hour'] = df['Start_Time'].dt.hour

# Count accidents by hour
hour_counts = df['Hour'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=hour_counts.index, y=hour_counts.values)
plt.title('Accidents by Hour of the Day')
plt.ylabel('Number of Accidents')
plt.xlabel('Hour of the Day')
plt.xticks(range(0, 24))
plt.grid()
plt.show()
import geopandas as gpd

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['Start_Lng'], df['Start_Lat']),
    crs='EPSG:4326'
)

# Create a base map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the accidents
plt.figure(figsize=(15, 10))
ax = world.boundary.plot()
gdf.plot(ax=ax, color='red', markersize=1, alpha=0.5)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
import geopandas as gpd

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['Start_Lng'], df['Start_Lat']),
    crs='EPSG:4326'
)

# Create a base map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the accidents
plt.figure(figsize=(15, 10))
ax = world.boundary.plot()
gdf.plot(ax=ax, color='red', markersize=1, alpha=0.5)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
