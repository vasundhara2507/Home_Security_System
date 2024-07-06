#Client
import tkinter as tk
import socket,cv2, pickle,struct

def exit_code():
    print("Code exited !!")
    exit()
def start_code():
    
    # Add your code here that you want to execute when the button is clicked
    print("Starting another code...")

# create socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_ip = '192.168.143.77' # paste your server ip address here
    port = 9999
    client_socket.connect((host_ip,port)) # a tuple
    data = b""
    payload_size = struct.calcsize("Q")
    msg1=client_socket.recv(1024).decode()
    print("-->",msg1)
    while True:
       
        while len(data) < payload_size:
            packet = client_socket.recv(4*1024) # 4K
            if not packet: break
            data+=packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        
        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        frame_data = data[:msg_size]
        data  = data[msg_size:]
        frame = pickle.loads(frame_data)
        cv2.imshow("RECEIVING VIDEO",frame)
        
        if cv2.waitKey(1) == ord("q"):
            window = tk.Tk()
            window.title("------OUTPUT_SCREEN------")
            frame = tk.Frame(window)
            label = tk.Label(window, text="\nDOORS ARE NOT OPENED FOR THIS PERSON !!\n")
            label.config(font=("Times New Roman", 40))
            label.pack()
            window.after(2000,lambda:window.destroy())
            frame.pack(padx=20, pady=20)
            window.mainloop()
            exit_code()
            client_socket.close()
            
        if cv2.waitKey(1) == ord("w"):
     
            window = tk.Tk()
            window.title("------OUTPUT_SCREEN------")
            frame = tk.Frame(window)
            label = tk.Label(window, text="\nDOORS ARE OPENED FOR THIS PERSON !!\n")
            label.config(font=("Times New Roman", 40))
            label.pack()
            window.after(2000,lambda:window.destroy())
            frame.pack(padx=20, pady=20)
            window.mainloop()
            exit_code()
            client_socket.close()            
            

window = tk.Tk()

# Set the window title
window.title("------HOME SECURITY-----")


# Create a frame for the button
frame = tk.Frame(window)



# Create a frame for the button
frame = tk.Frame(bg="white", bd=0)
# Create a bigger button with some styling
button = tk.Button(frame, text="Click For Face-Verification",command=start_code,font=("Arial", 16), padx=10, pady=10, fg="black", bg="sky blue", activebackground="sky blue", activeforeground="white")


# Add the button to the frame
button.pack()

# Add some padding to the frame
frame.pack(padx=10, pady=10)
window.after(4000,lambda:window.destroy())
window.mainloop()
window.destroy()