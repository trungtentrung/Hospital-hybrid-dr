# Bước 1
Tạo IAM user để xác thực danh tính để cho VM đẩy gửi data lên aws

# Bước 2
Tải công cụ aws cli để có thể giao tiếp được đến AWS

# Bước 3
Đăng nhập aws từ terminal

# Bước 4
Lấy id và secret từ bước đã tạo IAM lúc nãy để có thể đăng nhập vào AWS

# Bước 5
04:10 : dùng lệnh aws sts get-caller-identityaws sts get-caller-identity để kiểm tra đã đăng nhập vào được aws hay chưa và đăng nhập vào user nào

# Bước 6
Tạo thư mục để chứa scripts của đồ án

# Bước 7
Cấp quyền thực thi để cho file script chạy được và lập lịch tự động chạy script

# Bước 8
Khi lập lịch xong sẽ vào AWS Cloudwatch mục all metrics để kiểm tra xem heartbeat script có thực sự đang gửi data lên cloudwatch không

# Bước 9
Tạo alarm và liên kết heartbeat để liên tục theo dõi và báo động khi sự cố xảy ra

# Bước 10
Tạo dịch vụ DRS để aws chuẩn bị hạ tầng sẵn sàng nhận dữ liệu replication từ proxmox

# Bước 11
Launch templates để DRS có thể dựa vào templates để tạo con ec2 

# Bước 12
Tải bộ cài đặt DRS Agent từ server của AWS về VM , agent sẽ chạy ngầm và đồng bộ dữ liệu từ on-premise lên DRS theo thời gian thực

# Bước 13
Chạy bộ cài đặt Agent. bước này Agent sẽ cài vào VM và tự động đăng ký với DRS bắt đầu quá trình đồng bộ dữ liệu liên tục 

# Bước 14
Trên source servers DRS sẽ hiện thị quá trình đồng bộ VM

# Bước 15
Tạo lambda để tự động kích hoạt kịch bản DR khi có sự cố theo kịch bản

# Bước 16
Tạo roles cho lambda và add policy cho phép lambda được toàn quyền điều khiển DRS

# Bước 17
Vào alarms để kiểm tra trạng thái của alarm

# Bước 18
Tạo tình huống vm mất kết nối bằng lệnh kill 

# Bước 19
Vào alarms kiểm tra trạng thái sau khi kill heartbeat

# Bươcs 20
Kiểm tra log streams ở Cloudwatch đã ghi log hay chưa

# Bước 21
Vào recovery job history DRS kiểm tra trạng thái 

# Bước 22
24:36 sau recovery job history trạng thái completed qua recovery instances để xác nhận ec2 đã được tạo ra từ bản sao VM Proxmox
