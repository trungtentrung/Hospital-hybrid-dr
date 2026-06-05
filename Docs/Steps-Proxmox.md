## Cluster & Ceph
# Bước 1
Tạo cluster và lấy mã information pve-01 để pve-02 và pve-03 join mã information thành cluster

# Bước 2
Sau khi 3 pve thành cluster thì tải ceph về cho từng pve

# Bước 3
Add thêm ổ đĩa cho từng pve để thành 1 pool thống nhất cho ceph 

# Bước 4
Create OSD cho từng pve đã được add ổ đĩa ở trước đó

# Bước 5
Create pools cho ceph

# Bước 6
Create cephFS cho 3 pve và vào ổ đĩa đã create cephFS upload ISO

# Bước 7
Sau khi tạo vm xong thì sẽ tiến thành HA cho vm đã tạo

## PBS
# Bước 1
Tạo directory để chứa disk

# Bước 2
Add storage cho PBS 

# Bước 3
3:30 : tạo lịch backup cho PBS từ Proxmox VE
