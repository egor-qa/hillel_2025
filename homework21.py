from datetime import datetime, timedelta

def analyze_heartbeat_log(input_file='hblog.txt', output_file='hb_test.log'):
    key = "Key TSTFEED0300|7E3E|0400"
    timestamps = []

    # 1. Read file and filter lines with the key
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if key in line:
                ts_index = line.find("Timestamp ")
                if ts_index != -1:
                    time_str = line[ts_index + len("Timestamp "): ts_index + len("Timestamp ") + 8]
                    try:
                        ts = datetime.strptime(time_str, "%H:%M:%S")
                        timestamps.append((ts, line.strip()))
                    except ValueError:
                        continue  # Skip lines with invalid time format

    if len(timestamps) < 2:
        print("Not enough heartbeat entries to analyze.")
        return

    # 2. Analyze differences between consecutive timestamps
    with open(output_file, 'w', encoding='utf-8') as out:
        for i in range(len(timestamps) - 1):
            current_ts, current_line = timestamps[i]
            next_ts, next_line = timestamps[i + 1]

            # Handle midnight crossover (next timestamp earlier than current)
            if next_ts < current_ts:
                next_ts += timedelta(days=1)

            diff_seconds = (next_ts - current_ts).total_seconds()

            # 3. Log warnings/errors based on heartbeat interval
            if 31 < diff_seconds < 33:
                out.write(
                    f"WARNING at {current_ts.strftime('%H:%M:%S')} (diff={diff_seconds:.1f}s)\n"
                    f"Line: {current_line}\n\n"
                )
            elif diff_seconds >= 33:
                out.write(
                    f"ERROR at {current_ts.strftime('%H:%M:%S')} (diff={diff_seconds:.1f}s)\n"
                    f"Line: {current_line}\n\n"
                )

    print(f"Analysis complete. Results saved to '{output_file}'")

if __name__ == "__main__":
    analyze_heartbeat_log()