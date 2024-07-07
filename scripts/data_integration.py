import pandas as pd

def integrate_data(sources):
    data_frames = []
    for source in sources:
        data_frames.append(pd.read_csv(source))
    
    unified_data = pd.concat(data_frames, ignore_index=True)
    return unified_data

if __name__ == "__main__":
    sources = ['data/online_data.csv', 'data/in_store_data.csv', 'data/social_media_data.csv']
    unified_data = integrate_data(sources)
    unified_data.to_csv('data/unified_customer_data.csv', index=False)
