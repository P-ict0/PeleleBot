import re
import pandas as pd


class DataProcessor:
    """A class to process the WhatsApp data"""

    def __init__(self, raw_data: str) -> None:
        self.raw_data = raw_data

    def parse_data(self) -> pd.DataFrame:
        """
        Parse the WhatsApp text into a DataFrame with columns: date, time, sender, and message.

        :return: The parsed DataFrame
        """
        # Define a pattern to capture the date, time, and sender
        # Pre-compile the pattern for better performance
        pattern = re.compile(r"(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}\s[ap]m) - (.*?):")

        messages = []
        current_message = None

        # Split the text into lines
        lines = self.raw_data.split("\n")

        for line in lines:
            # Check if the line starts with a new message
            start = pattern.match(line)
            if start:
                # Save the current message if there is one
                if current_message:
                    messages.append(current_message)
                # Start a new message
                date = start.group(1)
                time = start.group(2)
                sender = start.group(3)
                message = line[len(start.group(0)) :]
                current_message = {
                    "Date": date,
                    "Time": time,
                    "Sender": sender,
                    "Message": message.strip(),
                }
            elif current_message:
                # Continuation of the current message
                current_message["Message"] += "\n" + line

        # Append the last message if the loop ends
        if current_message:
            messages.append(current_message)

        return pd.DataFrame(messages)

    @staticmethod
    def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the data by removing any rows with media messages or missing values.

        :param dataframe: The DataFrame to clean
        :return: The cleaned DataFrame
        """
        # Substitute the non-breaking space character with a regular space
        dataframe["Date"] = dataframe["Date"].str.replace("\u202f", " ", regex=True)
        dataframe["Time"] = dataframe["Time"].str.replace("\u202f", " ", regex=True)

        # Remove rows with missing values and media messages
        return dataframe.dropna().loc[
            ~dataframe["Message"].str.contains("<Media omitted>")
        ]

    @staticmethod
    def transform(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Transform the data by adding useful columns.

        :param dataframe: The DataFrame to transform
        :return: The transformed DataFrame
        """
        # Combine 'Date' and 'Time' into a single 'DateTime' column and convert to datetime type
        dataframe["DateTime"] = pd.to_datetime(
            dataframe["Date"] + " " + dataframe["Time"], format="%d/%m/%Y %I:%M %p"
        )
        dataframe.set_index("DateTime", inplace=True)  # Set 'DateTime' as the index

        # Add a 'Message_Count' column to count the number of messages per day
        dataframe["Message_Count"] = 1
        dataframe = dataframe.resample("D").sum()

        return dataframe

    def process_data(self) -> pd.DataFrame:
        """
        Process the data by parsing, cleaning, and transforming it.

        :return: The processed DataFrame
        """
        dataframe = self.parse_data()
        dataframe = self.clean_data(dataframe)
        dataframe = self.transform(dataframe)

        return dataframe
