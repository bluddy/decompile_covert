#!/usr/bin/env python3
import requests
import subprocess
import sys

def get_windows_host_ip():
    """Get Windows host IP from WSL"""
    try:
        result = subprocess.run(['cat', '/etc/resolv.conf'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if line.startswith('nameserver'):
                return line.split()[1]
    except:
        pass
    return None

def test_connection(host, port=8080):
    """Test connection to Ghidra server"""
    url = f"http://{host}:{port}/"
    print(f"Testing {url}")
    
    try:
        response = requests.get(url, timeout=5)
        print(f"✓ SUCCESS! Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False

def main():
    print("=== Testing Ghidra MCP Connection ===")
    
    # Test localhost
    print("\n1. Testing localhost:")
    if test_connection("127.0.0.1"):
        print("Use: python3 bridge_mcp_ghidra.py")
        return
    
    # Test Windows host IP
    print("\n2. Testing Windows host IP:")
    windows_ip = get_windows_host_ip()
    if windows_ip:
        print(f"Windows IP: {windows_ip}")
        if test_connection(windows_ip):
            print(f"Use: python3 bridge_mcp_ghidra.py --ghidra-server http://{windows_ip}:8080/")
            return
    
    # Test common IPs
    print("\n3. Testing common WSL IPs:")
    for ip in ["172.28.64.1"]:
        if test_connection(ip):
            print(f"Use: python3 bridge_mcp_ghidra.py --ghidra-server http://{ip}:8080/")
            return
    
    print("\n❌ No connection found! Check:")
    print("- Ghidra is running on Windows")
    print("- GhidraMCP plugin is enabled")
    print("- A project is open in Ghidra")
    print("- HTTP server is enabled in Tool Options")

if __name__ == "__main__":
    main()
