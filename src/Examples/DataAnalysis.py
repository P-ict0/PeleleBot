# Imports
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.dates as mdates

# Import data
with open('WhatsApp Chat with Peleles.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # print(lines)

# Function to parse data
def parse_message(message):
    if ' - ' not in message or ': ' not in message:
        return None  # Skip lines that don't contain expected delimiters
    date_time, message_part = message.split(' - ', 1)
    if ': ' in message_part:
        sender, message = message_part.split(': ', 1)
    else:
        return None  # Skip lines that don't contain a colon separating sender and message
    date, time = date_time.split(', ')
    return date, time, sender, message

# Parse each line
parsed_data = []
for line in lines:
    result = parse_message(line.strip())
    if result:
        parsed_data.append(result)

# Convert to DataFrame
df = pd.DataFrame(parsed_data, columns=['Date', 'Time', 'Sender', 'Message'])
df = df[df['Message'] != '<Media omitted>'] # Filter out rows where messages are '<Media omitted>'

# Messages per Pelele
message_counts = df.groupby('Sender').size().reset_index(name='Message Count')
message_counts = message_counts.sort_values(by='Message Count', ascending=False)
print(message_counts)

# Remove formatting issues
df['Date'] = df['Date'].str.replace(u'\u202f', ' ', regex=True)
df['Time'] = df['Time'].str.replace(u'\u202f', ' ', regex=True)

# Messages over time
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %I:%M %p') # Combine 'Date' and 'Time' into a single 'DateTime' column and convert to datetime type
df.set_index('DateTime', inplace=True) # Set 'DateTime' as the index
daily_messages = df['Message'].resample('D').count().reset_index(name='Message') # Messages per day (change 'D' to 'H' for hourly)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(daily_messages['DateTime'], daily_messages['Message'], marker='o', linestyle='-')
plt.title('Daily Message Activity Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Messages')
plt.grid(True)
plt.show()

# Create an interactive plot with Plotly
fig = px.line(daily_messages, x='DateTime', y='Message', title='Daily Message Activity Over Time',
              labels={'Message': 'Number of Messages', 'DateTime': 'Date'},
              markers=True)

# Improve hover information
fig.update_traces(mode='markers+lines', hoverinfo='x+y')

# Show the plot
fig.show()



### David Analysis
davids_messages = df[df['Sender'].str.contains('Rodri', case=False, na=False)]
race_counter = davids_messages['Message'].str.lower().str.count(r'').sum()
race_counter


