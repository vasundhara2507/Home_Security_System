#Server
import socket, cv2, pickle,struct,imutils

# Socket Create
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()#gives the host name
host_ip = socket.gethostbyname(host_name) # gives the host ip
print('HOST IP:',host_ip)
port = 9999   
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)
client_socket,addr = server_socket.accept()
print('GOT CONNECTION FROM:',addr)
print("CLICK TO START THE VERIFICATION !!")
data="CALLING FOR VERIFICATION!!"
client_socket.send(data.encode())
# Socket Accept
while True:
	
	if client_socket:
		vid = cv2.VideoCapture(0)
		
		while(vid.isOpened()):

			img,frame = vid.read()
			frame = imutils.resize(frame,width=320)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			
			try:
				client_socket.sendall(message)
			
				cv2.imshow('TRANSMITTING VIDEO',frame)
				if cv2.waitKey(1) == '13':
					client_socket.close()
				
			except:
				print("code exited !!")
				exit()