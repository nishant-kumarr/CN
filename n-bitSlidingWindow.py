import time
import random

def send_frame(frame_number):
    print(f"Sending frame {frame_number}...")
    return frame_number

def receive_ack(expected_ack, window_size):
    # Simulate a random chance of acknowledgment loss
    ack = random.choice([expected_ack, None])
    if ack is not None:
        print(f"ACK {ack} received (Cumulative for frames up to {ack}).")
    else:
        print(f"ACK {expected_ack} lost!")
    return ack

def sliding_window(window_size):
    total_frames = int(input("Enter the total number of frames to send: "))
    current_frame = 0  # Starting frame number
    last_acknowledged = -1  # Last acknowledged frame

    while last_acknowledged < total_frames - 1:
        # Send frames within the window
        for i in range(window_size):
            if current_frame < total_frames:
                send_frame(current_frame)
                current_frame += 1
            else:
                break

        # Simulate delay
        time.sleep(random.uniform(0.5, 2.0))

        # Receive cumulative acknowledgment for the window
        ack = receive_ack(current_frame - 1, window_size)

        if ack is not None:
            last_acknowledged = ack
            print(f"Frames up to {ack} successfully transmitted.\n")
        else:
            print(f"Timeout! Resending frames starting from {last_acknowledged + 1}...\n")
            current_frame = last_acknowledged + 1  # Retransmit from the last unacknowledged frame
            time.sleep(1)  # Simulate delay before resending

if __name__ == "__main__":
    print("\n\nN-Bit Sliding Window Protocol Simulation")
    window_size = int(input("Enter the sliding window size (N): "))
    sliding_window(window_size)
