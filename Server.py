## importing socket module
import socket
from PIL import Image
import cv2

# Take in base64 string and return cv image
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def StartServer():
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    # socket.
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

    HOST = "192.168.0.129"  # Standard loopback interface address (localhost)
    PORT = 7052        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        imgdata = b''
        with conn:
            print('Connected by', addr)
            while True:
                datum = conn.recv(1000000)
                if not datum:
                    break
                imgdata += datum
                conn.sendall(datum)
            imgData = base64.b64encode(imgdata)
            img = stringToRGB(imgData)
            cv2.imshow(img)
            

if __name__ == "__main__":
    StartServer()

