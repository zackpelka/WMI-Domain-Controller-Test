# Import the wmi module
import wmi

# Define the domain controller name and credentials
dc_name = "DC01"
dc_user = "Administrator"
dc_pass = "Password123"

# Create a WMI connection object
wmi_conn = wmi.WMI(dc_name, user=dc_user, password=dc_pass)

# Test the WMI connection by querying the Win32_OperatingSystem class
try:
    os_info = wmi_conn.Win32_OperatingSystem()[0]
    print(f"Successfully connected to {dc_name}")
    print(f"OS Name: {os_info.Caption}")
    print(f"OS Version: {os_info.Version}")
except wmi.x_wmi as e:
    print(f"Failed to connect to {dc_name}")
    print(f"Error: {e.com_error.hresult}")
