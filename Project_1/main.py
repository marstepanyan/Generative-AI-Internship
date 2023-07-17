from CPU_HDD_SSD import CPU, HDD, SSD

# Creating instances of CPU, HDD, and SSD
cpu1 = CPU(name="Intel Core i9-9900K", manufacturer="Intel", total=5, allocated=2, cores=8, socket="LGA1200", power_watts=95)
hdd1 = HDD(name="WD Blue HDD", manufacturer="Western Digital", total=10, allocated=4, capacity_gb=1000, size="3.5\"", rpm=7200)
ssd1 = SSD(name="Samsung 970 EVO", manufacturer="Samsung", total=7, allocated=1, capacity_gb=500, interface="NVMe")

# Claiming resources
print(cpu1.claim(1))
print(hdd1.claim(2))
print(ssd1.claim(1))

# Freeing up resources
print(cpu1.freeup(1))
print(hdd1.freeup(1))

# Retiring resources
print(hdd1.died(1))

# Purchasing new resources
print(cpu1.purchased(3))
print(ssd1.purchased(2))

# Printing the details of the resources
print(cpu1)
print(hdd1)
print(ssd1)

# Accessing computed property - category
print(cpu1.category)
print(hdd1.category)
print(ssd1.category)
