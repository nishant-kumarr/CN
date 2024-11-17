import time
import random

def send_frame(frame_number):
    print(f"Sending frame {frame_number}...")
    return frame_number

def receive_ack(expected_ack):
    ack = random.choice([expected_ack, None])  # Simulate ACK received or lost
    if ack is not None:
        print(f"ACK {ack} received.")
    else:
        print(f"ACK {expected_ack} lost!")
    return ack

def stop_and_wait():
    total_frames = int(input("Enter the number of frames to send: "))
    frame_number = 0

    while frame_number < total_frames:
        # Send frame
        sent_frame = send_frame(frame_number)

        # Simulate a delay in receiving ACK
        time.sleep(random.uniform(0.5, 2.0))

        # Receive ACK
        ack = receive_ack(sent_frame)

        if ack == sent_frame:
            print(f"Frame {frame_number} successfully transmitted.\n")
            frame_number += 1  # Move to the next frame
        else:
            print(f"Timeout! Resending frame {frame_number}...\n")
            time.sleep(1)  # Simulate delay before resending

if __name__ == "__main__":
    print("\n\n1-Bit Stop-and-Wait Protocol Simulation")
    stop_and_wait()
