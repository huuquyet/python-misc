import pandas as pd
import numpy as np
from mido import MidiFile, MidiTrack, Message
from sklearn.preprocessing import MinMaxScaler

def btc_to_midi(csv_file, midi_file, time_unit=480, max_notes=128):
    """
    Converts historical BTC weekly price data to a MIDI file.

    Args:
        csv_file: Path to the CSV file containing BTC price data (Date,Close).
        midi_file: Path to save the generated MIDI file.
        time_unit: MIDI time unit (ticks per beat). Adjust for tempo.
        max_notes: Maximum number of MIDI notes available (0-127).
    """

    try:
        df = pd.read_csv(csv_file, index_col='Date', parse_dates=True)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
        return
    except pd.errors.ParserError:
        print(f"Error: Could not parse CSV file. Check format (Date,Close).")
        return
    except KeyError:
        print(f"Error: CSV file must have 'Date' and 'Close' columns.")
        return

    if df.empty:
      print("Error: CSV file is empty.")
      return

    prices = df['Close'].values.reshape(-1, 1)

    # Normalize prices to the MIDI note range
    scaler = MinMaxScaler(feature_range=(31, max_notes - 1))  # Subtract 1 for 0-based indexing
    normalized_prices = scaler.fit_transform(prices).astype(int)

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Calculate price differences for note durations and velocities
    price_diffs = np.diff(prices.flatten())
    # Scale differences for durations and velocities
    diff_scaler = MinMaxScaler(feature_range=(time_unit // 4, time_unit)) #min duration is a quarter note
    normalized_diffs = diff_scaler.fit_transform(price_diffs.reshape(-1, 1)).astype(int)
    vel_scaler = MinMaxScaler(feature_range=(64, 127)) # Velocity range 64-127
    normalized_vels = vel_scaler.fit_transform(price_diffs.reshape(-1, 1)).astype(int)


    # Add note on/off events
    current_time = 0
    for i, note in enumerate(normalized_prices.flatten()):
        velocity = 64 #default velocity
        duration = time_unit #default duration
        if i < len(normalized_vels):
          velocity = normalized_vels[i][0]
        if i < len(normalized_diffs):
          duration = int(normalized_diffs[i][0] * 0.6)
        track.append(Message('note_on', note=note, velocity=velocity, time=current_time))
        current_time = duration
        track.append(Message('note_off', note=note, velocity=velocity, time=duration))
        current_time = 0

    try:
        mid.save(midi_file)
        print(f"MIDI file saved to '{midi_file}'")
    except Exception as e: #catch potential saving errors
        print(f"Error saving MIDI file: {e}")

# Example usage (replace with your actual file paths)
btc_csv = 'btc-price-binance.csv'  # CSV file with Date and Close columns
output_midi = 'btc_music.mid'
btc_to_midi(btc_csv, output_midi)
