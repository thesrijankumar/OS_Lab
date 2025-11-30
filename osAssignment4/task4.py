#!/usr/bin/env python3

import os
import subprocess
import re

def run_system_info():
    """Run system information collection using shell commands"""
    print("=" * 60)
    print("SYSTEM INFORMATION")
    print("=" * 60)
    
    system_info = {}
    
    # 1. Kernel Information
    print("\n1. KERNEL INFORMATION:")
    print("-" * 25)
    try:
        result = subprocess.run(['uname', '-r'], capture_output=True, text=True)
        kernel_version = result.stdout.strip()
        print(f"Kernel Version: {kernel_version}")
        system_info['kernel_version'] = kernel_version
    except Exception as e:
        print(f"Error getting kernel version: {e}")
    
    try:
        result = subprocess.run(['uname', '-s'], capture_output=True, text=True)
        kernel_name = result.stdout.strip()
        print(f"Kernel Name: {kernel_name}")
        system_info['kernel_name'] = kernel_name
    except Exception as e:
        print(f"Error getting kernel name: {e}")
    
    # 2. User Information
    print("\n2. USER INFORMATION:")
    print("-" * 25)
    try:
        result = subprocess.run(['whoami'], capture_output=True, text=True)
        current_user = result.stdout.strip()
        print(f"Current User: {current_user}")
        system_info['current_user'] = current_user
    except Exception as e:
        print(f"Error getting user info: {e}")
    
    # 3. Hardware Information
    print("\n3. HARDWARE INFORMATION:")
    print("-" * 25)
    try:
        result = subprocess.run(['lscpu'], capture_output=True, text=True)
        lscpu_output = result.stdout
        
        # Extract CPU model
        model_match = re.search(r'Model name:\s*(.+)', lscpu_output)
        if model_match:
            cpu_model = model_match.group(1).strip()
            print(f"CPU Model: {cpu_model}")
            system_info['cpu_model'] = cpu_model
        
        # Extract virtualization info
        virt_match = re.search(r'Virtualization:\s*(.+)', lscpu_output)
        if virt_match:
            virtualization = virt_match.group(1).strip()
            print(f"Virtualization: {virtualization}")
            system_info['virtualization'] = virtualization
        
        # Get CPU cores
        cores_match = re.search(r'CPU\(s\):\s*(\d+)', lscpu_output)
        if cores_match:
            cpu_cores = cores_match.group(1)
            print(f"CPU Cores: {cpu_cores}")
            system_info['cpu_cores'] = cpu_cores
            
    except Exception as e:
        print(f"Error getting hardware info: {e}")
    
    # 4. Memory Information
    print("\n4. MEMORY INFORMATION:")
    print("-" * 25)
    try:
        result = subprocess.run(['free', '-h'], capture_output=True, text=True)
        free_output = result.stdout
        lines = free_output.split('\n')
        if len(lines) > 1:
            mem_line = lines[1].split()
            if len(mem_line) >= 7:
                print(f"Total Memory: {mem_line[1]}")
                print(f"Used Memory: {mem_line[2]}")
                print(f"Free Memory: {mem_line[3]}")
                system_info['total_memory'] = mem_line[1]
                system_info['used_memory'] = mem_line[2]
                system_info['free_memory'] = mem_line[3]
    except Exception as e:
        print(f"Error getting memory info: {e}")
    
    # 5. Disk Information
    print("\n5. DISK INFORMATION:")
    print("-" * 25)
    try:
        result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
        df_output = result.stdout
        lines = df_output.split('\n')
        if len(lines) > 1:
            disk_line = lines[1].split()
            if len(disk_line) >= 6:
                print(f"Filesystem: {disk_line[0]}")
                print(f"Total: {disk_line[1]}, Used: {disk_line[2]}, Free: {disk_line[3]}")
                system_info['disk_total'] = disk_line[1]
                system_info['disk_used'] = disk_line[2]
                system_info['disk_free'] = disk_line[3]
    except Exception as e:
        print(f"Error getting disk info: {e}")
    
    # 6. OS Information
    print("\n6. OPERATING SYSTEM:")
    print("-" * 25)
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                os_release = f.read()
            pretty_name_match = re.search(r'PRETTY_NAME="([^"]+)"', os_release)
            if pretty_name_match:
                pretty_name = pretty_name_match.group(1)
                print(f"OS: {pretty_name}")
                system_info['os_name'] = pretty_name
        else:
            print("OS: Unknown")
    except Exception as e:
        print(f"Error getting OS info: {e}")
    
    return system_info

def check_dmi_info():
    """Check DMI system information for VM indicators"""
    print("\n" + "=" * 60)
    print("VIRTUAL MACHINE DETECTION")
    print("=" * 60)
    
    vm_indicators = []
    
    print("\n1. DMI SYSTEM INFORMATION:")
    print("-" * 25)
    
    try:
        # Check system manufacturer
        result = subprocess.run(['sudo', 'dmidecode', '-s', 'system-manufacturer'], 
                              capture_output=True, text=True, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            manufacturer = result.stdout.strip()
            print(f"System Manufacturer: {manufacturer}")
            
            vm_manufacturers = ['vmware', 'virtualbox', 'qemu', 'kvm', 'microsoft corporation', 'innotek', 'xen']
            manufacturer_lower = manufacturer.lower()
            for vm_man in vm_manufacturers:
                if vm_man in manufacturer_lower:
                    vm_indicators.append(f"VM manufacturer detected: {manufacturer}")
                    break
        else:
            print("System Manufacturer: Unable to check (need sudo privileges)")
        
        # Check system product name
        result = subprocess.run(['sudo', 'dmidecode', '-s', 'system-product-name'], 
                              capture_output=True, text=True, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            product_name = result.stdout.strip()
            print(f"System Product Name: {product_name}")
            
            vm_products = ['virtualbox', 'vmware', 'virtual machine', 'kvm', 'qemu']
            product_lower = product_name.lower()
            for vm_prod in vm_products:
                if vm_prod in product_lower:
                    vm_indicators.append(f"VM product name detected: {product_name}")
                    break
        else:
            print("System Product Name: Unable to check (need sudo privileges)")
                    
    except Exception as e:
        print(f"DMI check error: {e}")
    
    return vm_indicators

def check_cpu_info():
    """Check CPU information for VM indicators"""
    print("\n2. CPU INFORMATION ANALYSIS:")
    print("-" * 25)
    
    vm_indicators = []
    
    try:
        with open('/proc/cpuinfo', 'r') as f:
            cpuinfo = f.read()
        
        # Check for hypervisor flag
        if 'hypervisor' in cpuinfo:
            vm_indicators.append("Hypervisor flag present in CPU info")
            print("Hypervisor flag: Present (VM indicator)")
        else:
            print("Hypervisor flag: Not present")
        
        # Check processor model
        model_pattern = re.compile(r'model name\s*:\s*(.+)', re.IGNORECASE)
        match = model_pattern.search(cpuinfo)
        if match:
            model = match.group(1)
            print(f"CPU Model: {model}")
            
            vm_models = ['qemu', 'virtual', 'vmware', 'kvm']
            model_lower = model.lower()
            for vm_model in vm_models:
                if vm_model in model_lower:
                    vm_indicators.append(f"VM CPU model detected: {model}")
                    break
        
    except Exception as e:
        print(f"CPU info check failed: {e}")
    
    return vm_indicators

def check_kernel_modules():
    """Check loaded kernel modules for VM indicators"""
    print("\n3. KERNEL MODULES CHECK:")
    print("-" * 25)
    
    vm_indicators = []
    
    try:
        result = subprocess.run(['lsmod'], capture_output=True, text=True)
        if result.returncode == 0:
            lsmod_output = result.stdout.lower()
            
            vm_modules = ['vboxguest', 'vmw_balloon', 'vmw_vmci', 'xen', 'kvm']
            for module in vm_modules:
                if module in lsmod_output:
                    vm_indicators.append(f"VM kernel module detected: {module}")
                    print(f"VM Module {module}: Present")
                else:
                    print(f"VM Module {module}: Not present")
        else:
            print("Unable to check kernel modules")
    
    except Exception as e:
        print(f"Kernel modules check failed: {e}")
    
    return vm_indicators

def check_systemd_virtualization():
    """Check systemd for virtualization detection"""
    print("\n4. SYSTEMD VIRTUALIZATION DETECTION:")
    print("-" * 25)
    
    vm_indicators = []
    
    try:
        result = subprocess.run(['systemd-detect-virt'], capture_output=True, text=True)
        if result.returncode == 0:
            virt_type = result.stdout.strip()
            if virt_type != 'none':
                vm_indicators.append(f"Systemd detected virtualization: {virt_type}")
                print(f"Systemd Virtualization: {virt_type} (VM detected)")
            else:
                print("Systemd Virtualization: none (bare metal)")
        else:
            print("Systemd virtualization detection not available")
    
    except Exception as e:
        print(f"Systemd check failed: {e}")
    
    return vm_indicators

def analyze_vm_detection(vm_indicators):
    """Analyze collected indicators and determine if system is a VM"""
    print("\n" + "=" * 60)
    print("DETECTION ANALYSIS RESULTS")
    print("=" * 60)
    
    if vm_indicators:
        print("VIRTUAL MACHINE INDICATORS FOUND:")
        for indicator in vm_indicators:
            print(f"  - {indicator}")
        
        confidence = min(100, len(vm_indicators) * 25)
        print(f"\nDETECTION RESULT: VIRTUAL MACHINE DETECTED")
        print(f"CONFIDENCE LEVEL: {confidence}%")
        return True, confidence
    else:
        print("VIRTUAL MACHINE INDICATORS FOUND: None")
        print("\nDETECTION RESULT: BARE METAL SYSTEM")
        print("CONFIDENCE LEVEL: 85%")
        return False, 85

def main():
    """Main function for VM detection and system analysis"""
    print("TASK 4: VM DETECTION AND SYSTEM INFORMATION")
    print("=" * 60)
    
    # Collect system information
    system_info = run_system_info()
    
    # Collect all VM indicators
    all_vm_indicators = []
    
    all_vm_indicators.extend(check_dmi_info())
    all_vm_indicators.extend(check_cpu_info())
    all_vm_indicators.extend(check_kernel_modules())
    all_vm_indicators.extend(check_systemd_virtualization())
    
    # Analyze results
    is_vm, confidence = analyze_vm_detection(all_vm_indicators)
    
    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    
    if is_vm:
        print("CONCLUSION: This system is running in a VIRTUAL MACHINE")
        print("Virtualization technology detected with high confidence")
    else:
        print("CONCLUSION: This system is running on BARE METAL")
        print("No significant virtualization indicators found")
    
    print(f"\nDetection Confidence: {confidence}%")
    print(f"Total VM indicators found: {len(all_vm_indicators)}")
    
    # Display key system information
    print("\nKEY SYSTEM INFORMATION:")
    print("-" * 25)
    if 'os_name' in system_info:
        print(f"Operating System: {system_info['os_name']}")
    if 'kernel_version' in system_info:
        print(f"Kernel Version: {system_info['kernel_version']}")
    if 'cpu_model' in system_info:
        print(f"CPU Model: {system_info['cpu_model']}")
    if 'cpu_cores' in system_info:
        print(f"CPU Cores: {system_info['cpu_cores']}")
    if 'total_memory' in system_info:
        print(f"Total Memory: {system_info['total_memory']}")

if __name__ == "__main__":
    main()
