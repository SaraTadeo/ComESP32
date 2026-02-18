import tkinder as tk    # Para la interfaz gráfica 
from tkinter import ttk # Para agregar estilos 
import socket           # Para la comunicación en red
import threading 
import time             # Para mejorar tiempos de espera 

# --- cONFIGURACIÓN ---
IP_ESP32 = "192.168.20.15" # Cambio por el IP de el ESP32