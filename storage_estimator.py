import shutil
def storage_estimator():
    total, used, free = shutil.disk_usage("C:/")
    print("Total Storage:", round(total / 1024 ** 3, 2), "GB")
    print("Used Storage:", round(used / 1024 ** 3, 2), "GB")
    print("Free Storage:", round(free / 1024 ** 3, 2), "GB")
    required = float(input("Enter required storage (MB): "))
    if required <= free / 1024 ** 2:
        print("Sufficient storage available." , (free/1024**2 - required)/1024 , " GB remaining.")
    else:
        print("Insufficient storage. Clear up some space." ,(required-free/1024**2)/1024 , " GB more is required")
storage_estimator()
