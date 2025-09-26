import pandas as pd
import random
from conversations import generate_message

def generate_dataset(total_entries, spam_ratio):
    num_spam = int(total_entries * spam_ratio)
    num_ham = total_entries - num_spam

    data = []
    for _ in range(num_spam):
        data.append(["spam", generate_message(True)])
    for _ in range(num_ham):
        data.append(["ham", generate_message(False)])

    # Shuffle the dataset to mix spam and ham messages
    random.shuffle(data)
    
    df = pd.DataFrame(data, columns=['target', 'text'])
    df.to_csv('/mnt/j/sit327/simulation/data/generated_spam4.csv', index=False)
    print("Dataset generated with {} entries ({}% spam).".format(total_entries, int(spam_ratio * 100)))

# Parameters: Total entries and the spam ratio
generate_dataset(5000, 0.35)
